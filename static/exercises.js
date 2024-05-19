function displayExercises() {
    var group = document.getElementById("muscle-group-select").value;
    var exerciseList = document.getElementById("exercise-lists");

    exerciseList
        .querySelectorAll("div[class^='exercise-container']")
        .forEach(function (element) {
            if (element.id === group) {
                element.style.display = "block";
            } else {
                element.style.display = "none";
            }
        });
}

addEventListener("load", displayExercises);
onchange = displayExercises;
