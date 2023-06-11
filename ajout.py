import psycopg2
import fonctions 
from mod_python import Session
from mod_python import apache
#geocodage = apache.import_module("geocodage")
from geocodage import geocodage
def index(req):
    connexion = fonctions.connexionBD()
    s = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req, s)
    curseur = connexion.cursor()
    lat, lon = geocodage(req.form['adresse'])
    curseur.execute("insert into contact(nom, adresse, telephone, email, id_util, lat, lon) values ('{}','{}','{}','{}','{}','{}','{}')".format(
        req.form['nom'] ,req.form['adresse'] ,req.form['telephone'] ,req.form['email'], s['id_util'],lat, lon))
    connexion.commit()
    req.content_type = "text/html"
    req.write(fonctions.codeHTML('Ajout contact',"""<h2>Nouveau contact</h2><p>Le contact "{}" a bien ete ajoute.</p>{}""".format(req.form['nom'],
        fonctions.lien('form-ajout.py','Retour vers ajout contatct'))))