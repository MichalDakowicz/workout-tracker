// Set the current date as the default value for the date input
document.getElementById("dateInput").valueAsDate = new Date();

function addSetsFields() {
    const num = document.getElementsByClassName("setsFields").length + 1;
    const setsFieldsContainer = document.getElementById("setsFieldsContainer");
    const setsFields = document.createElement("div");
    setsFields.className = "setsFields";
    const buttons = document.getElementById("buttons");

    // Initialize the innerHTML with the first set
    setsFields.innerHTML = `<input type="number" id="repsInput${num}" min="1" placeholder="Set ${num} reps"><input type="number" id="weightInput${num}" min="0" placeholder="Weight (kg)">`;

    // Remove the previous Remove Set button if it exists
    try {
        const removeSetButton = document.getElementById("remove-set-button");
        if (removeSetButton) {
            removeSetButton.remove();
        }
    } catch (error) {
        console.log("No remove set button found");
    }

    if (num > 1) {
        // Add Remove Set Button
        setsFields.innerHTML += `<button id="remove-set-button" onclick="removeSetsFields()">Remove Set</button>`;
    }

    // Remove the save button and previous Add Set button
    const saveButton = document.getElementById("save-button");
    if (saveButton) {
        saveButton.remove();
    }
    const addSetButton = document.getElementById("add-set-button");
    if (addSetButton) {
        addSetButton.remove();
    }

    // Add the save button
    buttons.innerHTML += `<button id="add-set-button" onclick="addSetsFields(${
        num + 1
    })">Add Set</button><button id="save-button" onclick="saveRepsWeight()">Save reps</button>`;

    setsFieldsContainer.appendChild(setsFields);
}

function removeSetsFields() {
    const setsFields = document.getElementsByClassName("setsFields");

    // Remove the last set
    setsFields[setsFields.length - 1].remove();

    // If more than one set exists, add the remove set button
    if (setsFields.length > 1) {
        setsFields[
            setsFields.length - 1
        ].innerHTML += `<button id="remove-set-button" onclick="removeSetsFields()">Remove Set</button>`;
    }
}
function saveRepsWeight() {
    const ListRepWeight = [];
    const sets = document.getElementsByClassName("setsFields").length;
    console.log(sets);

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
