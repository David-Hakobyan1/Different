import xlsxwriter

workbook = xlsxwriter.Workbook('chartsheet.xlsx')
worksheet = workbook.add_worksheet()
chartsheet = workbook.add_chartsheet()
bold = workbook.add_format({'bold': 1})
headings = ['Number', 'Batch 1', 'Batch 2']
data = [[2, 3, 4, 5, 6, 7],[10, 40, 50, 20, 10, 50],[30, 60, 70, 50, 40, 30],]
worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])
chart1 = workbook.add_chart({'type': 'bar'})
chart1.add_series({'name':       '=Sheet1!$B$1','categories': '=Sheet1!$A$2:$A$7','values':     '=Sheet1!$B$2:$B$7',})
chart1.add_series({'name':       ['Sheet1', 0, 2],'categories': ['Sheet1', 1, 0, 6, 0],'values':     ['Sheet1', 1, 2, 6, 2],})
chart1.set_title ({'name': 'Results of sample analysis'})
chart1.set_x_axis({'name': 'Test number'})
chart1.set_y_axis({'name': 'Sample length (mm)'})
chart1.set_style(11)
chartsheet.set_chart(chart1)
chartsheet.activate();
workbook.close()
