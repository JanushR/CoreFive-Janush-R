import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 60)
        self.speed = 5
        self.score = 0
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = random.randint(3, 7)

    def reset_position(self):
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT:
            self.reset_position()

# Powerup Class
class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = 3

    def reset_position(self):
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(-300, -200)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT:
            self.reset_position()

# Game class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Space Dodge Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.font = pygame.font.Font(None, 36)

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        # Create player
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create initial enemies
        for _ in range(6):
            self.spawn_enemy()

        # Create initial powerup
        self.spawn_powerup()

    def spawn_enemy(self):
        enemy = Enemy()
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def spawn_powerup(self):
        powerup = Powerup()
        self.all_sprites.add(powerup)
        self.powerups.add(powerup)

    def handle_collisions(self):
        # Check for collisions with enemies
        hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for hit in hits:
            self.player.lives -= 1
            self.spawn_enemy()
            if self.player.lives <= 0:
                self.game_over = True

        # Check for collisions with powerups
        hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        for hit in hits:
            self.player.score += 100
            self.spawn_powerup()

    def draw_text(self):
        score_text = self.font.render(f'Score: {self.player.score}', True, WHITE)
        lives_text = self.font.render(f'Lives: {self.player.lives}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))

    def show_game_over(self):
        game_over_text = self.font.render('GAME OVER!', True, WHITE)
        score_text = self.font.render(f'Final Score: {self.player.score}', True, WHITE)
        restart_text = self.font.render('Press R to Restart or Q to Quit', True, WHITE)

        self.screen.blit(game_over_text, 
                         (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                          WINDOW_HEIGHT//2 - 60))
        self.screen.blit(score_text, 
                         (WINDOW_WIDTH//2 - score_text.get_width()//2, 
                          WINDOW_HEIGHT//2))
        self.screen.blit(restart_text, 
                         (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                          WINDOW_HEIGHT//2 + 60))

    def reset_game(self):
        self.all_sprites.empty()
        self.enemies.empty()
        self.powerups.empty()

        self.player = Player()
        self.all_sprites.add(self.player)

        for _ in range(6):
            self.spawn_enemy()
        self.spawn_powerup()

        self.game_over = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            self.reset_game()
                        elif event.key == pygame.K_q:
                            self.running = False

            if not self.game_over:
                self.all_sprites.update()
                self.handle_collisions()

                self.screen.fill(BLACK)
                self.all_sprites.draw(self.screen)
                self.draw_text()
            else:
                self.show_game_over()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Main game execution
if __name__ == '__main__':
    game = Game()
    game.run()
