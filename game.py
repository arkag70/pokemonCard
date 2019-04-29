from os import system
from gameFunctions import *

def game(p1,p2,d1,d2):
    rounds = 0
    exit_now = 0
    challenger = p1
    rival = p2
    c_set = d1
    r_set = d2

    while exit_now == 0:
        system('cls')
        if (len(r_set['name']) != 0) and (len(c_set['name']) !=0):
            print(f"Round {rounds+1}")
            #print(d1['name'])
            #print(d2['name'])

            while True:

                print(f"Challenger {challenger}'s card")
                disp(c_set,0)
                inp = input(f"\n{challenger} choose a Stat to fight \npress q to quit\n")
                if(inp.lower() == 'q'):
                    exit_now = 1
                    break
                elif inp in '12345678':
                    inp = move[int(inp)]
                    break
                else:
                    clear_output()
            if exit_now == 0:
                print(f"Rival {rival}'s card")
                disp(r_set,0)
                print(f"\n{c_set['name'][0]}'s {inp}: {c_set[inp][0]} vs {r_set['name'][0]}'s {inp}: {r_set[inp][0]}")

                if(c_set[inp][0] > r_set[inp][0]):
                    print(f"\n{challenger}'s {c_set['name'][0]} wins round!!")
                    c_set,r_set = rotate(c_set,r_set,0)


                elif(c_set[inp][0] < r_set[inp][0]):
                    print(f"\n{rival}'s {r_set['name'][0]} wins round!!")
                    c_set,r_set = rotate(c_set,r_set,1)
                    temp = challenger
                    challenger = rival
                    rival = temp

                    temp = c_set
                    c_set = r_set
                    r_set = temp

                else:
                    print("\nIt's a tie")
                    c_set,r_set = rotate(c_set,r_set,2)
                    temp = challenger
                    challenger = rival
                    rival = temp

                    temp = c_set
                    c_set = r_set
                    r_set = temp

                input('\nHit Enter to continue!')
                rounds += 1
        else:
            if len(r_set['name']) == 0:
                print(f"Challenger {challenger} wins the game!!")
            else:
                print(f"Rival {rival} wins the game!!")
            exit_now = 1
