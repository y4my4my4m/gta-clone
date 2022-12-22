import pygame

class Camera:
    def __init__(self, screen_width, screen_height, world_width, world_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height

        self.x = 0  # Initial x position of the camera
        self.y = 0  # Initial y position of the camera
        self.zoom = 1  # Initial zoom level
        self.speed = 5

    def update(self, x, y):
        # Update the camera's position to follow the given x and y coordinates
        self.x = x - self.screen_width // 2
        self.y = y - self.screen_height // 2
            
        keys = pygame.key.get_pressed()
        # Update the camera's position based on player input
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_PLUS]:
            self.zoom *= 1.1
        if keys[pygame.K_MINUS]:
            self.zoom /= 1.1
        # Keep the camera within the bounds of the world
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.screen_width > self.world_width:
            self.x = self.world_width - self.screen_width
        if self.y + self.screen_height > self.world_height:
            self.y = self.world_height - self.screen_height

    def zoom_in(self):
        # Zoom in by a factor of 1.1
        self.zoom *= 1.1

    def zoom_out(self):
        # Zoom out by a factor of 1.1
        self.zoom /= 1.1

    def apply(self, entity):
        # Convert the entity's position and size from world coordinates to screen coordinates
        return entity.rect.move(self.x, self.y).scale(self.zoom)
