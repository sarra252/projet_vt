# utils/report_generator.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(report_name, articles):
    file_path = f'reports/{report_name}.pdf'
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 750, "TechnoVigilance Report")
    
    y = 700
    for article in articles:
        c.drawString(100, y, f"Title: {article.title}")
        c.drawString(100, y-20, f"Summary: {article.summary[:100]}...")
        y -= 60
    
    c.save()
    return file_path
