from flask import Flask, render_template, request, jsonify
import ir_sender, time, tv_alarm_script, datetime
from threading import Timer
from threading import Thread


app = Flask(__name__)
app.debug = True

def check_alarm_times():
    with open("alarm_times.txt", "r") as f:
    #if f.mode == "r":
        alarm_times = f.readlines()
        now = datetime.datetime.now()
        for time in alarm_times:
            print("time = " + str(time))
            #if time == now:
            #    tv_alarm_script.run()

    #f.write("%s\n" % line.strip())


@app.route('/')
def render_start_page():
    return render_template('index.html')


@app.route('/remote_control', methods=['POST'])
def remote_control():
    button_request = request.get_json()['button_request']
    ir_sender.send(button_request)


timer = None

@app.route('/alarm', methods=['POST'])
def set_alarm():
    print("ALARM BITCHES!!!")
    #f = open("alarm_times.txt", "w+")
    with open("C:\Users\\natof\git\my_pi_server\\alarm_times.txt", "w+") as f:
        alarm_request = request.get_json()['alarm_data']
        alarm_request_hour = int(alarm_request[0:2])
        alarm_request_minute = int(alarm_request[3:5])
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        alarm_time = str(datetime.datetime(year, month, day, alarm_request_hour, alarm_request_minute, 0))
        f.write(alarm_time)

    return "Done"

    #alarm_request_hour = int(alarm_request[0:2])
    #alarm_request_minute = int(alarm_request[3:5])


def alarm():
    alarm_request = request.get_json()['alarm_data']
    if alarm_request != "clear alarm":
        alarm_request_hour = int(alarm_request[0:2])
        alarm_request_minute = int(alarm_request[3:5])
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        current_time = datetime.datetime(year,month,day,hour,minute,second)
        alarm_time = datetime.datetime(year, month, day, alarm_request_hour, alarm_request_minute, 0)
        time_diff = (alarm_time-current_time).total_seconds()
        if time_diff < 0:
            seconds_in_a_day = 24*3600
            time_diff = seconds_in_a_day + time_diff
        print("time_diff = " + str(time_diff))
        timer = Timer(time_diff, tv_alarm_script.run)
        timer.start()
        response = {
            'status': "200",
            'message': "Alarm set",
            'data': ""
        }
        resp = jsonify(response)
        resp.status_code = 200
        return resp
    else:
        response = {
            'status': "200",
            'message': "Alarm stopped",
            'data': ""
        }
        resp = jsonify(response)
        resp.status_code = 200
        return resp


if __name__ == '__main__':
    app.run()
