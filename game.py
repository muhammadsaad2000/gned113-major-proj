import pygame
import webbrowser

# Initialize pygame
pygame.init()

# Screen dimensions (increased height for two rows)
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animal Welfare Educational Game")

# Colors
WHITE = (255, 255, 255)

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

# Horizontal and vertical spacing
spacing_x = 50
spacing_y = 50
image_width = 300

# Set up animal data in a 4x3 grid with the last row centered
animals = [
    {"name": "Elephant", "image": elephant_image, "position": (0 * (image_width + spacing_x), spacing_y)},
    {"name": "Tiger", "image": tiger_image, "position": (1 * (image_width + spacing_x), spacing_y)},
    {"name": "Polar Bear", "image": polar_bear_image, "position": (2 * (image_width + spacing_x), spacing_y)},
    {"name": "Orangutan", "image": orangutan_image, "position": (3 * (image_width + spacing_x), spacing_y)},
    {"name": "Sea Turtle", "image": sea_turtle_image, "position": (0 * (image_width + spacing_x), spacing_y + 300)},
    {"name": "Amur Leopard", "image": amur_leopard_image, "position": (1 * (image_width + spacing_x), spacing_y + 300)},
    {"name": "Pangolin", "image": pangolin_image, "position": (2 * (image_width + spacing_x), spacing_y + 300)},
    {"name": "Vaquita", "image": vaquita_image, "position": (3 * (image_width + spacing_x), spacing_y + 300)},
    # Last row, centered on the screen
    {"name": "Red Panda", "image": red_panda_image, "position": (SCREEN_WIDTH // 2 - (image_width + spacing_x) // 2 - image_width, spacing_y + 600)},
    {"name": "Blue Whale", "image": blue_whale_image, "position": (SCREEN_WIDTH // 2 + (image_width + spacing_x) // 2 - image_width, spacing_y + 600)}
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
    
    # Draw animals on the screen
    for animal in animals:
        screen.blit(animal["image"], animal["position"])

    pygame.display.flip()

pygame.quit()
