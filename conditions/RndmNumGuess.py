#"""Write a program that simulates a simple guessing game. The program should generate a random number between 1 and 100, and then ask the user to guess the number. 
# Provide feedback (too high, too low, or correct) and keep prompting the user until they guess correctly."""
import random
a=random.randint(1,100)
b=int(input("Enter Number by guessing : "))
while a!=b:
    b=int(input("Your Guess is worng, Enter Another Guess :"))
    continue
print("Correcrt",a ,"is system num and ", b, "your guess")
