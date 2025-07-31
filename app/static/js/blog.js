document.addEventListener('DOMContentLoaded', () => {
  console.log("Blog JS loaded");
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(a => setTimeout(() => a.remove(), 3000));
});