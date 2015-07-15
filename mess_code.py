#encoding:utf8

"""Python如何解决中文网页乱码"""
import urllib2
import sys
import chardet

req =urllib2.Request("http://www.baidu.com/")##这里可以换成http://www.163.com,http://www.sohu.com
content = urllib2.urlopen(req).read()
typeEncode = sys.getfilesystemencoding()##系统默认编码
infoencode =chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
html =content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
print html

