import pygame
import random
import time
import shelve

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
WHITE = (255, 255, 255)
PLAYER_SIZE = 20
GHOST_SIZE = 20
PLAYER_SPEED = 5
GHOST_BASE_SPEED = 2
NEW_GHOST_DELAY = 15  # 15 seconds
SCORE_INCREMENT_DELAY = 10  # 10 seconds
SPEEDUP_DELAY = 20  # 20 seconds

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Define classes (Model Classes)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # Keep player within screen boundaries
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - PLAYER_SIZE))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - PLAYER_SIZE))

class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((GHOST_SIZE, GHOST_SIZE))
        self.image.fill((255, 0, 0))  # Red ghost
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        self.dx = random.choice([-1, 1]) * GHOST_BASE_SPEED
        self.dy = random.choice([-1, 1]) * GHOST_BASE_SPEED

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Reverse direction if hitting screen boundary
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy *= -1

# Create sprite groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Start of game ghosts
ghosts = pygame.sprite.Group()
for _ in range(3):  # Create 3 ghosts initially
    ghost = Ghost()
    ghosts.add(ghost)
    all_sprites.add(ghost)

# Timer variables
start_time = time.time()
last_ghost_spawn_time = start_time
last_score_increment_time = start_time
last_speedup_time = start_time

# Font for timer and score display
font = pygame.font.SysFont(None, 36)

# Initialize score
score = 0

# Main game variables
running = True
game_over = False
restart = False
high_score = 0

# Load high score from database
with shelve.open("high_score_db") as db:
    if "high_score" in db:
        high_score = db["high_score"]

while running:
    if restart:
        restart = False
        game_over = False
        score = 0
        start_time = time.time()
        player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        for ghost in ghosts:
            ghost.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            restart = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            restart = True

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        player.update(keys)

        # Ghost movement
        ghosts.update()

        # Spawn a new ghost every 15 seconds
        current_time = time.time()
        if current_time - last_ghost_spawn_time >= NEW_GHOST_DELAY:
            ghost = Ghost()
            ghosts.add(ghost)
            all_sprites.add(ghost)
            last_ghost_spawn_time = current_time

        # Increment score by 100 every 10 seconds
        if current_time - last_score_increment_time >= SCORE_INCREMENT_DELAY:
            score += 100
            last_score_increment_time = current_time

        # Speed up ghosts every 20 seconds
        if current_time - last_speedup_time >= SPEEDUP_DELAY:
            for ghost in ghosts:
                ghost.dx *= 1.2
                ghost.dy *= 1.2
            last_speedup_time = current_time

        # Collision detection
        if pygame.sprite.spritecollide(player, ghosts, False):
            game_over = True
            if score > high_score:
                high_score = score
                with shelve.open("high_score_db") as db:
                    db["high_score"] = high_score

        # Drawing
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Calculate elapsed time
        elapsed_time = int(current_time - start_time)

        # Render timer text
        timer_text = font.render(f"Time: {elapsed_time} seconds", True, WHITE)
        screen.blit(timer_text, (10, 10))

        # Render score text
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH - 150, 10))
    else:
        # Display game over message
        game_over_text = font.render("GAME OVER!", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

        # Display final score
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))

        # Display high score
        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()