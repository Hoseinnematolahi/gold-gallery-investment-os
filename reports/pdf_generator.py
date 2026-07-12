from reportlab.pdfgen import canvas



def create_report(filename,text):


    pdf=canvas.Canvas(filename)


    pdf.drawString(
    50,
    800,
    text
    )


    pdf.save()
