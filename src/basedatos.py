import sqlite3

def version_SQLite():
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'SELECT sqlite_version();'
        cursor.execute(query)
        row = cursor.fetchall()
        print('Version de SQLite: ', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def crear_tablas():
    #TablaUSUARIOS
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''
            CREATE TABLE IF NOT EXISTS usuario(
                user_id TEXT PRIMARY KEY,
                user_name TEXT NOT NULL,
                user_id_followers TEXT NOT NULL,
                user_id_baneados TEXT NOT NULL,
                user_id_recomendado TEXT NOT NULL,
                FOREIGN KEY (user_id_followers) REFERENCES followers (user_id),
                FOREIGN KEY (user_id_baneados) REFERENCES banned (user_id),
                FOREIGN KEY (user_id_recomendado) REFERENCES followers (user_id)
            );
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        print('Tabla creada correctamente', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

    #TABLAFOLLOWRES
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''
            CREATE TABLE IF NOT EXISTS followers(
                user_id TEXT PRIMARY KEY,
                user_name_seguido TEXT NOT NULL,
                ponderacion INTEGER NOT NULL
            );
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        print('Tabla creada correctamente', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

    #TABLABANNED
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''
            CREATE TABLE IF NOT EXISTS banned(
                user_id TEXT PRIMARY KEY,
                user_name_baneado TEXT NOT NULL,
            );
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        print('Tabla creada correctamente', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

    #TablaRECOMENDACIONES
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''
            CREATE TABLE IF NOT EXISTS recomendaciones(
                user_id TEXT PRIMARY KEY,
                user_name_recomendado TEXT NOT NULL,
            );
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        print('Tabla creada correctamente', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def agregar_usuario(id_usuario,nombre_usuaio,id_usuario_seguido,baneados):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO usuario VALUES 
                ('{}', '{}', '{}', '{}')""".format(id_usuario, nombre_usuaio, id_usuario_seguido, baneados)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def agregar_followers(id_usuario,nombre_usuario,ponderacion):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO followers VALUES 
                ('{}', '{}','{}')""".format(id_usuario, nombre_usuario, ponderacion)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def agregar_baneados(id_usuario, nombre_usuario):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO banned VALUES 
                ('{}', '{}')""".format(id_usuario, nombre_usuario)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def agregar_recomendaciones(id_usuario,nombre_usuario):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO recomendaciones VALUES 
                ({}, '{}')""".format(id_usuario, nombre_usuario)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion',error)
    finally:
        if(conexion):
            conexion.close()

def ver_todos_usuarios():
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT usu.id_usuario,usu.user_name,fol.user_name_seguido,ban.user_name_baneado,rec.user_name recomendado  FROM usuario usu JOIN follewers fol, banned ban, recomendaciones rec ON fol.user_id = usu.user_id_followers or ban.user_id = usu.user_id_baneados or rec.user_id = usu.user_id_recomendado;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id_usuario: {}\nNombre_Usuario: {}\nNombre_Usuarios_Seguidos: {}\nNombre_Usuarios_baneados: {}\nNombre_Usuario_Recomendado: {}'.format(*row))
        
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion',error)
    finally:
        if(conexion):
            conexion.close()

def eliminar_usuario(Id_usuario):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "DELETE FROM usuario WHERE user_id = {}".format(Id_usuario)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Eliminado Correctamente', resultado)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion',error)
    finally:
        if(conexion):
            conexion.close()