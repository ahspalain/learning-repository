import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>