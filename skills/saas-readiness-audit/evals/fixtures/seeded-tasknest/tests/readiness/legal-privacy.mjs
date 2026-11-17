import { withServerDb, verdict } from './_harness.mjs';
await withServerDb(async ({ call }) => {
  const p = await call('GET', '/privacy'); const t = p.text.toLowerCase();
  verdict([
    { name: '/privacy 200', ok: p.status === 200 },
    { name: 'no placeholder text', ok: !/lorem ipsum|todo|tbd/.test(t) },
    { name: 'section: data collected', ok: /collect/.test(t) },
    { name: 'section: processors/third parties', ok: /third[- ]part|processor/.test(t) },
    { name: 'section: retention', ok: /retain|retention/.test(t) },
    { name: 'section: contact', ok: /contact|@/.test(t.replace(/<footer>[\s\S]*<\/footer>/, '')) },
  ]);
});
