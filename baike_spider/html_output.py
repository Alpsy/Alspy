# encoding:utf-8
class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        else:
            self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write('<meta charset="UTF-8">')
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %(data['url']).encode('utf-8'))
            fout.write("<td>%s</td>" % (data['title']).encode('utf-8'))
            fout.write("<td>%s</td>" % (data['summary']).encode('utf-8'))
            fout.write('</tr>')

        fout.write("</table>")
        fout.write("</body>")

        fout.write("</html>")


        fout.close()