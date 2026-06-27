import sqlite3
from datetime import datetime


def create_monitoring():

    con = sqlite3.connect(
        "carecall.db"
    )

    cur = con.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS monitoring(
        id INTEGER PRIMARY KEY,
        name TEXT,
        bp INTEGER,
        glucose INTEGER,
        heart INTEGER,
        risk TEXT,
        date TEXT
        )
        """
    )

    con.commit()
    con.close()



def save_monitoring(
        name,
        bp,
        glucose,
        heart,
        risk):

    con=sqlite3.connect(
        "carecall.db"
    )

    cur=con.cursor()

    cur.execute(
        """
        INSERT INTO monitoring
        VALUES(NULL,?,?,?,?,?,?)
        """,
        (
        name,
        bp,
        glucose,
        heart,
        risk,
        datetime.now()
        )
    )

    con.commit()
    con.close()



def get_monitoring(name):

    con=sqlite3.connect(
        "carecall.db"
    )

    cur=con.cursor()

    cur.execute(
        """
        SELECT *
        FROM monitoring
        WHERE name=?
        """,
        (name,)
    )

    data=cur.fetchall()

    con.close()

    return data



def check_trend(records):

    if len(records)<2:

        return "Need more records"


    old=records[0][2]

    new=records[-1][2]


    if new-old > 20:

        return "⚠ BP increased. Health risk rising"


    return "✅ Health stable"