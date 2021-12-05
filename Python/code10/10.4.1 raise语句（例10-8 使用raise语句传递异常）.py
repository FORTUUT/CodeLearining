#10.4.1 raise语句（例10-8 使用raise语句传递异常）
try:
    try:
        raise IOError
    except IOError:
        print("inner exception")
        raise     # <same as raise IOError>
                  #再次抛出异常，将异常向外层传递
except IOError:
    print("outter exception")



