
  const inputSalida = document.getElementById('salida');
  const inputRegreso = document.getElementById('regreso');

  // Función para formatear fechas a 'YYYY-MM-DD'
  function formatearFecha(fecha) {
    return fecha.toISOString().split('T')[0];
  }

  // Establecer fecha de hoy como mínimo y valor por defecto para salida
  const hoy = new Date();
  const fechaHoy = formatearFecha(hoy);
  inputSalida.min = fechaHoy;
  inputSalida.value = fechaHoy;

  // Establecer fecha de regreso por defecto y mínimo (+2 días)
  const fechaRegresoInicial = new Date(hoy);
  fechaRegresoInicial.setDate(fechaRegresoInicial.getDate() + 2);
  const fechaRegresoStr = formatearFecha(fechaRegresoInicial);
  inputRegreso.min = fechaRegresoStr;
  inputRegreso.value = fechaRegresoStr;

  // Evento: al cambiar la fecha de salida, actualizar el mínimo de regreso
  inputSalida.addEventListener('change', () => {
    const nuevaSalida = new Date(inputSalida.value);
    nuevaSalida.setDate(nuevaSalida.getDate() + 2);
    const nuevoMinRegreso = formatearFecha(nuevaSalida);
    inputRegreso.min = nuevoMinRegreso;

    // Si la fecha actual de regreso es menor al nuevo mínimo, actualizarla también
    if (inputRegreso.value < nuevoMinRegreso) {
      inputRegreso.value = nuevoMinRegreso;
    }
  });
