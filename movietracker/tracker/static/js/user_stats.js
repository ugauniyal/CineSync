let myChart1 = document.getElementById('myChart1').getContext('2d');

Chart.defaults.font.family = 'Lato';
Chart.defaults.font.size = 18;

let statsChart = new Chart(myChart1, {
    type: 'pie',
    data: {
        labels: ['Plan to Watch', 'Watching', 'Completed'],
        datasets: [{
            labels: 'Movie Stats',
            data: [3, 2, 1],
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

let myChart2 = document.getElementById('myChart2').getContext('2d');

Chart.defaults.font.family = 'Lato';
Chart.defaults.font.size = 18;

let genreStatsChart = new Chart(myChart2, {
    type: 'pie',
    data: {
        labels: ['Comedy', 'Sci-Fi', 'Horror', 'Romance', 'Action', 'Thriller', 'Drama', 'Mystery', 'Crime', 'Animation', 'Adventure', 'Fantasy', 'Superhero'],
        datasets: [{
            labels: 'Movie Genre Stats',
            data: [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            backgroundColor: [
                '#6050dc', '#a63bc6', '#c233bd', '#d82db2', '#ee2e95', '#ff337a', '#ff515d', '#ff654b', '#ff763a', '#ff852c', '#ff921e', '#ff9f11', '#ffab05'
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
                text: 'Movie Genre Stats',
                font: {
                    size: 35
                },
                padding: {
                    top: 30,
                    bottom: 20
                }
            },
            legend: {
                display: false
            }
        }
    }
});