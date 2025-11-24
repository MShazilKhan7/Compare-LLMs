from curses import raw
import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from ..utils import extract_python_code

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # adjust if needed
load_dotenv(PROJECT_ROOT / ".env")

# Get API key and model from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLAMA_MODEL = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")  # default if not set

if not GROQ_API_KEY:
    raise EnvironmentError("Set GROQ_API_KEY in .env file")

# Initialize client
client = Groq(api_key=GROQ_API_KEY)

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

def generate_code(prompt: str, max_tokens: int = 4096) -> str:
    """Generate code using Groq-run LLaMA model."""
    completion = client.chat.completions.create(
        model=LLAMA_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.0,
    )
    print("completion is here", completion)
    return extract_python_code(completion.choices[0].message.content)


if __name__ == "__main__":
    print(generate_code("Write a Python function to compute factorial(n)."))
