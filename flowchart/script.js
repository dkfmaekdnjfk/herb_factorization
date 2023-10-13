function addRow() {
  const table = document.getElementById('inputTable');
  const newRow = table.insertRow(-1);
  for (let i = 0; i < 7; i++) {
      const newCell = newRow.insertCell(i);
      const input = document.createElement('input');
      input.type = 'text';
      newCell.appendChild(input);
  }
}

function saveData() {
  const table = document.getElementById('inputTable');
  // Convert table data to a format suitable for saving
  // Send data to backend for saving
}

// Additional functions to interpret the table as a flowchart and
// guide decision-making will be more complex and depend on your specific needs.
