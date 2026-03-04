from openai import OpenAI
import base64
import os
import streamlit as st

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(st.secrets.get("openai", {}).get("key"))

def analyze_ui(image_path):

    with open(image_path, "rb") as img:
        base64_image = base64.b64encode(img.read()).decode()

    prompt = '''
Analyze this UI screenshot from a product demo.

Identify:
- UI components
- layout structure
- navigation elements

Generate:
1. Wireframe (ASCII)
2. Component list
'''

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"user",
                "content":[
                    {"type":"text","text":prompt},
                    {"type":"image_url","image_url":{"url":f"data:image/png;base64,{base64_image}"}}
                ]
            }
        ]
    )

    return response.choices[0].message.content
