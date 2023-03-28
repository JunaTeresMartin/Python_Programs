logo1='''
  _   _ _       _                 _                           
 | | | (_) __ _| |__   ___ _ __  | |    _____      _____ _ __ 
 | |_| | |/ _` | '_ \ / _ \ '__| | |   / _ \ \ /\ / / _ \ '__|
 |  _  | | (_| | | | |  __/ |    | |__| (_) \ V  V /  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|    |_____\___/ \_/\_/ \___|_|   
          |___/                                               
'''
logo2='''
 _  _  ___ 
( \/ )/ __)
 \  / \__ \
  \/  (___/
'''


famous_people={
    "Rihanna":1,
    "Selena Gomez":2,
    "Justin Baebar":3,
    "Haley Baebar":4,
    "Messi":5,
    "Ronaldo":7,
    "Mohanlal":8,
    "Mammoootty":9,
    "Tom Criuse":10
}

import random
defenser=random.choice(list(famous_people.keys()))
user=random.choice(list(famous_people.keys()))
if defenser!=user:
    print(defenser)
    print(user)


