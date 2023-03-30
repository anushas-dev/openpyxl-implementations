from openpyxl import load_workbook

def edit(path, data):
    workbook = load_workbook(filename=path)
    sheet = workbook.active
    for cell in data:
        current_value = sheet[cell].value
        sheet[cell] = data[cell]
        print(f'Changing {current_value} to {data[cell]} for {cell}')
    workbook.save(path)



if __name__ == '__main__':
    data = {"C1": "Mars to Jupiter", "C2": "2090"}
    edit("books.xlsx", data)