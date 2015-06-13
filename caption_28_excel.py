# coding=utf-8
import xlwt
import xlrd

# 写
workBook = xlwt.Workbook(encoding='utf-8')
bookSheet = workBook.add_sheet('Sheet 1', cell_overwrite_ok=True)
workBook.add_sheet('Sheet 2')
DATA = (('学号', '姓名', '年龄', '性别', '成绩'),
        (1001, 'AAAA', 23, '男', 98),
        (1002, 'BBBB', 21, '女', 90),
        (1003, 'CCCC', 24, '女', 100),
        (1004, 'DDDD', 22, '女', 86),
        (1005, 'EEEE', 25, '女', 88),)

for i, row in enumerate(DATA):
    for j, col in enumerate(row):
        bookSheet.write(i, j, col)
bookSheet.col(0).width = 10
workBook.save('成绩单.xls')

# 读
workBook = xlrd.open_workbook('成绩单.xls')
print "There are {} sheets in the workbook".format(workBook.nsheets)
for bookSheet in workBook.sheets():
    print bookSheet.name
    for row in xrange(bookSheet.nrows):
        for col in xrange(bookSheet.ncols):
            print xlrd.cellname(row, col)
            print bookSheet.cell(row, col).value
