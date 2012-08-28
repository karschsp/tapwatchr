from Victory import Victory
from Pinocchios import Pinocchios
from DraftingRoom import DraftingRoom

victory = Victory('Victory', 'http://victorybeer.com/brewpub/on-tap');
victory.parse()
victory.show_beers()
victory.save_beers()

pinocchios = Pinocchios('Pinocchios', 'http://www.pinpizza.com/rotating-beer2012.asp?categoryID=78');
pinocchios.parse()
pinocchios.show_beers()
pinocchios.save_beers()


draftingroom = DraftingRoom('draftingroom', 'http://www.tdrtaplist.blogspot.com/');
draftingroom.parse()
draftingroom.show_beers()
draftingroom.save_beers()
