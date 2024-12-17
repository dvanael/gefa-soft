const ctx = document.getElementById('horizontalBarChart').getContext('2d');
const horizontalBarChart = new Chart(ctx, {
    type: 'bar', // tipo do gráfico
    data: {
        labels: ['Lenha', 'Mandioca', 'Manutenção'], 
        datasets: [{
            label: 'Custos (em real)', // legenda
            data: [40, 50, 50 ], // os dados que ditam o valor do label

            //estilo
            backgroundColor: 'rgb(255, 217, 93)', 
            borderColor: 'rgb(218, 170, 39)', 
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y', // define barras horizontais
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top' // dxibe a legenda no topo
            }
        },
        scales: {
            x: {
                beginAtZero: true // O eixo X começa do zero
            }
        }
    }
});