import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
def encode_req():
    url = "http://baidu.com"
    data = {"username":"admin","password":"123456"}
    req_data = urlencode(data)
    res = urlopen(url+'?'+req_data)
    res=res.read().decode()
    print(res)
#处理post请求,如果传输了data,则为post请求 
from urllib.request import Request
def post_dispatcher():
    url="http://www.baidu.com"
    data={"username":"admin","password":123456}
    data=urlencode(data)
    data.encode("utf-8")
    req_data=Request(url,data)
    with urlopen(req_data) as req:
     res=req.read().decode() #read 方法读取返回的数据内容，decode 是转换返回数据的bytes格式为str
     print(res)