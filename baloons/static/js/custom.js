// input control. Users input values less than "min", more than "max"
function enforceMinMax(el){
  if(el.value != ""){
    if(parseInt(el.value) < parseInt(el.min)){
      el.value = el.min;
    }
    if(parseInt(el.value) > parseInt(el.max)){
      el.value = el.max;
    }
  }
}

// adding eventListeners
var inputNumbers = document.querySelectorAll(".amount input[type=number]");
inputNumbers.forEach(() => addEventListener("keyup", () => enforceMinMax(event.target)));
