def music():
    print( "--------------------------------")
    print (  "WELCOE TO THE MUSIC CATEGORY")
    guesses = []
    correct_answer = 0
    question = 0
    for key in music_questions:
        print(key)
        for i in music_options[question]:
            print(i)
        guess = input("what your answer? \n a,b,c or d :\n ").lower()
        if len(guess) > 1:
            print('only one letter choice')
            guess = input("what your answer? \n a,b,c or d :\n ").lower()
        guesses.append(guess)
        correct_answer += asnwerChek(music_questions.get(key), guess)

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


music_questions = {'1. Halsey and this artist sang "Him and I", a well known hit in 2017.': 'c',
                   '2. Who is regarded as the Queen Salsa?': 'b',
                   '3. This famous music group created the song "Shoot to Thrill"?': 'a',
                   '4. Post Malone, Future and this artist sang the song "Die for me".': 'b',
                   '5. This artist is also known as the "Sun of Mexico".': 'a',
                   '6. This artist is regard as the "King of Bachata".': 'd',
                   '7. Drake and Rihanna sang this well regarded reggae song that became an instant hit.': 'b',
                   '8. "Empire State of Mind" was sang by Alicia Keys and this well regarded artist.': 'a',
                    '9. What artist created the song "Can I" in 2020? ': 'c',
                   '10. "In da club" was sung by this hip hop artist turned actor, turned entrepreneur.': 'b'

                   }
music_options = [['a) YungBlood', 'b)The Chainsmokers', 'c) G Eazy ', 'd) Even Peters'],
                 ['a) La India', 'b) Celia Cruz', 'c) Mariah Carey', 'd) Jennifer Lopez '],
                 ['a) ACDC   ', 'b) Metallica', 'c) John Mayer', 'd) Drown Pool'],
                 ['a)   Lil Kim ', 'b)  Halsey   ', 'c) Maddona', 'd) La Insuperable'],
                 ['a) Luis Miguel ', 'b)   Daddy Yankee', 'c) Miguel Angel', 'd) Maluma'],
                 ['a) Prince Royce', 'b) Dani J', 'c)  Nueva Era', 'c) Romeo Santos'],
                 ['a) No Guidance', 'b)Work   ', 'c) Needed Me ', 'd) Umbrella'],
                 ['a) Jay Z', 'b) 50 Cent ', 'c)Mac Miller', 'd) XXXTENTACION   '],
                 ['a) Beyonce', 'b) Rihanna ', 'c)Kehlani   ', 'd) TDivinyls'],
                 ['a)Wiz Khalifa', 'b)50 Cent', 'c)Kid Cudi   ', 'd) PARTYNEXTDOOR ']

                 ]
