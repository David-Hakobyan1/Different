import xlsxwriter

workbook = xlsxwriter.Workbook('my.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({"bold":True,"font_color":"red"})
data=("Taretiv","Azganun","Anun","Hayranun","Masnagitutyun")
worksheet.set_column(0, 4, 15)
worksheet.write_row('A1',data,bold)
green_format = workbook.add_format()
green_format.set_bold()
green_format.set_font_color('green')

def open_file():
    with open("file.txt") as f:
        return f.read().strip().split("\n")

def my_lis(my_file):
    lis = []
    for el in my_file:
        lis.append(el.split())
    return lis

def my_xlsxw(my_list):
    step=0
    for i in my_list:
        step+=1
        step1=-1
        for j in i:
            step1+=1
            if step1==0 and int(j)>1985:
                worksheet.write(step,step1,j,green_format)
            elif step1==4:
                worksheet.write_url(step,step1,j)
            else:
                worksheet.write(step,step1,str(j))
    workbook.close()

def main():
    my_file = open_file()
    my_list = my_lis(my_file)
    my_xlsx = my_xlsxw(my_list)

if __name__=="__main__":
    main()
