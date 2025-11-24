import uuid
import re
from pathlib import Path

def write_output(task_id: str, model_name: str, content: str, outputs_dir: Path):
    task_dir = outputs_dir / f"task_{task_id:02d}"
    task_dir.mkdir(parents=True, exist_ok=True)
    filename = task_dir / f"{model_name}.py"
    filename.write_text(content)
    return filename


def extract_python_code(text: str) -> str:
    """
    Extract only the Python code block from a model response.
    """
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if not match:
        raise ValueError("No Python code block found in model response.")
    return match.group(1).strip()



def safe_filename(name: str) -> str:
    return name.replace(" ", "_").lower()