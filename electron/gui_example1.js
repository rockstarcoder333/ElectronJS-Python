const ipc = require('electron').ipcRenderer;
const spawn = require("child_process").spawn;
var nodeConsole = require('console');
var my_console = new nodeConsole.Console(process.stdout, process.stderr);
const {remote} = require('electron');

var v_speed = 0;
var v_size = 0;
var count;
var count1;
var pythonProcess;

function print_both(str) {
    console.log('Javascript: ' + str);
    my_console.log('Javascript: ' + str);
}

function callback(resultValue){
    return resultValue;
}

async function start_count(speed, size, flag) {
    
    var result = 0
    const pythonProcess = spawn('python',["./external_programs/bean_counting.py", speed, size, flag]);
    if (flag == "start"){
        await new Promise((resolve, reject)=>{
            pythonProcess.stdout.on('data', (data) => {
                var qa_result = JSON.parse(data.toString());
                result = qa_result.count;
                resolve('done');
            });
            pythonProcess.stderr.on('data', (data) => {
                console.log("Error in python code::", data.toString())
                reject('error');
            });
        });
        return result;
    }
    else{
        // pythonProcess.kill();
        // pythonProcess.kill('SIGKILL')
        pythonProcess.stdin.write(flag);
        pythonProcess.stdout.on('data', (data) => {
            print_both('Following data has been piped from python program: ' + data.toString('utf8'));
        });
        pythonProcess.stdin.pause();
        pythonProcess.kill('SIGINT');
        // pythonProcess.stdin.end();
    }
    
}

// click calibration btn
async function calibration(evt) {
    document.getElementById("setting_container").style.display = 'none';
    document.getElementById("main_container").style.display = 'block';
    var elem_start = document.getElementById("btn_start");
    var elem_reset = document.getElementById("btn_reset");
    var elem_setting = document.getElementById("btn_setting");
    var elem_count_result = document.getElementById("h_count_result");
    var elem_v_speed = document.getElementById("v_speed");
    var elem_v_size = document.getElementById("v_size");
    // click start button
    // inactive contine
    elem_start.value = "Continue";
    elem_start.style.background = 'rgb(122, 136, 142)';
    elem_start.disabled = true;
    elem_start.style.cursor="default";
    // active stop
    elem_reset.value = "Stop";
    elem_reset.style.background = 'rgb(26, 22, 45)';
    elem_reset.disabled = false;
    elem_reset.style.cursor="pointer";
    // inactive setting
    elem_setting.style.background = 'url(../img/setting_btn_disabled.png)';
    elem_setting.style.pointerEvents = 'none';

    // call python counting function
    v_speed = elem_v_speed.value;
    v_size = elem_v_size.value;
    count = await start_count(v_speed, v_size, 'start');
    elem_count_result.innerHTML = count;
}

// click start&continue btn
async function start_continue_count(evt) {
    var elem_start = document.getElementById("btn_start");
    var elem_reset = document.getElementById("btn_reset");
    var elem_setting = document.getElementById("btn_setting");
    var elem_count_result = document.getElementById("h_count_result");
    var elem_v_speed = document.getElementById("v_speed");
    var elem_v_size = document.getElementById("v_size");
    // click start button
    if (elem_start.value == "Start") { 
        // inactive contine
        elem_start.value = "Continue";
        elem_start.style.background = 'rgb(122, 136, 142)';
        elem_start.disabled = true;
        elem_start.style.cursor="default";
        // active stop
        elem_reset.value = "Stop";
        elem_reset.style.background = 'rgb(26, 22, 45)';
        elem_reset.disabled = false;
        elem_reset.style.cursor="pointer";
        // inactive setting
        elem_setting.style.background = 'url(../img/setting_btn_disabled.png)';
        elem_setting.style.pointerEvents = 'none';

        // call python counting function
        v_speed = elem_v_speed.value;
        v_size = elem_v_size.value;
        count = await start_count(v_speed, v_size, 'start');
        elem_count_result.innerHTML = count;
    }

    // click continue button
    else if (elem_start.value == "Continue" && elem_start.style.background == 'rgb(26, 22, 45)') {
        // inactive start
        elem_start.style.background = 'rgb(122, 136, 142)';
        elem_start.disabled = true;
        elem_start.style.cursor="default";
        // active stop
        elem_reset.value = "Stop";
        // inactive setting
        elem_setting.style.background = 'url(../img/setting_btn_disabled.png)';
        elem_setting.style.pointerEvents = 'none';

        count1 = await start_count(v_speed, v_size, 'start', callback);
        count = parseInt(count) + parseInt(count1)
        elem_count_result.innerHTML = count;
    }

}

// click rest&stop btn
function reset_stop(evt) {
    var elem_start = document.getElementById("btn_start");
    var elem_reset = document.getElementById("btn_reset");
    var elem_setting = document.getElementById("btn_setting");
    var elem_count_result = document.getElementById("h_count_result");
    // click stop button
    if (elem_reset.value == "Stop") {
        // active reset
        elem_reset.value = "Reset";
        elem_reset.style.background = 'rgb(26, 22, 45)';
        elem_reset.disabled = false;
        elem_reset.style.cursor="pointer";
        // active contine
        elem_start.value = "Continue";
        elem_start.style.background = 'rgb(26, 22, 45)';
        elem_start.disabled = false;
        elem_start.style.cursor="pointer";

        elem_setting.style.background = 'url(../img/setting_btn.png)';
        elem_setting.style.pointerEvents = 'auto';

        count = start_count(1, 1, 'stop');
    }
    // click reset button
    else if (elem_reset.value == "Reset") {
        // inactive reset
        elem_reset.style.background = 'rgb(122, 136, 142)';
        elem_reset.disabled = true;
        elem_reset.style.cursor="default";
        // active start
        elem_start.value = "Start";
        // active setting
        elem_setting.style.background = 'url(../img/setting_btn.png)';
        elem_setting.style.pointerEvents = 'auto';

        elem_count_result.innerHTML = 0;
        count = 0;
        count1 = 0;
    }

}

// click setting btn
function setting(evt) {
    document.getElementById("setting_container").style.display = 'block';
    document.getElementById("main_container").style.display = 'none';
}

// click back_arrow btn
function back_to_main(evt) {
    document.getElementById("setting_container").style.display = 'none';
    document.getElementById("main_container").style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("btn_start").addEventListener("click", start_continue_count);
    document.getElementById("btn_reset").addEventListener("click", reset_stop);
    document.getElementById("btn_setting").addEventListener("click", setting);
    document.getElementById("btn_backarrow").addEventListener("click", back_to_main);
    document.getElementById("btn_calibration").addEventListener("click", calibration);

});