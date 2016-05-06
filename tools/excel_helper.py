# -*- coding: utf-8 -*-
__author__ = 'luxiao'
import xlsxwriter
from bottle import response
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


class Excel(object):
    """封装了一些excel的操作，包括生成excel文件，excel附件下载的请求"""
    def __init__(self, file_name):
        ext = u'%s.xlsx'
        self.file_name = ext % file_name

    def make_download(self, lines):
        '''在路由端初始化一个ExcelService实例，
        通过调用本实例方法即可生成excel文件下载请求'''
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8'
        content_disposition = 'attachment; filename=%s' % self.file_name
        headers = {'Content-Type': content_type,
                   'Content-Disposition': content_disposition}
        response.headers.update(headers)
        return self.write_stringio(lines)

    def write_stringio(self, lines):
        output = StringIO.StringIO()
        self.write_excel(output, lines)
        output.seek(0)
        return output.read()

    def make_file(self, data):
        self.write_excel(self.file_name, data)

    def write_excel(self, output, lines):
        '''将二维数组lines按行写入到excel，例如：[[1, 2],[3, 4],[5, 6]]，
        output可以是一个文件名，字符串流，字节流'''
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()
        for row, line in enumerate(lines):
            for column, cell in enumerate(line):
                worksheet.write(row, column, cell)
        workbook.close()

if __name__ == '__main__':
    # 生成本地excel文件
    lines = [['A', 'B'],
             [3, 4],
             [u'中文', 'abc']]
    file_name = 'test'
    es = Excel(file_name)
    es.make_file(lines)
