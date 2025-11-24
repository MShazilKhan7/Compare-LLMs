# LLM Code Comparison – Gemini 2.5 Flash vs LLaMA-3.3-70B (Groq) 

This project allows you to compare two Large Language Models (LLMs) — **Google Gemini 2.5 Flash** and **Meta LLaMA-3.3-70B** (via Groq) — on their ability to generate source code for different programming tasks.

The system provides a **complete automated pipeline**:

1. You write a task/problem description  
2. Both LLMs generate Python code for the task  
3. The generated code is automatically executed  
4. The system evaluates the code using various metrics  
5. A Streamlit dashboard displays everything neatly  

🚀

## Check out Demo Screenshots [Large Language Models Code Comparison Dashboard (Prototype)](https://mshazilkhandevs.vercel.app/projects/large-language-models-code-comparison-dashboard)

## What This Project Does

| Feature                                 | Description                                                                                                   |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ✅ **Create custom coding tasks**         | Write your own problem statements (e.g., “sort a list”, “find prime numbers”, etc.). Each task is saved as a `.txt` file inside the `tasks/` folder. |
| ✅ **Auto-generate code using two LLMs** | Sends each task prompt to Gemini and LLaMA (Groq) and saves the outputs (e.g., `outputs/task_1/gemini.py`, `outputs/task_1/llama.py`). |
| ✅ **Run evaluation automatically**      | Executes both scripts, measures runtime, memory usage, LOC, maintainability, correctness, etc., and stores results in `results/evaluation.csv`. |
| ✅ **View results inside Streamlit**      | comparison table with Task ID, Model, Runtime, Memory, LOC, Maintainability Index, Errors, Output. |

You get a **complete side-by-side comparison** between Gemini 2.5 Flash and LLaMA-3.3-70B.

## 📁 Folder Structure

```text
project/
├── src/
│   ├── app.py                # Streamlit dashboard
│   ├── orchestrator.py       # Generates code using both models
│   ├── config.py             # Folder paths & settings
│   ├── fetch_llm/
│   │    └── call_gemini.py   # (and call_groq.py, etc.)
│   └── evaluator/
│        ├── analyzer.py      # Runs evaluation
│        ├── metrics.py       # Computes LOC, MI, etc.
│        └── runner.py        # Executes code safely
│
├── tasks/                    # Your task .txt files go here
├── outputs/                  # Generated Python code (one subfolder per task)
├── results/                  # evaluation.csv stored here
└── README.md

| Metric                  | Description                                      |
|-------------------------|--------------------------------------------------|
| Runtime                 | Execution time (seconds)                         |
| Peak Memory Usage       | Maximum RAM consumed (MB)                        |
| Lines of Code (LOC)     | Total lines of generated code                    |
| Maintainability Index   | Standard MI score (higher = better)              |
| Raw Output              | Full stdout from execution                       |
```
## 🧩 How the Pipeline Works

This section explains how the entire code-generation and evaluation pipeline runs inside the project.

---

## 1. Create a Task

You can create tasks in two ways:

- Through the Streamlit UI  
- Or manually by adding a text file inside:

**Example task file content:**
Write a Python function to remove duplicates from a list.

## 2. Generate Code
Click the “Generate Code” button.This runs: run_generation()

## 3. Run Evaluation
Click the “Run Evaluation” button.This runs: run_evaluation()
Executes each generated Python file
Measures performance & quality metrics
Saves everything into results/evaluation.csv

### View Results
The Streamlit dashboard loads the CSV and displays:

Comparison table
Summary metrics
Execution outputs


