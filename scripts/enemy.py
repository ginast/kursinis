import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, scroll_x, scroll_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x - scroll_x  # Adjust the position based on scroll coordinates
        self.rect.y = y - scroll_y
        self.start_x = self.rect.x
        self.move_direction = 1
        self.move_counter = 0

    def update(self, player_rect):
        # Update the enemy's behavior here
        pass
