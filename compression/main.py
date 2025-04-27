import sys
from PyQt6.QtWidgets import QApplication
from gui import CompressionGUI

def main():
    """Main entry point of the application."""
    app = QApplication(sys.argv)
    window = CompressionGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 