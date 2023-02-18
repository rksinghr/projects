const event_tpDropdown = document.getElementById('event_tp');
const event_nmDropdown = document.getElementById('event_nm');
const namevar = document.getElementById('jsevelst');

event_tpDropdown.addEventListener('change', () => {
  // Clear the item dropdown list
  event_nmDropdown.innerHTML = '';

  const etp = event_tpDropdown.value;
  const namval = namevar.value;
  const data = JSON.parse(namval);

  const result = data.filter(function(ele){
    return ele.fields.Typeid == etp;
  });

  for (const item of result) {
    const option = document.createElement('option');
    option.value = item.pk;
    option.textContent = item.fields.Name;
    event_nmDropdown.appendChild(option);
  }

    
});
