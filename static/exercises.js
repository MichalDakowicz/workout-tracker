function displayExercises() {
    var group = document.getElementById("muscle-group-select").value;

    if (group === "chest") {
        document.getElementById("chest").style.display = "block";
        document.getElementById("back").style.display = "none";
        document.getElementById("shoulders").style.display = "none";
        document.getElementById("legs").style.display = "none";
        document.getElementById("arms").style.display = "none";
        document.getElementById("core").style.display = "none";
    } else if (group === "back") {
        document.getElementById("chest").style.display = "none";
        document.getElementById("back").style.display = "block";
        document.getElementById("shoulders").style.display = "none";
        document.getElementById("legs").style.display = "none";
        document.getElementById("arms").style.display = "none";
        document.getElementById("core").style.display = "none";
    } else if (group === "shoulders") {
        document.getElementById("chest").style.display = "none";
        document.getElementById("back").style.display = "none";
        document.getElementById("shoulders").style.display = "block";
        document.getElementById("legs").style.display = "none";
        document.getElementById("arms").style.display = "none";
        document.getElementById("core").style.display = "none";
    } else if (group === "legs") {
        document.getElementById("chest").style.display = "none";
        document.getElementById("back").style.display = "none";
        document.getElementById("shoulders").style.display = "none";
        document.getElementById("legs").style.display = "block";
        document.getElementById("arms").style.display = "none";
        document.getElementById("core").style.display = "none";
    } else if (group === "arms") {
        document.getElementById("chest").style.display = "none";
        document.getElementById("back").style.display = "none";
        document.getElementById("shoulders").style.display = "none";
        document.getElementById("legs").style.display = "none";
        document.getElementById("arms").style.display = "block";
        document.getElementById("core").style.display = "none";
    } else if (group === "abs") {
        document.getElementById("chest").style.display = "none";
        document.getElementById("back").style.display = "none";
        document.getElementById("shoulders").style.display = "none";
        document.getElementById("legs").style.display = "none";
        document.getElementById("arms").style.display = "none";
        document.getElementById("core").style.display = "block";
    }
}

addEventListener("load", displayExercises);
onchange = displayExercises;
