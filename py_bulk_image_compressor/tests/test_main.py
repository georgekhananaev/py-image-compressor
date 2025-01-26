import pytest
import subprocess
import sys
import os

def test_help_flag():
    """
    Ensure the script runs with -h and does not crash.
    We'll capture stdout to verify it contains 'usage' or 'help'.
    """
    cmd = [sys.executable, "main.py", "-h"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage" in result.stdout.lower() or "help" in result.stdout.lower()

@pytest.mark.parametrize("flag", ["-l", "-d"])
def test_missing_required_args(flag):
    """
    Test that missing required argument -l triggers an error.
    We'll check for returncode != 0.
    """
    # When we run the script without -l or incomplete arguments, it should fail
    cmd = [sys.executable, "main.py"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode != 0
    assert "error" in result.stderr.lower()
