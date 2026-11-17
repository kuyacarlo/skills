import { withServerDb, verdict, signupLogin } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const { token } = await signupLogin(call, 'st@x.test', 'pw123456');
  const pw = await call('POST', '/settings/password', { password: 'newpw123' }, token);
  const em = await call('POST', '/settings/email', { email: 'st2@x.test' }, token);
  verdict([
    { name: 'change password', ok: pw.status === 200 },
    { name: 'change email', ok: em.status === 200, detail: `got ${em.status}` },
  ]);
});
