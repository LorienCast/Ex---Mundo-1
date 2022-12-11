from ex115 import *
from time import sleep
from emoji import emojize
archive = open('DataBase.txt', 'a') # Create a text file, which will be working as a 'Data Base'.


while True: #This will create a loop which will always comeback to the menu (until the user types the third option 'Exit the System').  
    option = menu('\033[0;33mChoose an option: \033[m')
    if option == 1:
        Dashed_Line()
        print("Users".center(51))
        Dashed_Line() 
        print(open('DataBase.txt', 'r').read())
        sleep(2) #Sleep function to create a 'Loading Sensation'
        continue
    if option == 2:
        Dashed_Line()
        print("Create New User".center(51))
        Dashed_Line()
        CreateUser('\033[0;36mName: \033[m','\033[0;36mAge: \033[m')
        sleep(2)
        continue
    if option == 3: 
        sleep(2)
        Dashed_Line()
        print(emojize("\033[0;31mThank You for the preference :red_heart:   Feel free to come back anytime!\033[m".center(51)))
        Dashed_Line()
        break

