import random

'''
1 for snake
-1 for water
0 for gun

'''
try:
  computer  = random.choice([-1,0,1]);

  youstr = input("Enter your choice: ");
  you_Dict = { "s":1,"w":-1,"g":0}

  you = you_Dict[youstr];

  REVERSE_Dict = { 1:"s",-1:"w",0:"g"}
  print(f"you choose {REVERSE_Dict[you]}\ncomputer choose {REVERSE_Dict[computer]}")
  if(computer==you):
    print("GAME DRAW !!!");
  else:
       if(computer==1 and you==0):  
        print("YOU WIN !!!");

       elif(computer==1 and you==-1): 
        print("YOU LOSE !!!");

       elif(computer==-1 and you==0): 
        print("YOU WIN !!!");

       elif(computer==-1 and you==1): 
        print("YOU WIN !!!");

       elif(computer==0 and you==1): 
        print("YOU LOSE !!!");

       elif(computer==0 and you==-1): 
        print("YOU LOSE !!!");

       else:
        print("SOMETHING GONE WRONG !!!")
        
except Exception as e:
  print("Enter a correct string word from (s,w,g)");