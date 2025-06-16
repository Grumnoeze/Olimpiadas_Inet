let count = 1;

function updateDisplay() {
  // Selecciona todos los elementos con la clase "number" y actualiza su contenido
  document.querySelectorAll(".number").forEach(el => {
    el.textContent = count;
  });

  // También desactiva el botón "−" si el valor es 1
  document.querySelector(".decrease").disabled = count === 1;
}

function increase() {
  count++;
  updateDisplay();
}

function decrease() {
  if (count > 1) {
    count--;
    updateDisplay();
  }
}

// Inicializar
updateDisplay();
