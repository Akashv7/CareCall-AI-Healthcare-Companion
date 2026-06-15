import sqlite3
from datetime import datetime


# create database

def create_database():

    conn = sqlite3.connect(
        "carecall.db"
    )

    cursor = conn.cursor()


    cursor.execute(
    """

    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient_name TEXT,

        disease TEXT,

        risk TEXT,

        confidence REAL,

        date TEXT

    )

    """
    )


    conn.commit()

    conn.close()





# save prediction

def save_history(

        patient_name,
        disease,
        risk,
        confidence
):


    conn = sqlite3.connect(
        "carecall.db"
    )


    cursor = conn.cursor()


    cursor.execute(

    """

    INSERT INTO history(

        patient_name,
        disease,
        risk,
        confidence,
        date

    )

    VALUES (?,?,?,?,?)

    """,


    (

        patient_name,

        disease,

        risk,

        confidence,

        datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )

    )

    )


    conn.commit()


    conn.close()





# view history

def get_history():


    conn = sqlite3.connect(
        "carecall.db"
    )


    cursor = conn.cursor()


    cursor.execute(

        "SELECT * FROM history"

    )


    data = cursor.fetchall()


    conn.close()


    return data