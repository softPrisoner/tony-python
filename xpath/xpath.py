import xpath
from lxml import etree
# coding:utf-8

import urllib.request
from lxml import etree


def test():
    url = "https://tieba.baidu.com/f?ie=utf-8&kw=%E6%B8%B8%E6%88%8F%E8%B5%9A%E9%92%B1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
               }
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('UTF-8')
    # print(html)
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(html)
    print(content)
    link_list = content.xpath(
        '//li[@class="j_thread_list clearfix"]/div[@class="t_con cleafix"]/div[@class="col2_right j_threadlist_li_right"]/div/div/a')
    print(link_list)
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        print(link)


def xpathTest():
    sx = '''
    <body>
        <h1>title</h1>
        <img src="up.jpg"></img>
        <div>
            fd
            <img src="1.jpg"></img>
        </div>
    </body>
    '''
    exml = etree.XML(sx)
    # x = exml.find('.//div')
    # x=exml.xpath('//div')
    # print(x[0].text)
    # x=exml.xpath('div/img/@src')
    # print(x)
    x = exml.xpath("body")
        


if __name__ == "__main__":
    test()
