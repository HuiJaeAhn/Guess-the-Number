def game_process():
    import random

    com_num = random.randint(1,101)
    money = 100
    
    print("[+] UpDownGame ")
    print("> 1에서 100사이의 숫자를 맞춰보세요~~ 정답시 무려 원금의 2배!!!")
    print("> 총 5번의 기회!! 오픈 기념 100원 기본 증정!!")

    while(money > 0):
        print("남은 금액 : {}".format(money))
        
        betting_money = int(input("배팅 금액 : "))
        while(betting_money > money):            
            print("보유 금액을 초과하셨습니다.")
            betting_money = int(input("배팅 금액 : "))
        
        life = 5
        while(life > 0):
            print("{}번 남았습니다.".format(life))
            user_num = int(input("숫자 입력 : "))

            gameres = updowngame(com_num, user_num)

            if(gameres):
                print("정답!!")
                com_num = random.randint(1,101)
                break
            
            life = life - 1
        
        if(life > 0):
            money = (money - betting_money) + betting_money*2
        else:
            money = money - betting_money
            print("정답은 {}였습니다...".format(com_num))
            com_num = random.randint(1,101)

def updowngame(com_num, user_num):
    if(user_num > com_num):
        print("{}보다 작습니다".format(user_num))
    elif(user_num < com_num):
        print("{}보다 큽니다".format(user_num))
    else:
        return True

game_process()