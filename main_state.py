import gfw
from tkinter import *
from Logo import Logo
from main_func import MainFunc


def enter():
    global image, elapsed ,bg
    gfw.world.init(['mainfunc','logo'])
    global logo,m_func
    logo = Logo()
    m_func = MainFunc()
    #gfw.world.add(gfw.layer.mainfunc,m_func)
    #gfw.world.add(gfw.layer.logo,logo)


def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
        
def exit():
    global image
    pass

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
