import random
import time

"""
Note:
THIS IS NOT ACCURATE AND SHOULD NOT
BE TAKEN SERIOUSLY

I also know that this is terrible code
but I made this just to see if it was
possible to make something like this.
"""

population = 2
gen = 1
max_children = 1
min_children = 0

epidemic_chance = 10 # Extremely harsh conditions
chance_of_disaster = 2000

print("Starting simulation..")
time.sleep(2)
print("---------------------")

print("2 people: Generation 0")
time.sleep(1)
while True:
  for i in range(population):
    children = random.randint(min_children, max_children)
    
    population += children
    
  is_epidemic = random.randint(0, epidemic_chance)
  disaster = random.randint(0, chance_of_disaster)
  
  if disaster == round(chance_of_disaster/2):
    print(f"oh no meteor strike1!!1!1!!!")
    break
  
  if is_epidemic == round(epidemic_chance/2):
    print("(Epidemic)")
    deaths = random.randint(1, population)
    
    deaths = population / deaths
    population = round(deaths)
    
  if population == 0:
    print("(Civilization died)")
    break
  elif population == 1:
    print("(Civilization died)")
    break
  print(f"{population} people: Generation {gen}")
  gen += 1
  
  if population > 2000000:
    print(f"Civilization has become advanced with 2M+ people: Generation {gen-1}")
    break
  
  time.sleep(0.8)