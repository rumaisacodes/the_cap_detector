import random
import time

#1. Ask the user for their statement
statement = input("Enter what you just said: ")

#2. The computer thinks...(dramatic pause)
time.sleep(1.5) #The computer waits for 1.5 seconds
print ("Scaning brainwaves...🧠")
time.sleep(1.5) #The computer waits for another 1.5 seconds

#3. Create a list of seprate answers
verdicts = [
    "🚫NO CAP (Truth)", 
    "🧢 BIG CAP (Lie)",
    "💯 Facts", 
    "🥀 BRO, WHY YOU LYING LOL?"
    ]

#4. pick a random result and print it
print("--------------")
print("Verdict: ", random.choice(verdicts)) 