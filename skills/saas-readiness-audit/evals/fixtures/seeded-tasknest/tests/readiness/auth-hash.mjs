import { withServerDb, verdict, signupLogin } from './_harness.mjs';
await withServerDb(async ({ call, db }) => {
  await signupLogin(call, 'h@x.test', 'pw123456');
  const u = db.users.find(x => x.email === 'h@x.test'); const stored = u.password ?? u.passwordHash ?? '';
  verdict([
    { name: 'stored value != plaintext', ok: stored !== 'pw123456' },
    { name: 'stored value looks like argon2/bcrypt/scrypt', ok: /^\$(argon2|2[aby]|scrypt)/.test(stored) },
  ]);
});
