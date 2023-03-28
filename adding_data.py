from openpyxl import Workbook

def create_workbook(path):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Book Name"
    sheet["B1"] = "Author"
    sheet["C1"] = "Year of publishing"
    data = [
        ['Book 1', 'Author 1', 2023],
        ['Book 2', 'Author 2', 2022],
        ['Book 3', 'Author 3', 2021]
    ]
    for row in data:
        sheet.append(row)
    workbook.save(path)

if __name__ == '__main__':
    create_workbook('my_book_collection.xlsx')