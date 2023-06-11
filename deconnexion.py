from mod_python import Session, util

def index(req):
    s = Session.Session(req)
    s.delete()
    util.redirect(req, "./form-connexion.py")
