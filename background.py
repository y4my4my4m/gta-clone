import pygame

class Background:
    def __init__(self, screen_width, screen_height, world_width, world_height, image_path):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height

        # Load the background image and scale it to fit the size of the world
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.world_width, self.world_height))

        # Initialize the position of the background
        self.x = 0
        self.y = 0

    def update(self, camera):
        # Update the x and y position of the image based on the camera's position
        self.x = -camera.x
        self.y = -camera.y

    def render(self, screen):
        # Draw the background on the screen
        screen.blit(self.image, (self.x, self.y))
