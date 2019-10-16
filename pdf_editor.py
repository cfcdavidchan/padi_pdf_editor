#!/usr/bin/env python
# coding: utf-8
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image

# coach info
info = open("./source/coach_info.txt","r") 
info = info.readlines()
coach_name = info[0].replace('\n','')
padi_code = info[1].replace('\n','')
dive_shop_code = info[2].replace('\n','')
signature = ImageReader('./source/signature.png')

# signature day,month,year
sign_day = 16
sign_month = 10
sign_year = 2019

# student info
student_name = "Handsome Fung"
# birthday
student_bday_day = 30
student_bday_month = 2
student_bday_year = 2046


packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)

#Coach Name
can.drawString(100, 465, coach_name)
can.drawString(68, 453, padi_code)
can.drawString(190, 453, dive_shop_code)

can.setFont('Helvetica', 10)
can.drawString(227, 73, padi_code)
can.drawString(580, 437, padi_code)

# sign date
can.drawString(308, 453, str(sign_day))
can.drawString(332, 453, str(sign_month))
can.drawString(354, 453, str(sign_year))

can.drawString(695, 437, str(sign_day))
can.drawString(714, 437, str(sign_month))
can.drawString(730, 437, str(sign_year))

can.drawString(320, 72, str(sign_day))
can.drawString(338, 72, str(sign_month))
can.drawString(355, 72, str(sign_year))

#Student name
can.drawString(100, 548, student_name)
#birthdaay
# day
can.drawString(310, 548, str(student_bday_day))
# month
can.drawString(335, 548, str(student_bday_month))
# year
can.drawString(357, 548, str(student_bday_year))


can.drawImage(signature, 250, 465, width=20, height=15)
can.drawImage(signature, 470, 437, width=17, height=12)

can.save()
#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("./source/org_pdf.PDF", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
#add the next page
output.addPage(existing_pdf.getPage(1))
# finally, write "output" to a real file
outputStream = open("tmp.pdf", "wb")
output.write(outputStream)
outputStream.close()

