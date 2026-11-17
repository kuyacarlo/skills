import { withServerDb, verdict } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const s = await call('POST', '/signup', { email: 'c@x.test', password: 'pw123456' });
  const l = await call('POST', '/login', { email: 'c@x.test', password: 'pw123456' });
  const bad = await call('POST', '/login', { email: 'c@x.test', password: 'wrong' });
  const o = await call('POST', '/logout', null, l.json?.token);
  const after = await call('POST', '/projects', { name: 'x' }, l.json?.token);
  verdict([
    { name: 'signup 201', ok: s.status === 201 },
    { name: 'login returns token', ok: !!l.json?.token },
    { name: 'wrong password rejected', ok: bad.status === 401 },
    { name: 'logout ok', ok: o.status === 200 },
    { name: 'token dead after logout', ok: after.status === 401 },
  ]);
});
