
# Flask Portfolio - Ready Starter

This is a ready-to-run **Flask** portfolio project that includes:
- Home page with dark-mode toggle and twinkling stars background.
- Projects: Hospital demo, E-commerce demo, Sentiment Analyzer (rule-based).
- Resume download button.
- Contact form that saves submissions to `messages.csv`.
- Responsive layout and smooth scroll + simple CSS animations.

## How to run (locally)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows use `venv\Scripts\activate`
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## Notes
- The sentiment analyzer is a simple rule-based analyzer (no external ML libs) so it works out-of-the-box.
- Contact messages are stored in `messages.csv`.
- Replace `app.secret_key` with a secure random key before deploying publicly.

Made for quick demos and to be extended into production-level apps.
