import psycopg2 as psycopg2


def connection():
    conn = psycopg2.connect(
        host="localhost",
        database="DotaScope",
        user="postgres",
        password="kir54678199"
    )
    return conn


def insert_user(name: str, pas: str):
    conn = connection()
    cursor = conn.cursor()

    query = f"""
    INSERT INTO Users (name, password)
     VALUES ('{name}', '{pas}');
    """

    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def insertGame(id_user: int, score: int):
    conn = connection()
    cursor = conn.cursor()

    query = f"""
         INSERT INTO invoker_game (id_user, score)
         VALUES
            ({id_user}, {score});
        """

    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def get_user_by_name(name: str):
    conn = connection()
    cursor = conn.cursor()

    query = f"""
            SELECT * FROM users 
            WHERE users.name = '{name}'
           """

    cursor.execute(query)
    conn.commit()

    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_users():
    conn = connection()
    cursor = conn.cursor()

    query = f"""
                SELECT * FROM users 
            """

    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_invoker():
    conn = connection()
    cursor = conn.cursor()

    query = f"""
                SELECT * FROM invoker_game 
            """

    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_user_by_id(id: int):
    conn = connection()
    cursor = conn.cursor()

    query = f"""
            SELECT* FROM users 
            WHERE users.id_user = '{id}'
        """

    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_leader_board():
    conn = connection()
    cursor = conn.cursor()

    query = f"""
                SELECT users.name as Name, invoker_game.score as Score FROM invoker_game
                JOIN users ON invoker_game.id_user = users.id_user
                ORDER BY invoker_game.score DESC
                LIMIT 8;
            """

    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_user_records(userId: int):
    conn = connection()
    cursor = conn.cursor()

    query = f"""
                SELECT users.name as Name, invoker_game.score as Score FROM invoker_game 
                JOIN users ON invoker_game.id_user = users.id_user
                WHERE (users.id_user = {userId})
                ORDER BY invoker_game.score DESC
                LIMIT 5;
            """

    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


