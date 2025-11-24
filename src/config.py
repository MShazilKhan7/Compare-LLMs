import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"
OUTPUTS_DIR = ROOT / "outputs"
TESTS_DIR = ROOT / "tests"
RESULTS_DIR = ROOT / "results"


# API keys and endpoints via environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


# Groq config for LLaMA
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLAMA_MODEL = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")


# Runner config
RUN_TIMEOUT = int(os.getenv("RUN_TIMEOUT", "6")) # seconds per test run
PYTHON_BIN = os.getenv("PYTHON_BIN", sys.executable)


# Output CSV
RESULTS_CSV = RESULTS_DIR / "evaluation.csv"