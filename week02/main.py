# dices = [ n for n in range(1,7)]
# print(dices)

# dices = [ n for n in range(1,7) if n % 2 == 1]
# print(dices)

# rows = range(1, 3)
# cols = range(1, 4)
#  for row in rows:
#     for col in cols:
#         print(col, row)

# rows = range(1, 3)
# cols = range(1, 4)
# matrix = [(row, col) for row in rows for col in cols] # list comprehension
# for m in matrix: # packing
#     print(m)
# for r, c in matrix: # unpacking
#     print(r, c)

'''
    class & object
'''

class Person(): # class 이름은 카멜표기법
    def __init__(self, in_name, b = '0'): # 생성자
        # self.__name = name # private
        self.hidden_name = in_name # public
        self.blood_type = b

    # Method
    def sleep(self):
        print('쿨쿨')

    def eat(self, food):
        print(f'{food}를 냠냠~')

    # property
    @property
    def name(self):
        return self.hidden_name

    # name setter
    @name.setter
    def name(self, in_name):
        self.hidden_name = in_name

    # getter method
    # def get_name(self):
    #     return self.__name

p1 = Person('김인하')
p2 = Person('박인하', 'AB')
p1.name = '김인상'
# print(f'{p1.get_name()}의 혈액형은 {p1.blood_type}형 입니다.')
print(f'{p1.name}의 혈액형은 {p1.blood_type}형 입니다.')
print(p2.blood_type)
print(id(p1), id(p2))
print(p1.eat('와퍼버거'))

class Shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("도형을 그립니다.")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x,y)
        self.r = r

    def area(self):
        return self.r * self.r * 3.14

class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        super().__init__(x, y, r)
        self.h = h
        self.cir = super().area()

    def draw(self): # method overriding
        print("원기둥을 그립니다.")

    def vol(self):
        print(f"원기둥 부피 : {self.cir * self.h}")

cir = Circle(5, 5, 5)
print(cir.area())
cy = Cylinder(10, 10, 10, 5)
cy.vol()