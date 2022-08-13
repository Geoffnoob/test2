#program id: Zork game
#author: Geoffrey Zhang
#purpose: Coding an adventure like game.

#initial variables
roomnum = 1
inv_list=list()
life = 10

#defining rooms
def room_a():
  print("Spawn Point")
  print(inv_list)
  print(life)
  print("There seems to be a pathway East from here.")   


def room_b():
  print()
  print("Forest")
  print(inv_list)
  print(life)
  print("There seems to be 3 paths in this forest one to the Northeast(medium), one to the Southeast (easy), and one to the South(hard).")

def room_c():
  print()
  print("Goblin Camp")
  print(inv_list)
  print(life)
  sword_count = inv_list.count("sword")
  key_count = inv_list.count("key")
  if sword_count <1:
    print("You see a path to the Northeast but there are goblines in the way.")
  elif key_count <1:
    print("You can only go back Southwest to the forest from here.")
  else:
    print("You can go back Southwest to the forest or you can go Northeast into the Cave.")

def room_d():
  print()
  print("Goblin Cave")
  print(inv_list)
  print(life)


def room_e():
  print()
  print("Elf Forest")
  print(inv_list)
  print(life)
  bow_count = inv_list.count("bow")
  if bow_count < 1:
    print("You walk into the elf forest but its empty. There is however a flouting bow in the air. You pick it up and pull the string back forming a magic arrow that you fire at tree.")
    inv_list.append("bow")
    print(inv_list)  
  else:
    print("Theres nothing here.")
  print("There is a path North but you can go back Northwest.")

def room_f():
  print()
  print("Empty Camp")
  print(inv_list)
  print(life)
  sheild_count = inv_list.count("sheild")
  if sheild_count <1:
    print("You enter the Empty Camp and find a good sheild so you pick it up.")
    inv_list.append("sheild")
    print(inv_list)  
  print("There is a path to the Southeast but you can also go back North.")

def room_g():
  print()
  print("Trap Room")
  print(inv_list)
  print(life)
  print("Seems like the boss room is Southeast from here.")

def room_h():
  print()
  print("Dragon")
  print(inv_list)
  print(life)
  print("This is the last room. There is a dragon gaurding it's treasure. You just need to kill it to get all its treasures.")
  print("You enter the room and the Dragon wakes up to fight you.")

#game loop
while roomnum < 20:

  #spawn point
  if roomnum==1:
    room_a()
    where=input ("Which way do you want to go: ")
    where_l = where.lower()
    if where == "east":
      roomnum = 2
      print("You go east and get teleporteted to the middle of a forest.")  
    else:
      print("Sorry but the system dosn't understand this command.")
      roomnum = 1

  #forest
  if roomnum == 2:
    room_b()
    choice = input("What path would u like to take?: ")
    choice_l = choice.lower()
    if choice_l == "northeast":
      roomnum = 3
    elif choice_l == "southeast":
      roomnum = 4
    elif choice_l == "south":
      roomnum = 5
    else:
      print("Sorry but the system dosn't understand this command.")
      print()
      roomnum = 2

  #elf forest
  if roomnum == 4: 
    room_e()
    choice_3 = input("Where would you like to go?: ")
    choice_3l = choice_3.lower()
    if choice_3l == "northwest":
      roomnum = 2
    elif choice_3l == "north":
      print("You go north and there seems to be a magical wall forming behind you every step you take making you unable to walk back.")
      roomnum = 3
    else:
      print("Sorry but the system dosn't understand this command.")
      print()
      roomnum = 4    

  #goblin camp
  if roomnum == 3: 
    room_c()
    sword_count = inv_list.count("sword")
    if sword_count < 1: 
      if choice_l == "northeast":
        answer1 = input("What is 9+10? (meme answer): ")
      elif choice_3l == "north":
        answer1 = input("What is 20+1? (normal answer): ")
      if answer1 == 21:
          print("You were able to sneak up on the goblins and take them out easily. You also get a sword.")
          
      else:
        print("After a long fight with the goblins you lost 2 hearts and gained a sword.")
        life = life - 2 
      inv_list.append("sword")

    choice_2 = input("Where would you like to go?: ")
    choice_2l = choice_2.lower()
    if choice_2l == "northeast":
      roomnum = 6
    elif choice_2l == "southwest":
      roomnum = 2
    else:
      print("Sorry but the system dosn't understand this command.")
      print()
      roomnum = 3


  #empty camp
  if roomnum == 5: 
    room_f()
    choice_4 = input("Where would you like to go?: ")
    choice_4l = choice_4.lower()
    if choice_4l == "southeast":
      roomnum = 7
    elif choice_4l == "north":
      roomnum = 2
    else:
      print("Sorry but the system dosn't understand this command.")
      print()
      roomnum = 5      

  #goblin boss
  if roomnum == 6:
    room_d()
    answer_2 = input("Unscramble (ntepelha): ")
    if answer_2 == "elephant":
      print("After a long drawnout fight you get the upper hand with your sword and kill the Goblin King.")
    else:
      print("After a long fight the Goblin King starts getting the upper hand and you get knocked around a big before you use all ur might to finally take him down.")
      life = life - 6

    print("After beating the Goblin King you find a key around his neck and take it. But then the cave starts collapsing and you run Southest towords the Empty Goblin Camp.")

    roomnum = 3


  #trap room
  if roomnum == 7:
    room_g()
    key_count = inv_list.count("key")
    if key_count < 1:
      print("You dont have the key so you can't go threw the shortcut room. After fumbling through the trap room you active some of them making you lose 5 lives. Right before you got out you activate one more trap that you block with your sheild causing you to lose it too.")
      life = life -5
      inv_list.remove("sheild")
    choice_6 = input("Where would you like to go?: ")
    choice_6l = choice_6.lower()
    if choice_6l == "southeast":
      roomnum = 8
    elif choice_6l == "northwest":
      roomnum = 5
    else:
      print("Sorry but the system dosn't understand this command.")
      print()
      roomnum = 7   

  #dragon
  if roomnum == 8:
    room_h()
    print("The Dragon spreads its wings lets out a screech and assents to the air.")
    bow_count=inv_list.count("bow")
    if bow_count < 1:
      print("You don't have a bow so you can't shoot him down.")
      life = life - 9
    else:
      print("You take out your bow and aim.")
      answer_d1= input("What direction did you go from spawn.")
      answer_d1l = answer_d1.lower()
      if answer_d1 == "east":
        print("You take the shot and you hit its wings sending him to the ground.")
      else:
        print("You take the shot but miss.")
        life = life-9
    print(life)
    print("The Dragon lands and charges his fire breath.")
    sheild_count = inv_list.count("sheild")
    if sheild_count <1:
      answer_d2 = input("What is my favorite color?: ")
      if answer_d2 == "red":
        print("You don't have a sheild but your able to dodge by rolling the the left.")
      else:
        print("You dont react in time and get hit by the fire.")
        life=life-10
    else:
      answer_d2 = input("What is the color of blood?: ")
      answer_d2l = answer_d2.lower()
      if answer_d2 == "red":
        print("You take out your sheild and block his fire breath. ")
      else:
        print("You dont take you sheild out in time getting hit by some fire losing 7 lives.")
    print(life)
    print("Now hes and tired. You take this change to attack.")
    sword_count = inv_list.count("sword")
    if sword_count < 1:
      print("You go in for the kill but don't have a sword so you dont do enough. The Dragon gets back up and swings at you.")
      life=life-10
    else:
      print("You go in for the kill. You stab your sword into its head and kill the dragon. Now the Treasue is all yours.")
    roomnum = 21

#when the game ends
if life > 0:
  print("Congratulations you Win!!")
else:
  print("Game Over.")