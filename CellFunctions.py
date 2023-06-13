import random

# class Player:
#     def __init__(self, px, py, size, energy, movement)
class Player:
    def __init__(self, px, py, size, energy, movement):
        self.px = px
        self.py = py
        self.size = size
        self.energy = energy
        self.movement = movement 

class Cell:
    next_id = 0 
    def __init__(self, px, py, size, energy, movement):
        self.px = px
        self.py = py
        self.size = size
        self.energy = energy
        self.movement = movement
        self.cell_id = Cell.next_id
        Cell.next_id += 1

# @classmethod decorator is used to define a class method that operates on the class 
# itself rather than an instance. It allows you to perform class-level operations and 
# provides a convenient way to create new instances with random attribute values 

    @classmethod
    def cell_random(cls): #cls is just short for class
        px = random.randint(1,800)
        py = random.randint(1,600)
        size = random.randint(1, 5)
        energy = random.randint(20, 40)
        movement = random.uniform(0.2, 0.45)

        return cls(px, py, size, energy, movement)
    
    @classmethod
    def cell_new(cls, px, py, size, energy, movement):
        return cls(px, py, size, energy, movement)

# Once a cell reaches a certain size and has enough energy, it will cleave into two new cells, and the previous will be deleted   
    def cell_growth(self):
        if abs(self.energy) >= 100:
            self.size += 1
            self.energy = 0
  
    def cell_genesis(self): # currently bugged to not delete maxxed cells
        if self.size > 10 and self.energy > 100:
            self.cell_new((self.px + 2), (self.py + 2), 1, 0, 3)
            self.cell_new((self.px - 2), (self.py - 2), 1, 0, 3)       

    # Update the position of each cell for the current iteration of the loop
    def cell_movement(self):
        dx = random.uniform(-abs(self.movement), abs(self.movement))  # Random movement in the x-axis direction (-1, 0, or 1)
        dy = random.uniform(-abs(self.movement), abs(self.movement))  # Random movement in the y-axis direction (-1, 0, or 1)
        self.px += dx
        self.py += dy
        # Update the cell's position based on the random movement

    # If a cell is too close, one consumes the other based on which is larger
    


class Food:
    next_id = 0
    def __init__(self, px, py, size, energy):
        self.px = px
        self.py = py
        self.size = size
        self.energy = energy
        self.food_id = Food.next_id
        Food.next_id += 1

    @classmethod
    def feed_random(cls): #cls is just short for class
        px = random.randint(1,800) 
        py = random.randint(1,600)
        size = random.randint(1, 3)
        energy = random.randint(10, 50)
        # if energy <= 10:
        #     colour = "green"
        # elif 10 < energy <= 30:
        #     colour = "orange"
        # elif 30 < energy <= 40:
        #     colour = "red"
        # else:
        #     colour = "blue"

        return cls(px, py, size, energy)

def collision(cells, player, pantry):
    foodbin = []
    cellbin = []
    for C1 in cells.values():
        for C2 in range(C1.cell_id + 1, len(cells)):
            if (abs(C1.px - cells[C2].px) <= C1.size + cells[C2].size) or (abs(C1.py - cells[C2].py) <= C1.size + cells[C2].size):
                if C1.size > cells[C2].size:
                    C1.size += cells[C2].size
                    C1.energy += cells[C2].energy
                    cellbin.append[C2.cell_id]
                elif C1.size == cells[C2].size:
                    break
                else:
                    cells[C2].size += C1.size
                    cells[C2].energy += C1.energy
                    cellbin.append[C1.cell_id]
                    break

    # Cell/Player collision
    for C1 in cells.values():
        if (abs(C1.px - player.px) < C1.size + player.size) or (abs(C1.py - player.py) < C1.size + player.size):
            if C1.size > player.size:
                print("Player consumed by a larger cell. Game over!")
                event.type == pygame.QUIT
            elif C1.size == player.size:
                break
            else:
                player.size += C1.size
                player.energy += C1.energy
                cellbin.append[C1.cell_id]
                break

    # Cell/Food collision
    for C1 in cells.values():
        for f in pantry.values():
            if C1.px == f.px and C1.py == f.py:
                C1.size += 1
                foodbin.append[f]
                break

    # Player/Food collision
    for f in pantry.values():
        if abs(player.px - f.px) <= player.size: 
                player.size += 1
                foodbin.append[f]
    
    return foodbin, cellbin

def update_state(cells:dict) -> None:
    for cell in cells.values():
        cell.cell_growth()
        cell.cell_movement()
        cell.cell_genesis()

def setup_game(starting_food, starting_cells) -> dict: 
    pantry = {}
    cells = {}

    for food in range(starting_food):
        food = Food.feed_random()
        pantry[food.food_id] = food

    for cell in range(starting_cells):
        cell = Cell.cell_random()
        cells[cell.cell_id] = cell

    player = Player(400, 300, 10, 100, 0.5)

    return pantry, cells, player

    # Cell.cell_collision(cells)
    # Food.feed_collision(cells, pantry)
    # food = Food.feed_random()
    # pantry[food.food_id] = food

