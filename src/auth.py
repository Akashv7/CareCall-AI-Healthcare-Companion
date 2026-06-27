import streamlit as st


from src.database import (
    add_user,
    check_user
)


from src.otp import (
    send_otp,
    verify_otp
)





# ================= REGISTER PAGE =================


def register_page():


    st.subheader(

        "📝 Create Account"

    )





    name=st.text_input(

        "Username"

    )





    password=st.text_input(

        "Password",

        type="password"

    )







    role=st.selectbox(

        "Select Role",

        [

            "Patient",

            "Doctor",

            "Family"

        ]

    )






    family_email=""

    family_phone=""






    # ================= PATIENT DETAILS =================


    if role=="Patient":




        family_email=st.text_input(

            "Family Email for Alerts 📧"

        )





        family_phone=st.text_input(

            "Family Phone for Calls/SMS 📞"

        )






        st.info(

            "OTP, medicine reminders, emergency email and calls will be sent here"

        )








        # ================= SEND OTP =================


        if st.button(

            "Send OTP"

        ):





            if family_email=="":




                st.warning(

                    "Enter family email first"

                )






            else:




                status=send_otp(

                    family_email

                )






                if status:




                    st.success(

                        "OTP Sent Successfully 📩"

                    )





                else:




                    st.error(

                        "OTP Sending Failed ❌ Check Gmail Settings"

                    )









        otp=st.text_input(

            "Enter OTP"

        )








    else:




        otp="verified"













    # ================= REGISTER BUTTON =================


    if st.button(

        "Register"

    ):







        # ================= PATIENT REGISTER =================


        if role=="Patient":







            if (

                family_email==""

                or

                family_phone==""

            ):





                st.warning(

                    "Enter family email and phone number"

                )



                return









            if verify_otp(

                family_email,

                otp

            ):






                result=add_user(

                    name,

                    password,

                    role,

                    family_email,

                    family_phone

                )








                if result:




                    st.success(

                        "Account Created Successfully ✅"

                    )







                else:




                    st.error(

                        "Username already exists ❌"

                    )









            else:




                st.error(

                    "Invalid OTP Verification Failed ❌"

                )










        # ================= DOCTOR / FAMILY REGISTER =================


        else:







            result=add_user(

                name,

                password,

                role,

                "",

                ""

            )








            if result:




                st.success(

                    "Account Created Successfully ✅"

                )






            else:




                st.error(

                    "Username already exists ❌"

                )
















# ================= LOGIN PAGE =================


def login_page():




    st.subheader(

        "🔐 Login"

    )







    name=st.text_input(

        "Username"

    )






    password=st.text_input(

        "Password",

        type="password"

    )









    if st.button(

        "Login"

    ):







        user=check_user(

            name,

            password

        )








        if user:







            st.session_state.login=True



            st.session_state.user=user[1]



            st.session_state.role=user[3]








            st.success(

                "Login Successful ✅"

            )







            st.rerun()









        else:





            st.error(

                "Invalid Username or Password ❌"

            )