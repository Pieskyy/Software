from settings import *
from start import *
from lore import *
from choice import * 

player, dime = start()
lore(player, dime)
choose_path(player, dime, tree)