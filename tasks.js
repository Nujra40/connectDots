document.addEventListener("DOMContentLoaded", function () {

    let tasks = new Array();
    if (!localStorage.getItem("allTasks")) {
        localStorage.setItem("allTasks", '');
    } else {
        tasks = JSON.parse(localStorage.getItem("allTasks"));
    }

    for (let i = 0; i < tasks.length; i++) {
        const li = document.createElement('li');
        li.innerHTML = tasks[i];
        document.querySelector('#tasks').appendChild(li);
    }

    const taskField = document.querySelector('#task');
    const submitButton = document.querySelector('#submit');
    submitButton.disabled = true;
    document.querySelector('form').onsubmit = () => {

        const li = document.createElement('li');
        li.innerHTML = taskField.value;
        document.querySelector('#tasks').appendChild(li);
        
        tasks[tasks.length] = taskField.value;
        localStorage.setItem('allTasks', JSON.stringify(tasks));

        taskField.value = '';
        submitButton.disabled = true;
        
        return false;
    }

    taskField.addEventListener("keyup", () => {
        if (taskField.value.length === 0) {
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;
        }
    });
});