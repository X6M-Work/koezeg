import subprocess
import sys


def test_unknown_cow_exits_with_error():
    res = subprocess.run(
        [sys.executable, "-m", "koezeg", "-f", "paard", "Hallo"],
        capture_output=True,
        text=True,
    )
    assert res.returncode == 1
    assert "Onbekende koe: paard" in res.stdout or "Onbekende koe: paard" in res.stderr
    assert "Beschikbare koeien:" in res.stdout or "Beschikbare koeien:" in res.stderr


def test_known_cow_succeeds():
    res = subprocess.run(
        [sys.executable, "-m", "koezeg", "-f", "koe", "Hallo"],
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0
    assert "Hallo" in res.stdout
