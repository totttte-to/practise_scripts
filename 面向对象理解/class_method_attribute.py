"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : class_method_attribute.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/7 11:23 下午               
#                                                                   
#-------------------------------------------------------------------
#                  学习概念：  类，类属性，类方法，类的实例化，静态方法
#-------------------------------------------------------------------
"""


# 定义一个Cat类
class Cat:
    # 定义类属性species,用来表示猫所属的物种
    species = 'cat'

    # 定义类方法前需要加上一个@classmethod的修饰符；函数至少定义一个参数，通常为cls
    # 字符串格式化函数str.format()
    @classmethod
    def catch(cls):
        pass

    @classmethod
    def cry(cls):
        # cls表示当前的Cat类，通过.来访问类属性和类方法
        print('Cat is {}'.format(cls.species))

    # 定义静态方法需要加上一个@staticmethod的修饰符；静态方法与类方法区别在于，无需定义任何描述类的实参
    # 静态方法和类方法都是类作用域的全局方法，可以被所有实例化后的对象共享
    # 定义静态方法时，可以显式地定义和传递一个类型参数，以模拟类方法，定义一个cls参数，表示当前类型
    @staticmethod
    def pees(cls):
        print(cls.species)


# 直接通过类来访问类属性
print(Cat.species)
# 执行类方法时，无需显式的传递类类型作为参数
Cat.cry()

# 对Cat进行实例化，Kitty即为实例化后的Cat对象
Kitty = Cat()
# 类属性和类方法为所有对象共享，所以可以通过对象来访问类中的属性和方法
# 通过对象来访问类属性
print(Kitty.species)
# 通过对象来访问类方法
Kitty.cry()

# 执行类的静态方法，须显式的传递当前类作为参数
Kitty.pees(Cat)
