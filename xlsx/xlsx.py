# Xlsxwriter )))
import xlsxwriter
workbook=xlsxwriter.Workbook('David.xlsx')
worksheet=workbook.add_worksheet()
faile = open("anunner.txt", "r")
string=faile.read().strip()
sp=string.split("\n")
print(sp)
list1=[]
green_format=workbook.add_format()
green_format.set_pattern(1)
green_format.set_bg_color('#008000')
red_format=workbook.add_format()
red_format.set_pattern(1)
red_format.set_bg_color('#ff0000')
yellow_format=workbook.add_format()
yellow_format.set_pattern(1)
yellow_format.set_bg_color('#ffff00')

for i in sp:
    list1.append(i.split())
step=-1
for i in list1:
    step+=1
    step1=-1
    for j in i:
        step1+=1
        worksheet.set_column(step,step1, 15)
        worksheet.write(step,step1,str(j),yellow_format)

        if str(j)=="Cragravorox":

            worksheet.set_column(step,step1, 15)
            worksheet.write(step,step1,str(j),green_format)
        elif step1==2:
            worksheet.set_column(step,step1, 15)
            worksheet.write(step,step1,str(j),red_format)
workbook.close()
