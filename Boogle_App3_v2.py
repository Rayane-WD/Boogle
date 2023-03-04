import random
from sys import exit, argv
import Hash_app3 as h
import Dices_app3 as d
import Texte_app3 as t
import Colors_app3 as c
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout,
                             QToolBar, QAction, QMessageBox, QLabel, QHBoxLayout, QCheckBox, QLineEdit)
from PyQt5.QtCore import QCoreApplication, QSize, Qt, QTimer, QEventLoop
from PyQt5.QtGui import QIcon, QKeySequence




# =============================================================================
# MainWindow
# =============================================================================

class MainWindow(QMainWindow):

   def __init__(self):

      super().__init__()

      #Fenetre
      self.initUi()

      #On crée une toolbar
      self.myToolbar = QToolBar("Afficher la toolbar")
      self.myToolbar.setIconSize(QSize(16,16))
      self.addToolBar(self.myToolbar)

      # Action 'Comment jouer ?'
      self.action_cmt_jouer = QAction(QIcon("assets/book-question.png"),"Comment jouer ?", self)
      self.action_cmt_jouer.setShortcut(QKeySequence("Ctrl+H"))
      self.action_cmt_jouer.triggered.connect(self.onClickHowToPlay)
      self.myToolbar.addAction(self.action_cmt_jouer)

      # Action 'Qui sommes nous ?'
      self.action_qui_sm_ns = QAction(QIcon("assets/information-italic.png"),"Qui sommes nous ?", self)
      self.action_qui_sm_ns.setShortcut(QKeySequence("Ctrl+I"))
      self.action_qui_sm_ns.triggered.connect(self.onClickWhoAreWe)
      self.myToolbar.addAction(self.action_qui_sm_ns)

      #On commence sur la page de garde
      self.startCoverPage()



   def initUi(self):
      self.setWindowTitle('Woodle')
      self.setStyleSheet(f"background-color : {c.couleur_du_background}")
      self.setFixedSize(1500,850)

   def onClickHowToPlay(self):
      popup = QMessageBox(QMessageBox.Information, "Comment jouer", t.texte_regles_du_jeu)
      popup.exec()

   def onClickWhoAreWe(self):
      popup = QMessageBox(QMessageBox.Information, "Qui sommes nous ?", t.texte_qui_sommes_nous)
      popup.exec()

   def startCoverPage(self):
      #On initialise la page
      self.cover_page = CoverPage()
      #On l'applique
      self.setCentralWidget(self.cover_page)
      #On initialise le bouton qui permettra de changer de page
      self.cover_page.bouton_start_game.clicked.connect(self.startDicePageFromCover)

   def startDicePageFromCover(self):
      #On initialise la page
      self.dice_page = DicePage()
      #On l'applique
      self.setCentralWidget(self.dice_page)
      #On initialise le bouton qui permettra de changer de page
      self.dice_page.bouton_letsgo.clicked.connect(self.startGamePage)

   def startDicePageFromGame(self):
      #On initialise la page
      self.dice_page = DicePage()
      #On l'applique
      self.setCentralWidget(self.dice_page)
      #On initialise le bouton qui permettra de changer de page
      self.dice_page.bouton_letsgo.clicked.connect(self.startGamePage)

   def startGamePage(self):
      #On initialise la page
      self.game_page = GamePage(self.dice_page.available_letters)
      #On l'applique
      self.setCentralWidget(self.game_page)
      #On initialise le bouton qui permettra de changer de page
      self.game_page.bouton_rejouer.clicked.connect(self.startDicePageFromGame)
      #On initialise la boite de dialogue de fin



# =============================================================================
# Cover Page
# =============================================================================

class CoverPage(QWidget):
   def __init__(self):
      super().__init__()

      #Label de bienvenue
      welcome_phrase = QLabel(self)
      welcome_phrase.setStyleSheet('color : #03558c; font-size : 50px ; font-stlye : bold')
      welcome_phrase.setAlignment(Qt.AlignCenter)
      welcome_phrase.setText("Bienvenue sur Woodle")

      #Bouton pour commencer une partie
      self.bouton_start_game = QPushButton(" Commencer à jouer ")
      self.bouton_start_game.setStyleSheet(f"background-color : {c.couleur_boutons_utiles}; font-size : 60px; border-radius: 50px ; padding : 10px; border-style: solid; border-width:1px;max-width:100px;max-height:100px;min-width:600px;min-height:100px;")


      #On crée un layout vertical
      self.myVerticalLayout = QVBoxLayout()
      self.myVerticalLayout.setAlignment(Qt.AlignCenter)
      self.myVerticalLayout.setSpacing(150)
      self.myVerticalLayout.addWidget(welcome_phrase)
      self.myVerticalLayout.addWidget(self.bouton_start_game)

      #On ajoute le layout au widget
      self.setLayout(self.myVerticalLayout)




# =============================================================================
# Dice Page
# =============================================================================

class DicePage(QWidget):
   def __init__(self):
      super().__init__()

      #Bouton pour lancer les dés
      self.bouton_dices = QPushButton("Lancer les dés")
      self.bouton_dices.setStyleSheet(f"background-color : {c.couleur_boutons_utiles}; font-size : 40px; border-radius: 10px ; padding : 10px")
      self.bouton_dices.clicked.connect(self.onClickDices)
      self.bouton_dices.setEnabled(True)

      #Check box pour animation
      self.checkbox_animation = QCheckBox("Animations")
      self.checkbox_animation.setCheckState(2)

      #On crée un vertical layout
      self.myVertiLayout_left = QVBoxLayout()
      self.myVertiLayout_left.setAlignment(Qt.AlignCenter)
      self.myVertiLayout_left.setSpacing(5)
      self.myVertiLayout_left.addWidget(self.bouton_dices)
      self.myVertiLayout_left.addWidget(self.checkbox_animation)


      #On crée un layout grille
      self.myGridLayout_dices = QGridLayout()
      self.myGridLayout_dices.setSpacing(0)

      #Création et affichage des cases de dés
      self.cases_dices = []
      side_length = 150
      for height in range(4):
         for length in range(4):

            case = QLabel("")
            case.setAlignment(Qt.AlignCenter)
            case.setFixedWidth(side_length)
            case.setFixedHeight(side_length)
            case.setStyleSheet(f"background-color : {c.couleur_boutons_de_jeu}; font-size : 40px; border: 1px solid black")
            self.cases_dices.append(case)

            self.myGridLayout_dices.addWidget(case,height,length)


      #Bouton pour commencer la partie
      self.bouton_letsgo = QPushButton("Let's Go !")
      self.bouton_letsgo.setStyleSheet(f"background-color : {c.couleur_boutons_utiles}; font-size : 40px; border-radius: 10px ; padding : 10px")
      self.bouton_letsgo.setEnabled(False)


      #On crée un horizontal layout
      self.myHorizLayout_right = QHBoxLayout()
      self.myHorizLayout_right.addWidget(self.bouton_letsgo)


      #On crée un layout horizontal (le main)
      self.myVerticalLayout = QHBoxLayout()
      self.myVerticalLayout.setAlignment(Qt.AlignCenter)
      self.myVerticalLayout.setSpacing(60)

      self.myVerticalLayout.addLayout(self.myVertiLayout_left)
      self.myVerticalLayout.addLayout(self.myGridLayout_dices)
      self.myVerticalLayout.addLayout(self.myHorizLayout_right)


      #On ajoute le layout au widget
      self.setLayout(self.myVerticalLayout)

   def onClickDices(self):
      self.bouton_dices.setEnabled(False)
      self.throwDices()

   def throwDices(self):

      #Avec animations
      if self.checkbox_animation.checkState() :

         #On crée des séquences de dés aléatoires
         sequences_de_des = [d.createRandomSeq(sek) for sek in d.des_de_lettres]

         #On les affiche avec une animation à 'suspense'
         for k in range (0,15,4):

            sequences_de_4 = sequences_de_des[k:k+4]
            case = k
            time_paused = 50
            pause(300)

            for lettre in range(len(sequences_de_4[0])-1):
               case = k
               #On affiche une lettre dans 4 cases différentes
               for seq in sequences_de_4:
                  self.cases_dices[case].setText(seq[lettre])
                  case += 1

               #On s'arrête
               pause(time_paused)
               #On actualise le temps de pause suivant
               if time_paused < 120 : slow = 5
               elif time_paused < 200 : slow = 10
               else : slow = 20
               time_paused += slow


      #Sans animations
      else :
         c = [n for n in range(16)]
         random.shuffle(c)
         for k in c:
            self.cases_dices[k].setText(random.choice(d.des_de_lettres[k]))
            pause(250)

      #On récupère les lettres des cases
      self.available_letters = [case.text() for case in self.cases_dices]
      #On peut cliquer sur 'Lets'go'
      self.bouton_letsgo.setEnabled(True)



# =============================================================================
# Game Page
# =============================================================================

class GamePage(QWidget):
   def __init__(self, lettres_dispos):
      super().__init__()

      #Liste des boutons déjà utilisés
      self.buttons_already_used = []
      #Liste des mots déjà trouvés
      self.liste_mots_trouves = []

      #On recrée un grid layout
      self.myGL_btn_game = QGridLayout()
      self.myGL_btn_game.setSpacing(0)

      #Création et affichage des cases de dés avec des boutons cette fois
      side_length = 150
      n = 0
      self.buttons_in_grid = []
      for height in range(4):
         for length in range(4):

            button = QPushButton(lettres_dispos[n])
            n += 1

            button.clicked.connect(self.onClickLetter)
            button.setFixedSize(side_length, side_length)
            button.setStyleSheet(f"background-color : {c.couleur_boutons_de_jeu}; font-size : 40px")
            self.myGL_btn_game.addWidget(button,height,length)
            self.buttons_in_grid.append(button)


      #On crée le timer
      self.myTimer = QTimer()
      self.myTimer.start(1000) #on met le timer à jour toutes les 1 seconde
      self.myTimer.timeout.connect(self.showTime) #toutes les secondes cette méthode est appelée
      self.count = 120 #le compte à rebours commence à self.count secondes

      self.label_time = QLabel("Temps restant - 00:00")
      self.label_time.setStyleSheet("font-size : 30px ; border : 2px solid red ; border-radius: 10px")
      self.label_time.setAlignment(Qt.AlignCenter)

      #On crée le compteur de points
      self.score = 1
      self.label_points = QLabel("Score : 0000")
      self.label_points.setStyleSheet("font-size : 30px")

      #On crée la line edit
      self.lineEdit = QLineEdit()
      self.lineEdit.setTextMargins(0,10,0,10)
      self.lineEdit.setMaxLength(16)
      self.lineEdit.setReadOnly(True)
      self.lineEdit.setStyleSheet("font-size : 30px ; background-color : white ; color : black")


      #On crée le bouton de validation
      self.bouton_validation = QPushButton("Valider")
      self.bouton_validation.clicked.connect(self.onClickValider)
      self.bouton_validation.setStyleSheet("background-color : #52cf43; font-size : 40px;border-radius: 10px ; padding : 10px")
      self.bouton_validation.setFixedSize(300, 60)

      #On crée le bouton de supression du texte situé dans la line edit
      self.bouton_supression = QPushButton("Supprimer")
      self.bouton_supression.clicked.connect(self.onClickSupprimer)
      self.bouton_supression.setStyleSheet("background-color : #fa5f5f; font-size : 40px;border-radius: 10px ; padding : 10px")
      self.bouton_supression.setFixedSize(300, 60)

      #On crée un horiz layout pour les boutons valid et supr
      self.myHL_valsup_game = QHBoxLayout()
      self.myHL_valsup_game.addWidget(self.bouton_validation)
      self.myHL_valsup_game.addWidget(self.bouton_supression)

      #On crée le bouton rejouer
      self.bouton_rejouer = QPushButton("Rejouer")
      self.bouton_rejouer.setStyleSheet(f"background-color : {c.couleur_boutons_utiles}; font-size : 40px;border-radius: 10px ; padding : 10px")
      self.bouton_rejouer.setFixedSize(300, 60)

      #On crée un horiz layout pour le bouton rejouer
      self.myHL_rejouer_game = QHBoxLayout()
      self.myHL_rejouer_game.addWidget(self.bouton_rejouer)


      #On crée le label d'information
      self.label_info = QLabel("C'est parti ! Clique sur les bonnes lettres et valide ton choix.")
      self.label_info.setStyleSheet("font :italic 30px ; font-stlye : bold")
      self.label_info.setAlignment(Qt.AlignCenter)

      #On crée le label d'affichage des mots déjà trouvés
      self.label_mots_trouves = QLabel("")
      self.label_mots_trouves.setStyleSheet("font-size : 20px ; border : 2px solid blue ; border-radius: 10px")
      self.label_mots_trouves.setAlignment(Qt.AlignTop)
      self.label_mots_trouves.setWordWrap(True)


      #On crée un vertical layout
      self.myVL_side_game = QVBoxLayout()
      self.myVL_side_game.setSpacing(0)
      self.myVL_side_game.addWidget(self.label_time)
      self.myVL_side_game.addWidget(self.label_points)
      self.myVL_side_game.addWidget(self.lineEdit)
      self.myVL_side_game.addLayout(self.myHL_valsup_game)
      self.myVL_side_game.addLayout(self.myHL_rejouer_game)
      self.myVL_side_game.addWidget(self.label_info)
      self.myVL_side_game.addWidget(self.label_mots_trouves)

      #On crée un vL por le gL (voila pk qt = caca)
      self.vl2 = QVBoxLayout()
      self.vl2.addLayout(self.myGL_btn_game)

      #On crée un horizontal layout (le main)
      self.myHL_main_game = QHBoxLayout()
      self.myHL_main_game.setAlignment(Qt.AlignLeft)
      self.myHL_main_game.setSpacing(70)

      self.myHL_main_game.addLayout(self.vl2)
      self.myHL_main_game.addLayout(self.myVL_side_game)

      #On ajoute le layout au widget
      self.setLayout(self.myHL_main_game)




   def showTime(self):
      text_time = f"Temps restant - {self.count//60:02d} : {self.count%60:02d}"
      self.label_time.setText(text_time)
      self.count -= 30

      if self.count < 0 :
         self.label_info.setText("Temps écoulé !")
         self.myTimer.stop()

         #On affiche une fenêtre popup avec le score
         self.dialog_endgame = DialogEndGame(f"Score : {self.score}\n{t.txtScore(self.score)}")
         choix = self.dialog_endgame.exec()

         #Rejouer une autre partie
         if choix == QMessageBox.AcceptRole : self.bouton_rejouer.click()

         #Quitter le jeu
         elif choix == QMessageBox.DestructiveRole : exit(0)

         #Continuer sur la même partie
         else : pass


   def onClickLetter(self):

      #On ajoute la lettre dans la lineEdit
      letter = self.sender().text()
      self.lineEdit.insert(letter)

      #On ajoute le bouton dans la liste des utilisés, le bloque et le change de couleur
      self.buttons_already_used.append(self.sender())
      self.sender().setEnabled(False)
      self.sender().setStyleSheet("QPushButton:disabled { background-color: #5e8897; font-size : 40px ; color :#1a2d34}")

      #On active tout les boutons de la grille, sauf ceux déjà utilisés
      for b in self.buttons_in_grid :
         if b not in self.buttons_already_used :
            b.setEnabled(True)


      #On désactive tout bouton qui ne colle pas celui tapé
      btns_a_desactiver = self.findBtnNotAround(self.sender())
      for b in btns_a_desactiver : b.setEnabled(False)

   def onClickValider(self):
      word_typed = self.lineEdit.text()
      #On vérifie si le mot dans la line Edit existe
      if h.isWord(word_typed) and word_typed not in self.liste_mots_trouves:
         #On acctualise le score en conséquence
         self.addScore(word_typed)
         #On ajoute le mot à la liste des trouvés
         self.liste_mots_trouves.append(word_typed)
         #On informe le joueur
         self.label_info.setText(random.choice(t.texte_positif))
         self.label_mots_trouves.setText(self.label_mots_trouves.text() + word_typed + ", ")

      else :
         self.label_info.setText(random.choice(t.texte_negatif))

      self.setNewTry()


   def onClickSupprimer(self):
      self.setNewTry()


   def findBtnNotAround(self, btn_clicked):

      #On récupère sa position
      idx_btn_clicked = self.myGL_btn_game.indexOf(btn_clicked)
      pos_btn_clicked = self.myGL_btn_game.getItemPosition(idx_btn_clicked)

      #On retrouve les items qui collent le bouton cliqué
      pos_btns_around = []
      for ligne in range(-1,2):
         for colone in range(-1,2):
            pos_btns_around.append( (pos_btn_clicked[0] + ligne , pos_btn_clicked[1] + colone) )


      items_around = [self.myGL_btn_game.itemAtPosition(b[0], b[1]) for b in pos_btns_around
                      if b[0]>=0 and b[1]>=0 and b[0]<=15 and b[1]<=15 ]

      #On doit "caster" les items à leur état d'origine (de QWidgetItem à QPushButton)
      #Pour cela on récupère leur index et on les compare aux index de tout les boutons
      #On oublie pas de ne garder que les items non adjacents
      btns_not_around = [btn for idx,btn in enumerate(self.buttons_in_grid)
                     if self.myGL_btn_game.itemAtPosition(
                           self.myGL_btn_game.getItemPosition(idx)[0], self.myGL_btn_game.getItemPosition(idx)[1])
                     not in items_around]

      return btns_not_around

   def addScore(self, mot):

      #On actualise le score
      self.score += len(mot)

      #On actualise le label de points
      self.label_points.setText(f"Score : {self.score:04d}")

   def setNewTry(self):
      #On retablit la line Edit
      self.lineEdit.setText("")

      #On rétablit les boutons
      for b in self.buttons_in_grid :
         b.setStyleSheet(f"background-color : {c.couleur_boutons_de_jeu}; font-size : 40px")
         b.setEnabled(True)
      self.buttons_already_used.clear()


# =============================================================================
# Dialog Page (When game ends)
# =============================================================================

class DialogEndGame(QMessageBox):
   def __init__(self, texte):
      super().__init__()
      self.setWindowTitle("Fin du jeu")

      #Texte affiché
      self.setText(texte)

      #Boutons de la boite de dialoogue
      self.addButton("Rejouer",QMessageBox.AcceptRole)
      self.addButton("Continuer la partie",QMessageBox.RejectRole)
      self.addButton("Quitter",QMessageBox.RejectRole)




# =============================================================================
# Others methods
# =============================================================================


def pause(t):
   """
   Met le programme en pause pour un temps t (ms).

   t (int) -> durée de la pause (en ms)
   """
   loop = QEventLoop()
   QTimer.singleShot(t, loop.quit)
   loop.exec_()





#Test si l'app tourne déjà
myApp = QCoreApplication.instance()
if myApp is None :
   myApp = QApplication(argv)

#Creation d'une fenêtre
myWindow = MainWindow()
myWindow.show()
#Lancement de l'app
myApp.exec()