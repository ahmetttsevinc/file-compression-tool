import sys
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                           QHBoxLayout, QFileDialog, QLabel, QWidget, QProgressBar)
from PyQt5.QtCore import Qt
from compressor import Compressor

class CompressionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.compressor = Compressor()
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('File Compression Tool')
        self.setGeometry(100, 100, 600, 400)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create widgets
        self.status_label = QLabel('Select a file or directory to compress/decompress')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Create buttons
        compress_file_btn = QPushButton('Compress File')
        decompress_file_btn = QPushButton('Decompress File')
        compress_dir_btn = QPushButton('Compress Directory')
        
        # Create progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        
        # Add widgets to layout
        layout.addWidget(self.status_label)
        layout.addWidget(compress_file_btn)
        layout.addWidget(decompress_file_btn)
        layout.addWidget(compress_dir_btn)
        layout.addWidget(self.progress_bar)
        
        # Connect buttons to functions
        compress_file_btn.clicked.connect(self.compress_file)
        decompress_file_btn.clicked.connect(self.decompress_file)
        compress_dir_btn.clicked.connect(self.compress_directory)
        
    def compress_file(self):
        """Handle file compression."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File to Compress",
            "",
            f"Supported Files ({' '.join('*' + ext for ext in self.compressor.supported_extensions)})"
        )
        
        if file_path:
            try:
                compressed_path = self.compressor.compress_file(file_path)
                self.status_label.setText(f'Successfully compressed: {compressed_path}')
            except Exception as e:
                self.status_label.setText(f'Error: {str(e)}')
                
    def decompress_file(self):
        """Handle file decompression."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File to Decompress",
            "",
            "Compressed Files (*.gz)"
        )
        
        if file_path:
            try:
                decompressed_path = self.compressor.decompress_file(file_path)
                self.status_label.setText(f'Successfully decompressed: {decompressed_path}')
            except Exception as e:
                self.status_label.setText(f'Error: {str(e)}')
                
    def compress_directory(self):
        """Handle directory compression."""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Directory to Compress"
        )
        
        if dir_path:
            try:
                compressed_files = self.compressor.compress_directory(dir_path)
                self.status_label.setText(
                    f'Successfully compressed {len(compressed_files)} files in directory'
                )
            except Exception as e:
                self.status_label.setText(f'Error: {str(e)}') 