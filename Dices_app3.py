import random

des_de_lettres = ["ATUKNO"  ,  "EVGTIN"  ,  "DOCAMP" , "IELRSW" ,
                  "EHIFSE"  ,  "RMCALS"  ,  "ENTDOS" , "UFXRIA" ,
                  "NAVODZ"  ,  "EIOATA"  ,  "GLVNYU" , "BMAQJO" ,
                  "ELIBRA"  ,  "SPULTI"  ,  "TIMSOR" , "ENHRIU"]


#Creation d'une séquence aléatoire
def createRandomSeq(seq):
   """
   Renvoie une séquence répétée avec début aléatoire à partir
   d'une séquence donnée.
   
   liste (list/str) -> séquence à mélanger
   
   """
   random_chain = ""  
   random_start_char = random.choice(seq) #Début de la séquence
   
   #On boucle sur la séquence en partant de 'random_start_char'
   for c in range(seq.index(random_start_char)   ,   seq.index(random_start_char) + 27):
      random_chain += seq[c%len(seq)]
   
   return random_chain