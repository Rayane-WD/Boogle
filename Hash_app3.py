import unicodedata

base_de_donnees_mots_fr = []
table_de_hache = {}
tableau_des_collisions = []

def uniformizeWord(mot):
   """
   Renvoie un mot en majuscule et sans accents

   mot (str) -> mot à uniformiser
   """
   return unicodedata.normalize("NFKD", mot.rstrip()).encode("ASCII", "ignore").upper().decode("ASCII")



def initializeWordsDataBase(file = "liste_mots_fr.txt"):
   """
   Initialise la base de données en prenant les mots d'un fichier.
   Retourne une liste contenant les mots d'un fichier (uniformisés).

   file (str) -> nom du fichier
   """
#   t = 0
   liste_de_mots = []
   dernier_mot_enregistrer = ''

   #On parcourt le fichier
   with open (file, "r", encoding="utf-8") as f :
      for mot in f.readlines():
         mot = uniformizeWord(mot)

         #On garde tout mot superieur à 3 lettres (on enlève aussi les doublons)
         if len(mot) >= 3 and mot != dernier_mot_enregistrer:
            liste_de_mots.append(mot)
            dernier_mot_enregistrer = mot
#            t+=1

#         if t==300000:
#            break

   return liste_de_mots


def hashFunction(mot, add = False):
   """
   Assigne un mot à une table de hache (si add = True).
   Renvoie le nombre (valeur_du_hachage) d'un mot

   mot (str) -> mot à hacher
   """
   global table_de_hache, tableau_des_collisions

   #On hache || n sert à éviter la collision entre anagrammes
   valeur_du_hachage = 0
   for n,l in enumerate(mot) :
      valeur_du_hachage += (len(mot) - n )*ord(l)
   valeur_du_hachage %= len(base_de_donnees_mots_fr)

   #On met à jour le nombre de collision pour cette valeur
   if add :
      # nombre de collisions : 9341
      # nombre de collisions max mesuré pour une seule valeur : 205
      tableau_des_collisions[valeur_du_hachage] += 1
#      if tableau_des_collisions[valeur_du_hachage]>1 and valeur_du_hachage not in test : test.append(valeur_du_hachage)

      #On assigne à la table de hash sa clef
      try : table_de_hache[valeur_du_hachage].append(mot)
      except KeyError : table_de_hache[valeur_du_hachage] = [mot]

   return valeur_du_hachage


def isWord(mot):
   """
   Renvoie True si le mot est francais, false sinon.

   mot (str) -> mot dont on determine l'existence
   """

   try :
      mot in table_de_hache[hashFunction(mot)]
      return mot in table_de_hache[hashFunction(mot)]
   except KeyError : return False

   return False

def initializeHashTable():
   global tableau_des_collisions, base_de_donnees_mots_fr
   #test=[]
   base_de_donnees_mots_fr = initializeWordsDataBase()
   tableau_des_collisions = [0 for k in range(len(base_de_donnees_mots_fr))]

   for mot in base_de_donnees_mots_fr:
      hashFunction(mot, True)

initializeHashTable()












