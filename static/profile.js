var image_preview = document.getElementById("img_preview");
var image_input = document.getElementById("profile_picture_link");

image_input.addEventListener("input", function () {
    image_preview.src = this.value;
});