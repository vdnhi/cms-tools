import argparse
from utils.command import execute_command, make_add_user_command
from utils.excel import readCsvFileData, readExcelFileData
from utils.data_parser import getListAccount

def main():
    argParser = argparse.ArgumentParser(description="""
        Script to add multiple users from excel/csv file to CMS system and specific contest (default file type is excel).
    """)
    argParser.add_argument('-f', '--file-type', type=int, help='File type, 1 - excel/ 2 -csv', default=1)
    argParser.add_argument('file', type=str, help='File location')
    argParser.add_argument('-s', '--sheet-name', type=str, help='Sheet name', default='Sheet 1')
    argParser.add_argument('-u', '--username', type=str, help='Username header', default='Account')
    argParser.add_argument('-p', '--password', type=str, help='Password header', default='Password')
    argParser.add_argument('-r', '--root', help='Sudo or not', action='store_true')
    
    args = argParser.parse_args()
    if args.file_type == 1:
        data = readExcelFileData(args.file, args.sheet_name)
    else:
        data = readCsvFileData(args.file)
    
    listAccount = getListAccount(data, args.username, args.password)
    commands = []
    for user in listAccount:
        commands.append(make_add_user_command(firstname=user.get('username'), username=user.get('username'), password=user.get('password')))
    execute_command(commands)
    
    
    
if __name__ == '__main__':
    main()