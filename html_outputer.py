# -*- coding: utf-8 -*-
from urllib import request

class HtmlOutputer():
    def __init__(self):
        self.datas = []
        
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        
    def output_html(self):
        
        #添加了encoding='utf-8'解决标题和简介乱码问题
        with open('output.html', 'w', encoding='utf-8') as fout:
        
            fout.write("<html>")
            #fout.write("<head><meta http-equiv=\"content-type\" content=\" \
            #text/html;charset=utf-8\"></head>")
            fout.write("<body>")
            fout.write("<table>")
            
            for data in self.datas:
                fout.write("<tr>")
                #使用unquote()解决url输出乱码问题
                #fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % request.unquote(data['url']))
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'])
                fout.write("</tr>")
            
            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")
        
        
