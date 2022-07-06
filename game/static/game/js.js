function count(arr, data) {
    var c = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == data) {
            c++;
        }
    }
    return c;
}

let radBool = new Array();
function radPressed(id) {
    x = document.getElementById(id);
    radBool[id] = !radBool[id];
    x.checked = radBool[id];
    if (count(radBool, true) > 1) {
        processGameState();
    }
}

function lineBreak() {
    document.body.appendChild(document.createElement('br'));
}

function processGameState() {
    let pressed = new Array();
    for (let i = 0; i < radBool.length; i++) {
        if (radBool[i]) {
            pressed.push(document.getElementById(i))
        }
    }

    let x0 = Math.floor(pressed[0].getBoundingClientRect().x);
    let y0 = Math.floor(pressed[0].getBoundingClientRect().y);

    let x1 = Math.floor(pressed[1].getBoundingClientRect().x);
    let y1 = Math.floor(pressed[1].getBoundingClientRect().y);

    console.log("x0", x0, "y0", y0, "x1", x1, "y1", y1);

    line = document.createElement('h4');
    line.style.position = "fixed";
    if (y1 - y0 == 0) {
        if (Math.abs(x1 - x0) > 25) {
            alert("Cannot Join those points!");
        } else {
            line.style.top = (y0-33).toString() + "px";
            line.style.left = (x0+9).toString() + "px";
            line.innerHTML = "__";
        }
    } else if (x1 - x0 == 0) {
        if (Math.abs(y1 - y0) > 25) {
            alert("Cannot Join those points!");
        } else {
            line.style.top = (y1-35).toString() + "px";
            line.style.left = (x1+5).toString() + "px";
            line.innerHTML = "|";
        }
    } else {
        alert("Cannot Join those points!");
    }

    document.body.appendChild(line);

    for (let i = 0; i < radBool.length; i++) {
        if (radBool[i]) {
            document.getElementById(i).checked = false;
            radBool[i] = false;
        }
    }

    form.submit();
}

form = document.createElement('form');

for (let i = 0; i < 100; i++) {
    if (i%10 == 0) {
        lineBreak();
    }
    x = document.createElement('input');
    x.type = 'radio';
    x.id = i;
    x.setAttribute('onclick', 'radPressed(' + x.id + ')');
    form.appendChild(x);
}

form.setAttribute("action", )

document.body.appendChild(form);