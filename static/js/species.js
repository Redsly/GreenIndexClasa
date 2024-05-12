function hoverAnimation(element) {
    element.style.transition = "transform 0.5s";
    element.style.transform = "scale(2)"; 
}

function resetAnimation(element) {
    element.style.transition = "transform 0.5s"; 
    element.style.transform = "scale(1)"; 
}
