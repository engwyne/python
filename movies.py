def  movies():
    print("--------------------------------")
    print("WELCOE TO THE MOVIES CATEGORY")
    guesses=[]
    correct_answer=0
    question = 0
    for key in movie_questions:
        print (key)
        for i in  movie_options[question ]:
            print(i)
        guess=input("what your answer? \n a,b,c or d :\n ").lower()
        if len(guess) > 1:
            print('only one letter choice')
            guess = input("what your answer? \n a,b,c or d :\n ").lower()
        guesses.append (guess)
        correct_answer += asnwerChek(movie_questions.get(key), guess)

        question=question+1
    score_percetage(correct_answer,guess )


def asnwerChek(answer,guess):
    if answer== guess:
        print("Correct!")
        return 10
    else:
        print("Nope!")
        return 0


def score_percetage(correct_answer,guess ):
    print("RESULTS DISPLAY"  )
    percent= correct_answer
    print("your score is "+ str(percent) + "%")

    if percent >= 90:
        print(str(percent)+" Awesome Job! ")
    elif   80  <= percent <90:
        print(str(percent) +" Good work!")
    elif   70 <= percent <80:
        print(str(percent)+" Well, you tried.")
    else:
        print(str(percent)+" You may want to read more and put down the phone")


movie_questions={ '1. What movie made the song "Scotty doesnt know" famous?':'c', '2. Slade Wilson is a character in this movie.':'d',
  '3. What line was "I ll be your Huckleberry" in?':'b',  '4. Tom Holland played this Marvel superhero.':'d', '5. "Wakanda Forever" was a saying in this superhero movie.':'a' ,
   '6. Name of Harry Potters enemy.'  :'d', '7. Emily Browning and Vanessa Hudgens were two female warriors in this movie.':'a',
   '8. Ellen Ripley was the heroine in this movie':'b', '9. Vito Corleone was also called.':'c' , '10. The Ghost face mask was made famous in this movie.':'d'

                 }
movie_options= [['a) Van Wilder ','b) Lampoons Vacation','c) Eurotrip ','d) National Treasure' ],
                ['a) Batman ','b) Superman','c) Black Panther','d) Deadpool '],
                ['a) Wild West','b) Tombstone','c) Black Snake Moan','d) Django'],
                ['a) Batman','b) Deapool','c) Daredevil','d) Spiderman'],
                ['a) Black Panther','b) Batman','c) Spawn','d) Jessica Jones'],
                ['a) Dumbledore','b) Grindewald','c) Ronald Weasley','c) Ronald Weasley'],
                ['a) Suckerpunch','b) Striptease','c) Black Widow','d) Bates Motel'],
                ['a) Star Wars','b) Alien ','c) Close Encounter','d) E.T.'],
                ['a) Goodfella','b) Scarface','c) Godfather','d) Carlos'],
                ['a) Freddy Kruger','b) Friday 13th','c) The Punisher','d) Scream']

                ]
