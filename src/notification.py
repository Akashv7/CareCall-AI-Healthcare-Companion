import smtplib
import os

from email.message import EmailMessage

from dotenv import load_dotenv



load_dotenv(
    override=True
)



EMAIL_USER=os.getenv(
    "EMAIL_USER"
)


EMAIL_PASSWORD=os.getenv(
    "EMAIL_PASSWORD"
)





def send_email(

        receiver,

        subject,

        message

):


    try:


        email=EmailMessage()



        email["From"]=EMAIL_USER


        email["To"]=receiver.strip()


        # remove newline from subject

        clean_subject=subject.replace(
            "\n",
            " "
        ).replace(
            "\r",
            " "
        )


        email["Subject"]=clean_subject



        email.set_content(

            message

        )




        server=smtplib.SMTP(

            "smtp.gmail.com",

            587

        )



        server.starttls()



        server.login(

            EMAIL_USER,

            EMAIL_PASSWORD

        )



        server.send_message(

            email

        )



        server.quit()



        print(

            "EMAIL SENT SUCCESSFULLY TO:",

            receiver

        )



        return True




    except Exception as e:


        print(

            "EMAIL ERROR:",

            e

        )


        return False