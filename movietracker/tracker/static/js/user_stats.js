let myChart = document.getElementById('myChart').getContext('2d');

Chart.defaults.font.family = 'Lato';
Chart.defaults.font.size = 18;

let statsChart = new Chart(myChart, {
    type: 'pie',
    data: {
        labels: ['Plan to Watch', 'Watching', 'Completed'],
        datasets: [{
            labels: 'Movie Stats',
            data: [5, 2, 3],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 205, 86)',
                'rgb(54, 162, 235)'
            ],
            boderWidth: 1,
            borderColor: '#777',
            hoverBorderWidth: 1,
            hoverBorderColor: '#000',
            hoverOffset: 3
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Movie Stats',
                font: {
                    size: 35
                },
                padding: {
                    top: 30,
                    bottom: 20
                }
            },
            legend: {
                display: true,
                position: 'bottom',
                labels: {
                    color: '#000',
                }
            },
            tooltip: {
                usePointStyle: true
            }
        }
    }
});