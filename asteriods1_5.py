#asteriods 1.0
#Jessica Weinburger


#imports
from superwires import games, color
import random
import math


#Global Info
games.init(screen_width = 640, screen_height = 480, fps = 60)

#Classes
class Game(object):
    def __init__(self):
        self.level = 0
        #self.sound = games.load_sound("sounds/filenamehere")
        self.score = games.Text(value = 0,
        size = 30,
        color = color.white,
        top = 5,
        right = games.screen.width - 10,
        is_collideable = False)
        games.screen.add(self.score)
        self.ship = Ship(game = self,
        x = games.screen.width / 2,
        y = games.screen.height / 2)
        games.screen.add(self.ship)

    def play(self):
        #games.music.load("sounds/filenamehere")
        #games.music.play(-1)

        #load data
        bg_img = games.load_image("images/background.png")
        games.screen.background = bg_img

        self.advance()
        
        games.screen.mainloop()

    def advance(self):
        self.level += 1
        BUFFER = 150

        for i in range(8):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            x %= games.screen.width
            y %= games.screen.height
            new_asteroid = Asteroid(game = self, x = x, y = y, size = Asteroid.LARGE)
            games.screen.add(new_asteroid)

            level_message = games.Message(value = "Level" + str(self.level),
            size = 40,
            color = color.yellow,
            x = games.screen.width / 2,
            y = games.screen.width / 10,
            lifetime = 3 * games.screen.fps,
            is_collideable =  False)
            games.screen.add(level_message)

            #if self.level > 1:
                #self.sound.play()

    def end(self):
        end_message = games.Message(value = "Game Over",
        size = 90,
        color = color.red,
        x = games.screen.width / 2,
        y = games.screen.height / 2,
        lifetime = 5 * games.screen.fps,
        after_death = games.screen.quit,
        is_collideable = False)
        games.screen.add(end_message)

class Wrapper(games.Sprite):
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
    
    def die(self):
        self.destroy()

class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        #create explotion
        new_explosion = Explosion(x = self.x, y = self.y)
        #add to screen
        games.screen.add(new_explosion)
        self.destroy()

class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("images/asteriodsmall.png"),
    MEDIUM: games.load_image("images/asteriodmedium.png"),
    LARGE: games.load_image("images/asteriodlarge.png") }
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        Asteroid.total += 1
        super(Asteroid, self).__init__(image = Asteroid.images[size],
        x = x, 
        y = y,
        dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
        dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.size = size
        self.game = game

        # if self.overlapping_sprites:
        #     for sprite in self.overlapping_sprites:
        #         sprite.die()
        #     self.die()
    def die(self):
        #if asteroid isn't small, replace with two smaller asteroids
        #add score
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game, x = self.x,
                y = self.y,
                size = self.size - 1)
                games.screen.add(new_asteroid)

        if Asteroid.total == 0:
            self.game.advance()
        super(Asteroid, self).die()



class Ship(Collider):
    ship_image = games.load_image("images/ship.png")
    #sound = games.load_sound("sounds/thrust.wav")
    ROTATION_STEP = 5
    VELOCITY_STEP = .03
    MISSLE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super(Ship, self).__init__(image = Ship.ship_image, x = x, y = y)
        self.game = game
        self.missle_wait = 0

    def update(self):
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            #Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        if  self.missle_wait > 0:
            self.missle_wait -= 1

        if games.keyboard.is_pressed(games.K_SPACE) and self.missle_wait == 0:
            shot = Missle(self.x, self.y, self.angle)
            games.screen.add(shot)
            self.missle_wait = Ship.MISSLE_DELAY



class Missle(Collider):
    image = games.load_image("images/laser.png")
    #sound = games.load_sound("sounds/lasersound.wav")
    BUFFER = 40
    VELOCITY_FACTOR =  7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        #Missile.sound.play()
        angle = ship_angle * math.pi / 180


        #calculate missile's starting position
        buffer_x = Missle.BUFFER * math.sin(angle)
        buffer_y = Missle.BUFFER * -math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y
        
        dx = Missle.VELOCITY_FACTOR * math.sin(angle)
        dy = Missle.VELOCITY_FACTOR * -math.cos(angle)

        super(Missle, self).__init__(image = Missle.image,
        x = x,
        y = y,
        dx = dx,
        dy = dy)
        self.lifetime = Missle.LIFETIME
        self.angle = ship_angle

    def update(self):
        super(Missle, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

    


#main

class Explosion(games.Animation):
    #sound  = games.load_sound("sounds/filenamehere")
    explosion_files = ["images/explosion1.png",
    "images/explosion2.png",
    "images/explosion3.png",
    "images/explosion4.png",
    "images/explosion5.png",
    "images/explosion6.png",
    "images/explosion7.png"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.explosion_files,
        x = x,
        y = y,
        repeat_interval = 4,
        n_repeats = 1,
        is_collideable = False )
        #Explosion.sound.play() 

def main():
    astriods = Game()
    astriods.play()

main()
