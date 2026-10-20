// "Unsere Geschichte" video slider: endless loop, one video per step,
// previous/next buttons and auto-scroll (pauses while the mouse is over the slider or a control has keyboard focus).
(function () {
  "use strict";

  const root = document.querySelector(".origins");
  if (!root) return;

  const viewport = root.querySelector(".origins-viewport");
  const track = root.querySelector(".origins-track");
  const prevButton = root.querySelector(".origins-prev");
  const nextButton = root.querySelector(".origins-next");
  const main = document.querySelector("main");
  const footer = document.querySelector(".site-footer");

  const originals = Array.from(track.children);
  const count = originals.length;
  const CLONES = 5;       // as many as the most videos visible at once (see --visible in style.css)
  const AUTO_MS = 3000;   // time between two automatic steps
  const MOVE_MS = 500;    // duration of one step
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  if (count < CLONES) return;
  root.classList.add("is-enhanced");

  // Copies at both ends make the loop endless. Hidden from keyboard and screen readers, but NOT inert:
  // when scrolling manually they are visible for a moment and must still react to hover and clicks.
  function clone(item) {
    const copy = item.cloneNode(true);
    copy.setAttribute("aria-hidden", "true");
    copy.querySelector("a").tabIndex = -1;
    return copy;
  }
  const head = document.createDocumentFragment();
  originals.slice(-CLONES).forEach(function (item) { head.appendChild(clone(item)); });
  track.insertBefore(head, track.firstChild);
  const tail = document.createDocumentFragment();
  originals.slice(0, CLONES).forEach(function (item) { tail.appendChild(clone(item)); });
  track.appendChild(tail);

  let index = CLONES;     // position of the first visible video within the track (clones included)
  let moving = false;
  let hovering = false;
  let focused = false;
  let timer = null;

  function stepWidth() {
    // exact (fractional) distance; offsetLeft would round and the error adds up over several steps
    return track.children[1].getBoundingClientRect().left - track.children[0].getBoundingClientRect().left;
  }

  function place(animate) {
    track.style.transition = animate ? "transform " + MOVE_MS + "ms ease" : "none";
    track.style.transform = "translateX(" + (-index * stepWidth()) + "px)";
  }

  // After a step into the copies: jump (without animation) to the identical original
  function settle() {
    if (index >= CLONES + count) index -= count;
    else if (index < CLONES) index += count;
    place(false);
    moving = false;
  }

  function go(delta) {
    if (moving) return;
    moving = true;
    index += delta;
    const animate = !reduceMotion.matches;
    place(animate);
    setTimeout(settle, animate ? MOVE_MS + 30 : 0);
  }

  function updateAutoScroll() {
    clearInterval(timer);
    timer = null;
    if (hovering || focused || reduceMotion.matches) return;
    timer = setInterval(function () {
      if (!document.hidden) go(1);
    }, AUTO_MS);
  }

  prevButton.addEventListener("click", function () { go(-1); updateAutoScroll(); });
  nextButton.addEventListener("click", function () { go(1); updateAutoScroll(); });

  // Pause while the mouse is over the slider (touch taps don't count) or while a control has keyboard focus
  root.addEventListener("pointerenter", function (e) {
    if (e.pointerType === "mouse") { hovering = true; updateAutoScroll(); }
  });
  root.addEventListener("pointerleave", function () { hovering = false; updateAutoScroll(); });
  root.addEventListener("focusin", function (e) {
    focused = e.target.matches(":focus-visible");
    updateAutoScroll();
  });
  root.addEventListener("focusout", function () { focused = false; updateAutoScroll(); });
  reduceMotion.addEventListener("change", updateAutoScroll);

  // Tabbing to a video that is out of view: bring it in, undo the browser's own scrolling
  viewport.addEventListener("scroll", function () { viewport.scrollLeft = 0; });
  track.addEventListener("focusin", function (e) {
    const item = e.target.closest(".origins-item");
    const position = Array.prototype.indexOf.call(track.children, item);
    const visible = Number(getComputedStyle(root).getPropertyValue("--visible")) || 1;
    if (position < index || position > index + visible - 1) {
      index = position;
      place(false);
    }
  });

  // Let the page grow when the slider reaches below the first screen, so it never runs into the footer link
  function fitPage() {
    main.style.minHeight = "";
    const needed = root.getBoundingClientRect().bottom - main.getBoundingClientRect().top +
      (footer ? footer.offsetHeight : 0) + 16;
    if (needed > main.offsetHeight) main.style.minHeight = needed + "px";
  }

  function layout() {
    if (!moving) place(false);
    fitPage();
  }
  new ResizeObserver(layout).observe(viewport);
  window.addEventListener("load", layout);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitPage);

  layout();
  updateAutoScroll();
})();
