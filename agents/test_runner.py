from tools.code_executor import run_pytests
from utils.logger import log


class TestRunner:
    def __init__(self):
        pass

    def run_tests(self, target_dir: str = "workspace") -> dict:
        result = run_pytests(target_dir)
        log("TestRunner", "tests_run", result)
        return result
