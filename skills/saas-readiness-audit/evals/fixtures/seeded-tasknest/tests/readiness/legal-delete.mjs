import { withServerDb, verdict, signupLogin } from './_harness.mjs';
await withServerDb(async ({ call, db }) => {
  const { token } = await signupLogin(call, 'del@x.test', 'pw123456');
  const d = await call('POST', '/account/delete', null, token);
  const row = db.users.find(u => u.email === 'del@x.test');
  verdict([
    { name: 'delete endpoint succeeds', ok: d.status === 200 },
    { name: 'PII removed or anonymized (no email row)', ok: !row, detail: row ? `row still has email=${row.email}` : '' },
    { name: 'credentials removed', ok: !row || !row.password },
  ]);
});
