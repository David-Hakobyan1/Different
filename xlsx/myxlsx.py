import xlsxwriter
workbook = xlsxwriter.Workbook("my1.xlsx")
worksheet = workbook.add_worksheet()
bold = workbook.add_format({"bold":True,"font_color":"red"})
data=("Taretiv","Azganun","Anun","Hayranun","Masnagitutyun")
worksheet.set_column(0, 4, 15)
worksheet.write_row('A1',data,bold)
green_format = workbook.add_format()
green_format.set_bold()
green_format.set_font_color('green')
f=open("file.txt")
fc = f.read().strip().split("\n")
lis=[]
def Cragravorox():
    for i in fc:
        if "Cragravorox" in i:
            lis.append(i)
            
    for j in i:
        print(j)
Cragravorox()

