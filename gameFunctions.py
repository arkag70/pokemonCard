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

def win(a,b,w):
    if w == 0:
        a0 = a[0:1]
        b0 = b[0:1]
        return (a[1:]+a0+b0),b[1:]
    elif w == 1:
        a0 = a[0:1]
        b0 = b[0:1]
        return a[1:],(b[1:]+b0+a0)
    else:
        a0 = a[0:1]
        b0 = b[0:1]
        return (a[1:]+a0),(b[1:]+b0)

def rotate(set1,set2,w):
    set1['name'], set2['name'] = win(set1['name'],set2['name'],w)
    set1['type1'], set2['type1'] = win(set1['type1'],set2['type1'],w)
    set1['type2'], set2['type2'] = win(set1['type2'],set2['type2'],w)
    set1['hp'], set2['hp'] = win(set1['hp'],set2['hp'],w)
    set1['attack'], set2['attack'] = win(set1['attack'],set2['attack'],w)
    set1['defense'], set2['defense'] = win(set1['defense'],set2['defense'],w)
    set1['sp_attack'], set2['sp_attack'] = win(set1['sp_attack'],set2['sp_attack'],w)
    set1['sp_defense'], set2['sp_defense'] = win(set1['sp_defense'],set2['sp_defense'],w)
    set1['speed'], set2['speed'] = win(set1['speed'],set2['speed'],w)

    return set1,set2
