const categoryDropdown = document.getElementById('category');
const itemDropdown = document.getElementById('item');

const event_tpDropdown = document.getElementById('event_tp');
const event_nmDropdown = document.getElementById('event_nm');

// Make an AJAX request to the server-side script to fetch the data
fetch('mytime')
  .then(response => response.json())
  .then(data => {
    // Process the data and insert it into the HTML
    // let html = '';
    data.forEach(item => {
      console.log();
    });
    // dataContainer.innerHTML = html;
  })
  .catch(error => console.error(error));


categoryDropdown.addEventListener('change', () => {
  // Clear the item dropdown list
  event_nmDropdown.innerHTML = '';
  itemDropdown.innerHTML = '';

  console.log(event_tpDropdown.value);
//   console.log(event_data.value);
//   for (const event in event_data.value){
//     console.log(event.Id);
//     console.log(event.Name);
//   }

  // Populate the item dropdown list based on the category selection
  if (categoryDropdown.value === 'fruits') {
    const fruits = ['Apple', 'Banana', 'Orange'];
    for (const fruit of fruits) {
      const option = document.createElement('option');
      option.value = fruit;
      option.textContent = fruit;
      itemDropdown.appendChild(option);
    }
  } else if (categoryDropdown.value === 'vegetables') {
    const vegetables = ['Carrot', 'Broccoli', 'Cabbage'];
    for (const vegetable of vegetables) {
      const option = document.createElement('option');
      option.value = vegetable;
      option.textContent = vegetable;
      itemDropdown.appendChild(option);
    }
  }
});
