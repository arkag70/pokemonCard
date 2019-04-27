import pandas as pd

def randomizeCards():
    df = pd.read_csv('data.csv')
    df = df.head(150)
    n = int(input('How many cards to play with: '))
    #df_elements = df.sample(n=7)
    p1_df = df.sample(n=n)
    p2_df = df.sample(n=n)

    d1 = {}
    d2 = {}
    name = []
    type1 = []
    type2 = []
    hp = []
    attack = []
    defense = []
    sp_attack = []
    sp_defense = []
    speed = []

    for i in range(n):
        name.append(p1_df.iloc[i]['Name'])
        type1.append(p1_df.iloc[i]['Type 1'])
        type2.append(p1_df.iloc[i]['Type 2'])
        hp.append(p1_df.iloc[i]['HP'])
        attack.append(p1_df.iloc[i]['Attack'])
        defense.append(p1_df.iloc[i]['Defense'])
        sp_attack.append(p1_df.iloc[i]['Sp. Atk'])
        sp_defense.append(p1_df.iloc[i]['Sp. Def'])
        speed.append(p1_df.iloc[i]['Speed'])
    d1['name'] = name
    d1['type1'] = type1
    d1['type2'] = type2
    d1['hp'] = hp
    d1['attack'] = attack
    d1['defense'] = defense
    d1['sp_attack'] = sp_attack
    d1['sp_defense'] = sp_defense
    d1['speed'] = speed

    name = []
    type1 = []
    type2 = []
    hp = []
    attack = []
    defence = []
    sp_attack = []
    sp_defense = []
    speed = []

    for i in range(n):
        name.append(p2_df.iloc[i]['Name'])
        type1.append(p2_df.iloc[i]['Type 1'])
        type2.append(p2_df.iloc[i]['Type 2'])
        hp.append(p2_df.iloc[i]['HP'])
        attack.append(p2_df.iloc[i]['Attack'])
        defense.append(p2_df.iloc[i]['Defense'])
        sp_attack.append(p2_df.iloc[i]['Sp. Atk'])
        sp_defense.append(p2_df.iloc[i]['Sp. Def'])
        speed.append(p2_df.iloc[i]['Speed'])
    d2['name'] = name
    d2['type1'] = type1
    d2['type2'] = type2
    d2['hp'] = hp
    d2['attack'] = attack
    d2['defense'] = defense
    d2['sp_attack'] = sp_attack
    d2['sp_defense'] = sp_defense
    d2['speed'] = speed
    return d1,d2
