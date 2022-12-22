import pygame

class Vehicle:
    def __init__(self, x, y, speed):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.speed = speed  # Speed in pixels per frame
        self.image = pygame.image.load("img/vehicle.png")  # Load the vehicle image
        self.image = pygame.transform.scale(self.image, (125, 76))
        self.rect = self.image.get_rect()  # Get a rect object for the image to use for collision detection
        self.occupied = False  # Whether the car is occupied by a player
        self.direction = 0  # Initial direction in degrees

    def update(self):
        # Update the rect attribute to match the current x and y position
        self.rect.x = self.x
        self.rect.y = self.y
        # Check if the car is occupied by a player
        if self.occupied:
            # Update the car's position based on the player's input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed

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
        screen.blit(self.image, (self.x, self.y))
