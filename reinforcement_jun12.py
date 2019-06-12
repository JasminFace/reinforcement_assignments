import requests


# PART 1

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
owr = ottawa_wards_response.json()

owr.keys()                                                              
# dict_keys(['meta', 'objects'])

objects = owr['objects']                                                
objects.__class__
# list

for ward in objects:
    print(ward['name'])

# Barrhaven
# West Carleton-March
# Somerset
# Rideau-Goulbourn
# Cumberland
# Orléans
# Innes
# Rideau-Rockcliffe
# Rideau-Vanier
# Stittsville
# Alta Vista
# Gloucester-Southgate
# Kitchissippi
# Capital
# River
# Knoxdale-Merivale
# Kanata North
# Gloucester-South Nepean
# College
# Beacon Hill-Cyrville




# PART 2

reps = requests.get('https://represent.opennorth.ca/representatives/')
r = reps.json()                                                        

r.keys()                                                               
# dict_keys(['meta', 'objects'])

objects = r['objects']                                                 

objects.__class__                                                      
# list

for c in objects:
    print(c['name']) 
                                                                       
# Peter Stroud
# Bridget Doherty
# Jim Neill
# Simon Chapelle
# Wayne Hill
# Jeffrey Coffman
# Gary Oosterhof
# Rob Hutchison
# Jeff McLaren
# Robert Kiley
# Ryan Boehme
# Mary Rita Holland
# Bryan Paterson
# Lisa Osanic
# Mark Campbell
# Belinda Crowson
# Rob Miyashiro
# Blaine Hyggen
# Chris Spearman
# Joe Mauro