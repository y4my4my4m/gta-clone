import pygame
import random
import math

class NPC:
    def __init__(self, x, y, speed, game):
        self.x = x  # Initial x position
        self.y = y  # Initial y position
        self.speed = speed # Initial speed
        self.image = pygame.image.load("img/npc.png")  # Load the NPC image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction = random.randint(0, 360)  # Initial direction in degrees
        self.speed = random.uniform(0.5, 1.5)  # Speed in pixels per frame
        self.rotated_image = self.image
        self.game = game
        self.dead = False

    def update(self):
        self.hit_by_vehicle()  # Check if the NPC is being hit by a vehicle
        # Check for collisions with vehicles
        for vehicle in self.game.vehicles:
            if self.rect.colliderect(vehicle.rect):
                # NPC has been hit by a vehicle
                self.hit_by_vehicle()
        # Update the NPC's position based on their direction and speed
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))
        # Change the NPC's direction randomly
        if random.random() < 0.01:
            self.direction = random.randint(0, 360)
        # Rotate the NPC image
        self.rotated_image = pygame.transform.rotate(self.image, -self.direction)
        # Calculate the center of the rotated image
        center = self.rotated_image.get_rect().center
        x = self.x - center[0]
        y = self.y - center[1]
        # Update the NPC's rect attribute to match the current x and y position
        self.rect.move_ip(x - self.rect.x, y - self.rect.y)
        # if self.dead:
        #     self.game.enemies.remove(self)  # Remove the NPC from the game's enemies list

    def render(self, screen):
        if (self.dead == False):
            # Draw the NPC on the screen
            screen.blit(self.rotated_image, (self.x, self.y))

    def hit_by_vehicle(self):
        # Check if the NPC's rect is colliding with a vehicle's rect
        for vehicle in self.game.vehicles:
            if self.rect.colliderect(vehicle.rect):
                self.dead = True  # Set the NPC's dead flag to True

