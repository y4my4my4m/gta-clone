from player import Player
from vehicle import Vehicle
from camera import Camera
from npc import NPC
from background import Background
class Game:
    def __init__(self, screen_width, screen_height):
        # Initialize game state variables
        self.player = Player(screen_width/2, screen_height/2)  # Create a player object
        self.enemies = []  # Create a list to store enemy objects
        testNPC = NPC(450,120,2,self)
        self.npcs = [testNPC]  # Create a list to store NPC objects
        self.items = []  # Create a list to store item objects
        self.score = 0  # Initialize the score
        self.vehicles = [Vehicle(230,480,5)]
        self.camera = Camera(screen_width, screen_height, 4640*4, 4672*4)
        self.enemies.append(testNPC)
        self.background = Background(0, 0, 4640*4, 4672*4, "img/libertycity.png")

    def update(self):
        # Update camera position based on vehicle if player is in car
        if self.player.in_car:
            car = self.player.car
            self.camera.update(car.x, car.y)
        # else:
            # self.camera.update(self.player.world_x, self.player.world_y)

        # Update game objects
        self.player.update(self.camera)
        
        for vehicle in self.vehicles:
            vehicle.update()
            
        for npc in self.npcs:
            npc.update()

    def render(self, screen):
        # Clear the screen
        screen.fill((50, 50, 50))

        self.background.render(screen, self.camera)
        # Render the player
        self.player.render(screen, self.camera)

        # Render enemies
        # for enemy in self.enemies:
        #     enemy.render(screen)

        # Render items
        # for item in self.items:
        #     item.render(screen)

        # Render vehicles
        for vehicle in self.vehicles:
            vehicle.render(screen, self.camera)

        # Update the positions and states of NPCs
        for npc in self.npcs:
            npc.render(screen, self.camera)