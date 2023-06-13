def Execute_cette_cellule_pour_afficher_image(titre):
	from PIL import Image
	monImage=Image.open(titre)
	monImage