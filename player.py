import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.speed = 5  # Speed in pixels per frame
        self.image = pygame.image.load("img/player.png")  # Load the player image
        self.rect = self.image.get_rect()  # Get a rect object for the image to use for collision detection
        self.direction = 0  # Initial direction in degrees
        self.in_car = False  # Whether the player is currently in a car
        self.car = None  # The car the player is currently in

    def update(self):
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
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed

            # Keep the player within the bounds of the screen
            if self.x < 0:
                self.x = 0
            if self.x > 1024: #- self.image.get_width():
                self.x = 1024 #- self.image.get_width()
            if self.y < 0:
                self.y = 0
            if self.y > 720:# - self.image.get_height():
                self.y = 720# - self.image.get_height()

    def render(self, screen):
        # Rotate the player image
        rotated_image = pygame.transform.rotate(self.image, self.direction)

        # Calculate the center of the rotated image
        center = rotated_image.get_rect().center
        x = self.x - center[0]
        y = self.y - center[1]

        # Draw the rotated image on the screen
        screen.blit(rotated_image, (x, y))

    def interact_with_car(self, car):
        # Check if the player is currently in the car
        if self.in_car:
            # The player is already in the car, so exit the car
            self.in_car = False
            self.car = None
            car.occupied = False
        else:
            # Check if the car is occupied
            if car.occupied:
                return  # Do nothing if the car is already occupied
            # The player is not in the car, so try to enter the car
            self.in_car = True
            self.car = car
            car.occupied = True
