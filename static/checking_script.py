from time import sleep
import tv_alarm_script
import datetime


def check_alarm_times():
    # byt mot "/home/pi/my_flask_server/my_pi_server/alarm_times.txt" i Pi'en
    with open("C:\\Users\\natof\git\my_pi_server\\alarm_times.txt", "r") as f:
        alarm_time = f.readlines()
        now = datetime.datetime.now()
        print(alarm_time)
        if alarm_time[0] == str(now)[11:16]:
            tv_alarm_script.run()
            print("Running script!")
            sleep(60)
        else:
            print("Schlepping!")
            sleep(59)


while True:
    check_alarm_times()
