import pygame
from game import Game
# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1024, 720))
pygame.display.set_caption("My GTA-style Game")

# Set up the game clock
clock = pygame.time.Clock()
game = Game()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Check if the player is colliding with any cars
                for car in game.vehicles:
                    if game.player.rect.colliderect(car.rect):
                        # The player is colliding with a car, so interact with it
                        game.player.interact_with_car(car)
    # Update game state
    game.update()

    # Render the game
    game.render(screen)  # Render the player

    pygame.display.flip()  # Update the display

    # Limit the frame rate
    clock.tick(60)

# Clean up before exiting
pygame.quit()
