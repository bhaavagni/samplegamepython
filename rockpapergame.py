import random

list=["rock","paper","Scissor"]
def printresult(uinput,sinput):
    if (uinput-1) > sinput:
        print("System selected",list[sinput],"and won!")
    elif (uinput-1) == sinput:
        print("Clash")
    else:
        print("User selected",list[uinput-1],"and Won!")


def playgame():
    while True:
        print("Please enter your choice")
        print("1.Rock 2.Paper 3.Scissor")
        userinput=int(input())
        sysinput = random.randrange(0,2)
        #print("systemselected",list[sysinput],"input",sysinput)
        #print("User selected",list[userinput-1])
        printresult(userinput,sysinput)
        playagain = input("Play again??? (y/n): ")
        if playagain.lower() != "y":
            break

if __name__ == '__main__':
    playgame()
