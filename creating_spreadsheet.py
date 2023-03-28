from openpyxl import Workbook

def create_workbook(path):
    workbook = Workbook()
    workbook.save(path)

if __name__ == '__main__':
    create_workbook('my_book_collection.xlsx')