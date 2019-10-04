from flask import Flask, render_template, request, jsonify
import ir_sender, time, tv_alarm_script, datetime


app = Flask(__name__)
app.debug = True


def get_alarm_times():
    # byt mot "/home/pi/my_flask_server/my_pi_server/alarm_times.txt" i Pi'en
    with open("C:\\Users\\natof\git\my_pi_server\\alarm_times.txt", "r") as f:
        alarm_times = f.readlines()
        if alarm_times:
            response = alarm_times[0]
        else:
            response = ""
        return response


@app.route('/')
def render_start_page():
    alarm_time = get_alarm_times()
    return render_template('index.html', current_alarm=alarm_time)


@app.route('/remote_control', methods=['POST'])
def remote_control():
    button_request = request.get_json()['request_data']
    print("request_data = ", button_request)
    ir_sender.send(button_request)
    response = {
        'status': "200",
        'message': "",
        'data': ""
    }
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@app.route('/alarm', methods=['POST'])
def set_alarm():
    # byt mot "/home/pi/my_flask_server/my_pi_server/alarm_times.txt" i Pi'en
    with open("C:\\Users\\natof\git\my_pi_server\\alarm_times.txt", "w+") as f:
        alarm_request = request.get_json()['request_data']
        alarm_time = alarm_request[0:5]
        f.write(alarm_time)
        response = {
            'status': "200",
            'message': str(alarm_time),
            'data': ""
        }
        resp = jsonify(response)
        resp.status_code = 200
        return resp


@app.route('/clear_alarm', methods=['POST'])
def clear_alarm():
    with open("C:\\Users\\natof\git\my_pi_server\\alarm_times.txt", "w+") as f:
        f.write("")
        response = {
            'status': "200",
            'message': "Alarm cleared",
            'data': ""
        }
        resp = jsonify(response)
        resp.status_code = 200
        return resp


if __name__ == '__main__':
    app.run()
