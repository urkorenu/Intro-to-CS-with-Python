# turns dictionaries of people : countries > countries : people
d = {'Sagi' :['America', 'Swiss', 'Portugal', 'Thailand', 'Holand', 'Bulgaria'], 
     'Itay' :['Holand', 'America', 'China', 'Austria', 'Italy', 'Hong Kong', 'Turkey', 'Germany'], 
     'Ur'   :['Holand', 'India', 'Sri Lanka', 'Germany', 'Greece', 'Argentina'], 
     'Eyal' :['India', 'Austria', 'Holand', 'Thailand', 'Russia', 'Greece', 'Hong Kong', 'Romania'],
     'Keren':['Pruague', 'Greece', 'Scotland', 'Russia', 'Italy', 'Holand', 'Austria', 'Argentina', 'Mexico', 'Uruguay', 'Brazil', 'Colombia']
     }


new_d = {}

for name in d:
    for country in d[name]:
        if country not in new_d:
            new_d[country] = [name]
        else:
            new_d[country].append(name)
        
print(new_d)