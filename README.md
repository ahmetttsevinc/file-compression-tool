# File Compression Tool

## Project Title
**File Compression Tool**

## Purpose and Objectives
The purpose of this project is to develop a user-friendly tool that enables efficient compression and decompression of files, optimizing storage space and facilitating easier file transfers.

### Key Objectives
- Develop a core compression and decompression mechanism utilizing fundamental algorithms.
- Implement Object-Oriented Programming (OOP) principles to ensure modularity and scalability.
- Utilize file operations and exception handling for robust and error-free functionality.
- Ensure cross-platform compatibility so that users across different operating systems can benefit from the tool.
- Integrate a graphical user interface (GUI) using PyQt6 to enhance usability.

## Group Member and Roles
- **Ahmet Sevinç (2001833)** — Sole Developer  
Responsible for all aspects of the project, including design, development, testing, and implementation.

## Features
- File compression and decompression using gzip algorithm
- Support for multiple file types (.txt, .csv, .json, .xml, .log)
- Batch compression of directories
- Error handling for safe operations
- Modern and user-friendly GUI interface
- Cross-platform compatibility (Windows, macOS, Linux)

## Project Structure
```
file-compression-tool/
├── compression/
│   ├── __init__.py
│   ├── compressor.py    # Core compression logic
│   ├── gui.py          # GUI implementation
│   └── main.py         # Application entry point
├── tests/
│   └── test_compressor.py  # Unit tests
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Technologies Used
- **Python 3.8+**
- **PyQt6** for GUI
- **pytest** for testing
- Standard libraries: `os`, `sys`, `shutil`, `gzip`, `pathlib`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-compression-tool.git
   cd file-compression-tool
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python compression/main.py
   ```

2. Using the GUI:
   - Click "Compress File" to compress a single file
   - Click "Decompress File" to decompress a .gz file
   - Click "Compress Directory" to compress all supported files in a directory

## Running Tests
To run the test suite:
```bash
pytest tests/
```

For test coverage report:
```bash
coverage run -m pytest tests/
coverage report
```

## Supported File Types
- .txt (Text files)
- .csv (Comma-separated values)
- .json (JSON files)
- .xml (XML files)
- .log (Log files)

## Error Handling
The application handles various error cases:
- Unsupported file types
- Non-existent files or directories
- Invalid compression formats
- File access permissions

## Future Improvements
- Add support for more compression algorithms (zip, rar, 7z)
- Implement compression ratio selection
- Add progress tracking for large files
- Include file encryption options
- Add batch decompression for directories
