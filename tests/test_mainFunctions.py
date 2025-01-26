import os
import pytest
from pathlib import Path
from components import mainFunctions as mf

def test_create_folder(tmp_path):
    """Test that create_folder() actually creates the given folder."""
    test_dir = tmp_path / "test_folder"
    assert not test_dir.exists()
    mf.create_folder(str(test_dir))
    assert test_dir.exists()

def test_folder_size(tmp_path):
    """Test folder_size() returns correct size in KB."""
    test_dir = tmp_path / "test_folder2"
    mf.create_folder(str(test_dir))

    # Create a small file (1KB of data)
    file_path = test_dir / "dummy.txt"
    with open(file_path, "wb") as f:
        f.write(b'X' * 1024)

    result = mf.folder_size(str(test_dir))
    # Should be around 1KB. We'll just check if the substring is in the output
    assert "1.0 KB" in result or "1.0" in result

def test_get_percentage_difference():
    """Check the logic for get_percentage_difference."""
    # original_size=100, new_size=50 => saves 100%
    diff = mf.get_percentage_difference(num_a=100, num_b=50)
    assert diff == 100.0

    # original=50, new=100 => -50% (i.e., the new is bigger by 50%)
    diff = mf.get_percentage_difference(num_a=50, num_b=100)
    assert diff == -50.0
