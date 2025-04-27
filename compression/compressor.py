import os
import gzip
import shutil
from typing import Union, List
from pathlib import Path

class Compressor:
    """Main class for handling file compression and decompression operations."""
    
    def __init__(self):
        self.supported_extensions = ['.txt', '.csv', '.json', '.xml', '.log']
    
    def compress_file(self, file_path: Union[str, Path]) -> str:
        """
        Compress a single file using gzip compression.
        
        Args:
            file_path: Path to the file to be compressed
            
        Returns:
            str: Path to the compressed file
            
        Raises:
            FileNotFoundError: If the input file doesn't exist
            ValueError: If the file type is not supported
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if file_path.suffix not in self.supported_extensions:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")
            
        output_path = str(file_path) + '.gz'
        
        with open(file_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                
        return output_path
    
    def decompress_file(self, file_path: Union[str, Path]) -> str:
        """
        Decompress a gzip compressed file.
        
        Args:
            file_path: Path to the compressed file
            
        Returns:
            str: Path to the decompressed file
            
        Raises:
            FileNotFoundError: If the input file doesn't exist
            ValueError: If the file is not a gzip file
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if not str(file_path).endswith('.gz'):
            raise ValueError("File must be a gzip file (.gz extension)")
            
        output_path = str(file_path)[:-3]  # Remove .gz extension
        
        with gzip.open(file_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                
        return output_path
    
    def compress_directory(self, dir_path: Union[str, Path]) -> List[str]:
        """
        Compress all supported files in a directory.
        
        Args:
            dir_path: Path to the directory
            
        Returns:
            List[str]: List of paths to compressed files
            
        Raises:
            NotADirectoryError: If the input path is not a directory
        """
        dir_path = Path(dir_path)
        if not dir_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {dir_path}")
            
        compressed_files = []
        for file_path in dir_path.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.supported_extensions:
                try:
                    compressed_file = self.compress_file(file_path)
                    compressed_files.append(compressed_file)
                except Exception as e:
                    print(f"Error compressing {file_path}: {str(e)}")
                    
        return compressed_files 