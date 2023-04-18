function task1Open() {
    hideAlltasks();
    let x = document.getElementById("task1");
    x.style.display = "block";
}

function task2Open() {
    hideAlltasks();
    let x = document.getElementById("task2");
    x.style.display = "block";
}

function task3Open() {
    hideAlltasks();
    let x = document.getElementById("task3");
    x.style.display = "block";
}
function hideAlltasks() {
    for (i of document.querySelectorAll(".task")) {
        i.style.display = "none";
    }
}