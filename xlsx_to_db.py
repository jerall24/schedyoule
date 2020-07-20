# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("position_descriptions.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 


# loop through all rows to read in
for row in range(2, 3):
    new_entry = models.Role(int(sheet.cell_value(row, 0)), \ 
                sheet.cell_value(row, 1), \
                sheet.cell_value(row, 2), \
                sheet.cell_value(row, 3), \
                sheet.cell_value(row, 4), \
                sheet.cell_value(row, 5), \
                sheet.cell_value(row, 6), \
                sheet.cell_value(row, 7), \ 
                sheet.cell_value(row, 8), \
                sheet.cell_value(row, 9), \ 
                sheet.cell_value(row, 10), \
                sheet.cell_value(row, 11), \
                sheet.cell_value(row, 12) == "Yes", \ 
                sheet.cell_value(row, 13)== "Y", \
                sheet.cell_value(row, 14)== "Yes", \
                sheet.cell_value(row, 15), \
                sheet.cell_value(row, 16), \
                sheet.cell_value(row, 17), \
                sheet.cell_value(row, 18), \
                sheet.cell_value(row, 19), \
                sheet.cell_value(row, 20), \
                sheet.cell_value(row, 21), \
                sheet.cell_value(row, 22), \
                int(sheet.cell_value(row, 23)), \
                int(sheet.cell_value(row, 24)), \
                sheet.cell_value(row, 25), \
                sheet.cell_value(row, 26), \
                sheet.cell_value(row, 27), \
                sheet.cell_value(row, 28), \
                sheet.cell_value(row, 29), \ 
                sheet.cell_value(row, 30), \
                sheet.cell_value(row, 31), \
                sheet.cell_value(row, 32), \
                sheet.cell_value(row, 33), \
                sheet.cell_value(row, 34), \
                sheet.cell_value(row, 35), \
                sheet.cell_value(row, 36), \
                sheet.cell_value(row, 37), \
                int(sheet.cell_value(row, 38)))
#   db.session.add(new_entry)
# db.session.commit()

# EXAMPLE
# new_entry = models.Role(3145054, \
#             "New", \
#             "", \
#             "Any Location Globally", \
#             "Hong Kong", \
#             "Greater China", \
#             "", \
#             "UBS", \
#             "UBS AG Zürich - Securities", \
#             "Hong Kong", \
#             "Financial Services > FS Europe OU > FS Europe ASGR", \
#             "David,Frederick Ryan C.", \
#             True, True, False, \
#             "Spring Application Framework-11-Manila", \
#             "Act as software detectives, provide a dynamic service identifying and solving issues within multiple components of critical business systems.", \
#             "IDC/PDC Scheduling", '2019-11-21', "ABA", \
#             '2020-05-03', '2021-03-30', "Open - In Process", \
#             0, 0, \
#             "Software Engineering", "Application Support Engineer", "Hong Kong", \
#             "Technology", \
#             "No Technology Category", \
#             "No Technology Specialization", \
#             "", \
#             "", \
#             "Technology > No Technology Category > No Technology Specialization", \
#             " 1 - Java Enterprise Edition (P3 - Advanced) | 2 - Spring Application Framework (P3 - Advanced)", "Aquino,Carlo Antonio Soriano", "", \
#             "David,Frederick Ryan C.", \
#             0)
