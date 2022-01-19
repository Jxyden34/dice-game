import random
import time
import sys
WScore=0
WScore2=0
WScore3=0
WScore4=0
Winner=0
TS1=0
TS2=0
RT1=0
RT2=0

 

my_list = ["JAYDEN", "BOB", "JEFF", "STEWART","1","2","BREH","LEL","SHUTUP"]
name1= input("ENTER YOUR NAME ")
name1=name1.upper()
while name1 not in  my_list:
    print("WRONG NAME TRY AGAIN")
    name1= input("ENTER YOUR NAME ")
    name1=name1.upper()
print("WELCOME IN "+name1+" YOU ARE PLAYER 1")
print("")
name2= input("ENTER YOUR NAME ")
name2=name2.upper()
while name2 not in  my_list:
    print("WRONG NAME TRY AGAIN")
    name2= input("ENTER YOUR NAME ")
    name2=name2.upper()
print("WELCOME IN "+name2+" YOU ARE PLAYER 2")
print("")

 

for i in range(0,5):
    print("***************************************")
    print("ROUND "+str(i+1))
    print("")
    print(name1+"'S TURN TO ROLL THE DICE")
    input("PRESS ENTER TO ROLL THE DICE")
    value1=random.randint(1,6)
    value2=random.randint(1,6)
    RT1=value1+value2
    print("Dice 1:",value1)
    print("Dice 2:",value2)
    if RT1 % 2 == 0:
        print("EVEN +10")
        RT1=RT1+10
        print(name1+"'S TOTAL SCORE IS "+str(RT1))
    else:
        print("ODD -5")
        RT1=RT1-5
        print(name1+"'S TOTAL SCORE IS "+str(RT1))
    if value1== value2:
        print("DOUBLE SECOND DICE")
        input("PRESS ENTER TO ROLL THE DICE")
        value2=random.randint(1,6)
        print(value2)
        RT1=RT1+value2
        print(name1+"'S TOTAL SCORE IS "+str(RT1))
    TS1=TS1+RT1
    print("")
    print("")
    print(name2+"'S TURN TO ROLL THE DICE")
    input("PRESS ENTER TO ROLL THE DICE")
    value1=random.randint(1,6)
    value2=random.randint(1,6)
    RT2=value1+value2
    print("Dice1:",value1)
    print("Dice2:",value2)
    if RT2 % 2 == 0:
        print("EVEN +10")
        RT2=RT2+10
        print(name2+"'S TOTAL SCORE IS "+str(RT2))
    else:
        print("ODD -5")
        RT2=RT2-5
        print(name2+"'S TOTAL SCORE IS "+str(RT2))
    if value1== value2:
     print("DOUBLE SECOND DICE")
     input("PRESS ENTER TO ROLL THE DICE")
     value2=random.randint(1,6)
     print(value2)
     RT2=RT2+value2
     print(name2+"'S TOTAL SCORE IS "+str(RT2))
    TS2=TS2+RT2
    print("")
    print("***************************************")
    print("Round",i+1)
    print(name1+"'S RUNNING SCORE IS "+str(TS1))
    print(name2+"'S RUNNING SCORE IS "+str(TS2))

 

leaderFile = open("Leaderboard.txt","a")
print("***************************************")
if TS1>TS2:
 print(name1+" WINS :)")
 WScore=TS1
 Winner=name1
 leaderFile.close ()
elif TS1<TS2:
 print(name2+" WINS :)")
 WScore=TS2
 Winner=name2
 leaderFile.close ()
elif TS1==TS2:
 print("TIEBREKER")
 print(name1+"'S TURN TO ROLL THE SPECIAL DICE")
 input("PRESS ENTER TO ROLL THE SPECIAL DICE")
 value1=random.randint(1,100)
 print(value1)
 print("")
 print(name2+"'S TURN TO ROLL THE SPECIAL DICE")
 input("PRESS ENTER TO ROLL THE SPECIAL DICE")
 value2=random.randint(1,100)
 print(value2)
 print("")

 if value1<value2:
  print(name1+" IS THE TIEBREAKER WINNER :£")
  Winner=name1
  WScore=TS1
 elif value1>value2:
  print(name2+" IS THE TIEBREAKER WINNER ;£")
  Winner=name2
  WScore=TS2
else:
  print("Well how have you got hear then i think you may have broken the game u apsalue specimine of a person. Ngl think you need to replay this game to make it work cos thats not what is suppose to happen lol")

 

#Leaderboard

print("")
print(".......... Leaderboard ..........")
winner= (str(WScore/100),",",str(Winner))
print(winner)
f= open('leaderboard.txt','a')
f.write(''.join(winner))
f.write('\n')
f.close()
f=open("leaderboard.txt","r")
leaderboard=[line.replace('\n',' ') for line in f.readlines()]
leaderboard.sort(reverse=True)
leaderboard=leaderboard[0:5]
for i in range(5):
    print(leaderboard[i].replace(".",""))
f=open("leaderboard.txt","w")
for line in leaderboard:
    f.write(line)
    f.write('\n')
f.close()
print("...............................")
