import fonctions
import psycopg2
from mod_python import Session, apache

def index(req):
    s = Session.Session(req)

    fonctions.redirectionSiNonConnecte(req,s)
    req.content_type = "text/html"
    id_contact = req.form["id_contact"]
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    curseur.execute("select nom, telephone, email, adresse, id_contact from contact where id_contact = {};".format(id_contact))
    resultat = curseur.fetchone()
    
    liste = ["Nom", "Telephone", "Email", "Adresse"]
    req.write("<p><b>Fiche d'un contact</b></p> <table>")
    for index, element in enumerate(liste):
        if resultat[index] != "":  
            if element == "Email": 
                req.write("<tr><td>{} : </td><td> {}</td></tr>".format(liste[index], fonctions.lien("mailto:{}".format(resultat[index]), resultat[index])))
            else:
                req.write("<tr><td>{} : </td><td> {}</td></tr>".format(liste[index], resultat[index]))
    req.write("</table> <br>{} {}".format(fonctions.lien("./menu.py", "Retour au menu."), 
                                        fonctions.lien("suppresion.py?id_contact={}".format(id_contact), "Suppression du contact")))