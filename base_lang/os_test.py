import os,shutil,glob,sys,re

#history likes os
def os_test():
   # current_dictory = os.getcwd()
   # print(current_dictory)
   # os.chdir("D:")
   # os.system("mkdir today")
   # dir(os)
   # help(os)
   # shutil.copyfile("D://t.txt","E://t1.txt")
    print(glob.glob('*.py'))

    sys.stderr.write("warn  there is some error happened")
    #command line params
    print(sys.argv)
    
    print(re.findall(r'\bf[a-z]*',"which foot or hand fell fastest"))
    
    print(re.sub(r'(\b[a-z]+) \1',r'\1',"cat in the the hat"))

import zlib 
def zlib_test():
    s=b"witch which has which witches wrist watch"
    len(s)
    t = zlib.compress(s)
    len(t)
    zlib.decompress(t)
    b'witch which  has which witches wrist watch'
    zlib.crc32(s)



if __name__ == "__main__":
   # os_test()
   #zlib_test()
   print(os.name)