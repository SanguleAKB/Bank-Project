from google import genai
from google.genai import types

def generate(complaint, category):
    client = genai.Client(
        vertexai=True,
        project="main-instance-452911",  
        location="us-central1",  
    )

    si_text1 = """You are the Response Agent of AIComplaintHub, an AI-driven system for handling customer complaints. Your task is to write the body of a professional, polite letter to the customer based on their complaint and its classified category. Use these inputs:

- Complaint: "[Insert customer complaint here]"
- Category: [Insert category here, e.g., 'credit_card']

Write only the body of the letter (no salutation or closing) with these guidelines:
1. Thank the customer for reaching out.
2. Acknowledge their issue by briefly referencing the complaint.
3. Assure them the complaint is forwarded to the appropriate department (e.g., "Credit Card Department" for 'credit_card') for resolution "as soon as possible."
4. Keep the tone empathetic and concise."""

    model = "gemini-2.0-flash-001"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"Complaint: {complaint}. Category: {category}")
            ]
        )
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=2,
        top_p=0.95,
        max_output_tokens=8192,
        response_modalities=["TEXT"],
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
            types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
            types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
        ],
        system_instruction=[types.Part.from_text(text=si_text1)],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.text:
            response_text += chunk.text
    return response_text