from datetime import datetime


from src.notification import send_email


from src.voice_call import make_call


from src.database import (

    get_family_email,

    get_family_phone,

    save_alert

)





# ================= DUPLICATE ALERT CACHE =================


sent_alerts=set()







# ================= EMERGENCY ALERT =================


def emergency_alert(

        patient,

        disease,

        confidence

):



    # ---------- LOW RISK CHECK ----------


    if confidence < 70:


        return """

✅ Risk not critical

Emergency alert not required.

"""







    # ---------- FAMILY DETAILS ----------


    family_email=get_family_email(

        patient

    )



    family_phone=get_family_phone(

        patient

    )








    if (

        (family_email is None or family_email=="")

        and

        (family_phone is None or family_phone=="")

    ):


        return """

⚠ Alert Failed


No family contact found.


Please update:

Email 📧

or

Phone 📞

"""









    # ---------- DUPLICATE CHECK ----------


    alert_key=(

        patient,

        disease,

        str(datetime.now().date())

    )






    if alert_key in sent_alerts:



        return """

⚠ Emergency alert already sent today.

Duplicate blocked.

"""









    # ---------- MESSAGE ----------


    message=f"""

🚨 CARECALL AI EMERGENCY ALERT


Patient:

{patient}



Condition:

{disease}



Risk:

HIGH



AI Confidence:

{confidence}%



Time:

{datetime.now()}



Action:


Please check patient's health condition.


If symptoms are serious,

contact healthcare professional immediately.



- CareCall AI

"""








    email_status=False


    call_status=False









    # ================= EMAIL ALERT =================


    if family_email:


        email_status=send_email(


            family_email,


            "🚨 CareCall AI Emergency Alert",


            message

        )









    # ================= VOICE ALERT =================


    if family_phone:



        call_message=f"""


        Emergency alert from CareCall AI.


        Patient {patient}


        has high risk detected for {disease}.


        Confidence level is {confidence} percent.


        Please check immediately.


        """






        call_status=make_call(

            family_phone,

            call_message

        )









    # ================= SAVE RESULT =================


    if email_status or call_status:




        save_alert(

            patient,

            message

        )




        sent_alerts.add(

            alert_key

        )







        return f"""

🚨 Emergency Alert Sent Successfully


Email:

{family_email}


Phone:

{family_phone}

"""









    else:




        save_alert(

            patient,

            "FAILED ALERT : "+message

        )





        return """

⚠ Emergency Alert Failed


Check:

1. Internet

2. Gmail SMTP

3. Twilio Settings

"""