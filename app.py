import streamlit as st
from pathlib import Path
import time
import pandas as pd

# Import your existing orchestrator and evaluator
from src.orchestrator import run_generation
from src.evaluator.analyzer import evaluate_all
from src.config import TASKS_DIR

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(
    page_title="LLM Code Comparison",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧩 LLM Code Comparison Dashboard")
st.markdown(
    """
    This dashboard allows you to:
    1. Create new tasks (saved as text files).
    2. Generate code from tasks using Gemini 2.5 Flash and LLaMA-3.3-70B (Groq).
    3. Evaluate and compare the outputs.
    """
)

st.markdown("---")

# ----------------------------
# Section 1: Create New Task
# ----------------------------
with st.expander("📝 Create a New Task", expanded=True):
    task_text = st.text_area("Write the task/problem description here:", height=150)
    task_name = st.text_input(
        "Task Name (used as file name):", value=f"task_{int(time.time())}"
    )

    if st.button("💾 Create Task"):
        if not task_text.strip():
            st.warning("Please enter task text!")
        else:
            TASKS_DIR.mkdir(parents=True, exist_ok=True)
            file_path = TASKS_DIR / f"{task_name}.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(task_text)
            st.success(f"Task saved as `{file_path}`")
            st.info(f"Total tasks: {len(list(TASKS_DIR.glob('*.txt')))}")

st.markdown("---")

# ----------------------------
# Section 2: Generate Code
# ----------------------------
with st.expander("⚡ Generate Code", expanded=True):
    if st.button("🖥️ Generate Code for All Tasks"):
        with st.spinner("Generating code for all tasks... This may take a while."):
            run_generation()
        st.success("✅ Code generation completed!")

# ----------------------------
# Section 3: Run Evaluation
# ----------------------------
with st.expander("📊 Run Evaluation", expanded=True):
    if st.button("📈 Evaluate All Tasks"):
        with st.spinner("Running evaluation metrics..."):
            evaluate_all()
        st.success("✅ Evaluation completed!")

# ----------------------------
# Section 4: Show Evaluation Results
# ----------------------------
with st.expander("📋 Evaluation Results", expanded=True):
    RESULTS_CSV = Path("results/evaluation.csv")
    if RESULTS_CSV.exists():
        df = pd.read_csv(RESULTS_CSV)

        st.markdown("### Summary Table")
        st.dataframe(df)

        # Show key metrics in columns
        st.markdown("### Metrics Overview")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Tasks", len(df['task_id'].unique()))
        col2.metric("Total Models", len(df['model'].unique()))
        col3.metric("Avg Runtime (s)", round(df['runtime'].mean(), 2))
        col4.metric("Avg LOC", int(df['loc'].mean()))

        st.markdown("You can scroll the table above to see individual task results.")
    else:
        st.info("No evaluation results found yet. Run 'Evaluate All Tasks' first.")

st.markdown("---")
st.caption("Created by Shazil | LLM Code Comparison Project")
