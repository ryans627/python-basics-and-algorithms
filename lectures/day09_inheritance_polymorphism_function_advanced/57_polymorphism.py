# 多态的基本认知
# 多态是在继承的基础上才会发生

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Wolf")

class Cat(Animal):
    def speak(self):
        print("Meow")


# 定义一个函数来调用不同的对象叫法
def animal_speak(animal):
    animal.speak()


# 创建小猫小狗对象
cat = Cat()
dog = Dog()

# 同一个函数，不同的行为
animal_speak(cat) # Meow
animal_speak(dog) # Wolf