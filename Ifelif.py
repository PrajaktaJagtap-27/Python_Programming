#0-5   Free
#5-18  900
#18-40  1200
#40.... 500

print("---------------------------------------")  
print("---------Ticket Pricing Software-------")
print("---------------------------------------")

print("Pls Enter your age :")
Age = int(input())

if(Age <= 5):    
    print("Free Entry")

elif(Age > 5 and Age <= 18):
    print("Ticket price : 900")    
elif(Age > 18 and Age <= 40):
    print("Ticket price : 1200")   
else:
    print("Ticket price : 500")         


