"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : magic_attribute_doc.py                      
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/8 5:59 下午               
#                                                                   
#-------------------------------------------------------------------
#                   魔术属性：__doc__
#-------------------------------------------------------------------
"""


class Cat:
    def __init__(self, name):
        """ this cat is not a real cat,no rat """
        self.__name = name


print(Cat.__doc__)
