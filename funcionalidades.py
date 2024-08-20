import git

def crear_rama(direc, nombre_rama,mensaje_commit):

    try:

        repo = git.Repo(direc)
        commits_exist = repo.head.is_valid()

        if not commits_exist:
            print("El repositorio está vacío. Creando commit inicial...")

            with open(f'{repo.working_tree_dir}/README.md', 'w') as f:
                f.write("# Repositorio inicial")

            repo.git.add('README.md')
            repo.index.commit("Commit inicial")
            print("Commit inicial realizado.")


        new_branch = repo.create_head(nombre_rama)
        new_branch.checkout()
        print(f"Se ha creado y cambiado a la rama {nombre_rama}.")
        
    
        repo.git.add(all=True)  
        repo.index.commit(mensaje_commit)
        print(f"Se ha realizado un commit en la rama {nombre_rama}.")

  
        origin = repo.remote(name='origin')
        origin.push(refspec=f'{nombre_rama}:{nombre_rama}')
        print(f"La rama {nombre_rama} se ha subido al repositorio remoto.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")




def verificacion_cambios(direccion,nombre_rama):
    try:
        # Abrir el repositorio
        repo = git.Repo(direccion)
        
        # Verificar cambios no confirmados
        cambios_no_confirmados = repo.index.diff(None)
        if cambios_no_confirmados:
            print("Hay cambios no confirmados:")
            for cambio in cambios_no_confirmados:
                print(f"- {cambio.a_path} (Cambios no confirmados)")
        else:
            print("No hay cambios no confirmados.")

        # Verificar si la rama está detrás de la rama remota
        # Asegurarse de que 'origin' está configurado
        if 'origin' not in [remote.name for remote in repo.remotes]:
            print("No se encuentra la configuración de 'origin'.")
            return
        
        # Obtener la referencia remota de la rama
        rama_remota = f'origin/{nombre_rama}'
        try:
            repo.git.fetch()  # Actualizar información remota
            diff = repo.git.diff(f'{rama_remota}..{nombre_rama}')
            if diff:
                print(f"Hay cambios que no han sido subidos a la rama remota '{rama_remota}':")
                print(diff)
            else:
                print(f"La rama '{nombre_rama}' está actualizada con '{rama_remota}'.")

        except git.exc.GitCommandError as e:
            print(f"Error al comparar con la rama remota: {e}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
def verificar_estado_repositorio(direc):
    try:
        # Abrir el repositorio
        repo = git.Repo(direc)
        
        # Verificar cambios en el índice (preparados para commit)
        cambios_preparados = repo.index.diff('HEAD')
        if cambios_preparados:
            print("Cambios preparados para commit:")
            for cambio in cambios_preparados:
                print(f"- {cambio.a_path} (Cambios preparados)")
        else:
            print("No hay cambios preparados para commit.")

        # Verificar cambios en el directorio de trabajo (no preparados)
        cambios_no_preparados = repo.index.diff(None)
        if cambios_no_preparados:
            print("Cambios no preparados para commit:")
            for cambio in cambios_no_preparados:
                print(f"- {cambio.a_path} (Cambios no preparados)")
        else:
            print("No hay cambios no preparados para commit.")

        # Verificar archivos no rastreados
        archivos_no_rastreados = repo.untracked_files
        if archivos_no_rastreados:
            print("Archivos no rastreados:")
            for archivo in archivos_no_rastreados:
                print(f"- {archivo}")
        else:
            print("No hay archivos no rastreados.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

def realizar_commit_y_push(direc, mensaje_commit, nombre_rama):
    try:
        repo = git.Repo(direc)
        
        cambios_no_confirmados = repo.index.diff(None)
        if not cambios_no_confirmados:
            print("No hay cambios para hacer commit.")
            return

        repo.git.add(all=True)
        
        repo.index.commit(mensaje_commit)
        print(f"Commit realizado con el mensaje: '{mensaje_commit}'")

        origin = repo.remote(name='origin')
        
        repo.git.push('origin', nombre_rama)
        print(f"Push realizado para la rama '{nombre_rama}'.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")