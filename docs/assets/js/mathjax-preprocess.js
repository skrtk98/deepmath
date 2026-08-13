function convertMathFences(root = document) {
  // <pre class="language-math"><code>...</code></pre> -> $$...$$
  root.querySelectorAll('pre.language-math > code').forEach(code => {
    const tex = code.textContent;
    const div = document.createElement('div');
    div.textContent = `$$\n${tex}\n$$`;
    code.parentElement.replaceWith(div);
  });
}

function convertInlineDollarCodeDollar(root = document) {
  // $<code>...</code>$ -> \( ... \)
  for (const code of root.querySelectorAll("code")) {
    const prev = code.previousSibling;
    const next = code.nextSibling;
    if (!prev || !next) continue;
    if (prev.nodeType !== Node.TEXT_NODE) continue;
    if (next.nodeType !== Node.TEXT_NODE) continue;

    if (!/\$\s*$/.test(prev.textContent)) continue;
    if (!/^\s*\$/.test(next.textContent)) continue;

    const newPrev = prev.textContent.replace(/\$\s*$/, (m) => m.replace("$", ""));
    const newNext = next.textContent.replace(/^\s*\$/, (m) => m.replace("$", ""));

    const span = document.createElement("span");
    span.textContent = `\\(${code.textContent}\\)`;

    prev.textContent = newPrev;
    next.textContent = newNext;
    code.replaceWith(span);

    if (prev.textContent === "") prev.remove();
    if (next.textContent === "") next.remove();
  }
}

function convertInlineDollarMathToParen(root = document) {
  // code / pre / script 等の中は触らない（壊れる）
  const skip = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEXTAREA", "PRE", "CODE"]);

  const walker = document.createTreeWalker(
    root.body ?? root,
    NodeFilter.SHOW_TEXT,
    {
      acceptNode(node) {
        const p = node.parentNode;
        if (!p || p.nodeType !== Node.ELEMENT_NODE) return NodeFilter.FILTER_REJECT;
        const tag = p.tagName;
        if (skip.has(tag)) return NodeFilter.FILTER_REJECT;
        // 空白だけは無視
        if (!node.nodeValue || node.nodeValue.indexOf("$") === -1) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    }
  );

  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);

  const isEscaped = (s, idx) => {
    let backslashes = 0;
    for (let i = idx - 1; i >= 0 && s[i] === "\\"; i--) backslashes++;
    return (backslashes % 2) === 1;
  };

  function convertSingleDollarOnly(s) {
    let out = "";
    let i = 0;
    const n = s.length;

    while (i < n) {
      if (s[i] !== "$" || isEscaped(s, i)) {
        out += s[i];
        i++;
        continue;
      }

      // Preserve display math $$...$$ as-is.
      if (i + 1 < n && s[i + 1] === "$") {
        const start = i;
        i += 2;
        while (i + 1 < n) {
          if (s[i] === "$" && s[i + 1] === "$" && !isEscaped(s, i)) break;
          i++;
        }
        if (i + 1 < n) {
          out += s.slice(start, i + 2);
          i += 2;
        } else {
          out += s.slice(start);
          break;
        }
        continue;
      }

      const open = i;
      i += 1;
      let close = -1;
      while (i < n) {
        if (s[i] === "$" && !isEscaped(s, i)) {
          if (i + 1 < n && s[i + 1] === "$") {
            i += 2;
            continue;
          }
          close = i;
          break;
        }
        i++;
      }

      if (close < 0) {
        out += s.slice(open);
        break;
      }

      const body = s.slice(open + 1, close);
      if (!body.trim()) {
        out += s.slice(open, close + 1);
      } else {
        out += `\\(${body}\\)`;
      }
      i = close + 1;
    }

    return out;
  }

  for (const textNode of nodes) {
    const s = textNode.nodeValue;
    const replaced = convertSingleDollarOnly(s);

    if (replaced !== s) textNode.nodeValue = replaced;
  }
}

async function typesetMath() {
  const mj = window.MathJax;
  if (!mj) return;

  // Local MathJax bundles can load quickly, but startup may still be pending.
  if (mj.startup?.promise) {
    await mj.startup.promise;
  }

  if (typeof mj.typesetPromise === "function") {
    await mj.typesetPromise();
  }
}

async function runOnce() {
  convertMathFences();
  convertInlineDollarCodeDollar();
  convertInlineDollarMathToParen();    // $...$ → \( ... \)
  await typesetMath();
}

let runQueue = Promise.resolve();
function run() {
  runQueue = runQueue.then(runOnce).catch((err) => {
    console.error("[mathjax-preprocess] failed:", err);
  });
  return runQueue;
}

document.addEventListener("DOMContentLoaded", () => { void run(); });
document.addEventListener("md-content-updated", () => { void run(); });
// Material系/instant loading対策の保険
if (window.document$?.subscribe) {
  window.document$.subscribe(() => { void run(); });
}
window.addEventListener("load", () => { void run(); });
