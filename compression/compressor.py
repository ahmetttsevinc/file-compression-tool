import os
import gzip
import shutil
from typing import Union, List, Set
from pathlib import Path

class FileProcessor:
    """Core class for handling file operations."""
    
    def __init__(self):
        self.allowed_formats: Set[str] = {'.txt', '.csv', '.json', '.xml', '.log'}
    
    def pack_single(self, source_path: Union[str, Path]) -> str:
        """
        Pack a single file using gzip algorithm.
        
        Args:
            source_path: Location of the file to be packed
            
        Returns:
            str: Location of the packed file
            
        Raises:
            FileNotFoundError: If source file is missing
            ValueError: If file format is not supported
        """
        input_path = Path(source_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Unable to locate file: {input_path}")
            
        if input_path.suffix not in self.allowed_formats:
            raise ValueError(f"Format not supported: {input_path.suffix}")
            
        result_path = str(input_path) + '.gz'
        
        with open(input_path, 'rb') as source, gzip.open(result_path, 'wb') as target:
            shutil.copyfileobj(source, target)
                
        return result_path
    
    def unpack_single(self, source_path: Union[str, Path]) -> str:
        """
        Unpack a gzip packed file.
        
        Args:
            source_path: Location of the packed file
            
        Returns:
            str: Location of the unpacked file
            
        Raises:
            FileNotFoundError: If source file is missing
            ValueError: If not a gzip file
        """
        input_path = Path(source_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Unable to locate file: {input_path}")
            
        if not str(input_path).endswith('.gz'):
            raise ValueError("File must be in gzip format (.gz)")
            
        result_path = str(input_path)[:-3]
        
        with gzip.open(input_path, 'rb') as source, open(result_path, 'wb') as target:
            shutil.copyfileobj(source, target)
                
        return result_path
    
    def pack_folder(self, source_path: Union[str, Path]) -> List[str]:
        """
        Pack all supported files in a folder.
        
        Args:
            source_path: Location of the folder
            
        Returns:
            List[str]: Locations of packed files
            
        Raises:
            NotADirectoryError: If source is not a folder
        """
        input_path = Path(source_path)
        if not input_path.is_dir():
            raise NotADirectoryError(f"Not a valid folder: {input_path}")
            
        processed_files = []
        for file_path in input_path.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.allowed_formats:
                try:
                    packed_file = self.pack_single(file_path)
                    processed_files.append(packed_file)
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
                    
        return processed_files 