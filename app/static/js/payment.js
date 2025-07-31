document.addEventListener('DOMContentLoaded', () => {
  const paymentForm = document.querySelector('form');
  if (paymentForm) {
    paymentForm.addEventListener('submit', () => {
      alert('Processing your payment...');
    });
  }
});
