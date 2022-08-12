from movies import *
from Television import *
from music import *
from history import *
def category_selection():
    categories=  ['MOVIES','MUSIC','HISTORY','TELEVISOIN']
    for i in categories :
        print(i)
    category= input("Welcome, What category would you like to play today?" ).upper()
    if category== 'MOVIES':
        movies()
    elif category=="MUSIC":
        music()
    elif category =='HISTORY':
        history()
    elif category =='TELEVISION':
        television()
    else:
        print("There is no such category here!")

def play_again ():

    decision= ['MOVIES','MUSIC','HISTORY','TELEVISOIN','QUIT' ]
    for i in decision:
        print(i)

    play=input("What category would you like to play? " ).upper()
    if play== 'QUIT':
        return False

    if play == 'MOVIES':
        movies()
    elif play == "MUSIC":
        music()
    elif play == 'HISTORY':
        history()
    elif play == 'TELEVISION':
        television()
    else:
        print("check your category again")
        category_selection()


category_selection()

while play_again():
    play_again()




