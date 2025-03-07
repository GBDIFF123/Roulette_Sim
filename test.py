from http.client import CONTINUE
import random
import os
import time
from wsgiref.types import StartResponse

def RollTheWheel():
    RollNum = random.randint(-1,36)
    return RollNum

def RollSimplify(RollNum):
    if RollNum <= 0:
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
def Random_Color_Message(Message):
    Letter = 0
    for L in Message:
        r = random.randint(100,255)
        g = random.randint(100,255)
        b = random.randint(100,255)
        print(f"\033[38;2;{r};{g};{b}m", end="")
        print(Message[Letter], end="", flush=True)
        Letter += 1
        time.sleep(0.02)
    print("")

def Clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

def Valid_Number_Sim_Setup(Input):
    messagesim2 = "Invaled input, only whole positive numbers above 0 accepted"
    try:
        IntInput = int(Input)
    except:
        Clear_window()
        Random_Color_Message(messagesim2)
        time.sleep(3)
        return "Fail"
    if IntInput <= 0:
        Clear_window()
        Random_Color_Message(messagesim2)
        time.sleep(3)
        return "Fail"
    else:
        return IntInput
while True:
    MessageVer = "Welcome! Would you like to play (enter 1) or simulate the Martingale system (enter 2)"   
    messageFail1 = "Please enter 1 or 2 and nothing else"
    Random_Color_Message(MessageVer) 
    UseCase = input()
    try:
        UseCase = int(UseCase)
    except:
        Random_Color_Message(messageFail1)
        time.sleep(3)
        Clear_window()
        continue

    #Play the game
    if UseCase == 1:
        Money = 10000
        Bet = 0
        while True:
            while True:
                STR_money = "{:,}".format(Money)
                Money_message = "You have $" + STR_money + " available"
                Clear_window()
                Message = "Play Roulette, enter choice: 1 = black 2 = red 3 = green"
                Random_Color_Message(Message)
                User_Choice = input()
                Message2 = "I could'nt quite hear ya, say that again please?"
                if User_Choice == "1" or User_Choice == "2" or User_Choice == "3":
                    User_Choice = int(User_Choice)
                else:
                    Random_Color_Message(Message2)
                    time.sleep(3)
                    continue
                Message6 = "How Much would you like to bet?"
                Random_Color_Message(Message6)
                print(Money_message)
                Bet = input()
                try:
                    Bet = int(Bet)
                except:
                    Random_Color_Message(Message2)
                    time.sleep(3)
                    continue
                if Bet > Money or Bet <= 0:
                    Random_Color_Message(Message2)
                    time.sleep(3)
                    continue
                break
            Roll = RollSimplify(RollTheWheel())
            Result = CheckWin(User_Choice, Roll)
            if Result == 1:
                Message3 = "WOAH, BIG WINNER OVER HERE! GREEN IS GOLD!!"
                Random_Color_Message(Message3)
                Bet *= 35
            elif Result == 2:
                Message4 = "WINNER!!!!"
                Random_Color_Message(Message4)
                Bet += Bet
            else:
                Message5 = "Better Luck next time!"
                Random_Color_Message(Message5)
                Bet -= Bet * 2
            Money += Bet
            time.sleep(1.5)
            if Money <= 0:
                Message7 = "Get on out of here! Your all out of money! (you lose!)"
                Random_Color_Message(Message7)
                break
            if Money >= 100000:
                Message8 = "Well, we are dry out of cash! you're pretty good at this! (you win!)"
                Random_Color_Message(Message8)
                break
    #Run Sim
    if UseCase == 2:
        while True:
            Clear_window()
            messagesim1 = "Simulate Martingale system (Reds, US table): set starting money value"
            Random_Color_Message(messagesim1)
            SimStartMoney = input()
            SimStartMoney = Valid_Number_Sim_Setup(SimStartMoney)
            if SimStartMoney == "Fail":
                continue
            messagesim3 = "Now set the table limit (can't bet more than this ammount)"
            Random_Color_Message(messagesim3)
            Table_Limit = input()
            Table_Limit = Valid_Number_Sim_Setup(Table_Limit)
            if Table_Limit == "Fail":
                continue
            messagesim4 = "Now set the starting bet (this will be doubled after each loss)"
            Random_Color_Message(messagesim4)
            Starting_Bet = input()
            Starting_Bet = Valid_Number_Sim_Setup(Starting_Bet)
            if Starting_Bet == "Fail":
                continue
            messagesim5 = "Now set Number of simulations (numbers above 10000 may take awhile)"
            Random_Color_Message(messagesim5)
            NumberOfSims = input()
            NumberOfSims = Valid_Number_Sim_Setup(NumberOfSims)
            if NumberOfSims == "Fail":
                continue
            Clear_window()
            Running_Sim_msg = "RUNNING"
            Current_Bet = Starting_Bet
            Wins = 0
            Losses = 0
            Highest_Money = 0
            Current_Money = SimStartMoney
            Simulations_Ran = 0
            Complete_starting = 1
            while True:   
                if Simulations_Ran >= NumberOfSims:
                    break
                if Current_Bet > Current_Money or Current_Bet > Table_Limit:
                    Simulations_Ran += 1
                    Current_Bet = Starting_Bet
                    Current_Money = SimStartMoney
                    Complete = Simulations_Ran / NumberOfSims * 100
                    if int(Complete) > Complete_starting:
                        Clear_window()
                        print("Working " + str(int(Complete)) + "% " )
                        Complete_starting += 1
                    continue         
                if Current_Money >= 99999999:
                    Beat_The_System = "yup" 
                    break   
                Did_win = RollSimplify(RollTheWheel())
                if Did_win == 2:
                    Current_Money += Current_Bet * 2 
                    Current_Bet = Starting_Bet
                    Wins += 1
                else:
                    Current_Bet *= 2
                    Current_Money -= Current_Bet
                    Losses += 1
                if Highest_Money < Current_Money:
                    Highest_Money = Current_Money
            Results_msg1 = "Most money made $" + str(Highest_Money)
            Results_msg2 = "Wins " + str(Wins) + " Losses " + str(Losses)
            Continue_Msg = "Press Enter to continue"
            Random_Color_Message(Results_msg1)
            Random_Color_Message(Results_msg2)
            Random_Color_Message(Continue_Msg)
            input()
            Clear_window()
            break
    
            
#makes stops int values of not 1 or 2 from starting program            
    else:
        Random_Color_Message(messageFail1)
        time.sleep(3)
        Clear_window()
        continue