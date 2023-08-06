# SKY-EXCEL Module

> excel工具模块



# Part 1. Introduce

> 介绍

如果你不希望每一次需要把接口返回的字典数据导出成excel表格而去设计表头、合并单元格，而进行一次一次重复大量的编程活动。那么你可以尝试一下这个模块。sky-excel把表头设计与单元格设计耦合到一起，你只需要创建一个excel模板即可，然后进行配置对应输入的字段就可以实现，把接口的数据导出单元格。

这个模块仅仅做了一件事情，就是把你写好的表头版本抄写一般，把字典数据按照键值对匹配填充进去即可。

# Part 2. API Document

> API 接口文档

```python
export_instance = ExcelExport(
    input_dict=global_export_data, 
    excel_templet_path="./templet/templet.xlsx", 
    save_path="D:\\PySet/sky-excel/templet/"
)
参数介绍：
input_dict：输入的字典数据，格式是[{..},{..}......]
excel_templet_path:保存模板的路径，确保程序可以找到你的模板excel文件
excel_templet_title:当前仅仅可以导出一个sheet，不可以实现批量的导出。所以需要指定，默认值Sheet1
save_path:保存的文件路径，不传则返回文件流直接返回前端提供下载，注意返回时候需要修改响应头协议

导出方法：
data, err = export_instance.export()
data:返回文件地址，或者文件流。前提是没有异常的情况下，否则返回空。
err:返回的是异常提示
```