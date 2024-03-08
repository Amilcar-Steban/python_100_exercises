from openpyxl import Workbook
from openpyxl.styles import Font

book = Workbook()
sheet = book.active
sheet["A1"] = "Lista de numeros"

for i in range(1, 11):
    sheet[f"A{i+1}"] = i

book.save("Prueba.xlsx")