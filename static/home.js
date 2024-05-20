function bmi() {
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value;
    var bmi = weight / (((height / 100) * height) / 100);
    document.getElementById("bmi").innerHTML = bmi.toFixed(2);

    if (bmi < 18.5) {
        document.getElementById("level").innerHTML = "Underweight";
        document.getElementById("level").style.backgroundColor = "#00eeff";
        document.getElementById("level").style.color = "#000";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        document.getElementById("level").innerHTML = "Normal";
        document.getElementById("level").style.backgroundColor = "#00ff22";
        document.getElementById("level").style.color = "#000";
    } else if (bmi >= 25 && bmi <= 29.9) {
        document.getElementById("level").innerHTML = "Overweight";
        document.getElementById("level").style.backgroundColor = "#eeff00";
        document.getElementById("level").style.color = "#000";
    } else if (bmi >= 30 && bmi <= 34.9) {
        document.getElementById("level").innerHTML = "Obesity";
        document.getElementById("level").style.backgroundColor = "#ffb700";
        document.getElementById("level").style.color = "#fff";
    } else {
        document.getElementById("level").innerHTML = "Extreme Obesity";
        document.getElementById("level").style.backgroundColor = "#ff2200";
        document.getElementById("level").style.color = "#fff";
    }

    bmiPercentage = ((bmi - 17) / 18) * 100;

    if (bmiPercentage > 98.5) {
        bmiPercentage = 98.5;
    } else if (bmiPercentage < 0) {
        bmiPercentage = 0;
    }

    document.getElementById("marker").style.left = bmiPercentage + "%";
}
