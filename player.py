import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.world_x = self.x
        self.world_y = self.y
        self.speed = 5  # Speed in pixels per frame
        self.image = pygame.image.load("img/player.png")  # Load the player image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction = 0  # Initial direction in degrees
        self.in_car = False  # Whether the player is currently in a car
        self.car = None  # The car the player is currently in
        self.hidden = False  # Whether the player is hidden

    def update(self, camera):
        if self.in_car:
            # Update the player's position to match the car's position
            self.x = self.car.x
            self.y = self.car.y
            self.world_x = self.car.x
            self.world_y = self.car.y
        else:
            # Get the mouse position for rotation
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Calculate screen-space position
            screen_x = self.world_x - camera.x
            screen_y = self.world_y - camera.y
            
            # Calculate angle to mouse
            dx = mouse_x - screen_x
            dy = mouse_y - screen_y
            self.direction = math.degrees(math.atan2(-dy, dx))

            # Move the player in world coordinates
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.world_y -= self.speed
            if keys[pygame.K_s]:
                self.world_y += self.speed
            if keys[pygame.K_a]:
                self.world_x -= self.speed
            if keys[pygame.K_d]:
                self.world_x += self.speed

            # Update screen position
            self.x = screen_x
            self.y = screen_y
            
        # Update rect position
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def render(self, screen, camera):
        if not self.hidden:
            # Convert world coordinates to screen coordinates
            screen_x = self.world_x - camera.x
            screen_y = self.world_y - camera.y
            
            # Rotate the player image
            rotated_image = pygame.transform.rotate(self.image, self.direction)
            
            # Get the rect of the rotated image
            rotated_rect = rotated_image.get_rect(center=(screen_x, screen_y))
            
            # Draw the player
            screen.blit(rotated_image, rotated_rect.topleft)

    def interact_with_car(self, car):
        # Check if the player is currently in the car
        if self.in_car:
            # The player is already in the car, so exit the car
            self.in_car = False
            self.car = None
            car.occupied = False
            self.hidden = False
        else:
            # Check if the car is occupied
            if car.occupied:
                return  # Do nothing if the car is already occupied
            # The player is not in the car, so try to enter the car
            self.in_car = True
            self.car = car
            car.occupied = True
            self.hidden = True
