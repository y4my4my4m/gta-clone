from player import Player
from vehicle import Vehicle
class Game:
    def __init__(self):
        # Initialize game state variables
        self.player = Player(640,480)  # Create a player object
        self.enemies = []  # Create a list to store enemy objects
        self.items = []  # Create a list to store item objects
        self.score = 0  # Initialize the score
        self.vehicles = [Vehicle(230,480,5)]

    def update(self):

        # Update the player's position and state
        self.player.update()

        # Update the positions and states of enemies
        for enemy in self.enemies:
            enemy.update()

        # Update the positions and states of items
        for item in self.items:
            item.update()

        # Update the positions and states of vehicles
        for vehicle in self.vehicles:
            vehicle.update()

    def render(self, screen):
        # Clear the screen
        screen.fill((50, 50, 50))

        # Render the player
        self.player.render(screen)

        # Render enemies
        for enemy in self.enemies:
            enemy.render(screen)

        # Render items
        for item in self.items:
            item.render(screen)

        # Render vehicles
        for vehicle in self.vehicles:
            vehicle.render(screen)
