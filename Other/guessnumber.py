import os
import random
import time
os.system('cls' if os.name=='nt' else 'clear')

print("welcome to my game")
print("this game is \"Number Guessing in range 1-100\"  is this fun? yes or no")
ans = str(input('are you realdy: '))

if ans == "yes":
    start_time =int( time.time() )
    print("now you can think in your brain a number andd tell for me")
    x = int(input("your number is :"))
    list1 = [25,50,75,100]
    ys = (random.choice(list1)) #yoursorce
    cpnb = random.randint(1,100) #computer'number
    cp = abs(50-cpnb)
    if x == cpnb:
        print(f'congratulation! You won with yoursore : {ys}')
    else:
        print('incorrect')
        print('now i can improve for you a hint')
        print(f'i have \"cp\" = {cp} is a abs of your number with one of the number 1,50,100')
        ys = 100 - 10
        x = int(input("your new number :"))

        if x == cpnb:
            print(f'congratulation! You won with yoursore : {ys}')
        else:
            print("incorrect")
            print("you can try again")
            ys -= 20
            x = int(input('you guess new number is : '))

            if x == cpnb:
                print("hazzz,finally, yow win")

            elif x > 50:
                print("i have a final hint for you")
                print("this is  a number less than 50")
                x = int(input('you guess new number is : '))

                if x == cpnb:
                    print("hazzz,finally, yow win")
                else:
                    print("language: Vietnamese")
                    print("thoi nghi moe game di , khong tien")
                    print(f'my number is {cpnb}')
                    ys -= 30
                    print(f'this is your score : {ys} ')
                    
            elif x < 50:
                print("i have a final hint for you")
                print("this is  a number great than 50")
                x = int(input('Your new number part 3 :'))

                if x == cpnb:
                    print("hazzz,finally, yow win")

                else:
                    print("language: Vietnamese")
                    print("thoi nghi moe game di , khong tien")
                    print(f'my number is {cpnb}')
                    ys -= 30
                    print(f'this is your score : {ys} ')

    end_time =int( time.time())
    yt = end_time - start_time #time
    print("your time in game is : {}".format(yt) +" sec")                
else:
    print("oh i am sorry.See you tommorrow")
