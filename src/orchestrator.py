import csv
from pathlib import Path
from .config import TASKS_DIR, OUTPUTS_DIR
from .fetch_llm.call_gemini import generate_code as gemini_generate
from .fetch_llm.call_llama import generate_code as llama_generate
from .utils import write_output




def load_tasks():
    tasks = []
    for p in sorted(TASKS_DIR.glob("*.txt")):
        task_id = int(p.stem.split("_")[0])
        tasks.append((task_id, p.read_text()))
    return tasks




def run_generation():
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    tasks = load_tasks()


    for task_id, desc in tasks:
        print(f"Generating for task {task_id}")
        prompt = "Write Python code to solve the following problem:\n\n" + desc


        gem_code = gemini_generate(prompt)
        print("gemini response done", gem_code)
        llama_code = llama_generate(prompt)


        gem_file = write_output(task_id, "gemini", gem_code, OUTPUTS_DIR)
        llama_file = write_output(task_id, "llama", llama_code, OUTPUTS_DIR)

        print(f"Saved: {gem_file}, {llama_file}")
        # print(f"Saved:  {llama_file}")
        


if __name__ == "__main__":
    run_generation()
    