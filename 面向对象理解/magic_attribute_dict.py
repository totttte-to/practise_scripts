"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : magic_attribute_dict.py                      
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/8 5:50 下午               
#                                                                   
#-------------------------------------------------------------------
#                    魔术属性：__dict__
#-------------------------------------------------------------------
"""


class Cat:
    __species = 'cat'

    @classmethod
    def catch(cls):
        print("A cat that doesn't catch a mouse is not a good cat!")

    def __init__(self, name):
        # 在对象属性前面加上双下划线
        self.__name = name

    def miaow(self):
        # 在类内部可以访问被"隐藏"的属性和方法
        print('{} miaow when unhappy'.format(self.__name))


# 访问类型中的__dict__
print(Cat.__dict__)
"""
输出为：
{'__module__': '__main__', '_Cat__species': 'Cat', 'catch_mice': <classmethod object at 0x0000017C5EB6EE88>, '__init__': <function Cat.__init__ at 0x0000017C5EAFD5E8>, 'miaow': <function Cat.miaow at 0x0000017C5EAFD678>, '__dict__': <attribute '__dict__' of 'Cat' objects>, '__weakref__': <attribute '__weakref__' of 'Cat' objects>, '__doc__': None}
"""

# 访问对象中的__dict__
kitty = Cat('kitty')
print(kitty.__dict__)
"""
输出为：
{'_Cat__name': 'kitty'}
"""
