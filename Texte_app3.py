
texte_regles_du_jeu = ("Dans une limite de temps, vous devez trouver un maximum de mots "
"en formant des chaînes de  lettres contiguës. Plus le mot est long, plus les points qu'il vous rapporte sont "
"importants.\nVous pouvez passer d'une lettre à la suivante située directement à gauche, à droite, en haut, "
"en bas, ou sur l'une des quatre cases diagonales."
"\n\n•Une lettre ne peut pas être utilisée plus d'une fois pour un même mot."
"\n•Seuls les mots de trois lettres ou plus comptent."
"\n•Les accents ne sont pas importants. e peut être utilisé comme é, è, ê, etc.")

texte_qui_sommes_nous = "Nous sommes une petite entreprise familiale..."

texte_positif = ["Bien joué !", "Et un mot de plus !", "Ce mot existe bel et bien",
                 "Chapeau !", "Bravo pour celui là", "T'as un bon niveau, continue comme ça !", "Incroyable !",
                 "Mais quel génie !", "Wow, je l'avais même pas vu !", "Wow je te savais pas si fort"]

texte_negatif = ["Non, ça ne marchera pas ", "Essaye encore", "En mandarin peut-être oui...",
                 "Mauvais choix !", "T'es trop naze mdr", "Non, pas cette fois", "Ce mot est inexistant !",
                 "T'es surement pas le plus affuté du tiroir toi","Aïe, essaye de nouveau", "Joue serieusement !",
                 "À croire que tu fais exprès", "Mais nooon", "Toi, Parler, Français ?"]

def txtScore(pts) :
   if pts<10 : return "Aïe. Vous pouvez sûrement mieux faire..."
   elif pts<20 : return "Moyen. C'est déjà un bon début."
   elif pts<35 : return "Bien. Vous avez un très bon niveau !"
   else  : return "Excellent ! Vous maitrisez la langue française sur le bout des doigts."
