from apscheduler.schedulers.background import BackgroundScheduler

from src.reminder import check_medicine_time
from src.escalation import check_escalation


# ================= GLOBAL SCHEDULER =================

scheduler = None


# ================= START SCHEDULER =================

def start_scheduler():

    global scheduler

    try:

        if scheduler is not None and scheduler.running:
            return

        scheduler = BackgroundScheduler()

        # ================= MEDICINE REMINDER =================

        scheduler.add_job(

            check_medicine_time,

            trigger="interval",

            minutes=1,

            id="medicine_reminder_job",

            replace_existing=True,

            misfire_grace_time=30,

            coalesce=True

        )

        # ================= ESCALATION =================

        scheduler.add_job(

            check_escalation,

            trigger="interval",

            minutes=30,

            id="medicine_escalation_job",

            replace_existing=True

        )

        scheduler.start()

        print("Medicine Scheduler Started")

    except Exception as e:

        print("SCHEDULER ERROR:", e)


# ================= STOP SCHEDULER =================

def stop_scheduler():

    global scheduler

    if scheduler is not None:

        scheduler.shutdown(wait=False)

        scheduler = None

        print("Scheduler Stopped")