userData = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, Anytown, USA"
}

userInput = input("enter your age: ")

userData["age"] = userInput

print(userData.get("age"))
print(userData)
               

















# car  = "Toyota 2021 89213089 1300cc red"
# car_list = [["red", "Toyota", "2021", "89213089", "1300cc"], ['blue', 'Honda', '2020', '12345678', '1500cc']]

# car = {
#     "color": "red",
#     "brand": "Toyota",
#     "year": 2021,
#     "number": 8921308,
#     "engine": "1300cc"
# }
# # add new key value pair to dictionary
# # car["model"] = "Corolla"

# # read data from dictionary
# # print(car['brand'])
# # print(car.get("brand", "Key not found"))

# # update value of existing key
# # car["color"] = "blue"

# # delete key value pair from dictionary
# # del car["model"]
# car.pop("brand")
# car.popitem()
# print(car)

# # CRUD
# # C => Create / Add
# # R => Read
# # U => Update
# # D => Delete
