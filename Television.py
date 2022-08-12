def television():
    print("--------------------------------")
    print("WELCOE TO THE TELEVISION CATEGORY")
    guesses = []
    correct_answer = 0
    question = 0
    for key in television_questions:
        print(key)
        for i in television_options[question]:
            print(i)
        guess = input("what your answer? \n a,b,c or d :\n ").lower()
        if len(guess) > 1:
            print('only one letter choice')
            guess = input("what your answer? \n a,b,c or d :\n ").lower()
        guesses.append(guess)
        correct_answer += asnwerChek(television_questions.get(key), guess)

        question = question + 1
    score_percetage(correct_answer, guess)


def asnwerChek(answer, guess):
    if answer == guess:
        print("Correct!")
        return 10
    else:
        print("Nope!")
        return 0


def score_percetage(correct_answer, guess):
    print("RESULTS DISPLAY")
    percent = correct_answer
    print("your score is " + str(percent) + "%")

    if percent >= 90:
        print(str(percent) + " Awesome Job! ")
    elif 80 <= percent < 90:
        print(str(percent) + " Good work!")
    elif 70 <= percent < 80:
        print(str(percent) + " Well, you tried.")
    else:
        print(str(percent) + " You may want to read more and put down the phone")


television_questions = {'1. Ted Mosby was the main character in this television series.': 'd',
                   '2. These three brothers were famous for their goof ball antics in this 1920s television series.': 'c',
                   '3. "Will you be my neighbor" was a song that was sung by this prominent tv character.': 'd',
                   '4. This live action series featured the origins of Batman and his early villians and romantic interests.': 'a',
                   '5. This teen drama from 2012 was among Black Lively  first acts in.': 'b',
                   '6. Joseph Sikora plays this street wise character in both Power and Force television series.': 'd',
                   '7. This character in the show of the same name was first played by Andy Whitfield.': 'a',
                   '8. This show in which rapper 50 cent is the executive producers shows the rise of the Flenory brothers.': 'd',
                     '9. This television series which is also a titled movie previously with Jennifer Love Hewitt as the main heroine gave rise to urban legends.': 'c',
                   '10. This show features Clark Kents highschool years to early adulthood and eventually taking up the mantle of Superman.': 'c'

                        }
television_options = [['a) House', 'b) Friends', 'c) General Hospital ', 'd) How I Met Your Mother'],
                      ['a)  The Untouchables ', 'b) Boardwalk Empire', 'c) The Three Stooges', 'd) I Love Lucy '],
                      ['a) Zaboomafoo', 'b) Sesame Streets', 'c) For Kids By Kids', 'd) Mr Rogers Neighborhood'],
                      ['a)  Gotham  ', 'b)  Batman Original Series', 'c) The Batman', 'd) Birds of Prey'],
                      ['a) Jessica Jones', 'b)  Gossip Girl', 'c) Orange Is The New Black', 'd) Sheena'],
                      ['a) Kanan', 'b) James St Patrick', 'c) Symphony Bosket', 'c) Tommy Egan'],
                      ['a) Spartacus', 'b) Roman Empire', 'c) Rome ', 'd) Legion'],
                      ['a) Gun', 'b) Twelve ', 'c) Den of Thieves', 'd) BMF   '],
                      ['a) Scream', 'b)  Urban Legends Final Cut', 'c)I Know What You Did Last Summer ', 'd) The Walking Dead'],
                      ['a)Clark & Lois', 'b)Supergirl', 'c) Smallville   ', 'd) Krypton ']

                      ]
