from PyPDF2 import PdfFileWriter, PdfFileReader
import io, csv, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from time import strptime

root_path = os.getcwd()
source_path = os.path.join(root_path, 'source')


def date_to_list(date_string):
    date_list = date_string.split('-')
    date_list[1] = strptime(date_list[1], '%b').tm_mon
    date_list[2] = strptime(date_list[2], '%y').tm_year
    return date_list

def csv_to_list(csv_path):
    with open(csv_path, 'r') as csvfile:
        rows = csv.reader(csvfile)
        next(rows)
        student_info_list = []
        for row in rows:
            student_name = row[0]
            birthday = date_to_list(row[1])
            sign_date = date_to_list(row[2])

            student_info_list.append([student_name, birthday, sign_date])

    return student_info_list


def write_pdf(student_info, basefile_path, output_dir_path):
    # student info
    student_name = student_info[0]

    student_bday_day = student_info[1][0]
    student_bday_month = student_info[1][1]
    student_bday_year = student_info[1][2]

    sign_day = student_info[2][0]
    sign_month = student_info[2][1]
    sign_year = student_info[2][2]

    # create "watermark"
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)

    # "waterrmark" student info
    # Student name
    can.drawString(100, 548, student_name)
    # birthdaay
    # day
    can.drawString(310, 548, str(student_bday_day))
    # month
    can.drawString(335, 548, str(student_bday_month))
    # year
    can.drawString(357, 548, str(student_bday_year))

    # "waterrmark" sign date
    can.drawString(308, 453, str(sign_day))
    can.drawString(332, 453, str(sign_month))
    can.drawString(354, 453, str(sign_year))

    can.drawString(695, 437, str(sign_day))
    can.drawString(714, 437, str(sign_month))
    can.drawString(730, 437, str(sign_year))

    can.drawString(320, 72, str(sign_day))
    can.drawString(338, 72, str(sign_month))
    can.drawString(355, 72, str(sign_year))

    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)
    # create the new pdf for the "watermark"
    new_pdf = PdfFileReader(packet)

    # read your basefile PDF
    existing_pdf = PdfFileReader(open(basefile_path, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    output_path = os.path.join(output_dir_path, student_name.replace(' ', '') + '.pdf')
    outputStream = open(output_path, "wb")
    output.write(outputStream)
    outputStream.close()