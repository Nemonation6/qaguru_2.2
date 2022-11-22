import os
import csv
from PyPDF2 import PdfReader
from io import TextIOWrapper
from zipfile import ZipFile
import openpyxl


def create_zipfile():
    if os.path.exists('resources/testzip.zip'):
        os.remove('resources/testzip.zip')
    with ZipFile('resources/testzip.zip', mode='x') as myzip:
        myzip.write('./resources/testpdf.pdf', arcname='pdf_file.pdf')
        myzip.write('./resources/file_1000.xlsx', arcname='xlsx_file.xlsx')
        myzip.write('./resources/annual-survey.csv', arcname='csv_file.csv')


def verify_pdf_file():
    with ZipFile('resources/testzip.zip', mode='r') as myzip:
        with myzip.open('pdf_file.pdf', 'r') as mypdf:
            reader = PdfReader(mypdf)
            page = reader.pages[0]
            assert 'Тест 1' in page.extractText(), 'pdf сбоит'


def verify_csv_file():
    with ZipFile('resources/testzip.zip', mode='r') as myzip:
        with myzip.open('csv_file.csv', 'r') as mycsv:
            reader = csv.reader(TextIOWrapper(mycsv, 'utf-8'))
            i = 0
            for line_no, line in enumerate(reader, 1):
                if line_no == 10000:
                    assert 'Wood Product Manufacturing' in line, 'line should be 10000'


def verify_xlsx_file():
    with ZipFile('resources/testzip.zip', mode='r') as myzip:
        with myzip.open('xlsx_file.xlsx', 'r') as myxlsx:
            wb = openpyxl.load_workbook(myxlsx)
            ws = wb.active
            assert ws.cell(40,4).value == 'Female'


create_zipfile()
verify_pdf_file()
verify_csv_file()
verify_xlsx_file()