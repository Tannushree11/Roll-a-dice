import random 

#Saaket  --here you have created a function called response , and as a parameter 
#you have taken the same name. So it is not working properly.
#I am attaching the correct code in the other py file,see that.
def response(response):
    response = "y"
    while response=="y":
        no=random.randint(1,6)
        if no==1:
            print("[-----]")
            print("[ ]")
            print("[ 0 ]")
            print("[ ]")
            print("[-----]")
        if no==2:
             print("[-----]")
             print("[  0]") 
             print("[   ]") 
             print("[0  ]") 
             print("[-----]")
        if no==3:
             print("[-----]")
             print("[    0]") 
             print("[  0]") 
             print("[0  ]") 
             print("[-----]")
        if no==4:
             print("[-----]")
             print("[0  0]") 
             print("[    ]") 
             print("[0  0]") 
             print("[-----]")
        if no==5:
             print("[-----]")
             print("[0   0]") 
             print("[  0 ]") 
             print("[0   0]") 
             print("[-----]")
        if no==6:
             print("[-----]")
             print("[0  0]") 
             print("[0  0]") 
             print("[0  0]") 
             print("[-----]")
    response = input("enter 'y' for rolling the dice and 'n' for exit ")
    response = "n"