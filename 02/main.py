""" Method 1 """

num = int(input("Give me a number to check: ")) # prasa ievadīt skaitli
check = int(input("Give me a number to divide by: ")) # ievadīt skaitli ar kuru tiks dalīts

if num % 4 == 0:
    print(num, "is a multiple of 4") #  norāda ja tas reizinas ar 4 
elif num % 2 == 0:
    print(num, "is an even number") # norāda ja ir pāra skaitlis
else:
    print(num, "is an odd number") # norāda ja ir nepāra skaitlis

if num % check == 0: #parbauda vai nav 0 
    print(num, "divides evenly by", check) # norāda ja to ir iespējams dalīt
else:
    print(num, "doesn't divide evenly by", check) #norāda ja to nav iespējams dalit ar uzrakstito skaitli

""" Method 2 """
num = int(input("Enter a number: ")) # ievadit skaitli
mod = num % 2 # mob ir  skitlis kura atlikums ir 2
if mod > 0: #  norāda ja mod ir mazāks par 0
    print("You picked an odd number.") # norāda ja ir nepāra 
else:
    print("You picked an even number.") # norāda ja ir pāraS
