/* JavsScript Functions */

// This function will handle both the initialization and resizing of the graph.
function renderGraph() {
  // Calculate the desired width.
  const viewportWidth = Math.round(window.innerWidth * 0.95); // Add rounding here

  $.ajax({
    url: "/rivercharts/river-graph-data/",
    data: {
      width: viewportWidth,
    },
    dataType: "json",
    success: function (data) {
      if (data.error) {
        // This is an error case; handle it accordingly.
        window.location.href = "/error/" + encodeURIComponent(data.error) + "/";
      } else {
        // This is the success case; render your graph as before.
        $("#loading-indicator").hide();
        $("#graph-div").html(data.graph_div).show();
        $("#station-name")
          .text("Station: " + data.station_name)
          .show();
        $("#timestamp")
          .text("Last Updated: " + getCurrentTimestamp())
          .show();
        $("header h1")
          .html('RIVER <span class="title-highlight">CHARTS</span>')
          .show();
        $("footer").show();
        $(".logo-image").show();
        $("header").show();
      }
    },
    error: function () {
      // Handle the error here.
      // For instance, you might want to show an alert or redirect to a generic error page.
      window.location.href =
        "/error/" + encodeURIComponent("HTTP Error.") + "/";
    },
  });
}

function getCurrentTimestamp() {
  var now = new Date();
  return now.toLocaleString(); // Customize the timestamp format as needed
}

function debounce(func, wait) {
  var timeout;
  return function () {
    var context = this,
      args = arguments;
    clearTimeout(timeout);
    timeout = setTimeout(function () {
      func.apply(context, args);
    }, wait);
  };
}

$(document).ready(function () {
  // Call the function on page load to initialize the graph.
  renderGraph();

  // Use the same function to handle resizing with debouncing.
  // Wait for 300 milliseconds after the last resize event before invoking renderGraph
  $(window).resize(
    debounce(function () {
      renderGraph();
    }, 300)
  );
});
