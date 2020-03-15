# 操作excel表格数据

# 方式一：xlrd

### 获取数据

1、pip install xlrd 进行安装该模块

2、获取 excel：table = xlrd.open_workbook(file_name)

3、获取 sheet 中的数据：data = table.sheet_by_index(sheet_id), 此处可以有多种获取方式，可自行查看

4、获取单元格内容：value = data.cell_value(row,col) ，根据行和列获取

### 写入数据

1、pip install xlutils 模块

2、引入 copy:from xlutils.copy import copy

3、table = xlrd.open_workbook(file_name)        //打开要写入的 excel
   write_data = copy(table)               //copy 一份
   sheet_data = write_data.get_sheet(0)      //获取要操作的 sheet
   sheet_data.write(row,col,value)       //按照行和列进 u 行写入
   write_data.save(filename)       //保存文件

## 注意
使用 xlrd 写入的 excel 后，原先是 .xlsx 后缀的不能被打开，必须要将后缀改为 .xls 后才能打开

# 

