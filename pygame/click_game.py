wizard= Actor('character')
wizard.pos = 100,50

WIDTH = 500
HEIGHT = wizard.height + 20

def draw():
    screen.fill((255,0,0))
    wizard.draw()

def update():
    wizard.left= wizard.left + 2
    if wizard.left> WIDTH:
         wizard.right = 0
