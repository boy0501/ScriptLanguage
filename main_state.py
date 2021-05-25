import gfw
from tkinter import *
from Logo import Logo
from main_func import MainFunc
from info import InfoFunc


def enter():
    global image, elapsed ,bg
    gfw.world.init(['logo','mainfunc','infofunc'])
    global logo,m_func
    logo = Logo()
    m_func = MainFunc()
    gfw.Objects['main_func'] = []
    gfw.Objects['info'] =[]
    gfw.world.add(gfw.layer.logo,logo)
    gfw.world.add(gfw.layer.mainfunc,m_func)
    



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
