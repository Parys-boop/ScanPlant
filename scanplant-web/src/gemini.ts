const GEMINI_API_KEY = import.meta.env.VITE_GEMINI_API_KEY || '';
const GEMINI_MODEL = import.meta.env.VITE_GEMINI_MODEL || '';

const getModelFallbacks = () => {
  return Array.from(new Set([
    GEMINI_MODEL,
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-1.5-flash',
  ].filter(Boolean)));
};

const getGeminiText = (data: any) => {
  const parts = data?.candidates?.[0]?.content?.parts || [];
  return parts
    .map((part: any) => part?.text)
    .filter((text: any) => typeof text === 'string' && text.trim().length > 0)
    .join('\n')
    .trim();
};

export const isGeminiConfigured = () => GEMINI_API_KEY.trim().length > 0;

export const generateGeminiText = async (
  prompt: string,
  options: { responseMimeType?: string; temperature?: number } = {}
) => {
  if (!isGeminiConfigured()) {
    throw new Error('Chave Gemini não configurada. Defina VITE_GEMINI_API_KEY no arquivo .env.local.');
  }

  let lastError: Error | null = null;

  for (const model of getModelFallbacks()) {
    try {
      const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${encodeURIComponent(GEMINI_API_KEY)}`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            contents: [
              {
                role: 'user',
                parts: [{ text: prompt }],
              },
            ],
            generationConfig: {
              temperature: options.temperature ?? 0.2,
              ...(options.responseMimeType ? { responseMimeType: options.responseMimeType } : {}),
            },
          }),
        }
      );

      const data = await response.json().catch(() => null);

      if (!response.ok) {
        const message = data?.error?.message || `Erro ${response.status} ao chamar Gemini.`;
        lastError = new Error(message);

        if (response.status === 401 || response.status === 403) {
          throw lastError;
        }

        continue;
      }

      const text = getGeminiText(data);
      if (text) return text;

      const finishReason = data?.candidates?.[0]?.finishReason;
      lastError = new Error(finishReason ? `Gemini não retornou texto (${finishReason}).` : 'Gemini não retornou texto.');
    } catch (error: any) {
      lastError = error instanceof Error ? error : new Error(error?.message || 'Erro ao chamar Gemini.');
    }
  }

  throw lastError || new Error('Não foi possível obter resposta da Gemini.');
};

export const parseGeminiJson = (content: string) => {
  const cleaned = content
    .trim()
    .replace(/^```json\s*/i, '')
    .replace(/^```\s*/i, '')
    .replace(/\s*```$/i, '')
    .trim();

  try {
    return JSON.parse(cleaned);
  } catch {
    const start = cleaned.indexOf('{');
    const end = cleaned.lastIndexOf('}');
    if (start >= 0 && end > start) {
      return JSON.parse(cleaned.slice(start, end + 1));
    }
    throw new Error('A resposta da Gemini não veio em JSON válido.');
  }
};
