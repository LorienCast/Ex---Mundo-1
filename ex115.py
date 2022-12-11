def Dashed_Line (tam = 51):
    '''
    51 dashed lines used to separate, or highlight, contents/titles.
    '''
    return print('-'*tam)
    
def menu(msg):
    '''
    A menu will be displayed to introduce 3 actions that can be done by the user: See a list of all users in the system, create a new user and 
    exit the program. 

    Parameter:
    msg (int): the variable 'msg' takes 1 of 3 possible values to be choosen by the user. These values will define which one of the actions
               will be picked. 

    Return: 
    option (int): If the user type a number between 1-3, the choosen number will be return to the main program. However, if the user type
                  anything different from that, an error message will appear and, through the loop, they will be back to choose a valid option.                  
    '''

    Dashed_Line()
    print("Main Menu".center(51))
    Dashed_Line()
    print("\033[0;33m1\033[m - \033[0;34mUsers\033[m")
    print("\033[0;33m2\033[m - \033[0;34mCreate New User\033[m")
    print("\033[0;33m3\033[m - \033[0;34mExit\033[m")
    Dashed_Line()
    while True:
        try:
            option = int(input(f'\033[0;32m{msg}\033[m'))
        except (TypeError,ValueError):
            print('\033[0;31mERROR! Please, type a valid whole number!\033[m')
        else:
            if option >=1 and option <=3:
                return option
            else:
                print('\033[0;31mERROR! Please, type a valid option\033[m')
                continue
def CreateUser(msg1,msg2):
    '''
    A function to create an user. 

    Parameters:
    msg1 (str): Parameter 'msg1' takes a value that will be assigned to variable 'name'. 
    msg2 (str): Parameter 'msg2' takes a value that will be assigned to variable 'age'. Even though the value is a integer, it has been turned
                into a string, so the function 'rjust()' could be used.

    Return: 
    it has no return 
    '''
    
    name = str(input(msg1)).strip().title()
    age = str(input(msg2)).strip()
    archive = open('DataBase.txt', 'r') #Open, in the reading mode, the text file created in the main program. 
    content = archive.readlines() #Read all the current lines/content 
    content.append(f'{name.ljust(20)} {age.rjust(20)} years old\n') #Append the name and age of the users into the 'Data Base'
    archive = open('DataBase.txt', 'w') #Open, in the writing mode, the text file created in the main program 
    archive.writelines(content)#Write the content on the file
    archive.close()#close the text file 
    print(f'\033[0;32m{name} has been successfully created\033[m')