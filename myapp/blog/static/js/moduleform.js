const modal = document.getElementById('addModule');
modal.addEventListener('submit', function(e) {
    e.preventDefault();

    const ModalData = new ModalData(form);
    const data = {
        title: ModalData.get('title'),
        phase: ModalData.get('phase'),
        difficulty: ModalData.get('difficulty')
    };

    fetch('  ', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Add authorization headers if needed
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data) {
            alert('Module added successfully!');
            form.reset(); // Reset the form after successful submission
        }
    })
    .catch(error => console.error('Error:', error));
});


