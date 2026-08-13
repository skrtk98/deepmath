function wireCalloutCollapse(root = document) {
  const dts = root.querySelectorAll("dt.dm-callout-collapsible");

  for (const dt of dts) {
    if (dt.dataset.dmCalloutCollapseInit === "1") continue;

    const dd = dt.nextElementSibling;
    if (!dd || dd.tagName !== "DD") continue;

    dt.dataset.dmCalloutCollapseInit = "1";
    dt.setAttribute("role", "button");
    dt.setAttribute("tabindex", "0");

    const setOpen = (open) => {
      dd.style.display = open ? "" : "none";
      dt.classList.toggle("dm-callout-open", open);
      dt.classList.toggle("dm-callout-closed", !open);
      dt.setAttribute("aria-expanded", open ? "true" : "false");
    };

    const toggle = () => setOpen(!dt.classList.contains("dm-callout-open"));

    setOpen(dt.classList.contains("dm-callout-open"));

    dt.addEventListener("click", toggle);
    dt.addEventListener("keydown", (ev) => {
      if (ev.key === "Enter" || ev.key === " ") {
        ev.preventDefault();
        toggle();
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", () => wireCalloutCollapse(document));
document.addEventListener("md-content-updated", () => wireCalloutCollapse(document));
if (window.document$?.subscribe) window.document$.subscribe(() => wireCalloutCollapse(document));
