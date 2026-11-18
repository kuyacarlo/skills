// Browser checks for skills/anti-slop-design/examples.
// Clean regions (everything outside [data-slop]) must follow the skill: no text under 1.5rem,
// no px in inline styles or Tailwind arbitrary values, no horizontal scroll, no JS errors.
// Slop regions must exist on every page except landing-fixed.html.
// Usage: node scripts/check_slop_examples.cjs <puppeteer module path or name>
const http = require("http");
const fs = require("fs");
const path = require("path");
const puppeteer = require(process.argv[2] || "puppeteer");

const ROOT = path.join(__dirname, "..", "skills", "anti-slop-design", "examples");
const PAGES = ["index", "structure", "surfaces", "type", "copy", "motion", "behavior", "landing-slop", "landing-fixed"];
const TYPES = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript" };

// Tiny static server so the check needs nothing else running.
const server = http.createServer((req, res) => {
  const file = path.join(ROOT, decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html");
  if (!file.startsWith(ROOT) || !fs.existsSync(file)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": TYPES[path.extname(file)] || "application/octet-stream" });
  fs.createReadStream(file).pipe(res);
});

(async () => {
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  const base = `http://127.0.0.1:${server.address().port}`;
  const browser = await puppeteer.launch({ executablePath: process.env.PUPPETEER_EXECUTABLE_PATH, args: ["--no-sandbox"] });
  let failures = 0;
  for (const width of [390, 1280]) {
    for (const name of PAGES) {
      const page = await browser.newPage();
      await page.setViewport({ width, height: 844 });
      const errors = [];
      page.on("pageerror", (e) => errors.push(e.message));
      await page.goto(`${base}/${name}.html`, { waitUntil: "networkidle0" });
      const r = await page.evaluate(() => {
        const clean = (el) => !el.closest("[data-slop]");
        const label = (el) => `${el.tagName.toLowerCase()} "${(el.textContent || el.placeholder || "").trim().slice(0, 30)}"`;
        const small = [], px = [];
        for (const el of document.body.querySelectorAll("*")) {
          if (!clean(el) || el.closest("svg, script, style")) continue;
          const hasText = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
          const isField = /^(INPUT|SELECT|TEXTAREA)$/.test(el.tagName);
          if ((hasText || isField) && parseFloat(getComputedStyle(el).fontSize) < 23.5) small.push(`${label(el)} ${getComputedStyle(el).fontSize}`);
          const style = el.getAttribute("style") || "";
          const cls = typeof el.className === "string" ? el.className : "";
          if (/\dpx/.test(style) || /\dpx\]/.test(cls)) px.push(label(el));
        }
        return {
          overflow: document.documentElement.scrollWidth - innerWidth,
          slopZones: document.querySelectorAll("[data-slop]").length,
          small, px,
        };
      });
      const problems = [];
      if (r.overflow > 0) problems.push(`horizontal overflow ${r.overflow}px`);
      if (r.small.length) problems.push(`${r.small.length} small text: ${r.small.slice(0, 4).join("; ")}`);
      if (r.px.length) problems.push(`${r.px.length} px values: ${r.px.slice(0, 4).join("; ")}`);
      if (name === "landing-fixed" ? r.slopZones > 0 : r.slopZones === 0) problems.push(`slop zones: ${r.slopZones}`);
      if (errors.length) problems.push(`JS errors: ${errors.join("; ")}`);
      console.log(`${problems.length ? "FAIL" : "ok  "} ${width} ${name}${problems.length ? "\n     " + problems.join("\n     ") : ""}`);
      failures += problems.length ? 1 : 0;
      await page.close();
    }
  }
  await browser.close();
  server.close();
  console.log(failures ? `\n${failures} page checks failed` : "\nall example checks passed");
  process.exit(failures ? 1 : 0);
})();
