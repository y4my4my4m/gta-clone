import pygame

class Camera:
    def __init__(self, screen_width, screen_height, world_width, world_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height

        self.x = self.screen_width/2  # Initial x position of the camera
        self.y = self.screen_height/2  # Initial y position of the camera
        self.zoom = 1  # Initial zoom level
        self.speed = 5

    def update(self, x, y):
        # Update the camera's position to follow the given x and y coordinates
        self.x = x - self.screen_width // 2
        self.y = y - self.screen_height // 2
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHTBRACKET]:
            self.zoom *= 1.1
        if keys[pygame.K_LEFTBRACKET]:
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
        # Create a copy of the entity's rect
        transformed_rect = entity.rect.copy()
        # Offset the rect by the camera's position
        transformed_rect.x -= self.x
        transformed_rect.y -= self.y
        # Scale the rect by the camera's zoom level
        transformed_rect.x *= self.zoom
        transformed_rect.y *= self.zoom
        transformed_rect.w *= self.zoom
        transformed_rect.h *= self.zoom
        return transformed_rect