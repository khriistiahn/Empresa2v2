
function confirmarEliminar(id){
  Swal.fire({
    title: 'Estas seguro?',
    text: "No podras recuperar los datos!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Eliminar!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Eliminado!',
        'Tu archivo ha sido eliminado.',
        'success'
      ).then(function() {
        window.location.href = "/eliminar/"+id+"/";
      })
    }
  })

}