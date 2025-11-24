from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze




def compute_code_metrics(code_text: str):
    try:
        complexity = cc_visit(code_text)
        mi = mi_visit(code_text, True)
        raw = analyze(code_text)
        loc = raw.loc
        return {
        "cyclomatic_scores": complexity, # list of objects
        "maintainability_index": mi,
        "loc": loc,
        }
    except Exception as e:
        return {"error": str(e)}