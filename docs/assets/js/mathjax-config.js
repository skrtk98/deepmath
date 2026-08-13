window.MathJax = {
  loader: {
    paths: {
      // Keep core script local, but fetch optional components from official CDN.
      mathjax: "https://cdn.jsdelivr.net/npm/mathjax@3/es5"
    },
    load: ['ui/lazy', '[tex]/mathtools']
  },
  tex: {
    packages: {'[+]': ['mathtools']},
    inlineMath: [['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  }
};
