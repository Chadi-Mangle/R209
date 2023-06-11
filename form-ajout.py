import fonctions
from mod_python import Session
def index(req):
    s = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req, s)
    req.content_type = "text/html"
    html = """
<form method="post" action="ajout.py" onsubmit="return valider()">
 <table>
  <tr>
    <td>Nom: </td>
    <td><input type="text" name="nom" id="nom"/></td>
  </tr>  
   <tr>
    <td>Adresse: </td>
    <td><input type="text" name="adresse" id="adresse"/></td>
  </tr>
    <tr>
    <td>Email: </td>
    <td><input type="text" name="email" id="email"/></td>
  </tr>  
   <tr>
    <td>Telephone: </td>
    <td><input type="text" name="telephone" id="telephone"/></td>
    <td><input type="submit" value="Valider"/></td>
  </tr>
</table>
</form>
<script>
function valider(){
  var nom = document.getElementById("nom").value;
  var email = document.getElementById("email").value;
  var telephone = document.getElementById("telephone").value;

  if(nom == ""){
    alert("Entrer un nom d'utilisateur");
    return false;
  };
  if (email == ""){
      alert("Entrer une adresse mail");
      return false;}
  else{
    if (!email.match(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,4}$/)){
      alert("Adresse mail invalide");
      return false;
  }};
  if (!(telephone.length == 10 && isNaN(telephone) == false)){
    alert("Telephone invalide"); 
    return false
  }
  return true;
}
</script>    
"""
    req.write(fonctions.codeHTML('Ajout Contact', html))

