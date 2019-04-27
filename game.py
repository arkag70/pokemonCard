from os import system

move = ['name','type1','type2','hp','attack','defense','sp_attack','sp_defense','speed']

def disp(d,n):
    print(f"Pokemon    : {d['name'][n]}")
    print(f"1)Type 1     : {d['type1'][n]}")
    print(f"2)Type 2     : {d['type2'][n]}")
    print(f"3)HP         : {d['hp'][n]}")
    print(f"4)Attack     : {d['attack'][n]}")
    print(f"5)Defense    : {d['defense'][n]}")
    print(f"6)Sp. Attack : {d['sp_attack'][n]}")
    print(f"7)Sp. Defense: {d['sp_defense'][n]}")
    print(f"8)Speed      : {d['speed'][n]}")



def game(p1,p2,d1,d2):
    rounds = 0
    exit_now = 0
    challenger = p1
    rival = p2
    c_set = d1
    r_set = d2
    while exit_now == 0:
        system('cls')
        print(f"Round {rounds+1}")
        while True:
            print(f"Challenger {challenger}'s card")
            disp(c_set,rounds)
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
            disp(r_set,rounds)
            print(f"\n{c_set['name'][rounds]}'s {inp}: {c_set[inp][rounds]} vs {r_set['name'][rounds]}'s {inp}: {r_set[inp][rounds]}")

            if(c_set[inp][rounds] > r_set[inp][rounds]):
                print(f"\n{challenger}'s {c_set['name'][rounds]} wins round!!")


            elif(c_set[inp][rounds] < r_set[inp][rounds]):
                print(f"\n{rival}'s {r_set['name'][rounds]} wins round!!")

                temp = challenger
                challenger = rival
                rival = temp

                temp = c_set
                c_set = r_set
                r_set = temp

            else:
                print("\nIt's a tie")

                temp = challenger
                challenger = rival
                rival = temp

                temp = c_set
                c_set = r_set
                r_set = temp

            input('\nHit Enter to continue!')
            rounds += 1
