var addressPoints;

fetch('points')
.then(response => response.json())
.then(data => {
    adressPoints = data;
})
.catch(error => {
    console.log('Error', error);
})