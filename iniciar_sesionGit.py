import obtener_repositorios as repositorio
import funcionalidades as funcion
import git
def buscar_repositorio(repositorios,name):
    for e in repositorios:
        try:
            if e['Nombre'] == name:
                return e['URL']
        except:
            pass

username = "janobaf"
repositorios=repositorio.recuperacion_repositorios(#token=token,username=username)

direc = "C:\\Users\\artur\\Documents\\Python"
#resultado_creacion_rama=funcion.crear_rama(direc,"developer","xd")
#print(resultado_creacion_rama)
#proyecto = input("Ingrese el nombre del repositorio quiere descargar")
#url=buscar_repositorio(repositorios,proyecto)
#repo = git.Repo.clone_from(url, direc)
#print(f'Repositorio clonado en: {direc}')

#funcion.verificar_estado_repositorio(direc)

funcion.realizar_commit_y_push(direc,"v2","master")