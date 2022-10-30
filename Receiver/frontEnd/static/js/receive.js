setInterval(function() {
    fetch("http://127.0.0.1:5000/").then((res) => res.json()).then((data) => {
        heading.innerHTML = data['heading']
        content.innerHTML = '<br>Hour: ' + data['hour'] + '<br>' + 'Min: ' + data['min'] + '<br>' + 'Sec: ' + data['sec']

    })
}, 1000);