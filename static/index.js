
function setListeners() {
    var set_alarm_button = document.getElementById("set_alarm_button");
    var clear_alarm_button = document.getElementById("clear_alarm_button");
    var set_alarm_form = document.getElementById("set_alarm_form");
    var server_response = document.getElementById("server_response");
    //server_response.style.visibility = "hidden";


    set_alarm_button.addEventListener("click", function () {
        var alarm_clock_value = document.getElementById("clock-picker").value;
        //alert(alarm_clock_value);
        request = {url:"/alarm", data:alarm_clock_value};
        sendRequest(request);
        set_alarm_form.setAttribute("onsubmit", "return false;");
    });

    clear_alarm_button.addEventListener("click", function () {
        alert("Alarm cleared");
        request = {url:"/alarm", data:"clear alarm"};
        sendRequest(request);
        set_alarm_form.setAttribute("onsubmit", "return false;");
    });
}

function sendRequest(alarmRequest) {
    var server_response = document.getElementById("server_response");

    var request = new XMLHttpRequest();
    console.log("request: ", alarmRequest);
    request.open("POST", alarmRequest.url, true);
    var request_data = {alarm_data:alarmRequest.data};

    request.onreadystatechange = function () {
        //console.log("Got response from server!");
        if (this.readyState === 4) {
            console.log("Got response from server!", this.responseText);
            var response = JSON.parse(this.responseText).message;
            if (this.status === 200) {
                server_response.style.display = "block";
                server_response.style.visibility = "visibility";
                server_response.textContent = response;
            }

            //else if (this.status === 401) {
            else{
                server_response.style.display = "block";
                server_response.style.visibility = "visibility";
                server_response.textContent = "Dickssszz";
            }
        }
    };
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(request_data));

}

window.onload = function () {
    setListeners();
};
