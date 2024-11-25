import pygame
import webbrowser

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animal Welfare Educational Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)  # Default pygame font with size 36

# Load animal images
elephant_image = pygame.image.load('assets/elephant.png')
tiger_image = pygame.image.load('assets/tiger.png')
polar_bear_image = pygame.image.load('assets/polar_bear.png')
orangutan_image = pygame.image.load('assets/orangutan.png')
sea_turtle_image = pygame.image.load('assets/sea_turtle.png')
amur_leopard_image = pygame.image.load('assets/amur_leopard.png')
pangolin_image = pygame.image.load('assets/pangolin.png')
vaquita_image = pygame.image.load('assets/vaquita.png')
red_panda_image = pygame.image.load('assets/red_panda.png')
blue_whale_image = pygame.image.load('assets/blue_whale.png')

# Set up animal data in a grid
animals = [
    {"name": "Elephant", "image": elephant_image, "position": (50, 50)},
    {"name": "Tiger", "image": tiger_image, "position": (400, 50)},
    {"name": "Polar Bear", "image": polar_bear_image, "position": (750, 50)},
    {"name": "Orangutan", "image": orangutan_image, "position": (1100, 50)},
    {"name": "Sea Turtle", "image": sea_turtle_image, "position": (50, 350)},
    {"name": "Amur Leopard", "image": amur_leopard_image, "position": (400, 350)},
    {"name": "Pangolin", "image": pangolin_image, "position": (750, 350)},
    {"name": "Vaquita", "image": vaquita_image, "position": (1100, 350)},
    {"name": "Red Panda", "image": red_panda_image, "position": (550, 650)},
    {"name": "Blue Whale", "image": blue_whale_image, "position": (900, 650)}
]

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for animal in animals:
                rect = animal["image"].get_rect(topleft=animal["position"])
                if rect.collidepoint(mouse_pos):
                    # Open the map with animal details
                    webbrowser.open("http://localhost:5000/" + animal["name"].replace(" ", "_").lower())

    # Draw animals and their names on the screen
    for animal in animals:
        # Draw the animal image
        screen.blit(animal["image"], animal["position"])
        
        # Draw the name below the image
        text = font.render(animal["name"], True, BLACK)
        text_rect = text.get_rect(center=(animal["position"][0] + animal["image"].get_width() // 2, 
                                          animal["position"][1] + animal["image"].get_height() + 20))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
