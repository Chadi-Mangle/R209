import fonctions

def index(req):
    req.content_type = "text/html"
    req.write(fonctions.codeHTML("title","ma premiere page html"))
    