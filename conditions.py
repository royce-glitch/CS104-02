# CS104
# Royce Amburg 
# conditions.py
n = int(input("How many times do you want to run this code? "))
i = 0
while i < n:
    temp = int(input("Please enter the current temperature: "))
    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print ("Wear a heavy coat")
    else:
        print ("Stay Inside")
    i += 1
              
    
        
