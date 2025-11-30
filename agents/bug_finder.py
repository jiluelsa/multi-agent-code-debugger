from utils.logger import log


class BugFinder:
    def __init__(self):
        pass

    def run(self, code: str) -> list:
        """
        Very simple rule-based bug finder.
        You can later upgrade this to an LLM-powered agent.
        """
        bugs = []

        if "print(" in code:
            bugs.append("Debug print found.")

        if "==" in code:
            bugs.append("Possible comparison usage.")

        if "except:" in code:
            bugs.append("Bare except detected.")

        log("BugFinder", "bugs_detected", {"count": len(bugs)})
        return bugs
