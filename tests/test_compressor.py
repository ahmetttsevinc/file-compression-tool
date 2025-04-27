import os
import pytest
from pathlib import Path
from compression.compressor import Compressor

@pytest.fixture
def compressor():
    return Compressor()

@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as f:
        f.write("Test content for compression")
    return file_path

@pytest.fixture
def test_dir(tmp_path):
    # Create test directory with multiple files
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    
    # Create test files with different extensions
    files = [
        ("test1.txt", "Content 1"),
        ("test2.csv", "Content 2"),
        ("test3.json", "Content 3"),
        ("test4.exe", "Content 4"),  # Unsupported extension
    ]
    
    for filename, content in files:
        with open(dir_path / filename, "w") as f:
            f.write(content)
            
    return dir_path

def test_compress_file(compressor, test_file):
    """Test single file compression."""
    compressed_path = compressor.compress_file(test_file)
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.gz')

def test_decompress_file(compressor, test_file):
    """Test file decompression."""
    # First compress the file
    compressed_path = compressor.compress_file(test_file)
    
    # Then decompress it
    decompressed_path = compressor.decompress_file(compressed_path)
    assert os.path.exists(decompressed_path)
    
    # Check if content matches
    with open(test_file) as f1, open(decompressed_path) as f2:
        assert f1.read() == f2.read()

def test_compress_directory(compressor, test_dir):
    """Test directory compression."""
    compressed_files = compressor.compress_directory(test_dir)
    
    # Should compress only supported files
    assert len(compressed_files) == 3  # .txt, .csv, .json files
    
    # Check if all compressed files exist
    for compressed_file in compressed_files:
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.gz')

def test_unsupported_file_type(compressor, tmp_path):
    """Test compression of unsupported file type."""
    unsupported_file = tmp_path / "test.exe"
    with open(unsupported_file, "w") as f:
        f.write("Test content")
        
    with pytest.raises(ValueError):
        compressor.compress_file(unsupported_file)

def test_nonexistent_file(compressor):
    """Test compression of non-existent file."""
    with pytest.raises(FileNotFoundError):
        compressor.compress_file("nonexistent.txt")

def test_nonexistent_directory(compressor):
    """Test compression of non-existent directory."""
    with pytest.raises(NotADirectoryError):
        compressor.compress_directory("nonexistent_dir") 