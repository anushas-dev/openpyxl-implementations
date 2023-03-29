from openpyxl import load_workbook

def get_cell_info(path):
    workbook = load_workbook(filename=path, data_only=True) 
    # data_only set True for reading cell value and not formula applied
    sheet = workbook.active
    print(sheet)
    print(f'The title of this worksheet is: {sheet.title}')
    print(f'Value of A5 is: { sheet["A5"].value }')
    print(f'Value of B11 is: { sheet["B11"].value }')
    print(f'Value of E14 is { sheet["E14"].value}') # formula applied on column

if __name__ == '__main__':
    get_cell_info('books.xlsx')