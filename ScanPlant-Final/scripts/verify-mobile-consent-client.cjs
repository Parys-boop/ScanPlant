const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const photoScreen = fs.readFileSync(path.join(root, 'components', 'PhotoScreen.js'), 'utf8');
const api = fs.readFileSync(path.join(root, 'components', 'api.js'), 'utf8');
const envExample = fs.readFileSync(path.join(root, '.env.example'), 'utf8');

assert.match(photoScreen, /const requestExternalIdentification = \(selectedImage\) =>/);
assert.match(photoScreen, /text: 'Recusar', style: 'cancel'/);
assert.match(photoScreen, /text: 'Continuar', onPress: \(\) => identifyPlant\(selectedImage\)/);
assert.match(photoScreen, /requestExternalIdentification\(\{ uri: photo\.uri, mimeType: 'image\/jpeg' \}\)/);
assert.match(photoScreen, /requestExternalIdentification\(\{ uri: asset\.uri, mimeType: asset\.mimeType \|\| 'image\/jpeg' \}\)/);
assert.doesNotMatch(photoScreen, /api\.plant\.id|GROQ_API_KEY|PLANT_ID_API_KEY/i);

assert.match(api, /const EXTERNAL_FALLBACK_ENDPOINT = '\/plant-identification\/fallback'/);
assert.match(api, /formData\.append\('image'/);
assert.match(api, /formData\.append\('consentToExternalProcessing', 'true'\)/);
assert.match(api, /Authorization: `Bearer \$\{token\}`/);
assert.doesNotMatch(api, /api\.plant\.id|GROQ_API_KEY|PLANT_ID_API_KEY/i);
for (const status of [400, 413, 415, 429, 502, 503, 504]) {
  assert.match(api, new RegExp(`${status}:`));
}

assert.doesNotMatch(envExample, /plant\.id|groq|api[_ -]?key/i);

console.log('mobile consent/API-only seam verified');
