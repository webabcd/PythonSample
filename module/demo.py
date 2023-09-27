# 导入 module1.py（注：在一个文件中即使你多次 import 一个模块，这个模块也只会被导入一次）
import module1
# 然后就可以调用 module1 中的函数了（需要指定模块名）
module1.a()
# 可以给导入的模块或模块中的函数指定一个别名，之后就可以直接使用这个别名了
x = module1.b
x()


# 导入 module2.py 中的 a 函数和 b 函数，同时为 b 函数指定一个别名
from module2 import a, b as y # 如果全部导入的话就 from module2 import *
# 然后就可以调用 module2 中的函数了（不需要指定模块名）
a()
y()


# 通过包名的方式导入
import player.audio.codec
# 调用时需要指定全名
player.audio.codec.show()


# 从指定的包名中导入指定的模块，或从指定的模块全名中导入指定的函数，同时可以指定别名
from player.video import codec as videoCodec
# 调用时不需要指定全名
videoCodec.show()


'''
关于上面的通过包名方式导入的说明：
1、要求包的各个目录存在一个名为 __init__.py 的文件，这样才会被认为是一个包
2、导入时是支持星号的，类似这种 from xxx import *
   如果要为 * 定义自定义逻辑，则需要在每个目录中的 __init__.py 文件中写一行类似如下的代码（列表中配置的是当前目录中可以通过 * 导入的 py 文件的名称）
   __all__ = ["aaa", "bbb", "ccc"]
3、关于包开发的更多说明参见 package/main.py
'''