# for animal class

import os
import random
import game_config as gc

from pygame import image,transform

#dictionary for animal count.. Initially set to 0
animal_count=dict((a,0)for a in gc.asset_files)

def available_animals():
    return[a for a,c in animal_count.items() if c<2]

class Animal:
    #index 0-15 inclusive
    def __init__(self,index):
        self.index=index
        self.row=index // gc.num_tiles_side
        self.col = index % gc.num_tiles_side
        self.name=random.choice(available_animals())
        animal_count[self.name]+=1

        self.image_path = os.path.join(gc.asset_dir,self.name)
        self.image= image.load(self.image_path)
        self.image=transform.scale(self.image,(gc.image_size-2*gc.margin,gc.image_size-2*gc.margin))

        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip=False

