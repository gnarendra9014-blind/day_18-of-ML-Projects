import os, re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_code(description: str, language: str = "python") -> str:
    prompt = f"""You are an expert {language} developer.
Based on this diagram description, generate complete working {language} code.

Diagram description:
{description}

Requirements:
- Generate complete, runnable {language} code
- Include all classes, functions, and logic shown in the diagram
- Add brief comments explaining each section
- Make it production-quality code
- Return ONLY the code, no explanation

Generate the {language} code now:"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
    )
    code = res.choices[0].message.content.strip()
    code = re.sub(r'```\w*\n?', '', code)
    code = re.sub(r'```', '', code)
    return code.strip()

def save_code(code: str, language: str, image_name: str) -> str:
    ext = "py" if language == "python" else "js"
    base = os.path.splitext(image_name)[0]
    output_path = f"{base}_generated.{ext}"
    with open(output_path, "w") as f:
        f.write(code)
    return output_path