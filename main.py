# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import ScoreBoard
from gamestate import GameState

import sys

score = 0

def main():

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    GameState.score = 0

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    scoreboards = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    ScoreBoard.containers = (scoreboards,)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    scoreboard = ScoreBoard(pygame.font.Font(None, 36), 36, (400,50), "purple")
    scoreboards.add(scoreboard)

    asteroidfield = AsteroidField()

    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                print("Game over!")
                running = False
            
            for s in shots:
                if a.collides_with(s):
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        scoreboard.update(GameState.score)
        scoreboards.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()