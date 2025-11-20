Terminal College Game

Run a small curses-based terminal game where you walk a 40x20 ASCII campus, approach buildings, and attain elightenment by answering silly prompts evaluated by Google Gemini (or a local mock). Good answers will grant you degrees and five degrees = enlightenment. 

Quick start

1. Create a virtualenv and install dependencies:

If on Windows, you will need to run 'pip install windows-curses'. I have not tested this. Good luck.

You also need to have a terminal window of proper height/width. I recommend making the terminal window at least half the size of your screen. 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Provide your Gemini API key (or leave blank to use mock):

```bash
cp .env.example .env
# edit .env to set GEMINI_API_KEY
export GEMINI_API_KEY=your_real_key_here
```

3. Run the game:

```bash
python main.py
```

Controls

- Arrow keys: move
- `q`: quit
- When prompted for text, type your answer and press Enter

Notes

- Each degree requires 2 "pass" results to earn.
- You must register at `admin` before attempting degrees.
