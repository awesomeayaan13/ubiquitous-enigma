guess=int(input("Enter your guess: "))

number=3
chances=5
while (chances=5):

    if(guess<number):
        print:("Guess is to low")
        chances=chances-1
    elif(guess>number):
         print("Guess is to high")
         chances=chances-1       
    elif(guess=number):
         chances=chances-1
        print("Yay you did it")

if(chances=0):
    print("You lose get good")