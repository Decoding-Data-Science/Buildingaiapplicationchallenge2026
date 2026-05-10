# Python Tutor Bot

Python Tutor Bot is a beginner-friendly educational AI app built with **Python**, **Gradio**, and the **OpenAI Python SDK**.

It helps learners:
- Understand Python concepts
- Debug code and errors
- Practice with quizzes
- Improve code quality

## Features

- Clean Gradio interface
- Four learning modes:
  - Explain Concept
  - Debug Code
  - Quiz Me
  - Improve Code
- Reusable prompt templates (`prompts.py`)
- Error handling for empty input and missing API key
- Simple modular structure for beginners

## Project Structure

- `app.py` — Gradio UI and main logic
- `prompts.py` — Prompt templates and prompt builder
- `requirements.txt` — Dependencies
- `.env` — Store your OpenAI API key

## Setup

1. **Clone the repo** and open the project folder.
2. **Create a virtual environment** (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\\Scripts\\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set your API key** in `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Run the App

```bash
python app.py
```

Then open the local Gradio URL shown in your terminal.

## Notes for Beginners

- Start with **Explain Concept** mode to learn basics.
- Use **Debug Code** by pasting both your code and error message.
- In **Quiz Me**, you can ask for topics like `loops`, `functions`, or `dictionaries`.
- In **Improve Code**, paste your code and review suggestions step by step.
