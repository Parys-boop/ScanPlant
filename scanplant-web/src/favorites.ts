const FAVORITES_KEY_PREFIX = '@scanplant_favorites';

const getStorageKey = (userId?: string | null) => {
  return userId ? `${FAVORITES_KEY_PREFIX}_${userId}` : FAVORITES_KEY_PREFIX;
};

export const getFavoritePlantIds = (userId?: string | null): string[] => {
  try {
    const rawValue = localStorage.getItem(getStorageKey(userId));
    if (!rawValue) return [];

    const parsedValue = JSON.parse(rawValue);
    return Array.isArray(parsedValue) ? parsedValue.map(String) : [];
  } catch (error) {
    console.error('Erro ao carregar favoritos:', error);
    return [];
  }
};

export const setFavoritePlantIds = (plantIds: string[], userId?: string | null) => {
  try {
    const uniqueIds = Array.from(new Set(plantIds.map(String)));
    localStorage.setItem(getStorageKey(userId), JSON.stringify(uniqueIds));
  } catch (error) {
    console.error('Erro ao salvar favoritos:', error);
  }
};

export const isFavoritePlant = (plantId: string, userId?: string | null) => {
  return getFavoritePlantIds(userId).includes(String(plantId));
};

export const toggleFavoritePlant = (plantId: string, userId?: string | null) => {
  const normalizedId = String(plantId);
  const currentIds = getFavoritePlantIds(userId);
  const nextIds = currentIds.includes(normalizedId)
    ? currentIds.filter((id) => id !== normalizedId)
    : [...currentIds, normalizedId];

  setFavoritePlantIds(nextIds, userId);
  return nextIds;
};
