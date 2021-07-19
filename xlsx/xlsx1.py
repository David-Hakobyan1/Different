import xlsxwriter

anunner=["Hovhannisyan","Smbat","Arami"]
workbook = xlsxwriter.Workbook("im.xlsx")
worksheet = workbook.add_worksheet()
bold = workbook.add_format({"bold":True})
data=("Azganun","Anun","Hayranun")
worksheet.set_column(0, 2, 15)
worksheet.write_row('A1',data,bold)
green_format = workbook.add_format()
green_format.set_bold()
green_format.set_font_color('green')
nerq=1
aj=0
for i in anunner:
    worksheet.write(nerq,aj,i,red_format)
    aj+=1
workbook.close()
