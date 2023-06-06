import pygame
import CellFunctions

# Initialize the preset dictionaries first
def main():
    pantry = {}
    cells = {}

    starting_food = 40
    starting_cells = 5

    for f in range(starting_food):
        food = CellFunctions.Food.feed_random()
        pantry[food.food_id] = food

    for c in range(starting_cells):
        cell = CellFunctions.Cell.cell_random()
        cells[cell.cell_id] = cell

    # Set up the render environment
    pygame.init()

    width = 800
    height = 600

    # Create a Pygame window as the simulation environment
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Cell simulation")
    # Other functions for simulation setup and visualization

    running = True

    # Create an instance of the Player class
    player = CellFunctions.Player(400, 300, 10, 100, 0.5)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        
        if player == False:
            print("Cell has been consumed")
            restart = input("Restart? (Y/N)")
            if restart == "Y":
                pantry = {}
                cells = {}
                player = CellFunctions.Player(400, 300, 10, 100, 0.5)
            else:
                running = False
        
        keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
        if keys[pygame.K_LEFT]:    # Check if the left arrow key is pressed
            player.px -= abs(player.movement)

        if keys[pygame.K_RIGHT]:
            player.px += abs(player.movement)

        if keys[pygame.K_DOWN]:
            player.py -= abs(player.movement)

        if keys[pygame.K_UP]:
            player.py += abs(player.movement)
        
        if keys[pygame.K_SPACE]: 
            player.ability()  # Replace "perform_action()" with the actual action you want to perform (TBC)
        
        # CellFunctions.update_state()  # Update the positions of other competitor cells

        pygame.draw.circle(screen, (255, 0, 0), (player.px, player.py), player.size)
        # Drawing and updating the game state for each item
        CellFunctions.update_state(cells, pantry)

        for food in pantry.values():
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((food.px, food.py), (2, 2)))  # Replace with the appropriate code to draw rectangles
        
        for cell in cells.values():
            pygame.draw.circle(screen, (0, 0, 255), (cell.px, cell.py), abs(cell.size))  # Replace with the appropriate code to draw circles
        
        pygame.display.flip()

    # Game cleanup and exit
    pygame.quit()

if __name__ == "__main__":
    main()




