import openpyxl as excel

def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = (firstCol[cell].value)#.encode('utf-8')
        lst.append(contact)
    return lst
