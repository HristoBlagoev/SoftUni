from openpyxl import Workbook

workbook = Workbook()
current_cheet = workbook.active

current_cheet["A1"] = "1"
current_cheet["A2"] = "Python"
current_cheet["B1"] = "2"
current_cheet["B2"] = "SoftUni"
current_cheet["C1"] = "3"
current_cheet["C2"] = "Programing Basics"

workbook.save(filename='example_exel.xlsx')