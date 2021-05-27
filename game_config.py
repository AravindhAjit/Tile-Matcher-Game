import os
#----------global variables
image_size =128
screen_size =512
num_tiles_side=4
num_tiles_total=16
margin=4

#to import assets

#filename stored
asset_dir='assets'

#checks for png file in the asset folder
asset_files=[x for x in os.listdir(asset_dir) if x[-3:].lower() =='png']


assert len(asset_files) == 8

