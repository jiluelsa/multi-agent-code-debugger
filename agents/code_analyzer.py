from utils.context_compactor import summarize_text
from utils.logger import log


class CodeAnalyzer:
    def __init__(self):
        pass

    def run(self, code: str) -> dict:
        """
        Analyze a code file and return a short summary + potential issues.
        """
        summary = summarize_text(code)

        potential_issues = []
        if "print(" in code:
            potential_issues.append("Debug print detected")
        if "==" in code:
            potential_issues.append("Comparison operator found — check logic")
        if "for" in code:
            potential_issues.append("Loop found — consider optimization")

        log("Analyzer", "analysis_complete", {"issues": potential_issues})

        return {
            "summary": summary,
            "potential_issues": potential_issues
        }
