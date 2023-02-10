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

def set_wizard_normal():
    wizard.image = 'character'


def set_wizard_clicked():
    wizard.image = 'character_click'
    clock.schedule_unique(set_wizard_normal, .20)


def on_mouse_down(pos):
    if wizard.collidepoint(pos):
        print("Eek!")
        set_wizard_clicked()
        sounds.eep.play()
    else:
        print("You missed me!")

