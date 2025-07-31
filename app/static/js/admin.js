function showPanel(id) {
    const panels = document.querySelectorAll('.panel');
    panels.forEach(p => p.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}