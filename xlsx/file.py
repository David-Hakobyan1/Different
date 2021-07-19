import xlsxwriter

workbook = xlsxwriter.Workbook("im.myxlsxwriter")
worksheet = workbook.add_worksheet()
bold = workbook.add_format({"bold":True})
data=("Azganun","Anun","Hayranun")
worksheet.set_column(0, 2, 15)
worksheet.write_row('A1',data,bold)

#def open_file():
 #   with open("file.txt") as f:
#        return f.read().strip().split("\n")

#def my_lis(my_file):
 #   lis = []
  #  for el in my_file:
   #     lis.append(el.split())
    #return lis

#def my_xlsxw(my_list):
 #   for i in my_list:
  #      step=0
   #     step1=-1
    #    for j in i:
     #       step1+=1
      #      worksheet.write(step,step1,str(j))
#    workbook.close()

#def main():
 #   my_file = open_file()
  #  my_list = my_lis(my_file)
   # my_xlsx = my_xlsxw(my_list)
    #print(my_xlsx)
#main()
