function toggle(id) {
  var ele = document.getElementById("panel-"+id);
  var text = document.getElementById("heading-"+id);
  if(window.getComputedStyle(ele).display == "block") {
    ele.style.display = "none";
    text.innerHTML = "Click to expand";
  }
  else {
    ele.style.display = "block";
    text.innerHTML = "";
  }
}
