"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : constructor.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/7 11:45 下午               
#                                                                   
#-------------------------------------------------------------------
#                   学习概念：类的构造函数
#-------------------------------------------------------------------
"""


class Cat:
    species = 'cat'

    @classmethod
    def catch(cls):
        print('{} to catch mice'.format(cls.species))

    # 定义类的构造函数
    def __init__(self):
        print("a cat was born")

    def __init__(self, name):
        print('The cat named {}'.format(name))


# 对Cat类进行实例化，kitty即为实例化后的Cat对象
# kitty = Cat()

# 在对类进行实例化时，Python自动的调用了构造函数
# 在类的构造函数中，可以定义任何参数。一旦定义了参数，那么在对类进行实例化时，必须传递该参数
# 对Cat进行实例化时，必须传递与构造函数一致的函数；self参数，Python会自动将当前对象进行绑定，无需传递
Kitty = Cat('Kitty')
