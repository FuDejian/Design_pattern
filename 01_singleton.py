# 测试单例模式


class MySingleton:

    # 类属性
    __instance = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # cls.__instance = object.__new__(cls)
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # __init__ 方法是否需要重复执行，需要看实际情况
    def __init__(self, name):
        if MySingleton.__init_flag:
            print("init.....")
            self.name = name
            MySingleton.__init_flag = False


a = MySingleton('aa')
b = MySingleton('bb')
print(a)
print(b)
c = MySingleton('cc')
print(c)

'''
init.....
<__main__.MySingleton object at 0x0000018F993ABB38>
<__main__.MySingleton object at 0x0000018F993ABB38>
<__main__.MySingleton object at 0x0000018F993ABB38>
'''