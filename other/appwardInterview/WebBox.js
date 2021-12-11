let idCounter = 0;
let previousSelection = null;
let invert = false;
function hexToRGBA(hex, trans) {
  var c;
  try {
    if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
      c = hex.substring(1).split("");
      if (c.length == 3) {
        c = [c[0], c[0], c[1], c[1], c[2], c[2]];
      }
      c = "0x" + c.join("");
      return (
        "rgba(" +
        [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(",") +
        "," +
        trans +
        ")"
      );
    }
  } catch (e) {
    console.log("Bad Hex! Recalculating");
    var randColor = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
    hexToRGBA(randColor, trans);
  }
}

function createDivs() {
  var resizable = document.createElement("div");
  resizable.id = "mover" + idCounter;
  resizable.className = "resizable" + idCounter;
  resizable.classList.add("resizable");
  var randColor = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
  //--------Create random gradient background
  range1 = hexToRGBA(randColor, 0);
  range2 = hexToRGBA(randColor, 1);
  resizable.style.backgroundImage =
    "linear-gradient(" + range1 + "," + range2 + ")";
  resizable.setAttribute("border-color", randColor);
  resizable.setAttribute("count", idCounter);
  //-----Next Level
  var resizers = document.createElement("div");
  resizers.id = "resizers" + idCounter;
  resizers.className = "resizers" + idCounter;
  resizers.style.height = "100%";
  resizable.appendChild(resizers);
  //-----Next Level Mover && (Resize Corners)
  var mover = document.createElement("div");
  mover.id = "movermiddle" + idCounter;
  mover.className = "mover" + idCounter;
  mover.setAttribute("count", idCounter);
  mover.classList.add("mover");
  mover.innerHTML = "<p>Identifier:  " + idCounter + "</p>";
  mover.style.color = randColor;
  resizers.appendChild(mover);
  //CREATE RESIZERS
  var list = [
    "single-top",
    "single-bottom",
    "single-left",
    "single-right",
    "top-left",
    "top-right",
    "bottom-left",
    "bottom-right",
  ];
  var idsList = [
    "resizerT",
    "resizerB",
    "resizerL",
    "resizerR",
    "resizerTL",
    "resizerTR",
    "resizerBL",
    "resizerBR",
  ];
  var resizerT = document.createElement("div");
  var resizerB = document.createElement("div");
  var resizerL = document.createElement("div");
  var resizerR = document.createElement("div");
  var resizerTL = document.createElement("div");
  var resizerTR = document.createElement("div");
  var resizerBL = document.createElement("div");
  var resizerBR = document.createElement("div");
  var resizeVars = [
    resizerT,
    resizerB,
    resizerL,
    resizerR,
    resizerTL,
    resizerTR,
    resizerBL,
    resizerBR,
  ];
  for (var i = 0; i < resizeVars.length; i++) {
    resizeVars[i].id = idsList[i] + idCounter;
    resizeVars[i].className = "resizer" + idCounter + " " + list[i];
    resizeVars[i].classList.add(list[i]);
    resizeVars[i].classList.add("resizers");
    resizeVars[i].setAttribute("count", idCounter);
    resizers.appendChild(resizeVars[i]);
  }
  arrCorn = [resizerTL, resizerTR, resizerBL, resizerBR];
  for (var i = 0; i < arrCorn.length; i++) {
    arrCorn[i].classList.add("corners");
  }
  var arrLR = [resizerL, resizerR];
  for (var i = 0; i < arrLR.length; i++) {
    arrLR[i].classList.add("leftright");
  }
  var arrTB = [resizerT, resizerB];
  for (var i = 0; i < arrTB.length; i++) {
    arrTB[i].classList.add("topbottom");
  }
  var allVars = [
    resizable,
    resizers,
    mover,
    resizerT,
    resizerB,
    resizerL,
    resizerR,
    resizerTL,
    resizerTR,
    resizerBL,
    resizerBR,
  ];
  if (invert) {
    for (var i = 0; i < allVars.length; i++) {
      allVars[i].classList.toggle("invert");
    }
  }
  document.body.appendChild(resizable);
  makeResizableDiv(resizable, resizeVars);
  makeMovableDiv(resizable, mover);
  idCounter++;
  return resizable;
}

function clearSelection() {
  if (previousSelection != null) {
    var prevID = previousSelection.getAttribute("count");
    document.getElementById("mover" + prevID).style.border = "3px double black";
    previousSelection = null;
  }
  previousSelection = null;
}

document.addEventListener("mouseup", function (e) {
  e = e || window.event;
  var target = e.target || e.srcElement;
  if (target.id == "createtable") {
    currentDiv = createDivs();
    //target.style.backgroundColor = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
    clearSelection();
    return;
  } else if (target.id.includes("move") || target.className.includes("resiz")) {
    if (previousSelection == null) {
      highlightSwap(target);
      return;
    }
    highlightSwap(target);
    return;
  } else {
    clearSelection();
  }
});
document.addEventListener("mousedown", function (e) {
  e = e || window.event;
  var target = e.target || e.srcElement;
  if (target.id.includes("move") || target.className.includes("resiz")) {
    if (previousSelection == null) {
      highlightSwap(target);
      return;
    }
    if (previousSelection != null) {
      var prevID = previousSelection.getAttribute("count");
    }
    var currID = target.getAttribute("count");
    if (prevID != currID) {
      clearSelection();
      highlightSwap(target);
    }
  }
});

function highlightSwap(e) {
  let idCount = e.getAttribute("count");
  let element = document.getElementById("mover" + idCount);
  let currColor = element.getAttribute("border-color");
  element.style.border = "3px double " + currColor;
  previousSelection = element;
}

function makeMovableDiv(element, mover) {
  var pos1 = 0,
    pos2 = 0,
    pos3 = 0,
    pos4 = 0;
  mover.onmousedown = dragMouseDown;

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    highlightSwap(element);
    element.style.top = element.offsetTop - pos2 + "px";
    element.style.left = element.offsetLeft - pos1 + "px";
  }
  function closeDragElement() {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

function makeResizableDiv(element, resize) {
  const resizers = resize;
  const minimum_size = 150;
  let original_width = 0;
  let original_height = 0;
  let original_x = 0;
  let original_y = 0;
  let original_mouse_x = 0;
  let original_mouse_y = 0;
  for (let i = 0; i < resizers.length; i++) {
    const currentResizer = resizers[i];
    currentResizer.addEventListener("mousedown", function (e) {
      e.preventDefault();
      highlightSwap(element);
      original_width = parseFloat(
        getComputedStyle(element, null)
          .getPropertyValue("width")
          .replace("px", "")
      );
      original_height = parseFloat(
        getComputedStyle(element, null)
          .getPropertyValue("height")
          .replace("px", "")
      );
      original_x = element.getBoundingClientRect().left;
      original_y = element.getBoundingClientRect().top;
      original_mouse_x = e.pageX;
      original_mouse_y = e.pageY;
      window.addEventListener("mousemove", resize);
      window.addEventListener("mouseup", stopResize);
    });

    function resize(e) {
      highlightSwap(element);
      if (currentResizer.classList.contains("single-top")) {
        const height = original_height - (e.pageY - original_mouse_y);
        if (height > minimum_size) {
          element.style.height = height + "px";
          element.style.top = original_y + (e.pageY - original_mouse_y) + "px";
        }
      } else if (currentResizer.classList.contains("single-bottom")) {
        const height = original_height + (e.pageY - original_mouse_y);
        if (height > minimum_size) {
          element.style.height = height + "px";
        }
      } else if (currentResizer.classList.contains("single-left")) {
        const width = original_width - (e.pageX - original_mouse_x);
        if (width > minimum_size) {
          element.style.width = width + "px";
          element.style.left = original_x + (e.pageX - original_mouse_x) + "px";
        }
      } else if (currentResizer.classList.contains("single-right")) {
        const width = original_width + (e.pageX - original_mouse_x);
        if (width > minimum_size) {
          element.style.width = width + "px";
        }
      } else if (currentResizer.classList.contains("bottom-right")) {
        const width = original_width + (e.pageX - original_mouse_x);
        const height = original_height + (e.pageY - original_mouse_y);
        if (width > minimum_size) {
          element.style.width = width + "px";
        }
        if (height > minimum_size) {
          element.style.height = height + "px";
        }
      } else if (currentResizer.classList.contains("bottom-left")) {
        const height = original_height + (e.pageY - original_mouse_y);
        const width = original_width - (e.pageX - original_mouse_x);
        if (height > minimum_size) {
          element.style.height = height + "px";
        }
        if (width > minimum_size) {
          element.style.width = width + "px";
          element.style.left = original_x + (e.pageX - original_mouse_x) + "px";
        }
      } else if (currentResizer.classList.contains("top-right")) {
        const width = original_width + (e.pageX - original_mouse_x);
        const height = original_height - (e.pageY - original_mouse_y);
        if (width > minimum_size) {
          element.style.width = width + "px";
        }
        if (height > minimum_size) {
          element.style.height = height + "px";
          element.style.top = original_y + (e.pageY - original_mouse_y) + "px";
        }
      } else {
        const width = original_width - (e.pageX - original_mouse_x);
        const height = original_height - (e.pageY - original_mouse_y);
        if (width > minimum_size) {
          element.style.width = width + "px";
          element.style.left = original_x + (e.pageX - original_mouse_x) + "px";
        }
        if (height > minimum_size) {
          element.style.height = height + "px";
          element.style.top = original_y + (e.pageY - original_mouse_y) + "px";
        }
      }
    }

    function stopResize() {
      window.removeEventListener("mousemove", resize);
    }
  }
}

function change() {
  const elements = document.querySelectorAll("div", "button");
  invert = !invert;
  for (let element of elements) {
    element.classList.toggle("invert");
  }
}

const changeButton = document.querySelector("#darkmode");
changeButton.addEventListener("click", change);
