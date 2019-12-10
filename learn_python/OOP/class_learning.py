# class Student(object):
#     def __init__(self,name,score,grade=10):
#         self.__name=name
#         self.score=score
#         self.__grade=grade
#     pass
#     def print_score(self):
#         print(self.score)

#     def get_score(self):
#         if self.score>90:
#             return 'A'
#         elif self.score>60:
#             return 'B'
#         else:
#             return 'C'
#     def get_name(self):
#         return self.__name

#     def set_name(self,name):
#         self.__name=name
    
#     def set_grade(self,grade):
#         if grade<0 or grade>100:
#             raise ValueError('bad grade')
#         else:
#             self.__grade=grade
#     def get_grade(self):
#         return self.__grade

# ming=Student('ming',10);
# print(ming.get_score())
# # print(ming)
# print(ming._Student__name)
# # print(ming.score)
# ming.print_score()

# print(ming.get_name())
# ming.set_name('hong')
# print(ming.get_name())

# ming.set_grade(10)
# print(ming.get_grade())
# ming.__grade=20
# print(ming.get_grade())
# for k in dir(ming):
#     print(k)
# hong=Student('hong',20)

# for k in dir(hong):
#     print(k)

class Animal(object):
    # name='Animal'
    count=0
    def __init__(self,name='animal',age=10):
        self.name=name
        self._age=age
        Animal.count+=1#在类里面访问类属性用 Student.count 相当于全局变量
    def run(self):
        print('Animal is running...')

    __slots__=('name','_age')
    @classmethod
    def greet(self):
        print('I am an animal...')
    # @property
    # def age(self):
    #     return self._age


dog=Animal()

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name:%s)'%self.name
    __repr__=__str__

    def __iter__(self):
        return self
    def __next__(self):
        return 10
    
# ming=Student('ming')
# for i in ming:
#     print(i)


class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):

        self.a,self.b=self.b,self.a+self.b
        if(self.a>200):
            raise StopIteration()
        else:
            return self.a
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for i in range(n):
                a,b=b,a+b
            return a
        elif isinstance(n,slice):
            if n.start:
                start=n.start
            else:
                start=0
            if n.stop:
                stop=n.stop
            else:
                stop=10
            if n.step:
                step=n.step
            else:
                step=1
            L=[]
            a,b=1,1
            for i in range(start):
                a,b=b,a+b
            for i in range(start,stop):
                if (i-start)%step==0:
                    L.append(a)
                a,b=b,a+b
            return L

    def __getattr__(self,attr):
        if attr=='time':
            return lambda : print('I am function')
# f=Fib()
# # f.score()
# print(f.time())
# j=0
# for i in f:
#     print(i,f[j])
#     j+=1



# print(Chain().status.user.timeline.list)

# print(c.users('jlpang1997').repos)
# class Student(object):
#     def __init__(self,birth=1997):
#         self._birth=birth
#     @property #把method 编程 属性(也就是可以直接用.来引用)
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth=value

#     @property 
#     def age(self):
#         return 2019-self._birth

# # ming=Student()
# # print(ming.birth)
# # ming.birth=1998
# # print(ming.birth)
# # print(ming.age)
# # ming.age=10

# class Screen(object):
#     def __init__(self,width,height,resolution):
#         self.__width=width
#         self.__height=height
#         self.__resolution=resolution
#     @property
#     def width(self):
#         return self.__width
#     @width.setter
#     def width(self,width):
#         self.__width=width
#     @property
#     def height(self):
#         return self.__height
#     @height.setter
#     def height(self,value):
#         self.__height=value
    
#     @property
#     def resolution(self):
#         return self.__resolution


# s=Screen(10,20,1997)   
# s.width=10
# print(s.width)
# s.width=20
# print(s.width)
# print(s.resolution)
# s.resolution=1998

# dog.greet()
# dog.age=10
# dog.grade=4
# print(dog.age)
# dog.eat=lambda : print('Dog is eating...')
# dog.eat()
# a=Animal('dog')
# print(a.count)
# b=Animal('cat')
# print(a.count)

# print(a.name)
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')
    pass

class Cat(Animal):
    pass

# dog=Dog()
# dog.run()
# dog.eat()

# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))
# print(isinstance(dog,int))

def run_twice(animal):
    animal.run()
    animal.run()

# run_twice(Animal())
# run_twice(Dog())
# # class Cat(Animal):
# #     def run(self):
# #         print('Cat is running...')

# run_twice(Cat())
# print(type(123))
# print(type('apple'))
# print(type(None))
# print(type(abs))
# print(type(dog))
# print(type(Dog))
# print(hasattr(dog,'run'))
# print(hasattr(dog,'sleep'))
# print(getattr(dog,'run'))