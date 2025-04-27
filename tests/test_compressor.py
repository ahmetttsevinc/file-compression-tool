import os
import pytest
from pathlib import Path
from compression.compressor import FileProcessor

@pytest.fixture
def processor():
    return FileProcessor()

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    with open(file_path, "w") as f:
        f.write("Sample content for processing")
    return file_path

@pytest.fixture
def sample_folder(tmp_path):
    # Prepare test folder with various files
    folder_path = tmp_path / "sample_folder"
    folder_path.mkdir()
    
    # Create files with different formats
    test_files = [
        ("doc1.txt", "Content A"),
        ("data1.csv", "Content B"),
        ("config1.json", "Content C"),
        ("binary1.exe", "Content D"),  # Unsupported format
    ]
    
    for filename, content in test_files:
        with open(folder_path / filename, "w") as f:
            f.write(content)
            
    return folder_path

def test_pack_single(processor, sample_file):
    """Verify single file packing."""
    result_path = processor.pack_single(sample_file)
    assert os.path.exists(result_path)
    assert result_path.endswith('.gz')

def test_unpack_single(processor, sample_file):
    """Verify file unpacking."""
    # First pack the file
    packed_path = processor.pack_single(sample_file)
    
    # Then unpack it
    result_path = processor.unpack_single(packed_path)
    assert os.path.exists(result_path)
    
    # Verify content integrity
    with open(sample_file) as f1, open(result_path) as f2:
        assert f1.read() == f2.read()

def test_pack_folder(processor, sample_folder):
    """Verify folder processing."""
    result_files = processor.pack_folder(sample_folder)
    
    # Should process only supported formats
    assert len(result_files) == 3  # txt, csv, json files
    
    # Verify all processed files
    for result_file in result_files:
        assert os.path.exists(result_file)
        assert result_file.endswith('.gz')

def test_invalid_format(processor, tmp_path):
    """Verify handling of invalid format."""
    invalid_file = tmp_path / "test.exe"
    with open(invalid_file, "w") as f:
        f.write("Test content")
        
    with pytest.raises(ValueError):
        processor.pack_single(invalid_file)

def test_missing_file(processor):
    """Verify handling of missing file."""
    with pytest.raises(FileNotFoundError):
        processor.pack_single("nonexistent.txt")

def test_missing_folder(processor):
    """Verify handling of missing folder."""
    with pytest.raises(NotADirectoryError):
        processor.pack_folder("nonexistent_folder") 