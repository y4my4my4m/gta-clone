from player import Player
from vehicle import Vehicle
from camera import Camera
from npc import NPC
from background import Background
class Game:
    def __init__(self):
        # Initialize game state variables
        self.player = Player(640,480)  # Create a player object
        self.enemies = []  # Create a list to store enemy objects
        testNPC = NPC(450,120,2,self)
        self.npcs = [testNPC]  # Create a list to store NPC objects
        self.items = []  # Create a list to store item objects
        self.score = 0  # Initialize the score
        self.vehicles = [Vehicle(230,480,5)]
        self.camera = Camera(0, 0, 4000, 4000)
        self.enemies.append(testNPC)
        self.background = Background(0, 0, 4640*4, 4672*4, "img/libertycity.png")

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

        # Update the positions and states of NPCs
        for npc in self.npcs:
            npc.update()

        # Update the camera's position
        self.camera.update(self.player.x, self.player.y)

        # Update the background's position based on the camera's position
        # self.background.update(self.player.x, self.player.y)
        self.background.update(self.camera)

        # # Update the background position based on the player's position
        # self.background_x = -self.player.x + 640 / 2  # 640 is the 

    def render(self, screen):
        # Clear the screen
        screen.fill((50, 50, 50))

        self.background.render(screen)
        # Render the player
        self.player.render(screen, self.camera)

        # Render enemies
        for enemy in self.enemies:
            enemy.render(screen)

        # Render items
        for item in self.items:
            item.render(screen)

        # Render vehicles
        for vehicle in self.vehicles:
            vehicle.render(screen, self.camera)

        # Update the positions and states of NPCs
        for npc in self.npcs:
            npc.render(screen)