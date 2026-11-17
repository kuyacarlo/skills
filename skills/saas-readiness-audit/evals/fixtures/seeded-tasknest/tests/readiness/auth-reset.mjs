import { withServerDb, verdict, signupLogin } from './_harness.mjs';
await withServerDb(async ({ call, db }) => {
  await signupLogin(call, 'r@x.test', 'pw123456');
  const r1 = await call('POST', '/reset/request', { email: 'r@x.test' });
  const t = r1.json?.devResetToken;
  const c1 = await call('POST', '/reset/confirm', { token: t, password: 'newpass1' });
  const c2 = await call('POST', '/reset/confirm', { token: t, password: 'attacker1' });
  // expiry: age a fresh token by 25h
  const r2 = await call('POST', '/reset/request', { email: 'r@x.test' });
  const rec = db.resetTokens.get(r2.json?.devResetToken); if (rec) rec.created -= 25 * 3600 * 1000;
  const c3 = await call('POST', '/reset/confirm', { token: r2.json?.devResetToken, password: 'late1234' });
  verdict([
    { name: 'reset works once', ok: c1.status === 200 },
    { name: 'token single-use', ok: c2.status >= 400 },
    { name: 'token expires (25h old rejected)', ok: c3.status >= 400 },
  ]);
});
