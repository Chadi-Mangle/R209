import psycopg2
import fonctions 
from mod_python import Session
from mod_python import apache

def index(req):
    connexion = fonctions.connexionBD()
    s = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req, s)
    curseur = connexion.cursor()
    curseur.execute("insert into util(login, mdp) values ('{}','{}')".format(
        req.form['login'] ,req.form['mdp1']))
    connexion.commit()
    req.content_type = "text/html"
    req.write(fonctions.codeHTML('Ajout contact',"""<h2>Nouveau contact</h2><p>Le contact "{}" a bien ete ajoute.</p>{}""".format(req.form['login'],
        fonctions.lien('form-ajout-util.py','Retour vers ajout utilsateur'))))