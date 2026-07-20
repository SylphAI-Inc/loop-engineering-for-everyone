#!/usr/bin/env python3
"""Assemble slides/index.json + slides/*.html into a single offline HTML file."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOADER = ROOT / "beyond-loop-engineering.html"
INDEX = ROOT / "slides" / "index.json"
OUT = ROOT / "beyond-loop-engineering.assembled.html"


def main() -> None:
    loader = LOADER.read_text()
    style = re.search(r"<style>(.*?)</style>", loader, re.S).group(1)
    index = json.loads(INDEX.read_text())
    enabled = [s for s in index.get("slides", []) if s.get("enabled", True)]

    articles = []
    for i, entry in enumerate(enabled):
        html = (ROOT / "slides" / entry["file"]).read_text().strip()
        # ensure only the article
        m = re.search(r"<article[\s\S]*?</article>", html)
        if not m:
            raise SystemExit(f"No <article> in {entry['file']}")
        article = m.group(0)
        if i == 0:
            if 'class="slide title-slide"' in article:
                article = article.replace(
                    'class="slide title-slide"',
                    'class="slide title-slide active"',
                    1,
                )
            elif 'class="slide"' in article:
                article = article.replace('class="slide"', 'class="slide active"', 1)
        else:
            article = article.replace(" active", "")
        articles.append(article)

    slides_js = json.dumps(
        [{"id": s.get("id"), "file": s.get("file"), "title": s.get("title")} for s in enabled]
    )

    out = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Loop Engineering For Everyone — V1 Deck</title>
  <style>{style}</style>
</head>
<body>
  <main class="deck-shell">
    <section class="deck" id="deck-root" aria-label="Loop Engineering For Everyone V1 deck">
{chr(10).join(articles)}
    </section>

    <nav class="deck-controls" aria-label="Slide navigation">
      <button class="control-button" type="button" data-action="prev" aria-label="Previous slide">‹</button>
      <button class="control-button" type="button" data-action="next" aria-label="Next slide">›</button>
      <div class="progress-track" aria-hidden="true"><div class="progress-fill"></div></div>
      <div class="status" aria-live="polite">01 / {len(enabled):02d}</div>
    </nav>
  </main>

  <script>
    (() => {{
      const slides = Array.from(document.querySelectorAll('.slide'));
      const fill = document.querySelector('.progress-fill');
      const status = document.querySelector('.status');
      const prevButton = document.querySelector('[data-action="prev"]');
      const nextButton = document.querySelector('[data-action="next"]');
      const querySlide = Number(new URLSearchParams(window.location.search).get('slide'));
      let current = Number.isFinite(querySlide) && querySlide >= 1 && querySlide <= slides.length ? querySlide - 1 : 0;
      window.__deckIndex = {{ slides: {slides_js} }};

      function render() {{
        slides.forEach((slide, index) => {{
          slide.classList.toggle('active', index === current);
          slide.setAttribute('aria-hidden', index === current ? 'false' : 'true');
          const footer = slide.querySelector('.slide-foot span');
          if (footer) {{
            footer.textContent = `${{String(index + 1).padStart(2, '0')}} / ${{String(slides.length).padStart(2, '0')}}`;
          }}
        }});
        const rolePanel = slides[current].querySelector('.bridge-role-panel');
        if (rolePanel) rolePanel.classList.remove('is-swapped');
        fill.style.width = `${{((current + 1) / slides.length) * 100}}%`;
        status.textContent = `${{String(current + 1).padStart(2, '0')}} / ${{String(slides.length).padStart(2, '0')}}`;
        prevButton.disabled = current === 0;
        nextButton.disabled = current === slides.length - 1;
        document.title = `(${{current + 1}}/${{slides.length}}) Loop Engineering For Everyone`;
      }}

      function goTo(index) {{
        current = Math.max(0, Math.min(slides.length - 1, index));
        render();
      }}

      function next() {{
        const rolePanel = slides[current].querySelector('.bridge-role-panel');
        if (rolePanel && !rolePanel.classList.contains('is-swapped')) {{
          rolePanel.classList.add('is-swapped');
          return;
        }}
        goTo(current + 1);
      }}

      function prev() {{ goTo(current - 1); }}

      prevButton.addEventListener('click', prev);
      nextButton.addEventListener('click', next);
      window.addEventListener('keydown', (event) => {{
        if (event.altKey || event.ctrlKey || event.metaKey) return;
        if (event.key === 'ArrowRight' || event.key === ' ') {{
          event.preventDefault();
          next();
        }} else if (event.key === 'ArrowLeft') {{
          event.preventDefault();
          prev();
        }} else if (event.key === 'Home') {{
          event.preventDefault();
          goTo(0);
        }} else if (event.key === 'End') {{
          event.preventDefault();
          goTo(slides.length - 1);
        }}
      }});

      window.__loopEngineeringDeck = {{
        goToSlide: (slideNumber) => goTo(Number(slideNumber) - 1),
        next,
        prev,
        getState: () => ({{ current: current + 1, total: slides.length }})
      }};

      render();
    }})();
  </script>
</body>
</html>
"""
    OUT.write_text(out)
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(enabled)} slides)")


if __name__ == "__main__":
    main()
