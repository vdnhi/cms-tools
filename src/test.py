from utils.excel import readExcelFileData
from utils.data_parser import getListAccount
import os

SAMPLE_EXCEL_FILE = "../files/sample.xls"
SHEET_NAME = "thuandp"

def test():
    fileDir = os.path.abspath(SAMPLE_EXCEL_FILE)
    data = readExcelFileData(fileDir, SHEET_NAME)
    listAccount = getListAccount(data, "Account", "Password")

if __name__ == '__main__':
    test()