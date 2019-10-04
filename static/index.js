
function setListeners() {
    var set_alarm_button = document.getElementById("set_alarm_button");
    var clear_alarm_button = document.getElementById("clear_alarm_button");
    var set_alarm_form = document.getElementById("set_alarm_form");
    var pwr_btn = document.getElementById("pwr_btn");
    var mute_btn = document.getElementById("mute_btn");
    var tv_radio_btn = document.getElementById("tv_radio_btn");
    var volume_up_btn = document.getElementById("volume_up_btn");
    var volume_down_btn = document.getElementById("volume_down_btn");
    var channel_up_btn = document.getElementById("channel_up_btn");
    var channel_down_btn = document.getElementById("channel_down_btn");
    var ch1_btn = document.getElementById("ch1_btn");
    var ch2_btn = document.getElementById("ch2_btn");
    var ch3_btn = document.getElementById("ch3_btn");
    var ch4_btn = document.getElementById("ch4_btn");
    var ch5_btn = document.getElementById("ch5_btn");
    var ch6_btn = document.getElementById("ch6_btn");
    var ch7_btn = document.getElementById("ch7_btn");
    var ch8_btn = document.getElementById("ch8_btn");
    var ch9_btn = document.getElementById("ch9_btn");

    var server_response = document.getElementById("server_response");
    //server_response.style.visibility = "hidden";


    set_alarm_button.addEventListener("click", function () {
        var alarm_clock_value = document.getElementById("clock-picker").value;
        //alert(alarm_clock_value);
        var request = {url:"/alarm", data:alarm_clock_value};
        sendRequest(request);
        set_alarm_form.setAttribute("onsubmit", "return false;");
    });

    clear_alarm_button.addEventListener("click", function () {
       // alert("Alarm cleared");
        var request = {url:"/clear_alarm", data:""};
        sendRequest(request);
        set_alarm_form.setAttribute("onsubmit", "return false;");
    });
}

function remoteControlSender(buttonRequest) {
    var request = {url:"/remote_control", data:buttonRequest};
    sendRequest(request);
}

function sendRequest(newRequest) {
    var server_response = document.getElementById("server_response");

    var request = new XMLHttpRequest();
    console.log("request: ", newRequest);
    request.open("POST", newRequest.url, true);
    var request_data = {request_data:newRequest.data};

    request.onreadystatechange = function () {
        //console.log("Got response from server!");
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText).message;
            console.log("Got response from server!", response);
            if (this.status === 200) {
                server_response.style.display = "block";
                server_response.style.visibility = "visible";
                if(response){
                    server_response.textContent = "Current alarm: " + response;
                }else{
                    server_response.textContent = "";
                }
            }
            //else if (this.status === 401) {
            else{
                server_response.style.display = "block";
                server_response.style.visibility = "visible";
                server_response.textContent = "Something went wrong!";
            }
        }
    };
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(request_data));

}

window.onload = function () {
    setListeners();
};
