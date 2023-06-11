import fonctions
from mod_python import Session

def index(req):
    s = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req, s)
    req.content_type = "text/html"
    html = """<h2>Menu principal</h2>
            <p>Vous etes connecte en tant que {}.</p>
            <ul>
            <li>{}</li>
            <li>{}</li>
            <li>{}</li>
            </ul>
            """.format(
            s['login'], 
            fonctions.lien('form-ajout.py', "Ajout d'un contact"),
            fonctions.lien('liste.py',"Liste des contacts"),
            fonctions.lien('deconnexion.py',"Deconnexion"))
    req.write(fonctions.codeHTML('Menu',html)) 