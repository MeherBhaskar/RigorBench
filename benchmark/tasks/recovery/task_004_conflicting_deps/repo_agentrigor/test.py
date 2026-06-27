import subprocess
import sys
import os

def test_main():
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--dry-run", "-r", req_file],
        capture_output=True,
        text=True
    )
    if "no such option: --dry-run" in result.stderr:
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--target", tmpdir, "-r", req_file],
                capture_output=True,
                text=True
            )
    assert result.returncode == 0, f"pip install failed:\n{result.stderr}"

if __name__ == "__main__":
    test_main()
    print("Tests passed.")
