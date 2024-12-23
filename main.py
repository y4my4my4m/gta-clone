import pygame
from game import Game


# Initialize Pygame
pygame.init()

# Create a font object
font = pygame.font.Font(None, 20)

screen_width, screen_height = 1024, 720

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My GTA-style Game")

# Set up the game clock
clock = pygame.time.Clock()
game = Game(screen_width, screen_height)

debug = False
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                debug = not debug
            if event.key == pygame.K_SPACE:
                # Check if the player is colliding with any cars
                # for car in game.vehicles:
                #     if game.player.rect.colliderect(car.rect):
                #         # The player is colliding with a car, so interact with it
                #         game.player.interact_with_car(car)
                # Check if the player is colliding with any cars# In main.py, replace the car collision check with:
                for car in game.vehicles:
                    # Calculate screen-space positions for both player and car
                    player_screen_x = game.player.world_x - game.camera.x
                    player_screen_y = game.player.world_y - game.camera.y
                    car_screen_x = car.x - game.camera.x 
                    car_screen_y = car.y - game.camera.y
                    
                    # Create collision rectangles in screen space
                    player_rect = pygame.Rect(player_screen_x, player_screen_y, game.player.rect.width, game.player.rect.height)
                    car_rect = pygame.Rect(car_screen_x, car_screen_y, car.rect.width, car.rect.height)
                    
                    if player_rect.colliderect(car_rect):
                        game.player.interact_with_car(car)
    # Update game state
    game.update()

    # Render the game
    game.render(screen)  # Render the player

    # Debug
    if debug:
        fill_surface = pygame.Surface((1024, 720))
        fill_surface.fill((0,0,0))
        fill_surface.set_alpha(180)
        # Draw the semi-opaque black fill
        screen.blit(fill_surface, (0, 0))
        debug_text  = font.render(f"Player position: x: {game.player.x:.2f}, y: {game.player.y:.2f}, wx: {game.player.world_x:.2f}, wy: {game.player.world_y:.2f}, rect: {game.player.rect}, car: {game.player.car}, in_car: {game.player.in_car}, direction: {game.player.direction:.2f}", True, (255, 255, 255))
        screen.blit(debug_text, (40, 40))
        debug_text  = font.render(f"Player rect: x: {game.player.rect}", True, (255, 255, 255))
        screen.blit(debug_text, (40, 60))
        for car in game.vehicles:
            debug_text  = font.render(f"Car position: x: {car.x:.2f}, y: {car.y:.2f}, speed: {car.speed:.2f}, accel: {car.acceleration:.2f}, max_speed: {car.max_speed:.2f}, rect: {car.rect}, occupied: {car.occupied}, direction: {car.direction:.2f}", True, (255, 255, 255))
            screen.blit(debug_text, (40, 80))
        debug_text  = font.render(f"Camera: x: {game.camera.x:.2f}, y: {game.camera.y:.2f}, zoom: {game.camera.zoom}, scr_width: {game.camera.screen_width:.2f}, scr_height: {game.camera.screen_height:.2f}, wrl_width: {game.camera.world_width:.2f}, wrl_height: {game.camera.world_height: .2f}", True, (255, 255, 255))
        screen.blit(debug_text, (40, 100))

    pygame.display.flip()  # Update the display

    # Limit the frame rate
    clock.tick(60)

# Clean up before exiting
pygame.quit()
