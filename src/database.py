import sqlite3

from datetime import datetime


from src.security import (
    hash_password,
    verify_password
)



DB_NAME="carecall.db"




# ================= CREATE DATABASE =================

def create_database():

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    # ================= HISTORY =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        disease TEXT,

        risk TEXT,

        confidence REAL,

        date TEXT

    )
    """)

    # ================= USERS =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE,

        password TEXT,

        role TEXT,

        family_email TEXT,

        family_phone TEXT,

        verified TEXT

    )
    """)

    # ================= HEALTH RECORDS =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS health_records(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient TEXT,

        bp INTEGER,

        glucose INTEGER,

        heart_rate INTEGER,

        risk TEXT,

        date TEXT

    )
    """)

# ================= SAVE MEDICINE =================

def save_medicine(

        patient,

        medicine,

        dosage,

        frequency,

        start_date,

        end_date,

        time

):

    con = sqlite3.connect(DB_NAME)

    cur = con.cursor()

    cur.execute("""

    INSERT INTO medicine
    (
        patient,
        medicine,
        dosage,
        frequency,
        start_date,
        end_date,
        time
    )

    VALUES(?,?,?,?,?,?,?)

    """,(

        patient,

        medicine,

        dosage,

        frequency,

        start_date,

        end_date,

        time

    ))

    con.commit()

    con.close()

    # ================= ALERTS =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient TEXT,

        message TEXT,

        status TEXT,

        date TEXT

    )
    """)

    # ================= DOCTOR REVIEW =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctor_review(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient TEXT,

        question TEXT,

        ai_reply TEXT,

        doctor_reply TEXT,

        status TEXT,

        date TEXT

    )
    """)


# ================= MEDICINE STATUS =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medicine_status(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient TEXT,

        medicine TEXT,

        medicine_time TEXT,

        status TEXT DEFAULT 'Pending',

        retry INTEGER DEFAULT 0,

        taken_time TEXT,

        date TEXT

)
""")


    con.commit()
    con.close()




# ================= HISTORY =================


def save_history(
        name,
        disease,
        risk,
        confidence
):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()


    cur.execute(
    """

    INSERT INTO history

    VALUES(NULL,?,?,?,?,?)

    """,

    (

        name,
        disease,
        risk,
        confidence,
        str(datetime.now())

    )

    )


    con.commit()

    con.close()





def get_history():


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()


    cur.execute(

        "SELECT * FROM history"

    )


    data=cur.fetchall()


    con.close()


    return data









# ================= USER AUTH =================


def add_user(

        name,

        password,

        role,

        family_email,

        family_phone

):


    try:


        con=sqlite3.connect(DB_NAME)

        cur=con.cursor()



        cur.execute(
        """

        INSERT INTO users

        VALUES(NULL,?,?,?,?,?,?)

        """,

        (

            name,

            hash_password(password),

            role,

            family_email,

            family_phone,

            "YES"

        )

        )



        con.commit()

        con.close()



        return True



    except Exception as e:


        print(e)


        return False







def check_user(
        name,
        password
):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    SELECT *

    FROM users

    WHERE name=?

    """,

    (name,)

    )



    user=cur.fetchone()


    con.close()



    if user:


        if verify_password(
            password,
            user[2]
        ):


            return user



    return None







# ================= FAMILY DETAILS =================


def get_family_email(patient):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    SELECT family_email

    FROM users

    WHERE name=?

    """,

    (patient,)

    )


    result=cur.fetchone()


    con.close()



    if result:

        return result[0]


    return None







def get_family_phone(patient):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    SELECT family_phone

    FROM users

    WHERE name=?

    """,

    (patient,)

    )


    result=cur.fetchone()


    con.close()



    if result:

        return result[0]


    return None









# ================= MEDICINE =================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medicine(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient TEXT,

        medicine TEXT,

        dosage TEXT,

        frequency TEXT,

        start_date TEXT,

        end_date TEXT,

        time TEXT

)
""")



# ================= ALERT =================


def save_alert(

        patient,

        message

):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    INSERT INTO alerts

    VALUES(NULL,?,?,?,?)

    """,

    (

        patient,

        message,

        "NEW",

        str(datetime.now())

    )

    )



    con.commit()

    con.close()








def get_alerts():


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()


    cur.execute(

        "SELECT * FROM alerts"

    )


    data=cur.fetchall()


    con.close()


    return data







# ================= DOCTOR APPROVAL =================


def save_ai_review(

        patient,

        question,

        ai_reply

):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    INSERT INTO doctor_review

    VALUES(NULL,?,?,?,?,?,?)

    """,

    (

        patient,

        question,

        ai_reply,

        "",

        "PENDING",

        str(datetime.now())

    )

    )



    con.commit()

    con.close()







def get_pending_reviews():


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()


    cur.execute(
    """

    SELECT *

    FROM doctor_review

    WHERE status='PENDING'

    """
    )


    data=cur.fetchall()


    con.close()


    return data









def approve_review(

        review_id,

        doctor_reply

):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    UPDATE doctor_review

    SET doctor_reply=?,

    status='APPROVED'

    WHERE id=?

    """,

    (

        doctor_reply,

        review_id

    )

    )



    con.commit()

    con.close()








def get_patient_reviews(patient):


    con=sqlite3.connect(DB_NAME)

    cur=con.cursor()



    cur.execute(
    """

    SELECT *

    FROM doctor_review

    WHERE patient=?

    """,

    (patient,)

    )
    data=cur.fetchall()
    con.close()
    return data
def save_medicine_status(patient, medicine, medicine_time):

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    INSERT INTO medicine_status
    (
        patient,
        medicine,
        medicine_time,
        status,
        retry,
        taken_time,
        date
    )
    VALUES(?,?,?,?,?,?,?)
    """, (

        patient,
        medicine,
        medicine_time,
        "Pending",
        0,
        None,
        str(datetime.now())

    ))

    con.commit()
    con.close()
def update_medicine_status(record_id):

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    UPDATE medicine_status

    SET
        status=?,
        taken_time=?

    WHERE id=?
    """, (

        "Taken",

        str(datetime.now()),

        record_id

    ))

    con.commit()
    con.close()

# ================= GET STATUS =================

def get_medicine_status():

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""

    SELECT *

    FROM medicine_status

    ORDER BY id DESC

    """)

    data = cur.fetchall()

    con.close()

    return data



def get_pending_medicine():

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    SELECT *
    FROM medicine_status
    WHERE status='Pending'
    """)

    data = cur.fetchall()

    con.close()

    return data


def increase_retry(record_id):

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    UPDATE medicine_status

    SET retry = retry + 1

    WHERE id=?
    """, (record_id,))

    con.commit()
    con.close()


def get_total_patients():

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM users WHERE role='Patient'")

    total = cur.fetchone()[0]

    con.close()

    return total


def get_pending_count():

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM medicine_status
    WHERE status='Pending'
    """)

    total = cur.fetchone()[0]

    con.close()

    return total


def get_taken_count():

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM medicine_status
    WHERE status='Taken'
    """)

    total = cur.fetchone()[0]

    con.close()

    return total
def get_weekly_health_data(patient):

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
    SELECT bp, glucose, heart_rate, risk
    FROM health_records
    WHERE patient=?
    ORDER BY date DESC
    LIMIT 7
    """, (patient,))

    health = cur.fetchall()

    cur.execute("""
    SELECT medicine, status
    FROM medicine_status
    WHERE patient=?
    ORDER BY date DESC
    LIMIT 20
    """, (patient,))

    medicine = cur.fetchall()

    con.close()

    return health, medicine