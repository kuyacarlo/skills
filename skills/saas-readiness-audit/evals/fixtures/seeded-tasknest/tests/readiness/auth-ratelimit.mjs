import { withServerDb, verdict } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const hit = async (path, body) => { let got429 = false; for (let i = 0; i < 30; i++) { const r = await call('POST', path, body); if (r.status === 429) { got429 = true; break; } } return got429; };
  verdict([
    { name: 'login rate-limited within 30 attempts', ok: await hit('/login', { email: 'z@x.test', password: 'no' }) },
    { name: 'reset request rate-limited within 30', ok: await hit('/reset/request', { email: 'z@x.test' }) },
  ]);
});
