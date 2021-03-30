from apscheduler.schedulers.blocking import BlockingScheduler
from app import din, don, bom
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=30)
def print_interval():
    din()

@sched.scheduled_job('cron', day_of_week='fri', hour='15-19/2', timezone='Europe/Moscow')
def print_one():
    don()


@sched.scheduled_job('cron', day_of_week='fri', hour='12', minute='48', timezone='Europe/Moscow')
def print_one_crone():
    bom()