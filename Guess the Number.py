def game_process():
    import random

    com_num = random.randint(1,101)
    life = 5

    while(life > 0):
        print("life : {}".format(life))
        user_num = int(input("숫자 입력 : "))

        gameres = updowngame(com_num, user_num)

        if(gameres):
            print("success")
            exit()
        life = life - 1

    print("the game is over")
    print("the answer is {}".format(com_num))

def updowngame(com_num, user_num):
    if(user_num > com_num):
        print("dowm")
    elif(user_num < com_num):
        print("up")
    else:
        return True

game_process()
while(True):
    restart = input("Do you wanna retry?? [yes/no] : ")
    if (restart == "yes"):
        game_process()
    elif (restart == "no"):
        exit()
