// Tailwind play-CDN config: map utility colors to the gallery tokens.
window.tailwind = window.tailwind || {};
tailwind.config = {
  theme: {
    extend: {
      colors: {
        bg: "var(--bg)", surface: "var(--surface)", ink: "var(--ink)", muted: "var(--muted)",
        line: "var(--line)", accent: "var(--accent)", bad: "var(--bad)", good: "var(--good)", codebg: "var(--code-bg)",
      },
      fontFamily: { sans: ["IBM Plex Sans", "system-ui", "sans-serif"], mono: ["IBM Plex Mono", "ui-monospace", "monospace"] },
    },
  },
};

// Shared header: same on every gallery page, current page marked, primary action at the right end.
const PAGES = [
  ["index.html", "Overview"],
  ["structure.html", "Structure"],
  ["surfaces.html", "Surfaces"],
  ["type.html", "Type"],
  ["copy.html", "Copy"],
  ["motion.html", "Motion"],
  ["behavior.html", "Behavior"],
];

function renderHeader() {
  const host = document.getElementById("site-header");
  if (!host) return;
  const last = location.pathname.split("/").pop();
  const here = last.endsWith(".html") ? last : "index.html";
  const links = PAGES.map(([href, label]) => {
    const current = here === href || (href === "index.html" && here === "");
    return `<a class="nav-link" href="${href}"${current ? ' aria-current="page"' : ""}>${label}</a>`;
  }).join("");
  host.className = "site-header";
  host.innerHTML = `
    <div class="wrap flex flex-wrap items-center gap-x-3 gap-y-1" style="padding-block:0.5rem">
      <a href="index.html" class="font-semibold no-underline whitespace-nowrap mr-auto">Slop Specimens</a>
      <button type="button" id="theme-toggle" class="btn" aria-label="Toggle theme">Theme</button>
      <a class="btn btn-primary whitespace-nowrap" href="landing-slop.html">Landing demo</a>
      <nav aria-label="Pages" class="w-full min-w-0 overflow-x-auto flex">${links}</nav>
    </div>`;
}

// Theme toggle: explicit choice wins over the OS setting.
function initTheme() {
  const root = document.documentElement;
  let saved = null;
  try { saved = localStorage.getItem("slop-theme"); } catch (e) {}
  if (saved) root.dataset.theme = saved;
  const btn = document.getElementById("theme-toggle");
  if (!btn) return;
  const isDark = () => root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  const label = () => { btn.textContent = isDark() ? "Light" : "Dark"; };
  label();
  btn.addEventListener("click", () => {
    root.dataset.theme = isDark() ? "light" : "dark";
    try { localStorage.setItem("slop-theme", root.dataset.theme); } catch (e) {}
    label();
  });
}

// Copy buttons: copy on first click; only the clicked button says "Copied".
function initCopy() {
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    const original = btn.textContent;
    btn.addEventListener("click", async () => {
      const text = btn.dataset.copy;
      try { await navigator.clipboard.writeText(text); }
      catch (e) {
        const code = btn.closest(".pop, .copy-row")?.querySelector("code");
        if (code) { const r = document.createRange(); r.selectNodeContents(code); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
      }
      btn.textContent = "Copied";
      setTimeout(() => { btn.textContent = original; }, 1400);
    });
  });
}

// Keep popovers and pin tips inside the viewport: shift them left or right as needed.
function clampInto(anchor, layer) {
  layer.style.left = "0";
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
  const gutter = rem, vw = document.documentElement.clientWidth;
  const a = anchor.getBoundingClientRect(), w = layer.getBoundingClientRect().width;
  const ideal = layer.classList.contains("tip") ? a.left + a.width / 2 - w / 2 : a.left;
  const left = Math.max(gutter, Math.min(ideal, vw - gutter - w));
  layer.style.left = `${(left - a.left) / rem}rem`;
}
function initClamp() {
  document.querySelectorAll(".pop-wrap, .pin").forEach((anchor) => {
    const layer = anchor.querySelector(".pop, .tip");
    if (!layer) return;
    const run = () => requestAnimationFrame(() => clampInto(anchor, layer));
    anchor.addEventListener("mouseenter", run);
    anchor.addEventListener("focusin", run);
  });
}

document.addEventListener("DOMContentLoaded", () => { renderHeader(); initTheme(); initCopy(); initClamp(); });
