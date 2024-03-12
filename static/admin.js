function checkGroupDisplayMuscles() {
    var group = document.getElementById("group").value;
    var muscle = document.getElementById("muscle");
    if (group === "Chest") {
        // Upper, Middle, Lower
        muscle.innerHTML =
            '<option value="Upper Chest">Upper Chest</option><option value="Middle Chest">Middle Chest</option><option value="Lower Chest">Lower Chest</option>';
    } else if (group === "Back") {
        // Lat, Middle, Lower
        muscle.innerHTML =
            '<option value="Lat">Lat</option><option value="Middle Back">Middle Back</option><option value="Lower Back">Lower Back</option>';
    } else if (group === "Legs") {
        // Quads, Hamstrings, Calves, Glutes, Adductors, Abductors, Tibialis
        muscle.innerHTML =
            '<option value="Quads">Quads</option><option value="Hamstrings">Hamstrings</option><option value="Calves">Calves</option><option value="Glutes">Glutes</option><option value="Adductors">Adductors</option><option value="Abductors">Abductors</option><option value="Tibialis">Tibialis</option>';
    } else if (group === "Shoulders") {
        // Front, Side, Rear, Traps, Rotator Cuff
        muscle.innerHTML =
            '<option value="Front Delts">Front Delts</option><option value="Side Delts">Side Delts</option><option value="Rear Delts">Rear Delts</option><option value="Traps">Traps</option><option value="Rotator Cuff">Rotator Cuff</option>';
    } else if (group === "Arms") {
        // Biceps, Triceps, Forearms
        muscle.innerHTML =
            '<option value="Biceps">Biceps</option><option value="Triceps">Triceps</option><option value="Forearms">Forearms</option>';
    } else if (group === "Core") {
        // Upper, Middle, Lower, Oblique
        muscle.innerHTML =
            '<option value="Upper Abs">Upper Abs</option><option value="Middle Abs">Middle Abs</option><option value="Lower Abs">Lower Abs</option><option value="Oblique">Oblique</option>';
    }
}
document
    .getElementById("group")
    .addEventListener("change", checkGroupDisplayMuscles);
checkGroupDisplayMuscles();
