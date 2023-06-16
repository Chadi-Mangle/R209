import fonctions
import psycopg2
from mod_python import Session, apache, util

def index(req):
    s = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req,s)
    req.content_type = "text/html"
    id_contact = req.form["id_contact"]
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    curseur.execute("delete from contact where id_contact = {} and id_util = {};".format(id_contact, s['id_util']))
    connexion.commit()
    util.redirect(req,  "./liste.py")