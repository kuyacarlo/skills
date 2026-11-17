import { withServerDb, verdict } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const f = await call('GET', '/');
  verdict([{ name: 'support contact linked from footer', ok: /mailto:support@|href="\/(support|contact)"/.test(f.text) }]);
});
