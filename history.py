def history():
    print("--------------------------------")
    print("WELCOE TO THE HISTORY CATEGORY")
    guesses = []
    correct_answer = 0
    question = 0
    for key in history_questions:
        print(key)
        for i in history_options[question]:
            print(i)
        guess = input("what your answer? \n a,b,c or d :\n ").lower()
        if len(guess) > 1:
            print('only one letter choice')
            guess = input("what your answer? \n a,b,c or d :\n ").lower()
        guesses.append(guess)
        correct_answer += asnwerChek(history_questions.get(key), guess)

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


history_questions = {'1. The cradle of civilization is located in.': 'c',
                   '2. The founder of the Mongol empire was?': 'a',
                   '3. The Mayan empire originated in what country?.': 'c',
                   '4. Japans famous warriors were known as.': 'a',
                   '5. Famous Macedonian general who conquered persia and most of Eurasia.': 'c',
                   '6. The witch trials of 1692 were held in this old american town.': 'd',
                   '7. Ancient lost but found city in Peru is called?': 'd',
                   '8. What was the name of Romes most famous military general turned politician who was killed by being stabbed by 60': 'c',
                     '9.Name of the fabled Greek city believed to have been swalled by the ocean was called?  .': 'b',
                   '10. Who was the richest man in ancient history?': 'c'

                     }
history_options = [['a) Athens', 'b) Chichen Itza', 'c) Mesopotamia ', 'd) Sumer'],
                   ['a)  Genghis Khan', 'b) Kublai Khan', 'c) Sonin', 'd)  Ebilun '],
                   ['a) Brazil', 'b) Argentina', 'c) Mexico', 'd)Ecuador'],
                   ['a)  Samurai  ', 'b) Ninja', 'c) Sohei', 'd) Ashigaru'],
                   ['a) Leonidas', 'b)  Ptolemy', 'c) Alexander', 'd) Phillip'],
                   ['a) York', 'b) Richmond', 'c) Charleston', 'c) Salem'],
                   ['a) Caral', 'b) Teotihuacan', 'c) Cuzco ', 'd) Machu Picchu '],
                   ['a) Gaius Antonius', 'b) Marcus Crassus ', 'c) Julius Caesar', 'd) Mark Anthony  '],
                   ['a) Knossos', 'b)  Atlantis', 'c)Mu', 'd) Sparta'],
                   ['a)Elon Musk', 'b)Jeff Bezzos', 'c) Mansa Musa     ', 'd) Croesus ']

                   ]



