from utils.logger import log
import re

class RefactorAgent:
    def __init__(self):
        pass

    def run(self, code: str, bugs: list) -> str:
        """
        Improved rule-based refactor agent.
        - Removes debug prints
        - Removes developer comments (# BUG, debug notes)
        - Fixes '==' → '+' ONLY in return lines
        """
        new_code = code

        # ---------------------------------------------
        # 1. Remove debug prints
        # ---------------------------------------------
        if "Debug print found." in bugs:
            cleaned_lines = []
            for line in new_code.splitlines():
                if "print(" in line:
                    continue  # remove entire print line
                cleaned_lines.append(line)
            new_code = "\n".join(cleaned_lines)

        # ---------------------------------------------
        # 2. Remove comments like "# BUG:" or similar
        # ---------------------------------------------
        cleaned_lines = []
        for line in new_code.splitlines():
            # Remove anything after "# BUG"
            if "# BUG" in line:
                line = line.split("# BUG")[0].rstrip()
            cleaned_lines.append(line)
        new_code = "\n".join(cleaned_lines)

        # ---------------------------------------------
        # 3. Fix incorrect comparisons: return a == b → return a + b
        #    Only modify return statements
        # ---------------------------------------------
        pattern = r"return\s+(.+)==(.+)"
        replacement = r"return \1+\2"
        new_code = re.sub(pattern, replacement, new_code)

        # ---------------------------------------------
        # 4. Clean empty lines produced by deletions
        # ---------------------------------------------
        while "\n\n\n" in new_code:
            new_code = new_code.replace("\n\n\n", "\n\n")

        new_code = new_code.strip() + "\n"

        # ---------------------------------------------
        log("RefactorAgent", "refactor_done", {"changes": len(bugs)})
        return new_code
