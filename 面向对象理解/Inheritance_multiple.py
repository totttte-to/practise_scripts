"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : Inheritance_multiple.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/8 1:39 上午               
#                                                                   
#-------------------------------------------------------------------
#                   学习概念：继承多实例
#-------------------------------------------------------------------
"""


class Cat:
    # 定义类属性species, 表示猫所属的物种
    __species = "Cat"

    @classmethod
    def catch_mice(cls):
        # 不会抓老鼠的猫不是好猫
        print("A cat that doesn't catch a mouse is not a good cat!")

    def miaow(self):
        print("Cats miaow when they are unhappy")


# 定义Baby类，继承于Cat
class Baby(Cat):
    pass


class Wildcat(Cat):
    def miaow(self):
        print("wild cats miaow when they are hungry")


# 定义Kitty类，同时继承于Baby和Wildcat
class Kitty(Baby, Wildcat):
    pass


kitty = Kitty()
kitty.miaow()
