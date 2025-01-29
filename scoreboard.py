import pygame

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, font, size, position, color=(255, 255, 255)):
        super().__init__()  # Initialize the parent Sprite class

        self.font = pygame.font.Font(None, size)
        self.text = "Score: 0"
        self.color = color
        self.position = position
        
        # Create the text surface
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, new_score):
        """Update the score displayed on the scoreboard."""
        self.text = f"Score: {new_score}"
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.position)