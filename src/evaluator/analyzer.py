import csv
from pathlib import Path
from ..config import OUTPUTS_DIR, RESULTS_CSV
from .runner import run_file_with_input
from .metrics import compute_code_metrics
from .tasks_io import TASK_IO  # <-- import the dictionary

def evaluate_all(tasks_count: int = None):
    rows = []

    for task_dir in sorted(OUTPUTS_DIR.glob('task_*')):
        task_id = int(task_dir.name.split('_')[1])
        task_key = str(task_id)
        task_io = TASK_IO.get(task_key, None)

        for model_file in task_dir.glob('*.py'):
            model_name = model_file.stem
            print(f"Evaluating {task_dir}/{model_file.name}")

            # Get input for this task, fallback to default '10' if not defined
            if task_io:
                task_input = task_io['input']
            else:
                task_input = '10'
            print("task_input", task_input)
            run_res = run_file_with_input(model_file, task_input)
            code_text = model_file.read_text()
            code_metrics = compute_code_metrics(code_text)
            print("run_res", run_res)
            row = {
                'task_id': task_id,
                'model': model_name,
                'returncode': run_res['returncode'],
                'stdout': run_res['stdout'],
                'stderr': run_res['stderr'],
                'runtime': run_res['runtime'],
                'memory': run_res['memory'],
                'loc': code_metrics.get('loc'),
                'maintainability_index': code_metrics.get('maintainability_index'),
                # 'expected_output': task_io['expected_output'] if task_io else None,
                # 'passed': run_res['stdout'] == str(task_io['expected_output']) if task_io else None
            }
            rows.append(row)

    print("Rows", rows)

    # write CSV
    RESULTS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote results to {RESULTS_CSV}")


if __name__ == '__main__':
    print("Starting evaluation...")
    evaluate_all()
