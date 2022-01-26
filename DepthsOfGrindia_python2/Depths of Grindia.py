#Importing Packages
import time
import random
import sys

def CalculateEnemyStats(Monster, BaseAttk, BaseDef, BaseHP, PlayerLvl):
                if (PlayerLvl % 5 == 0):
                                BaseAttk = BaseAttk * (PlayerLvl/5)

def UseItem(Item):
   global PlayerHealth
   global MaxPlayerHealth
   global EnemyTempHealth
   global Poisoned
   global PlayerEXP
   global PlayerEXPMax
   global PlayerLevel
   global PlayerAttk
   global PlayerDef
   if (Item == 0):
      PlayerHealth = PlayerHealth + 30
      if (PlayerHealth >= MaxPlayerHealth):
         PlayerHealth = MaxPlayerHealth
      print "Health has been restored by 30!"
   elif (Item == 3):
       Poisoned = False
       print "You were cured from your illnesses."
   elif (Item == 1):
      print "You throw a bottle of holy water..."
      time.sleep(0.3)
      print "CRASH!"
      if (MonsterNO == 5) or (MonsterNO == 6)\
         or (MonsterNO == 7) or (MonsterNO == 8) \
         or (MonsterNO == 9) or (MonsterNO == 12) \
         or (MonsterNO == 13) or (MonsterNO == 14) \
         or (MonsterNO == 18) or (MonsterNO == 19) or \
         (MonsterNO == 20) or (MonsterNO == 23):
         EnemyTempHealth = EnemyTempHealth - 666
         time.sleep(0.3)
         print "It's weak to that!"
         time.sleep(0.1)
         print "You did 666 damage!"
      else:
         print "It didn't seem to do anything..."
   elif (Item == 2):
      Poisoned = True
      PlayerHealth = PlayerHealth - 5
      time.sleep(0.3)
      print "You were poisoned!"
   elif (Item == 4):
      PlayerEXP = PlayerEXP + 50
      print "You feel smarter already!"
      if (PlayerEXP >= PlayerEXPMax):
         print "In fact, you feel so smart that you leveled up!"
         PlayerLevel = PlayerLevel + 1
         PlayerAttk = PlayerAttk + 1
         PlayerDef = PlayerDef + 1
         MaxPlayerHealth = MaxPlayerHealth + 4
         PlayerHealth = MaxPlayerHealth
         PlayerEXP = PlayerEXP - PlayerEXPMax
         PlayerEXPMax = PlayerEXPMax + 20
         if (PlayerEXP >= PlayerEXPMax):
             print "Wow! You leveled up again!"
             PlayerLevel = PlayerLevel + 1
             PlayerAttk = PlayerAttk + 1
             PlayerDef = PlayerDef + 1
             MaxPlayerHealth = MaxPlayerHealth + 2
             PlayerHealth = MaxPlayerHealth
             PlayerEXP = PlayerEXP - PlayerEXPMax
             PlayerEXPMax = PlayerEXPMax + 20
   elif (Item == 5):
       PlayerDef = PlayerDef + 6
       print "Your defense has risen by 6!"
       EasterEgg = random.randrange(0,101)
       if (EasterEgg >= 90):
           time.sleep(0.5)
           print "You also hope that your coach won't find out you've been using these."
   elif (Item == 6):
       print "You toss the bomb..."
       time.sleep(0.5)
       print "KABOOM!"
       time.sleep(0.3)
       if (EnemyTempHealth != -666):
           EnemyTempHealth = EnemyTempHealth - 60
           print "You did 60 damage!"
       else:
           print "There was nothing to blow up!"
           time.sleep(0.3)
           print "Oh well."
   elif (Item == 8):
       print "You toss the big bomb..."
       time.sleep(0.5)
       print "Your ears started to ring..."
       time.sleep(0.3)
       if (EnemyTempHealth != -666):
           EnemyTempHealth = EnemyTempHealth - 120
           print "You did 120 damage!"
       else:
           print "There was nothing to blow up!"
           time.sleep(0.3)
           print "Your ears are still ringing."
   elif (Item == 7):
       print "I hope you don't plan on winning any olympic games with this..."
       time.sleep(0.3)
       PlayerAttk = PlayerAttk + 2
       print "Your attack went up by 2!"
   elif (Item == 9):
      PlayerHealth = PlayerHealth + 60
      if (PlayerHealth >= MaxPlayerHealth):
         PlayerHealth = MaxPlayerHealth
      print "Health has been restored by 60!"
   else:
      print "That item doesn't have code yet!"
   PlayerInventory.remove(Item)

#Enemy Data (Name, Attack, Defense, BaseHP)
EnemyData = ('Test Monster','0','0','1', \
             'Lost Feral Adventurer', 5, 1, 14, \
             'Snake', 2, 1, 10, \
             'Venomous Snake', 10, 1, 5, \
             'Cave Rat', 2, 1, 3, \
             'Corrupt Cave Dweller', 12, 4, 20, \
             'Lizard Demon', 6, 3, 40, \
             'Commodor Vic 20', 4, 8, 64, \
             'Cave Master', 20, 16, 1332, \
             'Ghool', 4, 6, 30, \
             'Spider', 2, 3, 10,\
             'Giant Spider', 4, 6, 20, \
             'Skeleton', 8, 4, 15, \
             'Bloody Skeleton', 10, 4, 30, \
             'Zombie', 12, 10, 60, \
             'Black Knight', 20, 20, 100, \
             'Dragon', 20, 6, 200, \
             'Firebreathing Dragon', 40, 12, 400, \
             'Zombie Dragon', 60, 24, 800, \
             'Decaying Zombie', 14, 4, 60, \
             'Knight', 10, 6, 50, \
             'Alchoholism', 30, 10, 70, \
             'Zombie Knight', 20, 14, 100, \
             'Nightmare', 30, 30, 200, \
             'Fungus Monster', 10, 16, 60, \
             'Overgrown Mushroom', 12, 30, 100, \
             'Your Sanity', 6, 7, 30)
AttackPrints = ('SLASH!', 'CRASH!', 'BUNF!', "It's super effective!", "BING!", 'CRACK!')
WeaponName = ('short sword', 'broad sword', 'skeleton sword', 'THE BONE ZONE', 'twig', 'rusty axe', 'rusty butcher knife', 'skeleton femur', 'bloody skeleton femur', 'DIY Home Depot hammer', "black knight's sword", 'SYNTAX ERROR', 'rock', 'brass knuckles', "knight's sword")
WeaponStats = (6, 12, 20, 16, 1, 14, 8, 7, 11, 10, 40, 25, 2, 10, 20)

GameStarted = False
EnemyTempHealth = -666
PlayerWeapon = 'dagger'
AreaNO = 1
PlayerLevel = 0
PlayerInventory = [0]
InventoryName = ('small potion','holy water', 'murky potion', 'clear potion', 'potion of knowledge', 'defense in a jar', 'bomb', 'steroids', 'big bomb', 'big potion')
PlayerEXP = 0
Steps = 0
StepsToGo = 0
Sections = 0
PlayerDamageBoost = 4
PlayerAttk = 2
PlayerDef = 0
PlayerEXPMax = 100

#Title Screen and Startup Code
while True:
   if (AreaNO == 1):
      GameStarted = False
   if (GameStarted != True):
      print "The Depths of Grindia"
      time.sleep(0.5)
      print
      print "What would you like to do?"
      print "S(Start game)"
      print "C(credits)"
      print "Q(Quit)"
      Menu = raw_input("> ")
      Menu = Menu.lower()
      #Debug menu
      if (Menu == "debug"):
                      GameStarted = True
                      #LastArea 1 brings you back to the main menu
                      LastArea = 1
                      print
                      print "Entered Debug Mode"
                      print "What would you like to test?"
                      print "B(Battle)"
                      print "C(Treasure chest(brings player to treasure chest))"
                      print "E(Ending sequence)"
                      DebugInput = raw_input ("> ")
                      DebugInput = DebugInput.lower()
                      if (DebugInput == "b"):
                                      print (len(EnemyData) / 4), 'monsters in role call'
                                      Poisoned = False
                                      MonsterNO = raw_input("Input Monster Number ")
                                      MonsterNO = int(MonsterNO)
                                      PlayerHealth = raw_input('Input Player HP ')
                                      PlayerHealth = int(PlayerHealth)
                                      MaxPlayerHealth = raw_input('Input Player Max HP ')
                                      MaxPlayerHealth = int(MaxPlayerHealth)
                                      PlayerLevel = raw_input('Input Player Level ')
                                      PlayerLevel = int(PlayerLevel)
                                      print "BATTLE!"
                                      print 'Monster number', MonsterNO, 'out of', len(EnemyData)/4
                                      #AreaNO variable determines where the character is
                                      AreaNO = 0
                      elif (DebugInput == 'c'):
                                      print "Setting AreaNO, SectionType and Steps variables..."
                                      Steps = 1
                                      StepsToGo = 12
                                      PlayerHealth = 5
                                      MaxPlayerHealth = 5
                                      Poisoned = False
                                      SectionType = 2
                                      AreaNO = 3
                                      SectionType = 0
                                      print
                                      print "READY"
                                      print
                      elif (DebugInput == 'e'):
                          print
                          print "Setting variables..."
                          StepsToGo = 10
                          Steps = 10
                          AreaNO = 3
                          SectionType = 0
                          PlayerHealth = 20
                          Advance = ' '
                          print
                          print "READY"
                          print
      elif (Menu == 'c'):
         print
         print "This game was done by Daylen Rickert"
         print
         time.sleep(0.5)
      elif (Menu == 's'):
         LastArea = 1
         AreaNO = 2
      elif (Menu == 'q'):
         break
      else:
         print
         print "I don't know what you typed, but I hope it wasn't an insult."
         print

   if (AreaNO == 2):
      Poisoned = False
      GameStarted = True
      PlayerLevel = 1
      PlayerHealth = 40
      MaxPlayerHealth = 40
      StepsToGo = random.randrange(100,400)
      Steps = 0
      print
      print "Would you like to skip the intro? (Y/N)"
      Skip = raw_input('> ')
      Skip = Skip.lower()
      if (Skip != 'y'):
         print "You've awoken in a dark and ominous looking cave that seems to go straight forever."
         time.sleep(1)
         print "The entrance behind you seems to have collapsed recently."
         time.sleep(1)
         print "You're not sure how or why you ended up here..."
         time.sleep(2)
         print "or even who you are."
         time.sleep(1)
         print "You're armed with a rather stubby dagger."
         time.sleep(1)
         print "Search the caves for another exit."
         time.sleep(1)
         print "Oh, and watch out for the monsters."
         time.sleep(2)
      else:
         print "Let's hop right in then!"
      AreaNO = 3

   if (AreaNO == 0):
      if (PlayerHealth > MaxPlayerHealth):
         PlayerHealth = MaxPlayerHealth
      #Area number 0 engages a battle
      TempPlayerAttk = (PlayerLevel * random.randrange(1,6) + PlayerDamageBoost + PlayerAttk)
      #print 'Your attack is', PlayerLevel
      AttackPos = (MonsterNO * 4 + 1)
      if (EnemyTempHealth == -666):
         if (PlayerLevel >= 5):
            #Enemy attack scaling
            EnemyAttackToCalc = EnemyData[AttackPos]
            EnemyAttackToCalc = int(EnemyAttackToCalc)
            TempMonsterAttk = EnemyAttackToCalc + PlayerLevel
            #Enemy defense scaling
            DefensePos = (MonsterNO * 4 + 2)
            EnemyDefenseToCalc = EnemyData[DefensePos]
            EnemyDefenseToCalc = int(EnemyDefenseToCalc)
            TempMonsterDef = EnemyDefenseToCalc + PlayerLevel - 3
            EnemyHealthToCalc = EnemyData[MonsterNO * 4 + 3]
            EnemyTempHealth = EnemyHealthToCalc + PlayerLevel - 2
            EnemyHealthToCalc = int(EnemyHealthToCalc)
            TempMaxHealth = EnemyTempHealth
         else:
            TempMonsterAttk = EnemyData[MonsterNO * 4 + 1]
            EnemyTempHealth = EnemyData[MonsterNO * 4 + 3]
            DefensePos = (MonsterNO * 4 + 2)
            TempMonsterDef = EnemyData[DefensePos]
            TempMaxHealth = EnemyData[MonsterNO * 4 + 3]
         BattleTurns = 0
         InvCounter = 0
         DontAttack = False
      elif (EnemyTempHealth <= 0):
         print
         time.sleep(0.3)
         print EnemyData[MonsterNO * 4], 'was defeated!'
         EXPGot = BattleTurns + random.randrange(1,70)
         PlayerEXP = PlayerEXP + EXPGot
         time.sleep(0.3)
         print 'Got', EXPGot, 'experience points!'
         if (PlayerEXP < PlayerEXPMax):
             print PlayerEXP, 'out of', PlayerEXPMax, 'for the next level'
         if (PlayerEXP >= PlayerEXPMax):
            PlayerLevel = PlayerLevel + 1
            PlayerAttk = PlayerAttk + 1
            PlayerDef = PlayerDef + 1
            MaxPlayerHealth = MaxPlayerHealth + 4
            PlayerHealth = MaxPlayerHealth
            time.sleep(0.2)
            print "You just leveled up!"
            time.sleep(0.3)
            print "You are now level", PlayerLevel
            PlayerEXP = PlayerEXP - PlayerEXPMax
            PlayerEXPMax = PlayerEXPMax + 20
         ItemGet = random.randrange(0, (len(InventoryName) + 1))
         if (ItemGet != 0):
             print
             time.sleep(0.3)
             print "You also got a", InventoryName[ItemGet - 1]
             PlayerInventory.append(ItemGet - 1)
             time.sleep(0.3)
             print
             print 'You took the', InventoryName[ItemGet - 1]
             time.sleep(0.3)
         else:
             print
             time.sleep(0.3)
             print "You got nothing..."
         AreaNO = LastArea
         SectionType = 0
         EnemyTempHealth = -666
         DontAttack = False
      elif (PlayerHealth <= 0):
         print
         time.sleep(0.3)
         print "You have been defeated!"
         time.sleep(0.3)
         AreaNO = 4
      else:
         print EnemyData[MonsterNO * 4], 'wants to battle!'
         print 'Its health is', EnemyTempHealth, 'out of', TempMaxHealth
         time.sleep(0.2)
         print 'Its attack is', TempMonsterAttk
         time.sleep(0.2)
         print 'Its defense is', TempMonsterDef
         time.sleep(0.2)
         print 'Your health is', PlayerHealth, 'out of', MaxPlayerHealth
         time.sleep(0.2)
#Remove this print command when done testing
         #print EnemyData
#Remove this break command when done testing
         print
         InvCounter = 0
         print 'What will you do?'
         print 'A(Attack)'
         print 'I(Inventory)'
         print 'F(Flee)'
         Action = raw_input('> ')
         Action = Action.lower()
         print
         BattleTurns = BattleTurns + 1
         #Player Attacking
         if (Action == 'a'):
            print 'You attack with your', PlayerWeapon
            time.sleep(0.5)
            DontAttack = False
            AttackGiven = ((TempPlayerAttk * random.randrange(1,3) - TempMonsterDef))
            if (AttackGiven <= 0):
                AttackGiven = 0
                print
                print "Not even a scratch..."
                print
            EnemyTempHealth = EnemyTempHealth - AttackGiven
            RandomPhrase = random.randrange(0,len(AttackPrints))
            print AttackPrints[RandomPhrase]
            time.sleep(0.3)
            print 'You did', AttackGiven, 'damage!'
            print
         #Item System
         elif (Action == 'i'):
            print
            print 'You have', len(PlayerInventory), 'items.'
            for item in PlayerInventory:
               print
               InvCounter = InvCounter + 1
               print '(' +str(item) + ')', InventoryName[item]
            print
            print 'Which item would you like to use? (Type item number or BACK)'
            UseItemNO = raw_input('> ')
            if (UseItemNO == 'BACK') or (UseItemNO == 'back'):
                ItemCount = 0
                DontAttack = True
            elif (UseItem != 'BACK') and (UseItem != 'back'):
               try:
                  UseItemNO = int(UseItemNO)
               except:
                   print "That wasn't an item number."
                   continue
               ItemCount = 0
               UseItemNO = UseItemNO
               for item in PlayerInventory:
                  if (item == (UseItemNO)):
                     ItemCount = ItemCount + 1
            if (ItemCount >= 1):
                UseItem(UseItemNO)
                DontAttack = False
            else:
                ItemCount = 0
                DontAttack = True
            InvCounter = 0
         #Fleeing from battle
         else:
            Chance = random.randrange(0,101)
            if (Chance >= 20):
                            EnemyTempHealth = -666
                            time.sleep(0.5)
                            print "You've succesfully fled from the battle."
                            AreaNO = LastArea
                            SectionType = 0
                            DontAttack = True
            else:
                            time.sleep(0.5)
                            print "Couldn't flee!"
                            DontAttack = False
         #Enemy Attacks
         if (EnemyTempHealth > 0) and (DontAttack != True):
            print
            print EnemyData[MonsterNO * 4], 'attacks!'
            RandomPhrase = random.randrange(0,len(AttackPrints))
            time.sleep(0.5)
            print AttackPrints[RandomPhrase]
            AttackTaken = (TempMonsterAttk * random.randrange(1,3) - PlayerDef)
            if (AttackTaken <= 0):
                print
                print "Not even a scratch..."
                print
                AttackTaken = 0
            PlayerHealth = PlayerHealth - AttackTaken
            time.sleep(0.3)
            print 'You took', AttackTaken, 'damage!'
            print
            if (Poisoned == True):
               PlayerHealth = PlayerHealth - 5
               time.sleep(0.2)
               print "You took 5 damage from the poison"

   if (AreaNO == 3):
      if (Steps >= StepsToGo):
          print
          print "You see the light at the end of the cave. You've made it out alive."
          GameStarted = False
          AreaNO = 4
      if (Steps == 0) and (GameStarted == True):
         SectionType = 0
         print
         print "There's a", InventoryName[0], 'in front of you.'
         print 'You took the', InventoryName[0]
      elif (Steps > 0) and (SectionType == 0) and (GameStarted == True):
         print
         print "There doesn't seem to be any other monsters around... for now."
      elif (Steps > 0) and (SectionType == 1):
         print
         print "There's something in the shadows..."
         MonsterNO = random.randrange(1, (len(EnemyData) / 4))
         LastArea = 3
         #Insert other battle data
         AreaNO = 0
      elif (SectionType == 2) and (GameStarted == True):
         print
         print "There's a treasure chest!"
         ChestType = random.randrange(0,3)
         if ChestType == 0:
                         print "It's empty..."
         elif ChestType == 1:
                         ChestItem = random.randrange(0,len(InventoryName))
                         print 'It had a', InventoryName[ChestItem]
                         print 'Will you take the', str(InventoryName[ChestItem]) + '?'
                         TakeItem = raw_input("(Y/N)> ")
                         TakeItem = TakeItem.lower()
                         if (TakeItem == 'y'):
                                         PlayerInventory.append(ChestItem)
                                         print 'You took the', InventoryName[ChestItem]
         else:
                         print "You found a weapon!"
                         WeaponRNG = random.randrange(0,len(WeaponName))
                         print "You found a", WeaponName[WeaponRNG] + '!'
                         print 'It adds', WeaponStats[WeaponRNG], 'extra attack points.'
                         print 'Your', PlayerWeapon + ' ', 'adds ', PlayerDamageBoost, 'attack points.'
                         print 'Will you take the', WeaponName[WeaponRNG] + '?'
                         TakeWeapon = raw_input("(Y/N)> ")
                         TakeWeapon = TakeWeapon.lower()
                         if (TakeWeapon == 'y'):
                             PlayerDamageBoost = WeaponStats[WeaponRNG]
                             PlayerWeapon = WeaponName[WeaponRNG]
                             print "You took the", WeaponName[WeaponRNG] + '!'
      print
      if (SectionType != 1) and (GameStarted == True):
                      print "What will you do?"
                      print "A(Advance Forward)"
                      print "I(Inventory)"
                      print "S(Stats)"
                      print "Q(Quit)"
                      Advance = raw_input("> ")
                      Advance = Advance.lower()
      if (Advance == 'a') and (GameStarted == True):
         Steps = Steps + 1
         SectionType = random.randrange(0,3)
         print
         print 'You advance further into the cave...'
         print
         time.sleep(0.3)
         if (Poisoned == True) and (GameStarted == True):
            PlayerHealth = PlayerHealth - 5
            print
            print "You took 5 damage from poison"
            time.sleep(0.2)
            print
         if (PlayerHealth <= 0):
            AreaNO = 4
      elif (Advance == 'q'):
                      SectionType = 0
                      AreaNO = 4
      elif (Advance == 'i'):
                      SectionType = 0
                      InvCounter = 0
                      #print PlayerInventory
                      print
                      print 'You have', len(PlayerInventory), 'items.'
                      for item in PlayerInventory:
                          print
                          InvCounter = InvCounter + 1
                          print '(' +str(item) + ')', InventoryName[item]
                      print
                      print 'Which item would you like to use? (Type item number or BACK)'
                      UseItemNO = raw_input('> ')
                      if (UseItemNO == 'BACK') or (UseItemNO == 'back'):
                          ItemCount = 0
                      elif (UseItem != 'BACK') and (UseItem != 'back'):
                          try:
                              UseItemNO = int(UseItemNO)
                          except:
                              print "That wasn't an item number."
                              continue
                          ItemCount = 0
                          UseItemNO = UseItemNO
                          for item in PlayerInventory:
                              if (item == (UseItemNO)):
                                  ItemCount = ItemCount + 1
                      if (ItemCount >= 1):
                          UseItem(UseItemNO)
                          DontAttack = False
                      SectionType = 0
      elif (Advance == 's'):
          print
          SectionType = 0
          print "PLAYER STATS"
          print str(PlayerHealth) + '/' + str(MaxPlayerHealth), "HP"
          print 'Level', PlayerLevel
          print str(PlayerEXP) + '/' + str(PlayerEXPMax), 'to next level'
          print 'Attack is', PlayerAttk
          print 'Defense is', PlayerDef
          print 'Current weapon:', PlayerWeapon
          print 'Current weapon attack boost:', PlayerDamageBoost
          print 'Steps Walked:', Steps
          print "Poisoned:", Poisoned
          
      else:
                      SectionType = 0
   if (AreaNO == 4):
      PlayerEXPMax = 100
      Poisoned = False
      GameStarted = False
      EnemyTempHealth = -666
      PlayerWeapon = 'dagger'
      AreaNO = 1
      PlayerLevel = 0
      PlayerInventory = [0]
      PlayerEXP = 0
      Steps = 0
      StepsToGo = 0
      Sections = 0
      PlayerDamageBoost = 4
      PlayerAttk = 2
      PlayerDef = 0
      RandomGameOver = random.randrange(0,3)
      if (PlayerHealth > 0):
          RandomGameOver = 0
      if (RandomGameOver == 0):
          print "GAME OVER!"
      elif (RandomGameOver == 1):
          print "YOU GOT REKT SON"
      else:
          print "WOW. THAT WAS ROUGH."
      #print "GAME OVER!"
      time.sleep(1)
      print "Try again?"
      Continue = raw_input('(Y/N)> ')
      if (Continue != 'Y') and (Continue != 'y'):
         break
      else:
         GameStarted = False
