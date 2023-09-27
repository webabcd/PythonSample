'''
当需要多个脚本文件实现一个功能时，就可以是使用包来封装这些脚本文件，可以把包当作是一个模块的集合

本例的目录结构
|--module2
|--|--main.py               用于调用包中的功能
|--|--sub                   这是包
|--|--|--__main__.py        如果通过 python -m package_name 执行包的话，则会自动执行此文件
|--|--|--__init__.py
|--|--|--m0.py
|--|--|--sub                这是包中的包
|--|--|--|--__init__.py
|--|--|--|--m1.py
|--|--|--|--m2.py
'''

'''
导入 sub.sub.m1
sub.sub.m1 中的 from .m2 import * 用于导入 m1 同目录下的 m2（.在包中代表同目录，如果需要在包中导入当前目录的所有脚本的话则 from . import *）
sub.sub.m1 中的 from ..m0 import * 用于导入 m1 父目录下的 m0（..在包中代表父目录，以此类推）

注：一般由非包目录中的脚本调用包目录中的功能，本例中如果直接把 sub.sub.m1 当做主脚本运行的话则会报找不到模块的错误
'''
import sub.sub.m1


'''
1、要求包的各个目录存在一个名为 __init__.py 的文件，这样才会被认为是一个包
2、导入时是支持星号的，类似这种 from xxx import *
   如果要为 * 定义自定义逻辑，则需要在每个目录中的 __init__.py 文件中写一行类似如下的代码（列表中配置的是当前目录中可以通过 * 导入的 py 文件的名称）
   __all__ = ["aaa", "bbb", "ccc"]
3、如果需要 python 执行一个包，则包目录内必须包含一个名为 __main__.py 的文件，这样在命令行直接输入 python -m package_name 就可以执行 __main__.py 文件
'''


'''
1、导入模块时，只能导入同级目录。导入包时可以通过 . 的方式导入同级目录或子目录或父目录
2、每个文件都有自己的 __name__，名字一般是 package_name.module_name，但是对于启动的文件来说其 __name__ 为 '__main__'
3、如果因为目录结构的限制，无法导入需要的模块或包时，可以考虑类似如下的方法，先把你相关的目录加载进来，然后在导入相关的模块或包
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))) 
# sys.path.append(".")
# sys.path.append("..")
'''