function addSetsFields() {
    var exercise = document.getElementById('exerciseSelect').value;
    var sets = document.getElementById('setsInput').value;
    var setsFieldsContainer = document.getElementById('setsFieldsContainer');
    var setsFields = document.createElement('div');
    setsFields.className = 'setsFields';
    setsFields.innerHTML = 'Set 1 <label for="repsInput1">Reps:</label><input type="number" id="repsInput1" min="1" value="1"><label for="weightInput1">Weight:</label><input type="number" id="weightInput1" min="0" value="0">kg';
    for (var i = 0; i < sets - 1; i++) {
        a = i + 2;
        setsFields.innerHTML += '<br>Set '+ a +' <label for="repsInput'+ a +'">Reps:</label><input type="number" id="repsInput'+ a +'" min="1" value="1"><label for="weightInput'+ a +'">Weight:</label><input type="number" id="weightInput'+ a +'" min="0" value="0">kg';
    }
    setsFields.innerHTML += '<br><button onclick="saveRepsWeight()">Save</button>';
    if (setsFieldsContainer.childElementCount > 0) {
        setsFieldsContainer.innerHTML = '';
    }
    setsFieldsContainer.appendChild(setsFields);
}
function saveRepsWeight() {
    var ListRepWeight = [];
    var sets = document.getElementById('setsInput').value;
    for (var i = 1; i <= sets; i++) {
        var reps = document.getElementById('repsInput'+i).value;
        var weight = document.getElementById('weightInput'+i).value;
        ListRepWeight.push([reps, weight]);
    }
    console.log(ListRepWeight);
    var setsFieldsContainer = document.getElementById('setsFieldsContainer');
    setsFieldsContainer.innerHTML = '';
    var exerciseListContainer = document.getElementById('exercise-list');
    var exercise = document.getElementById('exerciseSelect').value;
    var exerciseList = document.createElement('div');
    exerciseList.className = 'exerciseList';
    List2 = [];
    for (let index = 0; index < ListRepWeight.length; index++) {
        List2.push('Set ' + (index + 1) + ': ' + ListRepWeight[index][0] + ' reps, ' + ListRepWeight[index][1] + 'kg');
    }
    exerciseList.innerHTML = exercise + '<br> ' + List2.join(', <br>');
    exerciseListContainer.appendChild(exerciseList);
}