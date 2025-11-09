# -*- coding: utf-8 -*-
import random 
new_dic = {}

for lon in range(1,6):
    new_dic[lon] = random.randint(0, 20)
    print(f"Quiz {lon:>2}:  {new_dic[lon]:0>2}")
    
