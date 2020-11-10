"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : object_attribute.py.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/7 11:56 下午               
#                                                                   
#-------------------------------------------------------------------
#                  学习概念：对象属性
#-------------------------------------------------------------------
"""


class Cat:
    species = 'Cat'

    @classmethod
    def catch(cls):
        print('{} to catch mice'.format(cls.species))

    def __init__(self, name):
        # 定义一个name的属性,然后将参数name进行赋值
        self.name = name
        # 此时访问的是对象属性
        print('The cat named {}'.format(name))


Kitty = Cat('Kitty')