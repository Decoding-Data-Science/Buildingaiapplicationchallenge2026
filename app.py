import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from prompts import build_prompt

load_dotenv()


def generate_response(mode: str, user_input: str) -> str:
    """Generate a Python tutoring response based on selected mode and user input."""
    if not user_input or not user_input.strip():
        return "Please enter some text or code so I can help you."

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OPENAI_API_KEY is missing. Add it to your environment or .env file, then restart the app."

    try:
        client = OpenAI(api_key=api_key)
        prompt = build_prompt(mode=mode, user_input=user_input)

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=0.4,
        )
        return response.output_text.strip() or "I could not generate a response. Please try again."
    except Exception as error:
        return f"Something went wrong: {error}"


with gr.Blocks(title="Python Tutor Bot") as demo:
    gr.Markdown("# 🐍 Python Tutor Bot\nLearn Python with explanations, debugging help, quizzes, and code improvements.")

    mode = gr.Dropdown(
        choices=["Explain Concept", "Debug Code", "Quiz Me", "Improve Code"],
        value="Explain Concept",
        label="Choose Mode",
    )
    user_input = gr.Textbox(
        label="Enter your concept, question, code, or error",
        lines=10,
        placeholder="Example: Explain Python lists with examples...",
    )
    output = gr.Textbox(label="Tutor Response", lines=12)

    submit_button = gr.Button("Get Help")
    submit_button.click(fn=generate_response, inputs=[mode, user_input], outputs=output)


if __name__ == "__main__":
    demo.launch()
