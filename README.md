# cardsandempires.com

Temporary landing page for Cards & Empires, published with GitHub Pages at <https://cardsandempires.com>.

Static HTML and CSS, plus one small script (`lang.js`) that sends visitors of the main page to their browser's language and remembers a language chosen in the selector. No external fonts, scripts or assets; the Content Security Policy allows only files from this site. Images: the brand mark and the background artwork in `assets/art/`, provided by the project owner for this page. Third-party artwork must not be added here without documented rights.

The page exists in six languages (`/` in English, plus `/pt-br/`, `/es/`, `/fr/`, `/de/` and `/ru/`). Edit the texts in `tools/build.py` and run `python3 tools/build.py` to regenerate every `index.html`.
