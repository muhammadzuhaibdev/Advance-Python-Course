# Python For Loop Tutorial 🐍
This repository contains examples and explanations of the **Python `for` loop**.
It is designed for beginners who want to understand how loops work in Python.

## 📌 What is a For Loop?

A **for loop** is used to iterate over a sequence such as a list, string, tuple, dictionary, or range. It allows you to execute a block of code multiple times.

### Basic Syntax

```
for variable in listName:
    # code block
```

---

## 📂 Examples Included

### 1. Loop Through a List

```
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
```

---

### 2. Using range()

```
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

### 3. Loop Through a String

```
name = "Python"

for letter in name:
    print(letter)
```

---

### 4. Loop Through a Dictionary

```
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

for key in student:
    print(key, student[key])
```

---

## 🔹 break Statement

Stops the loop immediately.

```
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 🔹 continue Statement

Skips the current iteration.

```
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 🔹 Nested For Loop

A loop inside another loop.

```
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## 📚 Topics Covered

* Python for loop basics
* Iterating over lists
* Iterating over strings
* Using `range()`
* `break` and `continue`
* Nested loops
* List comprehension
