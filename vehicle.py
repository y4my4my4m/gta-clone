import pygame
import math
class Vehicle:
    def __init__(self, x, y, speed):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.speed = 0
        self.acceleration = 0
        self.brake_acceleration = -0.2  # Negative value for braking
        self.max_speed = 2  # Speed in pixels per frame
        self.image = pygame.image.load("img/vehicle.png")  # Load the vehicle image
        self.image = pygame.transform.scale(self.image, (125, 76))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.occupied = False  # Whether the car is occupied by a player
        self.direction = 0  # Initial direction in degrees
        self.rotated_image = self.image

        self.x2 = 0
        self.y2 = 0

    def update(self):
        # Update the rect attribute to match the current x and y position
        self.rect.move_ip(self.x - self.rect.x, self.y - self.rect.y)

        # Check if the car is occupied by a player
        if self.occupied:
            # Update the car's position based on the player's input
            keys = pygame.key.get_pressed()
            if self.speed > -4:  # Only allow turning if the car is moving
                if keys[pygame.K_a]:
                    self.direction -= self.speed / 2 
                if keys[pygame.K_d]:
                    self.direction += self.speed / 2
            # Update the car's acceleration based on the player's input
            if keys[pygame.K_w]:
                self.acceleration += 0.1
            if keys[pygame.K_s]:
                self.acceleration = self.brake_acceleration  # Apply braking acceleration
            else:
                self.acceleration *= 0.9  # Reset acceleration if S key is not pressed

        self.speed += self.acceleration
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))
        # Apply friction to slow down the car
        self.speed *= 0.9
        # Limit the speed to the maximum speed
        self.speed = max(self.speed, -self.max_speed)
        self.acceleration = min(1, self.acceleration)
        self.acceleration = max(0, self.acceleration)


        # Rotate the car image
        self.rotated_image = pygame.transform.rotate(self.image, -self.direction)
        # Calculate the center of the rotated image
        center = self.rotated_image.get_rect().center
        self.x2 = self.x - center[0]
        self.y2 = self.y - center[1]

        # Keep the car within the bounds of the screen
        if self.x < 0:
            self.x = 0
        if self.x > 1024:# - self.image.get_width():
            self.x = 1024# - self.image.get_width()
        if self.y < 0:
            self.y = 0
        if self.y > 720:# - self.image.get_height():
            self.y = 720# - self.image.get_height()

    def render(self, screen):
        # Draw the vehicle on the screen
        screen.blit(self.rotated_image, (self.x2, self.y2))
