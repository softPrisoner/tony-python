import re

def regex_test():
    print(re.match("www","www.baidu.com").span())
def regex_test2():
    print(str(re.match("com","www.baidu.com")))
def regex_match():
    line = "Cats are smarter than dogs"
    matchObject = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
    if matchObject:
        print(matchObject.group())
        print(matchObject.group(1))
        print(matchObject.group(2))
    else:
        print("No Match")

def  regex_search(pattern, string):
    re.search(pattern,string,flags=0)
def regex_sub ():
    phone = "2004-959-559 # 这是一个电话号码"
    #删除注释
    num = re.sub(r'#.*$',"",phone)
    print("电话号码",num)
    num = re.sub(r'\D',"",phone)
    print(num)
def regex_repl(matched):
    value = int(matched.group('value'))
    return str(value*2)

def regex_repl_in():
    s="A23G4HFD567"
    print(re.sub(r'(?P<value>\d+)',"double",s))
def regex_compile():
    pattern = re.compile(r'\d+')
    
if __name__ == "__main__":
    #regex_match()
    #regex_sub()
    regex_repl_in()