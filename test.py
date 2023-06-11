import fonction

def index(req):
    req.content_type = "text/html"
    req.write(fonction.codeHTML("title","ma premiere page html"))
    