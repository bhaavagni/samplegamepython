import random
# print("Please enter your choice")
# print("1.Rock 2.Paper 3.Scissor")
# userinput=input()
# sysinput = random.randrange(1,3)
list=["rock","paper","Scissor"]
while True:
    print("Please enter your choice")
    print("1.Rock 2.Paper 3.Scissor")
    userinput=int(input())
    sysinput = random.randrange(0,2)
    #print("systemselected",list[sysinput],"input",sysinput)
    #print("User selected",list[userinput-1])
    if (userinput-1) < sysinput:
        print("System selected",list[sysinput],"and won!")
    elif (userinput-1) == sysinput:
        print("Clash")
    else:
        print("User selected",list[userinput-1],"and Won!")

    playagain = input("Play again? (y/n): ")
    if playagain.lower() != "y":
        break


