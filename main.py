import tkinter as tk # Pour l'interface graphique
from math import atan2, cos, sin # Pour les calculs trigonométriques pour le positionnement des sommets dans l'arbre binaire de recherche graphique

# PARTIE 1

# Question 1.1 et 1.2

class Sommet(object):
    def __init__(self, valeur: float, lettre: str=None):
        """
        Initialise un objet Sommet avec une valeur et une lettre optionnelle.
        :param valeur: La valeur du sommet.
        :param lettre: La lettre associée au sommet (optionnelle).
        """
        self.valeur = valeur
        self.lettre = lettre


class ArbreB(object):
    def __init__(self, racine: Sommet, gauche=None, droite=None):
        """
        Initialise un objet ArbreB avec une racine et des sous-arbres gauche et droit optionnels.
        :param racine: L'objet Sommet qui est la racine de l'arbre.
        :param gauche: L'objet ArbreB qui est le sous-arbre gauche de l'arbre (optionnel).
        :param droite: L'objet ArbreB qui est le sous-arbre droit de l'arbre (optionnel).
        """
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def get_racine(self):
        """
        Retourne un objet Sommet qui est la racine de l'arbre.
        :return: L'objet Sommet qui est la racine de l'arbre.
        """
        return self.racine

    def get_gauche(self):
        """
        Retourne un objet ArbreB qui est le sous-arbre gauche de l'arbre.
        :return: L'objet ArbreB qui est le sous-arbre gauche de l'arbre.
        """
        return self.gauche

    def get_droit(self):
        """
        Retourne un objet ArbreB qui est le sous-arbre droit de l'arbre.
        :return: L'objet ArbreB qui est le sous-arbre droit de l'arbre.
        """
        return self.droite
    
    def inserer_arbre(self, arbre):
        """
        Insère un objet ArbreB dans l'arbre binaire de recherche.
        :param arbre: L'objet ArbreB à insérer dans l'arbre binaire de recherche.
        """
        if arbre.racine.valeur < self.racine.valeur:
            if self.gauche is None:
                self.gauche = arbre
            else:
                self.gauche.inserer_arbre(arbre)
        else:
            if self.droite is None:
                self.droite = arbre
            else:
                self.droite.inserer_arbre(arbre)

    def __add__(self, arbre):
        """
        Surcharge de l'opérateur + pour insérer un objet ArbreB dans l'arbre binaire de recherche.
        :param arbre: L'objet ArbreB à insérer dans l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après l'insertion.
        """
        if arbre.get_gauche() is None and arbre.get_droit() is None:
            self.inserer_arbre(arbre)
            return self
        else:
            self.fusion(arbre)
            return self
    
    def __iadd__(self, arbre):
        """
        Surcharge de l'opérateur += pour insérer un objet ArbreB dans l'arbre binaire de recherche.
        :param arbre: L'objet ArbreB à insérer dans l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après l'insertion.
        """
        if arbre.get_gauche() is None and arbre.get_droit() is None:
            self.inserer_arbre(arbre)
            return self
        else:
            self.fusion(arbre)
            return self

    def supprimer_arbre(self, valeur):
        """
        Supprime un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après la suppression.
        """
        if self.racine.valeur == valeur:
            if self.gauche is None and self.droite is None:
                return None
            elif self.gauche is None:
                return self.droite
            elif self.droite is None:
                return self.gauche
            else:
                successeur = self.droite
                while successeur.gauche is not None:
                    successeur = successeur.gauche
                self.racine = successeur.racine
                self.droite = self.droite.supprimer_arbre(successeur.racine.valeur)
                return self
        elif valeur < self.racine.valeur and self.gauche is not None:
            self.gauche = self.gauche.supprimer_arbre(valeur)
            return self
        elif valeur > self.racine.valeur and self.droite is not None:
            self.droite = self.droite.supprimer_arbre(valeur)
            return self
        else:
            return self

    def __sub__(self, valeur):
        """
        Surcharge de l'opérateur - pour supprimer un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après la suppression.
        """
        self.supprimer_arbre(valeur)
        return self
    
    def __isub__(self, valeur):
        """
        Surcharge de l'opérateur -= pour supprimer un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après la suppression.
        """
        self.supprimer_arbre(valeur)
        return self

    def modifier_etiquette_lettre_arbre(self, lettre, nouvelle_lettre):
        """
        Modifie l'étiquette d'un objet ArbreB avec une lettre donnée dans l'arbre binaire de recherche.
        :param lettre: La lettre de l'objet ArbreB dont l'étiquette doit être modifiée.
        :param nouvelle_lettre: La nouvelle lettre à attribuer à l'étiquette de l'objet ArbreB.
        """
        if self.racine.lettre == lettre:
            self.racine.lettre = nouvelle_lettre
        elif self.gauche is not None:
            self.gauche.modifier_etiquette_lettre_arbre(lettre, nouvelle_lettre)
        elif self.droite is not None:
            self.droite.modifier_etiquette_lettre_arbre(lettre, nouvelle_lettre)
        
    def modifier_etiquette_valeur_arbre(self, lettre, nouvelle_valeur):
        """
        Modifie l'étiquette d'un objet ArbreB avec une valeur donnée dans l'arbre binaire de recherche.
        :param lettre: La lettre de l'objet ArbreB dont l'étiquette doit être modifiée.
        :param nouvelle_valeur: La nouvelle valeur à attribuer à l'étiquette de l'objet ArbreB.
        """
        if self.racine.lettre == lettre:
            self.racine.valeur = nouvelle_valeur
        elif self.gauche is not None:
            self.gauche.modifier_etiquette_valeur_arbre(lettre, nouvelle_valeur)
        elif self.droite is not None:
            self.droite.modifier_etiquette_valeur_arbre(lettre, nouvelle_valeur)

    def rechercher_element(self, valeur):
        """
        Recherche un objet ArbreB avec une valeur donnée dans l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à rechercher dans l'arbre binaire de recherche.
        :return: L'objet ArbreB trouvé ou None si aucun objet ArbreB avec la valeur donnée n'est trouvé.
        """
        if self.racine.valeur == valeur:
            return self
        elif self.gauche and valeur < self.racine.valeur:
            return self.gauche.rechercher_element(valeur)
        elif self.droite and valeur > self.racine.valeur:
            return self.droite.rechercher_element(valeur)
        else:
            return None

    def fusion(self, autre_arbre):
        """
        Fusionne un autre arbre binaire de recherche avec cet arbre binaire de recherche.
        :param autre_arbre: L'arbre binaire de recherche à fusionner avec cet arbre binaire de recherche.
        """
        if autre_arbre is not None:
            if self.racine is None:
                self.racine = autre_arbre.racine
                self.gauche = autre_arbre.gauche
                self.droite = autre_arbre.droite
            elif autre_arbre.racine.valeur < self.racine.valeur:
                if self.gauche is None:
                    self.gauche = ArbreB(autre_arbre.racine, autre_arbre.gauche, autre_arbre.droite)
                else:
                    self.gauche.fusion(autre_arbre)
            else:
                if self.droite is None:
                    self.droite = ArbreB(autre_arbre.racine, autre_arbre.gauche, autre_arbre.droite)
                else:
                    self.droite.fusion(autre_arbre)

    def decomposition(self):
        """
        Décompose cet arbre binaire de recherche en une liste d'éléments.
        :return: Une liste d'objets Sommet représentant les éléments de l'arbre binaire de recherche.
        """
        elements = []
        if self.gauche is not None:
            elements.extend(self.gauche.decomposition())
        elements.append(self.racine)
        if self.droite is not None:
            elements.extend(self.droite.decomposition())
        return elements

    def __str__(self):
        """
        Surcharge de la méthode str pour afficher l'arbre binaire de recherche.
        :return: Une chaîne de caractères représentant l'arbre binaire de recherche.
        """
        return str([(str(arbre.lettre),str(arbre.valeur)) for arbre in self.decomposition()])

# Question 1.3

def test_arbre_binaire():
    """
    Fonction de test de la classe ArbreB.
    """
    # Définition des sommets de base
    sommet_a = Sommet(1, "A")
    sommet_b = Sommet(2, "B")
    sommet_c = Sommet(3, "C")
    # Création du premier arbre
    arbre1 = ArbreB(sommet_a)
    arbre1 += ArbreB(sommet_b)
    arbre1 += ArbreB(sommet_c)
    # Affichage du premier arbre
    print("Arbre 1 :")
    print(arbre1)
    # Création du deuxième arbre
    arbre2 = ArbreB(Sommet(4, "D"))
    arbre2 += ArbreB(Sommet(5, "E"))
    arbre2 += ArbreB(Sommet(6, "F"))
    # Fusion avec le premier arbre
    arbre1 += arbre2
    # Affichage du premier arbre après fusion
    print("Arbre 1 après fusion :")
    print(arbre1)
    # Suppression d'un élément
    arbre1 -= 3
    # Affichage du premier arbre après fusion et suppression
    print("Arbre 1 après fusion et suppression :")
    print(arbre1)
    # Modification de l'étiquette lettre d'un élément
    arbre1.modifier_etiquette_lettre_arbre('D', 'Z')
    # Affichage du premier arbre après fusion, suppression et modification
    print("Arbre 1 après fusion, suppression et modification :")
    print(arbre1)
    # Modification de l'étiquette valeur d'un élément
    arbre1.modifier_etiquette_valeur_arbre('Z', 7)
    # Affichage du premier arbre après fusion, suppression, modification et modification
    print("Arbre 1 après fusion, suppression, modification et modification :")
    print(arbre1)
    # Recherche d'un élément
    print("Recherche de l'élément 3 :")
    print(arbre1.rechercher_element(2))
    # Recherche d'un élément non présent
    print("Recherche de l'élément 10 :")
    print(arbre1.rechercher_element(10))

# Question 1.4 - Développer une interface graphique pour la représentation de l'arbre binaire de recherche.

# PARTIE 2

# Question 2.1 - Calcule du pourcentage d'occurence de chaque lettre dans un texte.

def occurence(texte):
    """
    Calcule le pourcentage d'occurence de chaque lettre dans un texte.
    :param texte: Le texte à analyser.
    :return: Un dictionnaire contenant les lettres et leur pourcentage d'occurence.
    """
    occurence = dict()
    texte_list = list(texte.lower())
    while " " in texte_list:
        texte_list.remove(" ")
    for lettre in set(texte_list):
        occurence[lettre] = round((texte_list.count(lettre) / len(texte_list)), 2)
    return occurence

# Question 2.2 - Construction d'un arbre binaire de cryptage.

def construire_arbreB_Huffman(texte):
    """ 
    Construit un arbre binaire de cryptage à partir d'un texte. 
    :param texte: Le texte à crypter.
    :return: L'arbre binaire de cryptage.
    """
    # Création de la liste des sommets
    dict_occurence = occurence(texte)
    liste_sommets = []
    for lettre, occ in dict_occurence.items():
        liste_sommets.append(ArbreB(Sommet(occ, lettre)))
    liste_sommets.sort(key=lambda arbre: arbre.get_racine().valeur)
    # Construction de l'arbre de Huffman
    while len(liste_sommets) > 1:
        sommet_1 = min(liste_sommets, key=lambda arbre: arbre.get_racine().valeur)
        liste_sommets.remove(sommet_1)
        sommet_2 = min(liste_sommets, key=lambda arbre: arbre.get_racine().valeur)
        liste_sommets.remove(sommet_2)
        sommet_3 = ArbreB(Sommet(valeur=(sommet_1.get_racine().valeur + sommet_2.get_racine().valeur)),
                          sommet_1, sommet_2)
        liste_sommets.append(sommet_3)
        liste_sommets.sort(key=lambda arbre: arbre.get_racine().valeur)
    return liste_sommets[0]

def test_construire_arbreB_Huffman():
    """
    Fonction de test de la fonction construire_arbreB_Huffman.
    """
    texte = "ProjetPython"
    print("Texte :")
    print(texte)
    print("Occurence des lettres :")
    print(occurence(texte))
    print("Arbre de Huffman :")
    print(construire_arbreB_Huffman(texte))

#test_construire_arbreB_Huffman()

# Question 2.3 - Codification d'un texte en entrée.

def trouver_chemins_feuilles(arbre, chemin):
    """
    Trouve les chemins de toutes les feuilles d'un arbre de Huffman.
    :param arbre: L'arbre de Huffman.
    :param chemin: Le chemin suivi pour arriver au sommet actuel.
    :return: Un dictionnaire contenant les chemins des feuilles de l'arbre de Huffman.
    """
    if arbre is None:
        return {}
    if arbre.gauche is None and arbre.droite is None:
        return {arbre.racine.lettre: chemin}
    chemins = {}
    chemins.update(trouver_chemins_feuilles(arbre.gauche, chemin + [0]))
    chemins.update(trouver_chemins_feuilles(arbre.droite, chemin + [1]))
    return chemins

# Ensuite pour coder un texte, il suffit de parcourir le texte et de remplacer chaque lettre par son chemin dans l'arbre de Huffman.
# Voir plus loin dans le code dans la fonction on_enter() de coder_texte() d'__init__() de la classe GUI.

# PARTIE 3

# Question 3.1 - Vérification de si un texte a été codé selon l'arbre de Huffman.

def verifier_texte_huffman(texte_code, arbre_huffman):
    """
    Vérifie si un texte a été codé selon l'arbre de Huffman.
    Cette fonction ne fonctionne pas correctement.
    :param texte_code: Le texte codé à vérifier.
    :param arbre_huffman: L'arbre de Huffman utilisé pour vérifier le texte.
    :return: True si le texte a été codé selon l'arbre de Huffman, False sinon.
    """
    chemins_feuilles = trouver_chemins_feuilles(arbre_huffman, [])
    chemin_actuel = []
    for caractere in texte_code:
        chemin_actuel.append(int(caractere))
        if chemin_actuel in chemins_feuilles.values():
            chemin_actuel = []
    return len(chemin_actuel) == 0

def test_verifier_texte_huffman():
    """
    Fonction de test de la fonction verifier_texte_huffman.
    """
    texte = "projetpython"
    arbre_huffman = construire_arbreB_Huffman(texte)
    chemins_feuilles = trouver_chemins_feuilles(arbre_huffman, [])
    texte_code = ''.join([str(chiffre) for lettre in texte for chiffre in chemins_feuilles[lettre]])
    texte_code_invalide = "01010101010101"
    # Affichage des résultats
    print("Texte original :", texte)
    print("Texte codé selon Huffman :", texte_code)
    print("Texte invalide :", texte_code_invalide)
    # Vérification des résultats
    print("Vérification du texte codé selon Huffman :", verifier_texte_huffman(texte_code, arbre_huffman))
    print("Vérification du texte invalide :", verifier_texte_huffman(texte_code_invalide, arbre_huffman))

#test_verifier_texte_huffman()

# Question 3.2 - Décodage d'un texte codé selon Huffman.

def decoder_texte_huffman(texte_code, arbre_huffman):
    """
    Décode un texte codé selon Huffman en utilisant l'arbre de Huffman.
    :param texte_code: Le texte codé selon Huffman.
    :param arbre_huffman: L'arbre de Huffman utilisé pour décoder le texte.
    :return: Le texte décodé.
    """
    chemins_feuilles = trouver_chemins_feuilles(arbre_huffman, [])
    texte_decode = ""
    chemin_actuel = []
    for caractere in texte_code:
        chemin_actuel.append(int(caractere))
        for lettre, chemin in chemins_feuilles.items():
            if chemin == chemin_actuel:
                texte_decode += lettre
                chemin_actuel = []
                break
    return texte_decode

def test_decoder_texte_huffman():
    """
    Fonction de test de la fonction decoder_texte_huffman.
    """
    texte = "projetpython"
    arbre_huffman = construire_arbreB_Huffman(texte)
    chemins_feuilles = trouver_chemins_feuilles(arbre_huffman, [])
    texte_code = str(''.join([str(chiffre) for lettre in texte for chiffre in chemins_feuilles[lettre]]))
    texte_decode = decoder_texte_huffman(texte_code, arbre_huffman)
    # Affichage des résultats
    print("Texte original :", texte)
    print("Texte codé selon Huffman :", texte_code)
    print("Texte décodé :", texte_decode)

#test_decoder_texte_huffman()

# Question 3.3 - Affichage du GUI.

import tkinter as tk

class CanvasArbreHuffman(tk.Canvas):
    def __init__(self, master, arbre, *args, **kwargs):
        """
        Initialise le canvas de l'arbre de Huffman.
        :param master: La fenêtre parente.
        :param arbre: L'arbre de Huffman à afficher.
        """
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.arbre = arbre
        self.width = 1000
        self.height = 375
        self.diametre_cercle = 80
        self.espacement_horiz = 8
        self.espacement_vert = 50
        self.positions = {} # Dictionnaire des positions des noeuds de l'arbre de Huffman.

    def afficher(self):
        """
        Affiche l'arbre de Huffman.
        """
        self.delete(tk.ALL) # Efface le canvas.
        self.positions.clear() # Efface le dictionnaire des positions.
        self._afficher_sous_arbre(self.arbre, self.width / 2, 10, self.width / 4)
    
    def _afficher_sous_arbre(self, arbre, x, y, h):
        """
        Affiche un sous-arbre de l'arbre de Huffman.
        :param arbre: Le sous-arbre à afficher.
        :param x: La position horizontale du sous-arbre.
        :param y: La position verticale du sous-arbre.
        :param h: L'espacement horizontal entre les sous-arbres.
        :return: La position du sous-arbre.
        """
        offset = 17 # Décalage des arêtes reliant les noeuds.
        if arbre is not None: # Si le sous-arbre n'est pas vide.
            gauche = self._afficher_sous_arbre(arbre.gauche, x - h, y + self.espacement_vert, h / 2)
            droite = self._afficher_sous_arbre(arbre.droite, x + h, y + self.espacement_vert, h / 2)
            texte = self.create_text(x, y + self.diametre_cercle / 2, text=("{:.0%}".format(arbre.racine.valeur)))
            if arbre.racine.lettre is not None: # Si le noeud est une feuille (si le noeud possède une lettre)).
                texte = self.create_text(x, y + self.diametre_cercle / 2 + 15, text=arbre.racine.lettre)
            self.positions[arbre] = (x, y, texte) # Ajoute la position du noeud dans le dictionnaire des positions.
            if gauche is not None: # Si le sous-arbre gauche n'est pas vide.
                # Calcul de l'angle de l'arête reliant les noeuds gauche et droit du sous-arbre courant (en radians) (voir https://docs.python.org/3/library/math.html#math.atan2).
                angle = atan2(gauche[1] - y - self.diametre_cercle / 2, gauche[0] - x)
                x1 = x + offset * cos(angle) # Calcul de la position horizontale du point de départ de l'arête.
                y1 = y + self.diametre_cercle / 2 + offset * sin(angle) # Calcul de la position verticale du point de départ de l'arête.
                x2 = gauche[0] - offset * cos(angle) # Calcul de la position horizontale du point d'arrivée de l'arête.
                y2 = gauche[1] + self.diametre_cercle / 2 - offset * sin(angle) # Calcul de la position verticale du point d'arrivée de l'arête.
                self.create_line(x1, y1, x2, y2, width=2) # Création de l'arête.
            if droite is not None: # Si le sous-arbre droit n'est pas vide.
                # Calcul de l'angle de l'arête reliant les noeuds gauche et droit du sous-arbre courant (en radians) (voir https://docs.python.org/3/library/math.html#math.atan2).
                angle = atan2(droite[1] - y - self.diametre_cercle / 2, droite[0] - x)
                x1 = x + offset * cos(angle) # Calcul de la position horizontale du point de départ de l'arête.
                y1 = y + self.diametre_cercle / 2 + offset * sin(angle) # Calcul de la position verticale du point de départ de l'arête.
                x2 = droite[0] - offset * cos(angle) # Calcul de la position horizontale du point d'arrivée de l'arête.
                y2 = droite[1] + self.diametre_cercle / 2 - offset * sin(angle) # Calcul de la position verticale du point d'arrivée de l'arête.
                self.create_line(x1, y1, x2, y2, width=2) # Création de l'arête.
            return x, y # Retourne la position du sous-arbre.
        else: # Si le sous-arbre est vide.
            return None # Retourne None.


class GUI(tk.Tk): # Classe de la fenêtre principale de l'application (voir https://docs.python.org/3/library/tkinter.html#tkinter.Tk).
    def __init__(self):
        """
        Initialise la fenêtre principale.
        """
        super().__init__()
        self.title("Codage de Huffman")
        self.geometry("1000x750")
        self.resizable(width=False, height=False)

        # Définition des variables globales
        texte_a_coder = ""
        arbre_a_representer = None
        texte_code = ""
        texte_a_decoder = ""
        texte_decode = ""

        # Définition des fonctions des boutons
        def coder_texte():
            """
            Fonction du bouton "Coder texte".
            """
            fenetre_coder = tk.Toplevel(width=500, height=225) # Création de la fenêtre de codage de texte.
            fenetre_coder.title("Coder texte")
            fenetre_coder.resizable(width=False, height=False)

            label_texte_a_coder = tk.Label(fenetre_coder, text="Texte à coder avec le codage de Huffman :")
            label_texte_a_coder.place(x=125*2, y=75, width=125*4-10, height=75-10, anchor="center")
            
            entry_texte_a_coder = tk.Entry(fenetre_coder)
            entry_texte_a_coder.place(x=125*2, y=75*2, width=125*4-10, height=75, anchor="center")
            
            def on_enter(event):
                """
                Fonction de la touche "Entrée".
                """
                nonlocal texte_a_coder, arbre_a_representer, texte_code
                texte_a_coder = entry_texte_a_coder.get()
                # Normalisation du texte à coder (suppression des espaces et des majuscules).
                texte_a_coder_normalise = list(texte_a_coder.lower())
                while " " in texte_a_coder_normalise:
                    texte_a_coder_normalise.remove(" ")
                fenetre_coder.destroy() # Fermeture de la fenêtre de codage de texte.
                arbre_a_representer = construire_arbreB_Huffman(str(texte_a_coder))
                chemins_feuilles = trouver_chemins_feuilles(arbre_a_representer, [])
                texte_code = ''.join([str(chiffre) for lettre in texte_a_coder_normalise for chiffre in chemins_feuilles[lettre]])
                self.canvas_arbre_huffman = CanvasArbreHuffman(self, arbre_a_representer) # Création du canvas de l'arbre de Huffman.
                self.canvas_arbre_huffman.afficher() # Affichage de l'arbre de Huffman.
                self.canvas_arbre_huffman.place(x=125*4, y=75*4.5, width=125*8-10, height=75*5-10, anchor="center") # Placement du canvas de l'arbre de Huffman.
            
            entry_texte_a_coder.bind("<Return>", on_enter) # Association de la touche "Entrée" à la fonction on_enter.
            fenetre_coder.wait_window(fenetre_coder) # Attente de la fermeture de la fenêtre de codage de texte.
            
            self.label_texte_a_coder.configure(text=f"Texte à coder : «{texte_a_coder}»") # Affichage du texte à coder.
            self.label_texte_code.configure(text=f"Texte codé : «{texte_code}»") # Affichage du texte codé.

        def decoder_texte():
            """
            Fonction du bouton "Décoder texte".
            """
            fenetre_decoder = tk.Toplevel(width=500, height=225) # Création de la fenêtre de décodage de texte.
            fenetre_decoder.title("Décoder texte")
            fenetre_decoder.resizable(width=False, height=False)
            
            label_texte_a_decoder = tk.Label(fenetre_decoder, text="Texte à décoder avec le codage de Huffman :")
            label_texte_a_decoder.place(x=125*2, y=75, width=125*4-10, height=75-10, anchor="center")
            
            entry_texte_a_decoder = tk.Entry(fenetre_decoder)
            entry_texte_a_decoder.place(x=125*2, y=75*2, width=125*4-10, height=75, anchor="center")

            def on_enter(event):
                """
                Fonction de la touche "Entrée".
                """
                nonlocal texte_a_decoder, texte_decode
                texte_a_decoder = entry_texte_a_decoder.get()
                texte_decode = decoder_texte_huffman(texte_a_decoder, arbre_a_representer)
                fenetre_decoder.destroy()
            
            entry_texte_a_decoder.bind("<Return>", on_enter)
            fenetre_decoder.wait_window(fenetre_decoder)
            
            self.label_texte_a_decoder.configure(text=f"Texte à décoder : «{texte_a_decoder}»")
            self.label_texte_decode.configure(text=f"Texte décodé : «{texte_decode}»")

        # Création des widgets
        self.bouton_coder_texte = tk.Button(self, text="Coder texte", command=coder_texte)
        self.label_texte_a_coder = tk.Label(self, text=f"Texte à coder : «{texte_a_coder}»")


        self.label_arbre_huffman = tk.Label(self, text="Arbre de Huffman du texte à coder :", anchor="w", justify="left")
        self.label_texte_code = tk.Label(self, text=f"Texte codé : {2+2}", anchor="w", justify="left")
        
        self.bouton_decoder_texte = tk.Button(self, text="Décoder texte", command=decoder_texte)
        self.label_texte_a_decoder = tk.Label(self, text=f"Texte à décoder : {2+2}")
        
        self.label_texte_decode = tk.Label(self, text=f"Texte décodé : {2+2}")

        # Création des lignes
        self.frame_ligne_1 = tk.Frame(self, width=1, height=75, bg="black")
        self.frame_ligne_2 = tk.Frame(self, width=1000, height=1, bg="black")
        self.frame_ligne_3 = tk.Frame(self, width=1000, height=1, bg="black")
        self.frame_ligne_4 = tk.Frame(self, width=1, height=75, bg="black")
        self.frame_ligne_5 = tk.Frame(self, width=1000, height=1, bg="black")

        # Placement des lignes
        self.frame_ligne_1.place(x=125*2, y=0, width=1, height=75, anchor="nw")
        self.frame_ligne_2.place(x=0, y=75, width=1000, height=1, anchor="nw")
        self.frame_ligne_3.place(x=0, y=75*8, width=1000, height=1, anchor="nw")
        self.frame_ligne_4.place(x=125*2, y=75*8, width=1, height=75, anchor="nw")
        self.frame_ligne_5.place(x=0, y=75*9, width=1000, height=1, anchor="nw")

        # Placement des widgets
        self.bouton_coder_texte.place(x=125, y=75/2, width=125*2-10, height=75-10, anchor="center")
        self.label_texte_a_coder.place(x=125*5, y=75/2, width=125*6-10, height=75-10, anchor="center")
        
        self.label_arbre_huffman.place(x=125*4, y=75+75/2, width=125*8-10, height=75-10, anchor="center")
        
        self.label_texte_code.place(x=125*4, y=75*7+75/2, width=125*8-10, height=75-10, anchor="center")
        
        self.bouton_decoder_texte.place(x=125, y=75*8+75/2, width=125*2-10, height=75-10, anchor="center")
        self.label_texte_a_decoder.place(x=125*5, y=75*8+75/2, width=125*6-10, height=75-10, anchor="center")
        self.label_texte_decode.place(x=125*4, y=75*9+75/2, width=125*8-10, height=75-10, anchor="center")

interface_graphique = GUI()
interface_graphique.mainloop()
