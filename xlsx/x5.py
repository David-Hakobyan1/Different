import xlsxwriter

workbook = xlsxwriter.Workbook("nor_pie.xlsx")
worksheet = workbook.add_workshet()
chart = workbook.add_chart({"type":"pie"})

data = [["pitanie","ucheba","otdix","dela","son"],[2,9,2,3,8]]
worksheet.write_column("A1",data[0])
worksheet.write_column("B1",data[1])
chart.add_series({"categories":"=Sheet1!A1:A5","values":"Sheet1!B1:B5"})
worksheet.insert_chart("D5",chart)
workbook.close()
