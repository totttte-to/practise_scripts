"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : Inheritance_single.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/8 12:19 上午               
#                                                                   
#-------------------------------------------------------------------
#                   学习概念：继承单实例
#-------------------------------------------------------------------
"""


# (1)单继承
# 定义Cat类，作为父类
class Cat:
    __species = 'Cat'

    @classmethod
    def catch(cls):
        print("A cat that doesn't catch a mouse is not a good cat!")

    def __init__(self, name):
        self.__name = name


# 定Baby类，表示家猫，继承自Cat
class Baby(Cat):
    def __init__(self, name, weight):
        # 通过super()返回一个代理对象，通过代理对象执行父类的__init__方法
        super().__init__("cat")
        self.__name = name
        self.__weight = weight

    @classmethod
    def catch_mice(cls):
        # 通过super()来执行父类的catch方法
        super().catch()
        print("baby is too fat to catch mice!")


# Python抛出了TypeError异常信息，指示在进行实例化时，缺少一个参数。
# 在上文的代码实例中，父类Cat的构造函数带一个name的参数，子类在实例化时必须显示地传递一个参数。
# baby = Baby()

kitty = Baby("kitty", 18)
kitty.catch()
