function bmi() {
    var weight = document.getElementById('weight').value;
    var height = document.getElementById('height').value;
    var bmi = weight / (height / 100 * height / 100);
    document.getElementById('bmi').innerHTML = bmi.toFixed(2);
}
        