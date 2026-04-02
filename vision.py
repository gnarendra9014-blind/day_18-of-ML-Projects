import os, base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def get_image_type(image_path: str) -> str:
    ext = image_path.lower().split(".")[-1]
    types = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "gif": "gif", "webp": "webp"}
    return types.get(ext, "jpeg")

def describe_diagram(image_path: str) -> str:
    image_data = encode_image(image_path)
    image_type = get_image_type(image_path)

    res = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{image_type};base64,{image_data}"
                    }
                },
                {
                    "type": "text",
                    "text": """Analyze this whiteboard/diagram image in detail.
Describe:
1. What type of diagram is this (flowchart, class diagram, wireframe, etc.)
2. All boxes, shapes, and their labels
3. All arrows and connections between elements
4. Any text written on the diagram
5. The overall logic or flow being represented
Be very specific and detailed."""
                }
            ]
        }],
        max_tokens=600,
    )
    return res.choices[0].message.content