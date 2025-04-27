import sys
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                           QHBoxLayout, QFileDialog, QLabel, QWidget, QProgressBar)
from PyQt5.QtCore import Qt
from compression.compressor import FileProcessor

class ProcessorInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.processor = FileProcessor()
        self.setup_interface()
        
    def setup_interface(self):
        """Configure the user interface."""
        self.setWindowTitle('File Processing Tool')
        self.setGeometry(100, 100, 600, 400)
        
        # Setup main container
        main_container = QWidget()
        self.setCentralWidget(main_container)
        main_layout = QVBoxLayout(main_container)
        
        # Setup display elements
        self.info_display = QLabel('Select files or folders for processing')
        self.info_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Setup action buttons
        pack_btn = QPushButton('Pack File')
        unpack_btn = QPushButton('Unpack File')
        folder_btn = QPushButton('Process Folder')
        
        # Setup progress indicator
        self.progress_indicator = QProgressBar()
        self.progress_indicator.setVisible(False)
        
        # Arrange elements
        main_layout.addWidget(self.info_display)
        main_layout.addWidget(pack_btn)
        main_layout.addWidget(unpack_btn)
        main_layout.addWidget(folder_btn)
        main_layout.addWidget(self.progress_indicator)
        
        # Connect actions
        pack_btn.clicked.connect(self.handle_pack)
        unpack_btn.clicked.connect(self.handle_unpack)
        folder_btn.clicked.connect(self.handle_folder)
        
    def handle_pack(self):
        """Process pack file request."""
        source_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose File to Pack",
            "",
            f"Supported Formats ({' '.join('*' + ext for ext in self.processor.allowed_formats)})"
        )
        
        if source_path:
            try:
                result_path = self.processor.pack_single(source_path)
                self.info_display.setText(f'Successfully packed: {result_path}')
            except Exception as e:
                self.info_display.setText(f'Error: {str(e)}')
                
    def handle_unpack(self):
        """Process unpack file request."""
        source_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose File to Unpack",
            "",
            "Packed Files (*.gz)"
        )
        
        if source_path:
            try:
                result_path = self.processor.unpack_single(source_path)
                self.info_display.setText(f'Successfully unpacked: {result_path}')
            except Exception as e:
                self.info_display.setText(f'Error: {str(e)}')
                
    def handle_folder(self):
        """Process folder request."""
        source_path = QFileDialog.getExistingDirectory(
            self,
            "Choose Folder to Process"
        )
        
        if source_path:
            try:
                processed_files = self.processor.pack_folder(source_path)
                self.info_display.setText(
                    f'Successfully processed {len(processed_files)} files in folder'
                )
            except Exception as e:
                self.info_display.setText(f'Error: {str(e)}') 