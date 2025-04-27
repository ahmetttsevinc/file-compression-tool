from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT

def create_project_report():
    doc = SimpleDocTemplate(
        "project_report.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Justify',
        alignment=TA_JUSTIFY
    ))
    
    # Title
    elements.append(Paragraph("File Processing Tool", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Group Members
    elements.append(Paragraph("Group Members", styles['Heading1']))
    elements.append(Paragraph("Ahmet Sevinç (2001833)", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Project Description
    elements.append(Paragraph("Project Description", styles['Heading1']))
    description = """
    The File Processing Tool is a desktop application designed to efficiently handle file compression and decompression
    operations. It provides a user-friendly graphical interface that allows users to compress individual files or entire
    folders, as well as decompress previously compressed files. The tool supports various file formats and implements
    robust error handling to ensure reliable operation.
    """
    elements.append(Paragraph(description, styles['Justify']))
    elements.append(Spacer(1, 12))
    
    # Implemented Features
    elements.append(Paragraph("Implemented Features", styles['Heading1']))
    features = [
        "Single file compression using gzip algorithm",
        "Batch compression of folders",
        "File decompression capability",
        "Support for multiple file formats (.txt, .csv, .json, .xml, .log)",
        "Modern graphical user interface using PyQt5",
        "Comprehensive error handling and user feedback",
        "Cross-platform compatibility",
    ]
    for feature in features:
        elements.append(Paragraph(f"• {feature}", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Technologies Used
    elements.append(Paragraph("Technologies and Libraries", styles['Heading1']))
    tech_data = [
        ["Technology", "Purpose"],
        ["Python 3.8+", "Core programming language"],
        ["PyQt5", "Graphical user interface framework"],
        ["gzip", "File compression algorithm"],
        ["pytest", "Testing framework"],
        ["pathlib", "File system operations"],
        ["typing", "Type hints and annotations"],
    ]
    tech_table = Table(tech_data, [4*inch, 3*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(tech_table)
    elements.append(Spacer(1, 12))
    
    # Challenges and Solutions
    elements.append(Paragraph("Challenges and Solutions", styles['Heading1']))
    challenges = [
        ("Cross-platform Compatibility", """
        Challenge: Ensuring consistent file path handling across different operating systems.
        Solution: Implemented pathlib for platform-independent path manipulation."""),
        
        ("Error Handling", """
        Challenge: Graceful handling of various error scenarios (invalid files, permissions, etc.).
        Solution: Implemented comprehensive try-except blocks and user-friendly error messages."""),
        
        ("User Interface Design", """
        Challenge: Creating an intuitive and responsive interface.
        Solution: Utilized PyQt5's layout management system and implemented progress feedback."""),
    ]
    for title, desc in challenges:
        elements.append(Paragraph(title, styles['Heading2']))
        elements.append(Paragraph(desc, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Code Snippets
    elements.append(Paragraph("Code Snippets", styles['Heading1']))
    code_sample = '''
    def pack_single(self, source_path: Union[str, Path]) -> str:
        """Pack a single file using gzip algorithm."""
        input_path = Path(source_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Unable to locate file: {input_path}")
            
        if input_path.suffix not in self.allowed_formats:
            raise ValueError(f"Format not supported: {input_path.suffix}")
            
        result_path = str(input_path) + '.gz'
        
        with open(input_path, 'rb') as source, gzip.open(result_path, 'wb') as target:
            shutil.copyfileobj(source, target)
                
        return result_path
    '''
    elements.append(Preformatted(code_sample, styles['Code']))
    elements.append(Spacer(1, 12))
    
    # References
    elements.append(Paragraph("References", styles['Heading1']))
    references = [
        "Python Documentation - https://docs.python.org/",
        "PyQt5 Documentation - https://www.riverbankcomputing.com/static/Docs/PyQt5/",
        "gzip Module Documentation - https://docs.python.org/3/library/gzip.html",
    ]
    for ref in references:
        elements.append(Paragraph(f"• {ref}", styles['Normal']))
    
    # Build the PDF
    doc.build(elements)

if __name__ == '__main__':
    create_project_report() 