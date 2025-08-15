document.addEventListener("DOMContentLoaded", function () {
  // Initialize price chart
  const ctx = document.getElementById("priceChart").getContext("2d");

  // Sample price data (in a real app, this would come from your Django backend)
  const labels = [];
  const data = [];
  let currentPrice = 40000;

  // Generate 30 days of price data
  for (let i = 30; i >= 0; i--) {
    const date = new Date();
    date.setDate(date.getDate() - i);
    labels.push(
      date.toLocaleDateString("en-US", { month: "short", day: "numeric" })
    );

    // Random price movement
    currentPrice += (Math.random() - 0.45) * 1000;
    data.push(currentPrice);
  }

  const priceChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "BTC Price (USD)",
          data: data,
          borderColor: "#3a5af9",
          backgroundColor: "rgba(58, 90, 249, 0.1)",
          borderWidth: 2,
          fill: true,
          tension: 0.4,
          pointRadius: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          mode: "index",
          intersect: false,
        },
      },
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            color: "rgba(255, 255, 255, 0.7)",
          },
        },
        y: {
          grid: {
            color: "rgba(255, 255, 255, 0.1)",
            drawBorder: false,
          },
          ticks: {
            color: "rgba(255, 255, 255, 0.7)",
          },
        },
      },
    },
  });

  // Time filter functionality
  const timeFilters = document.querySelectorAll(".time-filter");
  timeFilters.forEach((filter) => {
    filter.addEventListener("click", function () {
      timeFilters.forEach((f) => f.classList.remove("active"));
      this.classList.add("active");

      // In a real app, this would fetch new data for the selected time period
      // For now, we'll just simulate it by adjusting the chart
      const days =
        this.textContent === "24h"
          ? 1
          : this.textContent === "7d"
          ? 7
          : this.textContent === "1m"
          ? 30
          : this.textContent === "3m"
          ? 90
          : 365;

      const newLabels = [];
      const newData = [];
      let newPrice = data[data.length - 1];

      for (let i = days; i >= 0; i--) {
        const date = new Date();
        date.setDate(date.getDate() - i);
        newLabels.push(
          date.toLocaleDateString("en-US", { month: "short", day: "numeric" })
        );

        // Random price movement
        newPrice += (Math.random() - 0.45) * (1000 / (days / 30));
        newData.push(newPrice);
      }

      priceChart.data.labels = newLabels;
      priceChart.data.datasets[0].data = newData;
      priceChart.update();
    });
  });
});
