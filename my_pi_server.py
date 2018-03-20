from flask import Flask, render_template, request, jsonify
import ir_sender, time, tv_alarm_script, datetime
from threading import Timer


app = Flask(__name__)
app.debug = True


@app.route('/')
def render_start_page():
    return render_template('index.html')


@app.route('/remote_control', methods=['POST'])
def remote_control():
    button_request = request.get_json()['button_request']
    ir_sender.send(button_request)


timer = None

@app.route('/alarm', methods=['POST'])
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
        timer.cancel()
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
