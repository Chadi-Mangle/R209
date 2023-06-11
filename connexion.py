import fonctions
from mod_python import Session, apache

def index(req):
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    login = req.form['login']
    curseur.execute("select id_util, mdp from util where login = '{}';".format(login))
    resultat = curseur.fetchone()
    req.content_type = "text/html"
    
    if resultat is not None:
        id_util, mdp = resultat
        if mdp == req.form['password']:
            session = Session.Session(req)
            session['id_util'] = id_util
            session['login'] = login
            session.save()
            msg = 'Connexion reussie. '
            lien = fonctions.lien('menu.py','Menu du site')
            return fonctions.codeHTML('Connexion', msg + lien)
        msg = 'Mot de passe incorrect '
        lien = fonctions.lien('./form-connexion.py','Retour')
        return fonctions.codeHTML('Connexion', msg + lien)
    msg = 'Utilisateur inexistant '
    lien = fonctions.lien('./form-connexion.py','Retour')   
    return fonctions.codeHTML('Connexion', msg + lien)