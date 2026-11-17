// Fixture "TaskNest" — a tiny SaaS with deliberately seeded readiness defects.
import express from 'express';
import crypto from 'node:crypto';

const html = (title, body) => `<!doctype html><html><head><title>${title}</title></head><body>${body}
<footer><a href="/terms">Terms</a> · <a href="/privacy">Privacy</a> · <a href="mailto:support@tasknest.test">Support</a></footer></body></html>`;

export function createApp() {
  const db = { users: [], sessions: new Map(), resetTokens: new Map(), verifyTokens: new Map(), projects: [] };
  const app = express();
  app.use(express.json());
  const tok = () => crypto.randomBytes(16).toString('hex');

  const auth = (req, res, next) => {
    const t = (req.headers.authorization || '').replace('Bearer ', '');
    const uid = db.sessions.get(t);
    const user = db.users.find(u => u.id === uid && !u.deleted);
    if (!user) return res.status(401).json({ error: 'unauthorized' });
    req.user = user; req.token = t; next();
  };

  app.get('/', (_q, r) => r.send(html('TaskNest', '<h1>TaskNest</h1><a href="/signup">Sign up</a>')));
  app.get('/signup', (_q, r) => r.send(html('Sign up', '<form>...</form><p>By signing up you agree to the <a href="/terms">Terms</a>.</p>')));
  app.get('/terms', (_q, r) => r.send(html('Terms', '<h1>Terms of Service</h1><p>These terms govern use of TaskNest...</p>')));
  // DEFECT: placeholder privacy policy
  app.get('/privacy', (_q, r) => r.send(html('Privacy', '<h1>Privacy Policy</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')));

  app.post('/signup', (req, res) => {
    const { email, password } = req.body;
    if (db.users.some(u => u.email === email)) return res.status(409).json({ error: 'exists' });
    // DEFECT: plaintext password storage
    const user = { id: db.users.length + 1, email, password, verified: false, deleted: false };
    db.users.push(user);
    const vt = tok(); db.verifyTokens.set(vt, user.id);
    res.status(201).json({ id: user.id, devVerifyToken: vt });
  });
  app.post('/verify', (req, res) => {
    const uid = db.verifyTokens.get(req.body.token);
    if (!uid) return res.status(400).json({ error: 'bad token' });
    db.users.find(u => u.id === uid).verified = true; db.verifyTokens.delete(req.body.token);
    res.json({ ok: true });
  });
  // DEFECT: no rate limiting
  app.post('/login', (req, res) => {
    const u = db.users.find(x => x.email === req.body.email && x.password === req.body.password && !x.deleted);
    if (!u) return res.status(401).json({ error: 'invalid' });
    const t = tok(); db.sessions.set(t, u.id); res.json({ token: t });
  });
  app.post('/logout', auth, (req, res) => { db.sessions.delete(req.token); res.json({ ok: true }); });

  // DEFECT: reset tokens never expire and are reusable
  app.post('/reset/request', (req, res) => {
    const u = db.users.find(x => x.email === req.body.email);
    const t = tok(); if (u) db.resetTokens.set(t, { uid: u.id, created: Date.now() });
    res.json({ ok: true, devResetToken: u ? t : undefined });
  });
  app.post('/reset/confirm', (req, res) => {
    const rec = db.resetTokens.get(req.body.token);
    if (!rec) return res.status(400).json({ error: 'bad token' });
    db.users.find(u => u.id === rec.uid).password = req.body.password;
    res.json({ ok: true });
  });

  // DEFECT: password change does not invalidate other sessions; no change-email route
  app.post('/settings/password', auth, (req, res) => { req.user.password = req.body.password; res.json({ ok: true }); });

  // DEFECT: "delete" only soft-flags; email and password remain
  app.post('/account/delete', auth, (req, res) => { req.user.deleted = true; res.json({ ok: true }); });

  // DEFECT: privileged action does not require verified email
  app.post('/projects', auth, (req, res) => { const p = { id: db.projects.length + 1, owner: req.user.id, name: req.body.name }; db.projects.push(p); res.status(201).json(p); });

  app.get('/boom', () => { throw new Error('kaboom from /boom'); });

  app.use((_q, r) => r.status(404).send(html('Not found', '<h1>Page not found</h1>')));
  // DEFECT: error handler leaks stack trace regardless of NODE_ENV
  app.use((err, _q, r, _n) => r.status(500).send(`<pre>${err.stack}</pre>`));

  return { app, db };
}
