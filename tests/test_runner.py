import subprocess

def test_behave():
    result = subprocess.run(["behave"], capture_output=True, text=True)
    assert result.returncode == 0, f"Behave tests failed:\n{result.stdout}\n{result.stderr}"
