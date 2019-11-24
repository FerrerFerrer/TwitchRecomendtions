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
                user_followers_id INTEGER,
                user_followers_name TEXT,
                baneados TEXT,
                user_recomendado TEXT,
                ponderacion float
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

def agregar_usuario(id_usuario,nombre_usuaio,id_usuario_seguido,baneados,nombre_usuario_seguido,ponderacion):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO usuario VALUES
                ({}, '{}', '{}', '{}','{}',{})""".format(id_usuario, nombre_usuaio, id_usuario_seguido, nombre_usuario_seguido, baneados, recomendaciones, ponderacion)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def mostrar_usuario():
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """SELECT * FROM usuario"""
        resultado = cursor.execute(query)
        conexion.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


def eliminar_usuario(nombre_usuario):
    try:
        conexion = sqlite3.connect('api_twitch.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "DELETE FROM usuario WHERE user_name = '{}'".format(nombre_usuario)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Eliminado Correctamente', resultado)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion',error)
    finally:
        if(conexion):
            conexion.close()
