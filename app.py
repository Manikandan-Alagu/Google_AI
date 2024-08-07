
import os
import gradio as gr
import google.generativeai as genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)
genai.configure(api_key=GEMINI_API_KEY)

def model(input):
    
    # Create the model
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
      # safety_settings = Adjust safety settings
      # See https://ai.google.dev/gemini-api/docs/safety-settings
      system_instruction="give the response in friendly tone",
    )

    chat_session = model.start_chat(
      history=[
          
      ]
    )

    response = chat_session.send_message(input)

    return response.text



demo = gr.Interface(fn=model, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch()