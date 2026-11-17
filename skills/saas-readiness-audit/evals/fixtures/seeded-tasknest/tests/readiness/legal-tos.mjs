import { withServerDb, verdict } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const t = await call('GET', '/terms'); const f = await call('GET', '/'); const s = await call('GET', '/signup');
  verdict([
    { name: '/terms 200 with ToS heading', ok: t.status === 200 && /terms of service/i.test(t.text) },
    { name: 'footer links /terms', ok: f.text.includes('href="/terms"') },
    { name: 'signup page links /terms', ok: s.text.includes('href="/terms"') },
  ]);
});
