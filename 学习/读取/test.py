# -*- coding: utf-8
import xlrd


def core():
  worksheet1 = xlrd.open_workbook('test.xlsx')
  worksheet2 = xlrd.open_workbook('test1.xlsx')   #打开excel文件
  sheet_names= worksheet1.sheet_names()    #获取excel中所有工作表名
  print(sheet_names)
  sheet1 = worksheet1.sheet_by_name('Sheet1')    #根据Sheet名获取数据
  sheet2 = worksheet2.sheet_by_index(0)     #根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
  num = min(sheet1.nrows,sheet2.nrows)
  for row_index in range(num):
    value_in_sheet1 = sheet1.cell(row_index, 0).value
    value_in_sheet2 = sheet2.cell(row_index, 0).value
    print('sheet1:%s , sheet2:%s , equal: %s' % (value_in_sheet1, value_in_sheet2, value_in_sheet1==value_in_sheet2))
    pass
  pass


if __name__ == '__main__':
  core()