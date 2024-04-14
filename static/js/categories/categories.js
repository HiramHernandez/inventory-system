console.log("Hola entro al script categories.js")
$(document).ready(function () {
    $('.btnEditarCategoria').click(function () {
        var categoriaId = $(this).data('id');
        var nombreCategoria = $(this).data('nombre');; // Aquí puedes obtener el nombre de la categoría mediante una solicitud AJAX
        $('#editarCategoria').val(nombreCategoria);
        $('#idCategoria').val(categoriaId);
        
        let editCategoryUrl = `edit-category/${categoriaId}/`;
        $('#editCategoryForm').attr('action', editCategoryUrl);

    });
});
$(document).ready(function () {
    $('.btnEliminarCategoria').click(function () {
        var categoriaId = $(this).data('id');
        let removeCategoryUrl = `remove-category/${categoriaId}`;
        swal({
            title: '¿Está seguro de borrar la categoría?',
            text: "¡Si no lo está puede cancelar la acción!",
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText: 'Cancelar',
            confirmButtonText: 'Si, borrar categoría!'
        }).then(function (result) {

            if (result.value) {
                $.ajax({
                    url: removeCategoryUrl,
                    
                    data: {
                        'csrfmiddlewaretoken': '{{ csrf_token }}',
                        'categoria_id': categoriaId
                    },
                    success: function (response) {
                        // Manejar la respuesta según sea necesario
                        console.log(response);
                        // Por ejemplo, puedes recargar la página o actualizar la tabla de categorías
                        location.reload();
                    },
                    error: function (xhr, status, error) {
                        // Manejar errores si es necesario
                        console.error(xhr.responseText);
                    }
                });

            }

        })
    });
});