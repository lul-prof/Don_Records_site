document.addEventListener("DOMContentLoaded", function() {
  console.log("Producer portal ready.");
  const buttons = document.querySelectorAll("button");
  buttons.forEach(btn => {
    btn.addEventListener("click", () => alert("Action executed"));
  });
});
