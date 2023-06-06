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

# Redundant
    # def handle_input(self):
    #     keys = pygame.key.get_pressed() 

    #     if keys[pygame.K_LEFT]:
    #         self.px -= self.movement
    #     if keys[pygame.K_RIGHT]:
    #         self.px += self.movement
    #     if keys[pygame.K_UP]:
    #         self.py -= self.movement
    #     if keys[pygame.K_DOWN]:
    #         self.py += self.movement

class Cell: 
    def __init__(self, px, py, size, energy, movement):
        self.px = px
        self.py = py
        self.size = size
        self.energy = energy
        self.movement = movement
        self.cell_id = 0

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
    def cell_collision(self, cells, player):
        for i in range(len(cells)):
            for j in range([i] + 1, len(cells)):
                if abs(cells.position[i] - cells.position[j]) <= abs(cells.size[i]) or abs(cells.size[j]): 
                    if abs(cells.size[i]) > abs(cells.size[j]):
                        cells.size[i] += abs(cells.size[j])
                        cells.energy[i] += abs(cells.energy[j])
                        del cells[j]             
                    else:
                        cells.size[j] += abs(cells.size[i])
                        cells.energy[j] += abs(cells.energy[i])
                        del cells[i]
                    
            if abs(cells.position[i] - player.position) < abs(cells[i].size) or abs(player.size):
                if abs(cells.size[i] > player.size):
                    print("Player consumed by a larger cell. Game over!")
                    # create a failstate
                else:
                    player.size += abs(cells.size[i])
                    player.energy += abs(cells.energy[i])
                    del cells[i]

                    break                   

class Food:
    def __init__(self, px, py, size, energy, colour):
        self.px = px
        self.py = py
        self.size = size
        self.energy = energy
        self.colour = colour
        self.food_id = 0

    @classmethod
    def feed_random(cls): #cls is just short for class
        px = random.randint(1,800) 
        py = random.randint(1,600)
        size = random.randint(1, 3)
        energy = random.randint(10, 50)
        if energy <= 10:
            colour = "green"


            
        elif 10 < energy <= 30:
            colour = "orange"
        elif 30 < energy <= 40:
            colour = "red"
        else:
            colour = "blue"

        return cls(px, py, size, energy, colour)
    
    def feed_collision(cells, pantry):
            for cell in cells:
                for food in pantry:
                    if cells[cell].position == pantry[food].position:
                        cell.size += 1
                        del pantry[food]

def update_state(cells:dict, pantry:dict) -> None:
    for cell in cells.values():
        cell.cell_growth()
        cell.cell_movement()
        cell.cell_genesis()

    # Cell.cell_collision(cells)
    # Food.feed_collision(cells, pantry)
    # food = Food.feed_random()
    # pantry[food.food_id] = food

