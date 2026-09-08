import random
import time
Green = "\033[92m"
Red = "\033[91m"
Yellow ="\033[93m"
Cyan ="\033[96m"
Reset ="\033[0m"


while True:
  print(Cyan +"\n🎮 Number Match Game" + Reset)
  chances = 3
  print("\rComputer is choosing.",end="")
  time.sleep(0.5)
  print("\rComputer is choosing..",end="")
  time.sleep(0.5)
  print("\rComputer is choosing...",end="")
  time.sleep(0.5)
  print("\r\033[K",end="")
  computer_number = random.randint(1,100)
  while chances >0:
    print("❤️ Chances:", chances)
    try:
      your_number = int(input("Enter Your Number (1-100): "))
    except ValueError:
      print(Yellow + "❌ Please Enter A Valid Number." + Reset)
      continue
    if your_number < 1 or your_number > 100:
      print(Yellow + "Please Enter A Number Between 1 and 100." + Reset)
      continue
    
    print("Your Number: ",your_number)
    if your_number == computer_number:
     print(Green + "🎉You Win" + Reset)
     print("Computer's Number:",computer_number)
     break
    else:
     print(Red +"❌You Lose!" + Reset)
     chances = chances-1
     if chances >0:
      if your_number<computer_number:
        print(Yellow + "🔺Try a Higher Number!"+Reset)
      else:
        print(Yellow + "🔻Try a Lower Number!"+Reset)
  if chances == 0:
    print(Red+"💀 Game Over!"+ Reset)
    print("Computer's Number:",computer_number)
  time.sleep(1.2)
  restart = input("\nPlay Again?(Y/N):").lower()
  if restart != "y":
   print(Cyan + "Game Closed!" + Reset)
   break
