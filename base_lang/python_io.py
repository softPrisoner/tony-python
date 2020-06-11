#-*- coding: UTF-8 -*-
import io
def io_test():
    print("python is good param language")
    in_str = input("请输入")
    print("your input is "+in_str)
def open_test(file_name):
   '''
   t 文本模式 只可以读数据
   x 写模式 如果存在会报异常
   b 二进制模式
   + 可读可写模式
   U 通用换行模式
   r 读模式
   rb+ 以二进制打开一个文件用于只读，文件指针将会放在文件开头，这是默认模式，一般用于非文本文件如图片
   w 打开一个文件用于写入，如果该文件已经存在则打开文件，并从头开始编辑，即原有内容会被删除，如果文件不存在，则创建新文件
   wb 以二进制格式打开一个文件用于写入。如果该文件已经存在，主要用于非文本文件如图片
   w+ 打开一个文件用于读写。如果该文件已经存在则打开文件，并从开头进行编辑，即原有内容会被删除，如果文件不存在，创建新的文件
   wb+ 以二进制打开一个文件用于读写，如果该文件已经存在，则打开文件，并从开头进行编辑，即原有的文件会被删除，如果文件不存在，创建的新文件
   a 打开一个文件的追加，如果文件已经存在,文件指针将会放在文件的末尾，也就是说，新的内容将会被写到已有的内容之后
   ab 以二进制格式打开一个文件用于追加，如果文件存在，文件指针将会放到文件的结尾。也就是说，新的内容会被写入内容之后，如果文件不存在将会创建细腻的文件
   a+ 打开一个文件用于读写。如果该文件已经存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新的文件用于读写
   ab+ 以二进制格式打开一个文件用于追加，如果文件已存在，文件指针将会放在文件的结尾，如果该文件不存在，创建新文件用于读写。
   '''
   #file = open(file_name,"x")
   #file = open(file_name,"a+")
   #file = open(file_name,"t")
   file = open(file_name,"a")
   #content = file.readline()
   #print(content)
   file.write("python3  is a good language")
   file.close()
   #file.tell() 对象当前位置
   #file.seek()
if __name__ == "__main__":
    io_test()
    open_test("D://t.txt")
