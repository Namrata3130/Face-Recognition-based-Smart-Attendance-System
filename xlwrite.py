import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path

'''style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
'''

def output(filename, sheet, present_students):
    my_file = Path(f'Report/{filename}{datetime.now().date()}.xls')

    if my_file.is_file():
        rb = open_workbook(f'Report/{filename}{datetime.now().date()}.xls')
        book = copy(rb)
        sh = book.get_sheet(0)
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)

        # Set up styles
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                             num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

        # Write header
        sh.write(0, 0, datetime.now().date(), style1)
        sh.write(1, 0, 'Name', style0)
        sh.write(1, 1, 'Present', style0)

    # Write present students to the sheet
    for i, student in enumerate(present_students):
        sh.write(i + 2, 0, student)
        sh.write(i + 2, 1, 'Present')

    # Save the workbook
    fullname = f'{filename}{datetime.now().date()}.xls'
    book.save(f'Report/{fullname}')
    return fullname


