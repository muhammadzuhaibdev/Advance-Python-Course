class Course:
    def __init__(self):
        self.courseId = "CS101"
        self.courseName = "Introduction to Computer Science"
        self.courseCode = "CS101"
        self.description = "This course provides an introduction to computer science concepts and programming."
        self.credits = 3
        self.department = "Computer Science"
        
    def addCourse(self, courseName):
        print(f"Course {courseName} added successfully.")
    
    def updateCourse(self, courseId):
        print(f"Course with ID {courseId} updated successfully.")
        
    def deleteCourse(self, courseId):
        print(f"Course with ID {courseId} deleted successfully.")
    
    def assignInstructor(self, instructorName):
        print(f"Instructor {instructorName} assigned to course successfully.")


output = Course()
print(output.courseId)
print(output.courseName)
print(output.courseCode)
print(output.description)
print(output.credits)
print(output.department)

output.addCourse("Data Structures")
output.updateCourse("CS101")
output.deleteCourse("CS101")
output.assignInstructor("Dr. Smith")






# class StudentClass:
#     def __init__(self, name, email, phone, rollNo):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.rollNo = rollNo    
    
#     def display(self, changeName):
#         self.name = changeName
#         print(f"Name: {self.name}")


# output = StudentClass("John Doe", "john.doe@example.com", "123-456-7890", "S12345")
# print(output.name, output.email, output.phone, output.rollNo)
# output.display("Zuhaib")

# output2 = StudentClass("Jane Smith", "jane.smith@example.com", "098-765-4321", "S54321")
# print(output2.name, output2.email, output2.phone, output2.rollNo)
# output2.display("Hamza")



# Four Pillars of OOP
# 1) Inheritence
# 2) Encapsulation
# 3) Abstraction
# 4) Polymorphism
