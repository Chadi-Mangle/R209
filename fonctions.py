import psycopg2
from mod_python import util

def codeHTML(titre, corps): 
	return """<!DOCTYPE html> 
	<html>
		<head>
			<title>{}</title>
			<meta charset="UTF-8">
		</head>
		<body>
			{}
		</body>
	</html>""".format(titre, corps)

def connexionBD(): 
	return psycopg2.connect(host='localhost',
			dbname='devweb',
			user='english', 
			password='user')
def lien(url, texte):
	return "<a href='{}'/>{}</a>".format(url, texte)
def redirectionSiNonConnecte(req, s): 
	if s.is_new():
		util.redirect(req, "./form-connexion.py")
