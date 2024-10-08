import pygame
import webbrowser

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animal Welfare Educational Game")

# Colors
WHITE = (255, 255, 255)

# Load animal images
elephant_image = pygame.image.load('assets/elephant.png')
tiger_image = pygame.image.load('assets/tiger.png')
polar_bear_image = pygame.image.load('assets/polar_bear.png')
# Load additional images for the other animals
# Example: red_panda_image = pygame.image.load('assets/red_panda.png')

# Animal data with locations and details
animals = [
    {"name": "Elephant", "image": elephant_image, "position": (100, 300), "info": "Elephants are endangered due to poaching for their ivory."},
    {"name": "Tiger", "image": tiger_image, "position": (200, 150), "info": "Tigers are endangered due to habitat loss and poaching."},
    {"name": "Polar Bear", "image": polar_bear_image, "position": (400, 50), "info": "Polar Bears are endangered due to climate change."},
    # Add other animals
    # {"name": "Red Panda", "image": red_panda_image, "position": (500, 200), "info": "..."},
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
                    # Open the map with information in the browser
                    webbrowser.open("http://localhost:5000/" + animal["name"].lower())
    
    # Draw animals on the screen
    for animal in animals:
        screen.blit(animal["image"], animal["position"])

    pygame.display.flip()

pygame.quit()
