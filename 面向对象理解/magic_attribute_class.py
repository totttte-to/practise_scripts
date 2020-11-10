"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : magic_attribute_class.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/8 5:45 下午               
#                                                                   
#-------------------------------------------------------------------
#                    魔术属性：__class__
#-------------------------------------------------------------------
"""


class Cat:
    def __init__(self, mame):
        self.__name = mame


kitty = Cat('kitty')
print(kitty.__class__)
"""
(1) 执行print后的输出：
<class '__main__.Cat'>
(2) __class__的输出是一个类类型，所以可以通过__class__来进行对象的实例化
例如：lisa = kitty.__class__("lisa")
"""