import { withServerDb, verdict } from './_harness.mjs';
process.env.NODE_ENV = 'production';
await withServerDb(async ({ call }) => {
  const nf = await call('GET', '/definitely-not-here'); const boom = await call('GET', '/boom');
  verdict([
    { name: 'custom 404', ok: nf.status === 404 && /not found/i.test(nf.text) },
    { name: '500 returns 500', ok: boom.status === 500 },
    { name: 'no stack trace in prod 500', ok: !/at .+\(.+:\d+:\d+\)|\.mjs:\d+/.test(boom.text) },
  ]);
});
