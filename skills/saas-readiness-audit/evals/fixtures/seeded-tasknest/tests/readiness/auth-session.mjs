import { withServerDb, verdict, signupLogin } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const { token: a } = await signupLogin(call, 's@x.test', 'pw123456');
  const b = (await call('POST', '/login', { email: 's@x.test', password: 'pw123456' })).json.token;
  await call('POST', '/settings/password', { password: 'changed1' }, a);
  const other = await call('POST', '/projects', { name: 'x' }, b);
  verdict([{ name: 'other sessions invalidated after password change', ok: other.status === 401, detail: `other session got ${other.status}` }]);
});
