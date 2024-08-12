document.addEventListener('paste', function (event) {
    let items = (event.clipboardData || event.originalEvent.clipboardData).items;
    for (let index in items) {
        let item = items[index];
        if (item.kind === 'file') {
            let blob = item.getAsFile();
            let formData = new FormData();
            formData.append('file', blob, blob.name);
            uploadImage(formData);
        }
    }
});

function uploadImage(formData) {
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#links').innerHTML += data;
        })
        .catch(error => console.error('Error:', error));
}
