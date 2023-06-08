import pygame, sys
from settings import *
from human import *
from shark import Shark

# Miscellaneous - initializing game, assigning basic variables, playing music
pygame.init()
screen = pygame.display.set_mode((tile_width * 16, tile_height * 16))
clock = pygame.time.Clock()
screen.fill("blue")
shark_group = pygame.sprite.GroupSingle()
shark = Shark(screen)
shark_group.add(shark)
human_group = pygame.sprite.Group()
score = 0
pygame.mixer.music.load("music/finaljaws.wav")
pygame.mixer.music.play(-1)

death_sound = pygame.mixer.Sound("music/death.mp3")
death_sound_playing = False
collision_sound = pygame.mixer.Sound("music/death2.mp3")
collision_sound_playing = False
# Creates human and adds it to the group
for i in range(1):
    human1 = Human()
    human_group.add(human1)

# Runs functions inside event moveShark every 200 ms
moveShark = pygame.USEREVENT
pygame.time.set_timer(moveShark, 200)

# Functions for collisions with humans, with itself, and with the walls of the game
def collision():
    global human1, score, death_sound_playing
    if human1.location == shark.body[0]:
        human_group.empty()
        human1 = Human()
        human_group.add(human1)
        shark.body.insert(0, shark.body[0] + shark.direction)
        score += 1
        if not death_sound_playing:
            death_sound.play()
            death_sound_playing = False

def self_collision():
    global death_sound_playing, collision_sound_playing
    for block in shark.body[1:]:
        if block == shark.body[0]:
            if not collision_sound_playing:
                collision_sound.play()
                collision_sound_playing = False
                pygame.time.delay(1000)
            pygame.quit()
            sys.exit()

def environment_collision():
    global death_sound_playing, collision_sound_playing
    if shark.body[0].x > 15 or shark.body[0].x < 0:
        if not collision_sound_playing:
            collision_sound.play()
            collision_sound_playing = False
            pygame.time.delay(1000)
        pygame.quit()
        sys.exit()
    if shark.body[0].y > 15 or shark.body[0].y < 0:
        if not collision_sound_playing:
            collision_sound.play()
            collision_sound_playing = False
            pygame.time.delay(1000)

        pygame.quit()
        sys.exit()


# Game loop - handles quitting the game, runs event moveShark
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == moveShark:
            shark.move_shark()
            collision()
            self_collision()
            environment_collision()

    screen.fill("blue")

    # Uses font to create text on the screen (for the score)
    font = pygame.font.Font("slkscre.ttf", 32)
    text = font.render("Score: " + str(score), True, (0, 0, 0))

    # Draws shark, humans, and text, updates game
    human_group.draw(screen)
    screen.blit(text, (0, 0))
    shark.get_input()
    shark.draw_shark(screen)
    pygame.display.update()
    clock.tick(fps)
