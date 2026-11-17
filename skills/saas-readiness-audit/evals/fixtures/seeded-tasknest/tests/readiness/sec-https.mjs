import { withServerDb, verdict } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const r = await call('GET', '/');
  verdict([{ name: 'HSTS header present', ok: /max-age=\d+/.test(r.headers.get('strict-transport-security') || '') }]);
});
