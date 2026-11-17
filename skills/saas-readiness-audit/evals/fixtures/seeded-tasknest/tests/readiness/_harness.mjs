// Shared probe harness. Exit codes: 0 PASS, 1 FAIL, 3 PARTIAL, 2 ERROR (setup/env failure).
import { createApp } from '../../src/app.mjs';

// Variant that exposes the db for storage-level assertions.
export async function withServerDb(fn) {
  const { app, db } = createApp();
  const server = await new Promise((res, rej) => { const s = app.listen(0, () => res(s)); s.on('error', rej); }).catch(e => { console.error('SETUP_ERROR', e); process.exit(2); });
  const base = `http://127.0.0.1:${server.address().port}`;
  const call = async (method, path, body, token) => {
    const r = await fetch(base + path, { method, headers: { 'content-type': 'application/json', ...(token ? { authorization: `Bearer ${token}` } : {}) }, body: body ? JSON.stringify(body) : undefined });
    const text = await r.text(); let json; try { json = JSON.parse(text); } catch {}
    return { status: r.status, text, json, headers: r.headers };
  };
  try { return await fn({ base, call, db }); } finally { server.close(); }
}

export function verdict(results) {
  // results: [{name, ok}]
  for (const r of results) console.log(`${r.ok ? 'ok  ' : 'FAIL'} ${r.name}${r.detail ? ' :: ' + r.detail : ''}`);
  const passed = results.filter(r => r.ok).length;
  console.log(`RESULT ${passed}/${results.length}`);
  const partialOk = process.env.PARTIAL_OK === '1';
  process.exit(passed === results.length ? 0 : partialOk && passed > 0 ? 3 : 1);
}

export async function signupLogin(call, email = 'a@x.test', password = 'hunter22') {
  const s = await call('POST', '/signup', { email, password });
  const l = await call('POST', '/login', { email, password });
  return { signup: s, token: l.json?.token, verifyToken: s.json?.devVerifyToken };
}
