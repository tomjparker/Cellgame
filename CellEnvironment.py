import pygame
import CellFunctions

def main():
    # Instance the variables
    starting_food = 40
    starting_cells = 5
    pantry, cells, player = CellFunctions.setup_game(starting_food, starting_cells)

    # Set up the render environment
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Cell simulation")
    # Other functions for simulation setup and visualization

    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Cell has been consumed")
                restart = input("Restart? (y/n)")
                if restart == "y" or "Y" or "Yes" or "yes":
                    pantry, cells, player = CellFunctions.setup_game(starting_food, starting_cells)
                    # put in delay logic for audio failure
                else:
                    running = False
        
        screen.fill((255, 255, 255))
        
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
        
        # Updating the game state for each item
        CellFunctions.update_state(cells)

        # Temporarily make a list of consumed cells or food
        
        CellFunctions.collision(cells, player, pantry)

        # Drawing each game element
        pygame.draw.circle(screen, (255, 0, 0), (player.px, player.py), player.size)
        for food in pantry.values():
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((food.px, food.py), (2, 2)))  # Replace with the appropriate code to draw rectangles
        
        for cell in cells.values():
            pygame.draw.circle(screen, (0, 0, 255), (cell.px, cell.py), abs(cell.size))  # Replace with the appropriate code to draw circles
        
        clock.tick(60)

        pygame.display.flip()

    # Game cleanup and exit
    pygame.quit()

# to prevent it running straight away
if __name__ == "__main__":
    main()




