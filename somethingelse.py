from superwires import games, color
import random

SCORE = 0
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pizza(games.Sprite):
    def update(self):
        global SCORE

    #Reverse a velocity component if edge of screen reached
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            SCORE +=1
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
            SCORE += 1

    #teleport mec

    # if self.left > games.screen.width:
    #     self.right = 0
    #     SCORE +=1
    # if self.right <0:
    #     self.left = games.screen.width
    #     SCORE +=1
    # if self.bottom > games.screen.height:
    #     self.top = 0
    #     SCORE +=1
    # if self.top < 0:
    #     self.bottom = 0
    #     SCORE += 1

class ScText(games.Text):
    def update(self):
        self.value = SCORE


def main():
    #loaded img
    bg_img = games.load_image("images/sky.PNG", transparent = False)
    pizza_img = games.load_image("something")

    #added img to bg
    games.screen.background = bg_img

    #create sprite

    pizza = Pizza(image = pizza_img,
                  x=games.screen.width/2,
                  y=games.screen.height/2,
                  dx = random.randint(-10,10),
                  dy=random.randint(-10,10),
                  )
    pizza1 = Pizza(image = pizza_img,
                  x=games.screen.width/2,
                  y=games.screen.height/2,
                  dx = random.randint(-10,10),
                  dy=random.randint(-10,10),
                  )
    pizza2 = Pizza(image = pizza_img,
                  x=games.screen.width/2,
                  y=games.screen.height/2,
                  dx = random.randint(-10,10),
                  dy=random.randint(-10,10),
                  )

    #create txt obj
    score = ScText(value=SCORE,
                size=60,
                color=color.black,
                x=550,
                y = 30
                )

    #draw objs to screen
    games.screen.add(pizza)
    games.screen.add(pizza1)
    games.screen.add(pizza2)
    games.screen.add(score)

    #start mainloop
    games.screen.mainloop()

    ##game_over = games.Message(value = "Game Over,"
    #                   size= 100,
    #                   color = color.blue,
    #                   x = games.screen.width/2,
    #                   y = games.screen.height/2,
    #                   lifetime = 250,
    #                   after_death = games.screen.quit)
#games.screen.add
main()
