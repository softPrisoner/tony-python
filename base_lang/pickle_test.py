import pickle,pprint

def pickle_test():
    data={
        "a":[1,2.0,3,4+6j],
        "b":("string",u"Unicode string"),
        "c":None
    }
    selfref_list=[1,2,3]
    selfref_list.append(selfref_list)
    output=open("D://t.txt","wb")
    #Pickle dictionary using protocol
    pickle.dump(data,output)
    pickle.dump(selfref_list,output,-1)
    output.close()
def pprint_test():
    pkl_file = open("D://t.txt","rb")
    data1=pickle.load(pkl_file)
    pprint.pprint(data1)
    data2=pickle.load(pkl_file)
    pprint.pprint(data2)
if __name__ == "__main__":
    #pickle_test()
    pprint_test()