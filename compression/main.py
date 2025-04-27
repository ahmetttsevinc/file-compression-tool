import sys
from PyQt5.QtWidgets import QApplication
from compression.gui import ProcessorInterface

def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    window = ProcessorInterface()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 