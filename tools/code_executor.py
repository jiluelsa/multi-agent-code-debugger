import subprocess
import shlex
from typing import Tuple


def run_command(cmd: str, cwd: str = None, timeout: int = 120) -> Tuple[int, str, str]:
    try:
        proc = subprocess.run(
            shlex.split(cmd),
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as e:
        return -1, "", f"Timeout: {e}"


def run_pytests(target_dir: str = "workspace") -> dict:
    code, out, err = run_command(f"pytest -q {target_dir}")
    return {
        "code": code,
        "stdout": out,
        "stderr": err
    }
