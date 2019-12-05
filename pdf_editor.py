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
            if any(data.strip() for data in row):
                student_name = row[0]
                birthday = date_to_list(row[1])
                coach_1_start = date_to_list(row[2])
                coach_2_start = date_to_list(row[3])
                coach_2_end = date_to_list(row[4])

                student_info_list.append([student_name, birthday, 
                                          coach_1_start, coach_2_start, coach_2_end])
    
    return student_info_list


def write_pdf(student_info, basefile_path, output_dir_path):
    # student info
    student_name = student_info[0]
    
    student_bday_day = student_info[1][0]
    student_bday_month = student_info[1][1]
    student_bday_year = student_info[1][2]
    
    coach_1_start_day = student_info[2][0]
    coach_1_start_month = student_info[2][1]
    coach_1_start_year = student_info[2][2]
    
    coach_2_start_day = student_info[3][0]
    coach_2_start_month = student_info[3][1]
    coach_2_start_year = student_info[3][2]
    
    coach_2_end_day = student_info[4][0]
    coach_2_end_month = student_info[4][1]
    coach_2_end_year = student_info[4][2]
    
    #create "watermark"
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('Helvetica', 10)
    # "waterrmark" student info
    #Student name
    can.drawString(100, 548, student_name)
    #birthdaay
    # day
    can.drawString(310, 548, str(student_bday_day))
    # month
    can.drawString(335, 548, str(student_bday_month))
    # year
    can.drawString(357, 548, str(student_bday_year))
    
    # "waterrmark" sign date
    # coach_1_start
    can.drawString(308, 453, str(coach_1_start_day))
    can.drawString(332, 453, str(coach_1_start_month))
    can.drawString(354, 453, str(coach_1_start_year))

    can.drawString(695, 437, str(coach_1_start_day))
    can.drawString(714, 437, str(coach_1_start_month))
    can.drawString(730, 437, str(coach_1_start_year))

    can.drawString(320, 72, str(coach_1_start_day))
    can.drawString(338, 72, str(coach_1_start_month))
    can.drawString(355, 72, str(coach_1_start_year))
    
    # coach_2_start
    can.drawString(308, 397, str(coach_2_start_day))
    can.drawString(332, 397, str(coach_2_start_month))
    can.drawString(354, 397, str(coach_2_start_year))
    
    can.drawString(440, 385, str(coach_2_start_day))
    can.drawString(455, 385, str(coach_2_start_month))
    can.drawString(471, 385, str(coach_2_start_year))
    
    can.drawString(440, 372, str(coach_2_start_day))
    can.drawString(455, 372, str(coach_2_start_month))
    can.drawString(471, 372, str(coach_2_start_year))
    
    # coach_2_end
    can.drawString(630, 385, str(coach_2_end_day))
    can.drawString(647, 385, str(coach_2_end_month))
    can.drawString(665, 385, str(coach_2_end_year))
    
    can.drawString(630, 372, str(coach_2_end_day))
    can.drawString(647, 372, str(coach_2_end_month))
    can.drawString(665, 372, str(coach_2_end_year))
    
    can.drawString(695, 163, str(coach_2_end_day))
    can.drawString(715, 163, str(coach_2_end_month))
    can.drawString(732, 163, str(coach_2_end_year))
    
    can.drawString(695, 115, str(coach_2_end_day))
    can.drawString(715, 115, str(coach_2_end_month))
    can.drawString(732, 115, str(coach_2_end_year))
    
    can.drawString(695, 73, str(coach_2_end_day))
    can.drawString(715, 73, str(coach_2_end_month))
    can.drawString(732, 73, str(coach_2_end_year))
    
    can.drawString(695, 41, str(coach_2_end_day))
    can.drawString(715, 41, str(coach_2_end_month))
    can.drawString(732, 41, str(coach_2_end_year))
    
    can.save()
    #move to the beginning of the StringIO buffer
    packet.seek(0)
    #create the new pdf for the "watermark"
    new_pdf = PdfFileReader(packet)
    
    # read your basefile PDF
    existing_pdf = PdfFileReader(open(basefile_path, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    output_path = os.path.join(output_dir_path, student_name.replace(' ','')+'.pdf')
    outputStream = open(output_path, "wb")
    output.write(outputStream)
    outputStream.close()