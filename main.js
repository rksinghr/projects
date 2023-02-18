const categoryDropdown = document.getElementById('category');
const itemDropdown = document.getElementById('item');

categoryDropdown.addEventListener('change', () => {
  // Clear the item dropdown list
  itemDropdown.innerHTML = '';

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
