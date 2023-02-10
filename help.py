#Stone Paper Scissors Game 
# 1. Stone 
# 2. Paper 
# 3. Scissors
# we  wil play this game 10 times in a row 
import random
print("------WELCOME TO THE GAME OF STONE PAPER SCISSORS------");
options = [1 , 2 , 3 ]  ;
i=1 ;
pscore=0 ;
cscore=0 ;
while( i<11):
    choice = random.choice(options) ;
    print("--ENTER YOUR CHOICE---");
    print("PRESS 1. FOR STONE ");
    print("PRESS 2. FOR PAPER ");
    print("PRESS 3. FOR SCISSORS ");
    playerinput=int(input("ENTER YOUR CHOICE  : ")) ; 
    print(playerinput,choice) ;
    if (playerinput == choice ) :
        print("--OOPS IT'S A TIE--");
        cscore=cscore+1 ;
        pscore=pscore+1;
        print(f"SCORE :  {pscore} - {cscore} ");
    else :
        if(playerinput == 2 and choice== 1):   #player: paper and CPU : stone 
            pscore=pscore+1;
            print("--YOU WIN--");

        elif playerinput == 1 and choice == 2:# player:stone and  CPU : paper
            print("--CPU WINS--") ;
            cscore=cscore+1 ;

        elif(playerinput == 1 and choice== 3):   #player: stone  and CPU : scissors 
            pscore=pscore+1;
            print("--YOU WIN--");

        elif (playerinput == 3 and choice == 1 ) :# player:scissors and  CPU : stone
            print("--CPU WINS--") ;
            cscore=cscore+1 ;
        
        elif(playerinput == 3 and choice== 2):   #player: scissors and CPU : paper 
            pscore=pscore+1;
            print("--YOU WIN--");

        elif (playerinput == 2 and choice == 3 ) : # player:paper and  CPU : scissors
            print("--CPU WINS--") ;
            cscore=cscore+1 ;

    print(f"SCORE :  {pscore} - {cscore} ");
    print(f"END OF TURN : {i} \n") ;
    i=i+1 ; 
print(f"FINAL SCORE : {pscore} - {cscore}");
print("-------END OF THE GAME-------");
