
function setListeners() {
    var set_alarm_button = document.getElementById("set_alarm_button");
    var alarm_clock_form = document.getElementById("alarm_clock_form");

    set_alarm_button.addEventListener("click", function () {
        alert("NU GÅR LARMET!!!");
        alarm_clock_form.setAttribute("onsubmit", "return false;");
    });
}

window.onload = function (ev) {
    setListeners();
};
