class Class1:

    # 双下划线开头用于定义私有属性（外部不能调用，子类也不能调用）
    __id = ""
    
    # 定义公共属性
    country = ""

    # 通过 __init__ 定义构造函数
    # 第一个参数必须是 self
    def __init__(self, name, age):
        # 定义公共属性，并赋值
        self.name = name
        # 定义公共属性，并赋值
        self.age = age
        
        self.__id = "0001"

    # 定义公共方法
    # 第一个参数必须是 self
    def toString(self):
        return self.__getString()

    # 双下划线开头用于定义私有方法（外部不能调用，子类也不能调用）
    # 第一个参数必须是 self
    def __getString(self):
        return f"id:{self.__id}, name:{self.name}, age:{self.age}, country:{self.country}"

    # 定义 [] 方式的操作逻辑
    __dict = {}
    def __setitem__(self, name, value): 
        self.__dict[name] = "myvalue_" + value 
    def __getitem__(self, name): 
        if self.__dict.__contains__(name):
            return self.__dict[name]
        return None
    def __delitem__(self, name): 
        del self.__dict[name] 