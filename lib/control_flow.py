#!/usr/bin/env python3

def admin_login(username, password):
    # Check if username is "admin" (case-insensitive) and password is "12345"
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    # Return appropriate message based on temperature
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    return "It's perfect out there!"

def fizzbuzz(num):
    # Return "FizzBuzz", "Fizz", "Buzz", or the number based on divisibility
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num

def calculator(operation, num1, num2):
    # Perform the operation or return "Invalid operation!" for invalid input
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
