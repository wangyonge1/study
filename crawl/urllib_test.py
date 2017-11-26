#-*- coding:utf-8 -*-

import urllib2,cookielib,re
from bs4 import BeautifulSoup

# url = 'https://www.baidu.com'
# print '第一种方法'
# response1=urllib2.urlopen(url)
# print response1.getcode()
# print len(response1.read())

# print '第二种方法'
# request = urllib2.Request(url)
# request.add_header('user-agent','Mozilla/5.0')
# response2=urllib2.urlopen(request)
# print response2.getcode()
# print len(response2.read())

# print '第三种方法'
# cj=cookielib.CookieJar()
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
# response3=urllib2.urlopen(url)
# print response3.getcode()
# print cj
# print response3.read()

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup= BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
links=soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print '获取第二个url'
link_node=soup.find('a',href='http://example.com/lacie',string=re.compile(r'Laci'))
print link_node.name,link_node['href'],link_node.get_text()

print '正则匹配'
link_node1=soup.find('a',href=re.compile(r'lli'))
print link_node1.name,link_node1['href'],link_node1.get_text()

print 'p段落文字'
p_node=soup.find('p',class_="title")
print p_node.name,p_node.get_text()