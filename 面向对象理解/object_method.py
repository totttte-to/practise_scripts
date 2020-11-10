"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : object_method.py                      
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/8 12:01 上午               
#                                                                   
#-------------------------------------------------------------------
#                   学习概念：对象方法
#-------------------------------------------------------------------
"""


class Cat:
    species = 'Cat'

    @classmethod
    def catch(cls):
        print('{} to catch mice'.format(cls.species))

    def __init__(self, name):
        self.name = name
        print('The cat named {}'.format(name))

    # 定义一个名为miaow的对象方法
    def miaow(self):
        # 可以通过self参数来访问和定义对象属性
        # 也可以通过self参数来访问对象方法
        # 因为self表示的是当前对象
        print('{} when miaow unhappy'.format(self.name))


kitty = Cat('Kitty')
# 调用对象方法miaow, Python会自动将对象与self参数进行绑定，无需显式传递
kitty.miaow()
