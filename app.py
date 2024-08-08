import os
#import gradio as gr
import google.generativeai as genai

# Configure API key for Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)
genai.configure(api_key=GEMINI_API_KEY)

# Create the model and chat session once
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="give the response in a friendly tone",
)

chat_session = model.start_chat(
    history=[]
)

input = input()

def chat(input):
    response = chat_session.send_message(input)
    return response.text

# Create Gradio interface

#gr.Textbox(placeholder="Let Chat")
#outputs = chat(inputs)
#gr.Textbox()
#demo = gr.Interface(fn=chat, inputs=inputs, outputs=outputs)

# Launch the Gradio interface
#if __name__ == "__main__":
   # demo.launch()
