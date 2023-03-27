import openpyxl

def iterating_over_values(path, sheet_name, cell_range):
    workbook = openpyxl.load_workbook(filename=path)
    if sheet_name not in workbook.sheetnames:
        print(f'{sheet_name} not found.')
        return
    sheet = workbook[sheet_name]

    for col in sheet[cell_range]:
        for cell in col:
            if isinstance(cell, openpyxl.cell.cell.MergedCell):
                continue
            print(f'{cell.column_letter}{cell.row} = {cell.value}')
if __name__ == '__main__':
    iterating_over_values('books.xlsx', 'books', 'B2:C6')