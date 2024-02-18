

## Arrays of Records


from dataclasses import dataclass
@dataclass
class Avenger:
    name: str = ""
    alias: str = ""
    human: bool = True
    strength: int = 0
    age: int = 0
def createStructure():
    avengersAssemble = [
        Avenger("Tony Stark", "Iron Man", True, 100, 48),
        Avenger("Steve Rogers", "Captain America", True, 90, 105),
        Avenger("Bruce Banner", "The Hulk", True, 95, 54),
        Avenger("Thor Odinson", "God of Thunder", False, 98, 1500),
        Avenger("Natasha Romanoff", "Black Widow", True, 85, 32),
        Avenger("Clint Barton", "Hawkeye", True, 80, 47),
        Avenger("Nick Fury", "Director Fury", True, 70, 80)
    ]
    return avengersAssemble
# Avengers data
avengersAssemble = createStructure()




# Find the oldest Avenger
max_strength = avengersAssemble[0].strength # Assume the first Avenger has the maximum age
max_strength_position = 0  # Position of the Avenger with the maximum age
for i in range(1, len(avengersAssemble)):
    if avengersAssemble[i].strength > max_strength:
        max_strength = avengersAssemble[i].strength
        max_strength_position = i
# Display the details of the oldest Avenger

max_strength = 0 
for i in range(1, len(avengersAssemble)):
    if avengersAssemble[i].strength > avengersAssemble[max_strength].strength:
        max_strength = i


# Display the details of the oldest Avenger
print(avengersAssemble[max_strength].name,
      avengersAssemble[max_strength].alias,
      avengersAssemble[max_strength].strength,)

avengersAssemble = createStructure()



