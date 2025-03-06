import random
import os
import time

def RollTheWheel():
    RollNum = random.randint(1,36)
    return RollNum

def RollSimplify(RollNum):
    if RollNum <= 2:
        return 1
    elif RollNum >= 19:
        return 2
    else:
        return 3

def CheckWin(Choice, SimpleRoll):
    if Choice == 3 and SimpleRoll == 1:
        return 1
    elif Choice != 3 and SimpleRoll == 2:
        return 2
    else:
        return 3
def Random_Color_Message(Message, speed):
    Letter = 0
    for L in Message:
        r = random.randint(100,255)
        g = random.randint(100,255)
        b = random.randint(100,255)
        print(f"\033[38;2;{r};{g};{b}m", end="")
        print(Message[Letter], end="", flush=True)
        Letter += 1
        time.sleep(speed)
    print("")

def Clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

#Play the game
Money = 10000
Bet = 0
while True:
    while True:
        STR_money = "{:,}".format(Money)
        Money_message = "You have $" + STR_money + " available"
        Clear_window()
        Message = "Gambling simulator enter choice: 1 = black 2 = red 3 = green"
        Random_Color_Message(Message, 0.02)
        User_Choice = input()
        Message2 = "I could'nt quite hear ya, say that again please?"
        if User_Choice == "1" or User_Choice == "2" or User_Choice == "3":
            User_Choice = int(User_Choice)
        else:
            Random_Color_Message(Message2, 0.02)
            time.sleep(3)
            continue
        Message6 = "How Much would you like to bet?"
        Random_Color_Message(Message6, 0.02)
        print(Money_message)
        Bet = input()
        try:
            Bet = int(Bet)
        except:
            Random_Color_Message(Message2, 0.02)
            time.sleep(3)
            continue
        if Bet > Money or Bet <= 0:
            Random_Color_Message(Message2, 0.02)
            time.sleep(3)
            continue
        break
    Roll = RollSimplify(RollTheWheel())
    Result = CheckWin(User_Choice, Roll)
    if Result == 1:
        Message3 = "WOAH, BIG WINNER OVER HERE! GREEN IS GOLD!!"
        Random_Color_Message(Message3, 0.02)
        Bet *= 35
    elif Result == 2:
        Message4 = "WINNER!!!!"
        Random_Color_Message(Message4, 0.02)
        Bet += Bet
    else:
        Message5 = "Better Luck next time!"
        Random_Color_Message(Message5, 0.02)
        Bet -= Bet * 2
    Money += Bet
    time.sleep(1.5)
    if Money <= 0:
        Message7 = "Get on out of here! Your all out of money! (you lose!)"
        Random_Color_Message(Message7, 0.02)
        break
    if Money >= 100000:
        Message8 = "Well, we are dry out of cash! you're pretty good at this! (you win!)"
        Random_Color_Message(Message8, 0.02)
        break