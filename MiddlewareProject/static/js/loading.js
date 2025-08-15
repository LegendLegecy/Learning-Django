document.addEventListener("DOMContentLoaded", function () {
  let blocks = 0;
  let sources = 0;
  let indicators = 0;

  const blocksInterval = setInterval(() => {
    blocks += Math.floor(Math.random() * 50) + 10;
    document.getElementById("blocks-scanned").textContent =
      blocks.toLocaleString();
  }, 300);

  const sourcesInterval = setInterval(() => {
    if (sources < 12) {
      sources += 1;
      document.getElementById("market-sources").textContent = sources;
    }
  }, 500);

  const indicatorsInterval = setInterval(() => {
    indicators += Math.floor(Math.random() * 5) + 1;
    document.getElementById("indicators").textContent =
      indicators.toLocaleString();
  }, 400);
});
