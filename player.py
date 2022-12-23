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
        # Update the rect attribute to match the current x and y position
        self.rect.move_ip(self.x - self.rect.x, self.y - self.rect.y)
        # Check if the player is in a car
        if self.in_car:
            # Update the player's position to match the car's position
            self.x = self.car.x
            self.y = self.car.y
        else:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate the angle to the mouse in radians
            dx = mouse_x - self.x
            dy = mouse_y - self.y
            radians = math.atan2(-dy, dx)
            # Convert the angle to degrees
            self.direction = math.degrees(radians)

            # Check for input from the player
            keys = pygame.key.get_pressed()
            camera.x -= self.speed if keys[pygame.K_a] else 0
            camera.x += self.speed if keys[pygame.K_d] else 0
            camera.y -= self.speed if keys[pygame.K_w] else 0
            camera.y += self.speed if keys[pygame.K_s] else 0

    def render(self, screen, camera):
        # Apply the camera transformation to the player's rect
        transformed_rect = camera.apply(self)
        transformed_rect = pygame.transform.scale(self.image, (transformed_rect.w,transformed_rect.h))

        # Rotate the player image
        rotated_image = pygame.transform.rotate(transformed_rect, self.direction)

        # Calculate the center of the rotated image
        center = rotated_image.get_rect().center
        x = self.x - center[0]
        y = self.y - center[1]
        self.world_x = x + camera.x
        self.world_y = y + camera.y
        # Draw the rotated image on the screen
        if not self.hidden:
            screen.blit(rotated_image, (x,y))

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
