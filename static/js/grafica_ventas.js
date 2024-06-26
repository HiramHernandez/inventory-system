let avoidCache = false
let ventasPorDiaUrl = `/dashboard/ventas-por-dia?avoid-cache=${avoidCache}`;
$(document).ready(function () {
    // Solicitar datos de la API usando AJAX
    $.getJSON(ventasPorDiaUrl, function (data) {
        // Procesar los datos obtenidos
        var datosGrafico = []; // Arreglo para almacenar los puntos del gráfico
        for (var i = 0; i < data.length; i++) {
            var punto = {
                fecha__date: data[i].fecha__date,
                ventas_por_dia: data[i].ventas_por_dia,
                total_por_dia: data[i].total_por_dia
            };
            datosGrafico.push(punto);
        }

        // Crear el gráfico de líneas de Morris usando los datos procesados
        new Morris.Line({
            element: 'line-chart-ventas',
            data: datosGrafico,
            xkey: 'fecha__date',
            ykeys: ['total_por_dia'],
            labels: ['Valor'],
            axes: true, // Habilitar ejes (necesario para la configuración)
            grid: true, // Habilitar cuadrícula
            yaxes: [
                {
                    grid: true, // Habilitar cuadrícula en el eje Y
                    beginAtZero: false, // Permitir que el eje Y comience en un valor distinto de cero
                    // Opcional: Especificar el rango máximo del eje Y (en este caso, lo configuraremos dinámicamente)
                    max: function (data) {
                        return Math.max(...data.map(function (row) { return row.y; }));
                    }
                }
            ]
        });
    });
});