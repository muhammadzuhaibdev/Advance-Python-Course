# Inheritence (Multilevel , Multiple Inheritence)
# class StudentClass:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
        
        
# class TeacherClass(StudentClass):
#     def __init__(self, degree, name, email, age):
#         super().__init__(name, email, age)
#         self.degree = degree
        
# class Principle(TeacherClass):
#     def __init__(self, experience, degree, name, email, age):
#         super().__init__(degree, name, email, age)
#         self.experience = experience

    
# teacher = TeacherClass("BSCS", 'Zuhaib', 'zuhaib@gmail.com', 24)
# principle = Principle(40,"BSCS", 'shahbaz', 'shahbaz@gmail.com', 24)
# student = StudentClass("Hamza", "hamza@gmail.com", 18) 

# class StudentClass:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.__email = email
#         self.age = age
   
#     def getEmail(self):
#         return self.__email
    
    
# class TeacherClass(StudentClass):
#     def __init__(self, degree, name, email, age):
#         super().__init__(name, email, age)
#         self.degree = degree

# teacher = TeacherClass("BSCS", "Zuhaib", "zuhaib@gmail.com", 24)
# output = teacher.getEmail()
# print(output)

# studentData = StudentClass("Hamza", "hamza@gmail.com", 36)
# studentData2 = StudentClass("Abdullah", "Abdullah@gmail.com",45)
# studentData.setPhone("7654356789")
# print(studentData.studentName)
# print(studentData.email)
# print(studentData.age)
# print(studentData.phone)
# studentData2.setPhone("7654356789")
# print(studentData2.studentName)
# print(studentData2.email)
# print(studentData2.age)
# print(studentData2.phone)





class AbstractClass:
    def addStudent():
        pass
    def deleteStudent():
        pass
    def UpdateStudent():
        pass
    
class Student(AbstractClass):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def addStudent(self):
        return "Course Added Successfully!"
    def UpdateStudent(self):
        return "Course Updated Successfully!"
    def deleteStudent(self):
        return "Course Deleted Successfully!"
    
student = Student("Zuhaib", 24)
output = student.addStudent()
print(output)





class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!