import os
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
from ..utils import extract_python_code
# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise EnvironmentError("Set GEMINI_API_KEY in .env file")

# Configure API key
genai.configure(api_key=GEMINI_API_KEY)


SYSTEM_INSTRUCTION = """
You are a code generator.
Return ONLY Python code.
Wrap the output in triple backticks like:

```python
# code here
```

No explanation. No text outside the code block. 
Only valid Python code, including function docstrings or # comments.
"""

def generate_code(prompt: str, max_output_tokens: int = 4096) -> str:
    """
    Generates code using the Gemini model with a system instruction.
    """
    model = genai.GenerativeModel(GEMINI_MODEL, system_instruction=SYSTEM_INSTRUCTION)

    response = model.generate_content(
        
        contents=[
            # Only user/model roles go here
            {"role": "user", "parts": [{"text": prompt}]},
        ],
        generation_config={
            "temperature": 0.0,
            "max_output_tokens": max_output_tokens,
        }
    )
    print("response is here", response)
    return extract_python_code(response.text)


# if __name__ == "__main__":
#     p = PROJECT_ROOT / "tasks" / "01_fibonacci.txt"
#     prompt = p.read_text()
#     print(generate_code(prompt, max_output_tokens=2048))
