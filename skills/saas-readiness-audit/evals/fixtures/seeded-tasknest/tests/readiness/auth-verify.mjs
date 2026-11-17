import { withServerDb, verdict, signupLogin } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const { token } = await signupLogin(call, 'v@x.test', 'pw123456');
  const p = await call('POST', '/projects', { name: 'x' }, token);
  verdict([{ name: 'unverified user blocked from privileged action', ok: p.status === 403, detail: `got ${p.status}` }]);
});
