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
