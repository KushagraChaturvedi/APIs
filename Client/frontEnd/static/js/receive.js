async function getData() {
    const res = await fetch('http://127.0.0.1:5000/2');
    const img = await res.blob();
    document.getElementById('flower').src = URL.createObjectURL(img);
}

getData();
