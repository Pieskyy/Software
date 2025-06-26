from settings import tree, barry, harry, larry, garry, trowser
from start import start
from lore import lore
from choice import choose_path

player, dime = start()
lore(player, dime)
choose_path(player, dime, tree, barry, harry, larry, garry, trowser)
