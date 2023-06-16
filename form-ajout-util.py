import fonctions
from mod_python import Session

def index(req):
    s = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req, s)
    req.content_type = "text/html"
    html = """
<h2>Ajout d'un utilisateur</h2>
<form method="post" action="ajout-util.py" onsubmit="return valider()">
 <table>
  <tr>
    <td>Login: </td>
    <td><input type="text" name="login" id="login"/></td>
  </tr>  
   <tr>
    <td>Mot de passe: </td>
    <td><input type="password" name="mdp1" id="mdp1"/></td>
  </tr>
    <tr>
    <td>Confirmation du mot de passe: </td>
    <td><input type="password" id="mdp2"/></td>
    <td><input type="submit" value="Valider"/></td>
  </tr>  
</table>
</form>
<script>
function valider(){
  var login = document.getElementById("login").value;
  var mdp1 = document.getElementById("mdp1").value;
  var mdp2 = document.getElementById("mdp2").value;
  if(login == ""){
    alert("Entrer un nom d'utilisateur");
    return false;
  };
  if (!(mdp1.length >= 8)){
    alert("Mot de passe trop court"); 
    return false
  }
  if (mdp1 != mdp2)
  alert("Les deux mots de passe ne sont pas indentique");
  return false;
  } 
  return true;
}
</script>    
"""
    req.write(fonctions.codeHTML('Ajout Contact', html))

