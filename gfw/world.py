from functools import reduce
import gfw
from pico2d import *
import math

objects = []
trashcan = []
pos = (0,0)
dtheta = 0
def init(layer_names):
    global objects
    objects = []
    gfw.layer = lambda: None
    layerIndex = 0
    for name in layer_names:
        objects.append([])
        gfw.layer.__dict__[name] = layerIndex
        layerIndex += 1

def add(layer_index, obj):
    global objects
    objects[layer_index].append(obj)

def remove(obj):
    global trashcan
    trashcan.append(obj)

def all_objects():
    global objects
    for layer_objects in objects:
        for obj in layer_objects:
            yield obj

def objects_at(layer_index):
    global objects
    for obj in objects[layer_index]:
        yield obj

def count_at(layer_index):
    global objects
    return len(objects[layer_index])

def count():
    return reduce(lambda sum, a: sum + len(a), objects, 0)

def clear():
    global objects
    for o in all_objects():
        del o
    objects = []

def clear_at(layer_index):
    global objects
    for o in objects[layer_index]:
        del o
    objects[layer_index] = []


def update():
    global dtheta
    global pos
    reference = [pos]
    for obj in all_objects():
        obj.update()
        obj.screenshake(reference)
        pos = reference[0]
    if len(trashcan) > 0:
        empty_trashcan()
    #ㅡㅡㅡㅡㅡ 화면 흔들림효과
    #pos =(math.sin(dtheta*180/math.pi) * 10, math.sin(dtheta*180/math.pi) * 10)
    #dtheta = (dtheta+1) % 360
    #ㅡㅡㅡㅡㅡ 화면 흔들림효과
    counts = list(map(len, objects))
    #print('count:', counts, count())
    #print(objects)
    #print(trashcan)

def draw():
    global pos
    for obj in all_objects():
        obj.draw(pos)

def empty_trashcan():
    global trashcan
    global objects
    
    for obj in trashcan:
        for layer_objects in objects:
            # if obj in layer_objects:
            #     layer_objects.remove(obj)
            try:
                layer_objects.remove(obj)
            except ValueError:
                pass
    trashcan = []


