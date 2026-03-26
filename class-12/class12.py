studentsData = [
    {
        "id": 1,
        "name":"zuhaib",
        "email":"zuhaib@gmail.com",
        "phone": "656789",
        "course": "Python"
    },
    {
        "id": 2,
        "name":"hamza",
        "email":"hamza@gmail.com",
        "phone": "1894189",
        "course": "WMAD"
    },
    {
        "id": 3,
        "name":"abdullah",
        "email":"abdullah@gmail.com",
        "phone": "9897486",
        "course": "Agentic Ai"
    },
]

# Create Data
userName = input("Please enter your Name: ")
userEmail = input("Please enter your email: ")
phone = input("Please enter your Phone: ")
course = input("Please enter your course: ")

userData = {
    "id": len(studentsData) + 1,
    "name": userName,
    "email": userEmail,
    "phone": phone,
    "course": course,
}

studentsData.append(userData)
print(studentsData)


# Read Data
for student in studentsData:
    print("id", student["id"])
    print("name", student["name"])
    print("course",student["course"])


# Delete Data
deleteId = int(input("Please enter id:"))

def filterFunc(student):
    if not student['id'] == deleteId:
        return student
    
output =  list(filter(filterFunc, studentsData))
print(output)

# Update Data
updated_id = int(input("Enter document id: "))
updated_email = input("Please enter updated email: ") 

def mapFunc(student):
    if student['id'] == updated_id:
        return {
            "id": student['id'],
            "name": student['name'],
            "email": updated_email,
            "phone": student['phone'],
            "course": student['course'],
        }
    else:
        return student

output = list(map(mapFunc, studentsData))
print(output)