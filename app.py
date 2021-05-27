import pygame
import game_config as gc

from pygame import display,event,image
from animal import Animal
from time import sleep


pygame.init()

display.set_caption("Animal Matcher")

screen=display.set_mode((512,512))

#load image
matched=image.load('other_assets/matched.png')
victory=image.load('other_assets/victory.png')
running=True

tiles=[Animal(i) for i in range(0,gc.num_tiles_total)]
current_images=[]

def find_index(x,y):
    row=y//gc.image_size
    col = x//gc.image_size
    index= row*gc.num_tiles_side +col

    return index


while running:
    current_events=event.get()

    for e in current_events:
        if e.type==pygame.QUIT:
            running=False
        
        if e.type == pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:
                running=False

        if e.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            index=find_index(mouse_x,mouse_y)
            if index not in current_images: 
                current_images.append(index)
            if len(current_images)==2:
                if tiles[current_images[0]].name != tiles[current_images[1]].name:
                    sleep(0.2)
                    current_images=[]

    screen.fill((255,255,255))

    score=0
    

    for _,tile in enumerate(tiles):
        image_i=tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i,(tile.col*gc.image_size+gc.margin,tile.row*gc.image_size+gc.margin))
        else:
            score+=1
    display.flip()



    if len(current_images)==2:
        i1,i2=current_images
        if tiles[i1].name == tiles[i2].name:
            tiles[i1].skip=True
            tiles[i2].skip=True
            sleep(0.1)
            screen.blit(matched,(0,0)) 
            display.flip()
            sleep(0.5)           
            current_images=[]
    if score==len(tiles):
        screen.blit(victory,(0,0))
        display.flip()
        running=False




print("Goodbye")
