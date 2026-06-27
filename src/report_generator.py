import os

from datetime import datetime


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


from reportlab.lib.styles import (
    getSampleStyleSheet
)





def create_report(

        patient,
        disease,
        risk,
        confidence

):


    if not os.path.exists(

        "reports"

    ):


        os.mkdir(

            "reports"

        )





    filename=f"reports/{patient}_CareCall_Report.pdf"





    pdf=SimpleDocTemplate(

        filename

    )



    styles=getSampleStyleSheet()



    data=[]





    data.append(

        Paragraph(

            "CareCall AI Medical Report",

            styles["Title"]

        )

    )




    data.append(

        Spacer(

            1,

            20

        )

    )





    text=f"""


Patient:

{patient}


<br/><br/>


Disease:

{disease}


<br/><br/>


Risk:

{risk}


<br/><br/>


Confidence:

{confidence}%


<br/><br/>


Generated:

{datetime.now()}



"""




    data.append(

        Paragraph(

            text,

            styles["BodyText"]

        )

    )





    pdf.build(

        data

    )




    return filename