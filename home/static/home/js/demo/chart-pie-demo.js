// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

console.log(enem, psc, vestibular);

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["ENEM", "PSC", "Vestibular"],
    datasets: [{
      data: [enemProp, pscProp, vestibularProp],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, data) {
          var label = data.labels[tooltipItem.index] || '';
          var value = data.datasets[0].data[tooltipItem.index];
          var quantidadeReal = [enem, psc, vestibular][tooltipItem.index]; // Seleciona a quantidade real com base no índice do tooltip
          // Inclui as quantidades reais das porcentagens no tooltip
          return label + ': ' + value + '% (' + quantidadeReal + ')';
        }
      }
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
