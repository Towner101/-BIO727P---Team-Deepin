function handleAnalysisChange(url) {
  if (url) {
    window.location.href = url;
  }
}
document.addEventListener('DOMContentLoaded', function() {
  var selectElement = document.getElementById('analysis-select');
  if (selectElement) {
    selectElement.addEventListener('change', function() {
      handleAnalysisChange(this.value);
    });
  }
});


document.querySelectorAll('.superpopulation-input').forEach(input => {
  input.addEventListener('change', updatePopulationVisibility);
});

function updatePopulationVisibility() {
  // Obtain all selected superpopulations
  const selectedSuperpopulations = Array.from(document.querySelectorAll('.superpopulation-input:checked')).map(input => input.value);
  
  // Toggle visibility of population groups based on selected superpopulations
  document.querySelectorAll('.population-group').forEach(group => {
      const superpopulationValue = group.getAttribute('data-superpopulation');
      if (selectedSuperpopulations.includes(superpopulationValue)) {
          group.style.display = 'block'; // Show this population group
      } else {
          group.style.display = 'none'; // Hide this population group
          // Optionally, uncheck all populations within this hidden group
          group.querySelectorAll('.form-check-input').forEach(checkbox => { checkbox.checked = false; });
      }
  });
}


