var addressPoints;

fetch('points')
.then(response => response.json())
.then(data => {
    addressPoints = data;
})
.catch(error => {
    console.log('Error', error);
})