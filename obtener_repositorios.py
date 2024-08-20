import requests
def recuperacion_repositorios(token,username):
    try:
        headers = {
            "Authorization": f"token {token}"
        }
        url = f"https://api.github.com/users/{username}/repos"

        # Realizar la petición GET para obtener los repositorios
        response = requests.get(url, headers=headers)

        # Comprobar si la petición fue exitosa
        if response.status_code == 200:
            repos = response.json()
            lista_repositorios = list()
            for repo in repos:
                diccionario = {"Nombre":None,"URL":None}
                diccionario["Nombre"] = repo['name']
                diccionario["URL"] =repo['html_url']
                lista_repositorios.append(diccionario)
            return lista_repositorios
            
        else:
            print(f"Error: {response.status_code}")
    except:
        return False