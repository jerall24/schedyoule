# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("position_descriptions.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(0, 0)) 

# new_entry = models.Role(request.form["title"], request.form["text"])
#     db.session.add(new_entry)
#     db.session.commit()