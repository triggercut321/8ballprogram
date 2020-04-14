#My magic 8 ball program

def main():

    import random

    ballanswers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes Definitely', 'You may rely on it', 
    'As I see it yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply Hazy, try again',
    'Ask me later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 
    'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    question = input("I am the magic 8 ball, I will give you the answer you seek! Ask me anything or say anything to me, please type it...\n")
    answer = random.choices(ballanswers)

    print("'"+ question + "'" + " " + "Is your question...\n" + "This is my answer..." + "\n" + str(answer))

    Repeat = input("Would you like to try again.. ?(type yes to try again)").lower()
    if Repeat =="yes":
        main()
    else:
        print("Have a good day.. !")
        exit()
main()