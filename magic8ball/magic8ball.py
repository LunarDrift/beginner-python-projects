import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


print(r'  __  __          _____ _____ _____    ___  ')
print(r' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(r' | \  / |  /  \ | |  __  | || |      | (_) |')
print(r' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(r' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(r' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print(r'')
print(r'')
print(r'')

name = input("Hello World, what is your name? ")
print(f"Hello {name}")

def Magic8Ball():
    print("Ask me a yes or no question.")
    input()
    print(answers[random.randint(0, len(answers)-1)])
    print("I hope that helped!")
    Replay()

def Replay():
    print("Do you have another question? [Y/N] ")
    reply = input()
    if reply == "Y":
        Magic8Ball()
    elif reply == "N":
        exit()
    else:
        print("Sorry, I didn't catch that. Please try again.")
        Replay()

Magic8Ball()