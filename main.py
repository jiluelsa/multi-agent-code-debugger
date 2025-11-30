from agents.code_analyzer import CodeAnalyzer
from agents.bug_finder import BugFinder
from agents.refactor_agent import RefactorAgent
from agents.test_runner import TestRunner
from utils.file_manager import load_code, save_code


def main():
    print("\n=== Multi-Agent Debugger System ===\n")

    # Load the code
    code = load_code()
    print("Loaded code.\n")

    # Run analyzer
    analyzer = CodeAnalyzer()
    analysis = analyzer.run(code)
    print("Analysis:", analysis, "\n")

    # Find bugs
    bug_finder = BugFinder()
    bugs = bug_finder.run(code)
    print("Bugs Found:", bugs, "\n")

    # Refactor
    refactor_agent = RefactorAgent()
    improved_code = refactor_agent.run(code, bugs)
    save_code(improved_code)
    print("Refactored code saved.\n")

    # Run tests
    test_runner = TestRunner()
    results = test_runner.run_tests()
    print("Test Results:\n", results)


if __name__ == "__main__":
    main()
