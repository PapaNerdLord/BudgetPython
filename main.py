#get payday info from user

""""
print("Hello, Please Enter Payday Amount:")
paydayA = input()
print("Payday Ammount is: " + paydayA)

paydayA = int(paydayA)

a = 300
b = 400
c = 500
d = 600
e = 700
f = 800
g = 900
h = 1000
j = 1100
k = 1200

if  paydayA >= a and paydayA <= b:
    save_amount = (1/20) * paydayA
    print("Save this much: " + str(save_amount))

"""
#this is how I'd write this probably even though magic numbers are bad lol
def alex_function():
    #get payday info from user
    print("Hello, Please Enter Payday Amount:")
    paydayA = input()
    print("Payday Ammount is: " + paydayA)
    
    #convert paydayA to int so you can use it with other ints later
    paydayA = int(paydayA)
    
    #if you make between 300 and 400 save 1/20th of it lol
    if  paydayA >= 300 and paydayA <= 400:
        save_amount = (1/20) * paydayA
        print("Save this much: " + str(save_amount))

alex_function()

#this is how I'd write this if other people had to look at it or work on it with me
def alex_tryhard_function():
    #set up payday numbers
    lower_savings = 300
    upper_savings = 400
    savings_ratio = 1/20

    #get payday info from user
    print("Hello, Please Enter Payday Amount:")
    payday = input()
    print("Payday Ammount is:", payday)
    
    #convert paydayA to int so you can do math with it
    payday = int(payday)
    
    #if you make between 300 and 400 save 1/20th of it lol
    if  payday >= lower_savings and payday <= upper_savings:
        save_amount = payday * savings_ratio
        print("Save this much:", save_amount)

alex_tryhard_function()