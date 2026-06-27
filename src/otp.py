import random


from src.notification import send_email




otp_store={}




# =============== SEND OTP ===============


def send_otp(email):


    otp=str(

        random.randint(
            100000,
            999999
        )

    )



    otp_store[email]=otp



    message=f"""

🔐 CareCall AI Verification


Your OTP Code:


{otp}



Do not share this OTP.


- CareCall AI

"""




    status=send_email(

        email,

        "CareCall OTP Verification",

        message

    )



    if status:


        print(

            "OTP SENT:",
            otp
        )


        return True



    else:


        print(

            "OTP FAILED"
        )


        return False








# =============== VERIFY OTP ===============


def verify_otp(

        email,

        otp

):


    print(

        otp_store

    )



    if email in otp_store:


        if otp_store[email]==otp:


            del otp_store[email]


            return True



    return False