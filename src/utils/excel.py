import pandas as pd

def readExcelFileData(fileDir: str, sheetName: str): 
    data = pd.read_excel(fileDir, sheet_name=sheetName)
    return data

def readCsvFileData(fileDir: str):
    data = pd.read_csv(fileDir).to_numpy()
    return data
