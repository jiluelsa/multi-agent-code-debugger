from agents.code_analyzer import CodeAnalyzer
from agents.bug_finder import BugFinder
from agents.refactor_agent import RefactorAgent
from agents.test_runner import TestRunner
from utils.file_manager import save_code


def run_pipeline(input_code: str) -> dict:
    """
    Full pipeline: analyze → detect bugs → refactor → save → test
    """
    # 1. Analyze
    analyzer = CodeAnalyzer()
    analysis = analyzer.run(input_code)

    # 2. Find bugs
    bug_agent = BugFinder()
    bugs = bug_agent.run(input_code)

    # 3. Refactor
    refactor_agent = RefactorAgent()
    refactored = refactor_agent.run(input_code, bugs)

    # 4. SAVE refactored code to workspace/my_code.py
    # == THIS is what makes pytest use the fixed version ==
    save_code(refactored)

    # 5. Run tests
    tester = TestRunner()
    test_results = tester.run_tests()

    return {
        "analysis": analysis,
        "bugs": bugs,
        "refactored_code": refactored,
        "tests": test_results
    }
