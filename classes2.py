#Q.1 Create a circle class and initialize it with radius.
#Make two methods getArea and getCircumference inside this class.
class Circle():
  def __init__(self,r):
    self.r = r
  def  getArea(self):
    return 3.14*self.r*self.r
  def getCircumference(self):
    return self.r*2*3.14
newcircle=Circle(6)
print(newcircle.getArea())
print(newcircle.getCircumference())

print('-'*50)

#Q.2 Create a Student class and initialize it with name and roll number.
#Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student
#3. setMarks - It should assign marks to the student.

class Student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print (self.name)
        print (self.rollno)
    def setAge(self,age):
        self.age=age
        temp=self.age
        return temp
    def setMarks(self,marks):
        self.marks=marks
        temp1=self.marks
        return temp1
newstudent=Student('Rahul',45)
print(newstudent.display())
print(newstudent.setAge(20))
print(newstudent.setMarks(85))
print('-'*50)

#Q.3 Create a Temprature class and create two methods: 
#1.convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2.convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature():
    def convertFahrenheit(self,celsius):
        return(celsius*(9/5))+32
    def convertCelsius(self,fahrenheit):
        return(fahrenheit-32)*(5/9)
newtemperature=Temperature()
print(newtemperature.convertFahrenheit(100))
print(newtemperature.convertCelsius(50))
print('-'*50)
#Q.4 Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.

class MovieDetails():
    def __init__(self, moviename ,yearofrelease,ratings):
        self.moviename=moviename
        self.yearofrelease=yearofrelease
        self.ratings=ratings
    def display(self):
        print(self.moviename)
        print(self.yearofrelease)
        print(self.ratings)
    def update(self,moviename,yearofrelease,ratings):
        self.moviename=input("enter the moviename:")
        self.yearofrelease=input(" enter the year of release:")
        self.ratings=input("give your ratings:")
        print(self.moviename,self.yearofrelease,self.ratings)
movie=MovieDetails('Roy',2015,3.3)
print(movie.display())

print(movie.update("m","A","y"))
print('-'*50)
#Q.5 Create a class Animal as a base class
#and define method animal_attribute.
#Create another class Tiger which is inheriting Animal
#and access the base class method.

class Animal():
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
    def bark(self):
        print("...Roar...")

class Tiger(Animal):
    
    def bark(self):
        print("Tiger roars")

if __name__=="__main__":
    pet1=Tiger("Black","4")
    pet1.bark()
    print(pet1.color,",",pet1.legs)
print('-'*50)

#Q.6 What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())
print('-'*50)
#Q.7 Create a class Shape.Initialize it with length
#and breadth Create the method Area.
#Create class rectangle and square which inherits shape
#and access the method Area.

class Shape():
  length=float()
  breadth=float()

  def AreaR(self,length,breadth):
    self.length=length
    self.breadth=breadth
    return self.length*self.breadth
  def AreaS(self,a):
    self.side=a
    return self.side*self.side
class rectangle(Shape):
  def display_area1(self):
    l=20
    b=8
    print("area of rectangle:",self.AreaR(l,b))
r=rectangle()
r.display_area1()

class square(Shape):
  def display_area2(self):
    a=50
    print("area of square:",self.AreaS(a))
s=square()
s.display_area2()

    
     
    

