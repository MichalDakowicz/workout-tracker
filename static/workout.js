// Set the current date as the default value for the date input
document.getElementById("dateInput").valueAsDate = new Date();

function addSetsFields() {
    const sets = document.getElementById("setsInput").value;
    const setsFieldsContainer = document.getElementById("setsFieldsContainer");
    const setsFields = document.createElement("div");
    setsFields.className = "setsFields";

    // Initialize the innerHTML with the first set
    setsFields.innerHTML =
        'Set 1 <label for="repsInput1">Reps:</label><input type="number" id="repsInput1" min="1" value="1"><label for="weightInput1">Weight:</label><input type="number" id="weightInput1" min="0" value="0">kg';

    // Add the remaining sets
    for (let i = 1; i < sets; i++) {
        const setNumber = i + 1;
        setsFields.innerHTML += `<br>Set ${setNumber} <label for="repsInput${setNumber}">Reps:</label><input type="number" id="repsInput${setNumber}" min="1" value="1"><label for="weightInput${setNumber}">Weight:</label><input type="number" id="weightInput${setNumber}" min="0" value="0">kg`;
    }

    // Add the save button
    setsFields.innerHTML +=
        '<br><button onclick="saveRepsWeight()">Save</button>';

    // Clear the container and add the new fields
    setsFieldsContainer.innerHTML = "";
    setsFieldsContainer.appendChild(setsFields);
}

function saveRepsWeight() {
    const sets = document.getElementById("setsInput").value;
    const ListRepWeight = [];

    // Collect the reps and weight for each set
    for (let i = 1; i <= sets; i++) {
        const reps = document.getElementById(`repsInput${i}`).value;
        const weight = document.getElementById(`weightInput${i}`).value;
        ListRepWeight.push([reps, weight]);
    }

    // Clear the sets fields and display the exercise list
    const setsFieldsContainer = document.getElementById("setsFieldsContainer");
    setsFieldsContainer.innerHTML = "";

    const exerciseListContainer = document.getElementById("exercise-list");
    const exercise = document.getElementById("exerciseSelect").value;
    const exerciseList = document.createElement("div");
    exerciseList.className = "exerciseList";

    const List2 = ListRepWeight.map(
        (set, index) => `Set ${index + 1}: ${set[0]} reps, ${set[1]}kg`
    );

    exerciseList.innerHTML = `${exercise}<br> ${List2.join(", <br>")}`;
    exerciseListContainer.appendChild(exerciseList);
}

function saveWorkout() {
    const date = document.getElementById("dateInput").value;
    const exerciseListContainer = document.getElementById("exercise-list");
    const exerciseList =
        exerciseListContainer.getElementsByClassName("exerciseList");
    const exercises = [];
    let name = document.getElementById("workoutName").value;

    if (name === "") {
        name = "Workout";
    }

    for (let index = 0; index < exerciseList.length; index++) {
        const exerciseText = exerciseList[index].innerText;
        const exerciseParts = exerciseText.split("\n");
        const exerciseName = exerciseParts[0];
        const sets = exerciseParts.slice(1).map((setText) => {
            const setTextParts = setText.split(", ");
            const reps = parseInt(setTextParts[0].split(" ")[2]);
            const weight = parseInt(setTextParts[1].split(" ")[0]);
            return [reps, weight];
        });
        exercises.push({ [exerciseName]: sets });
    }

    const dateInput = document.getElementById("date");
    const exercisesInput = document.getElementById("exercises");
    dateInput.value = date;
    exercisesInput.value = JSON.stringify({ [name]: exercises });

    document
        .getElementById("return-form")
        .getElementsByTagName("input")[2]
        .click();
}
