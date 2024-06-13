import turtle
import random

t = turtle.Turtle()
t.speed("fast")

class pile:
  def __init__(self):
    self.valeurs=[]
  def empiler(self,valeur):
    self.valeurs.append(valeur)
  def depiler(self):
    if self.valeurs:
      return self.valeurs.pop()
  def estVide(self):
    return self.valeurs==[]
  def taille(self):
    return len(self.valeurs)
  def lireSommet(self):
    return self.valeurs[-1]
  def dessine(self,num) : #méthode avec le nombre de tour à dessiner
    dessine_bloc(num)
    y=0
    for x in self.valeurs:#desine les anneaux rouges
      t.goto(-193+150*num,10*(y+1)+10)
      t.forward(32)
      t.backward(x*4/2)
      t.pendown()
      t.color('red')
      y=y+1
      for i in range(2) :
        t.forward(x*4)
        t.left(90)
        t.forward(10)
        t.left(90)
      t.penup()
  def __str__(self):

    ch=""
    for x in self.valeurs:

      ch="/\t"+str(x)+"\t/"+"\n"+ch
    ch="\nEtat de la pile:\n"+ ch
    return ch

#dessine une tour
def dessine_bloc(num):
  t.penup()
  t.goto(-200+150*num,0)
  t.pendown()
  t.color('black')
  t.begin_fill()
  for i in range(2) :
    t.forward(80)
    t.left(90)
    t.forward(20)
    t.left(90)
  t.end_fill()
  t.forward(34)
  t.left(90)
  t.forward(10)
  for i in range(2) :
    t.forward(85)
    t.right(90)
    t.forward(10)
    t.right(90)
  t.right(90)

tab=[]#crée les differentes tour avec l'aleatoire
tab_verif=[]#tour de reference pour la fin du jeu
ma_pile=[] #pile de jeu

def inittour (nbr_piles) :
  for i in range(nbr_piles): #crée le nombre de piles demandées et les ajoute au tableau "ma_pile".
    ma_pile.append(pile())

#nombre d'anneaux par tour
def initanneaux(nbranneaux,nbr_piles) :
    for i in range(nbranneaux):
      tab.append((i+1)*5) 
      tab_verif.append((i+1)*5)
      tab_verif.reverse()
    random.shuffle(tab)  
    if nbr_piles==3:
      for i in range(nbranneaux):
        ma_pile[0].empiler(tab[i])
      random.shuffle(tab)
      for i in range(nbranneaux):
        ma_pile[1].empiler(tab[i])
    if nbr_piles==4:      
      for i in range(nbranneaux):
        ma_pile[0].empiler(tab[i])
      random.shuffle(tab)
      for i in range(nbranneaux):
        ma_pile[1].empiler(tab[i])
      random.shuffle(tab)
      for i in range(nbranneaux):
        ma_pile[2].empiler(tab[i])

#permet de dessiner les elements
def visualiser (nombre):
  t.clear()
  for i in range(nombre) :
    ma_pile[i].dessine(i)


# pour demander le nombre d'anneaux de départ
def input_nbr_anneaux():
  Pass=False
  while not (Pass) :
    
    r=input('Combien d anneaux voulez vous ? ')
    try :
      nombre=int(r)
    except :
      print('vous devez rentrer un nombre')
    else :
      if nombre>1 and nombre <8 :
        Pass=True
        return nombre
      else :
        print("vous devez rentrer un chiffre entre 2 et 7")


# pour demander le nombre de tour, 
def demande_entre(max,min,text) :
  Pass=False
  while not (Pass) :
    
    r=input(text)
    try :
      nombre=int(r)
    except :
      print('vous devez rentrer un nombre')
    else :
      if nombre>min and nombre <max :
        Pass=True
        return nombre
      else :
        print("vous devez rentrer une valeur entre " + str(min+1) +" et " + str(max-1) )

#permet de jouer, donc demande sur quel tour il doit transposer les anneaux et termine le jeu quand il le faut
def jeu(nbr_piles,nbranneaux):
  w=0
  score=0
  if nbr_piles==3:
    while not ((ma_pile[0].valeurs==tab_verif) and (ma_pile[1].valeurs==tab_verif)):
      x=demande_entre(nbr_piles+1,0,"De quelle tour voulez vous prendre l anneau")#pile de laquelle on prend l'anneau
      y=demande_entre(nbr_piles+1,0,"Sur quelle tour voulez vous deposer l anneau")#pile sur laquelle on pose l'anneau
      if ma_pile[x-1].taille() == 0: #on verifie que la pile de depart n'est pas vide
        print("La pile de depart est vide")
      elif ma_pile[y-1].taille()<nbranneaux:
        w=ma_pile[x-1].depiler()
        ma_pile[y-1].empiler(w)
        visualiser(nbr_piles)
        score+=1
      else:
        print("Il y a deja trop d anneaux sur cette tour")
    print ('Felicitation vous avez reussi le jeu en', score ,'coups')  
    fin()  
  if nbr_piles==4:  
    while not ((ma_pile[0].valeurs==tab_verif) and (ma_pile[1].valeurs==tab_verif) and (ma_pile[2].valeurs==tab_verif)):
      x=demande_entre(nbr_piles+1,0,"De quelle tour voulez vous prendre l anneau")
      y=demande_entre(nbr_piles+1,0,"Sur quelle tour voulez vous deposer l anneau")
      if ma_pile[y-1].taille()<nbranneaux:
        w=ma_pile[x-1].depiler()
        ma_pile[y-1].empiler(w)
        visualiser(nbr_piles)
        score+=1
      else:
        print("Il y a deja trop d anneaux sur cette tour")
    print('Felicitation vous avez reussi le jeu en', score ,'coups')
    fin()

#permet de rejouer
def fin():
  rep=input('Voulez vous rejouer ? (o/n)')
  if rep=="o":
    partie()

#demarre completement une partie de 0
def partie():
  t.clear()#reinitialisation
  del tab[:]#reinitialisation
  del tab_verif[:]#reinitialisation
  del ma_pile[:]#reinitialisation
  inputtour=demande_entre(5,2,'Combien de tours voulez vous ?')
  inputanneaux=input_nbr_anneaux()
  inittour(inputtour)
  initanneaux(inputanneaux,inputtour)
  visualiser(inputtour)
  jeu(inputtour,inputanneaux)

partie()
