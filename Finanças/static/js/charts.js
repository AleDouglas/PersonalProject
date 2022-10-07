
function lineGraphic(dados, titulo, hAxisTitutlo, elementName){
    google.load('visualization', '1.0', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable(
            dados
        );

        var options = {
            title: titulo,
            hAxis: {title: hAxisTitutlo,  titleTextStyle: {color: '#333'}},
            vAxis: {minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById(elementName));
        chart.draw(data, options);
    }
    $(window).resize(function(){
        drawChart()
    });
}

function columChart(dados, titulo, elementName){
    google.load('visualization', '1.0', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable(
            dados
            );

        var options = {
            title: titulo,
            bar: {groupWidth: "95%"},
            legend: { position: "none" },
        };
        var chart = new google.visualization.ColumnChart(document.getElementById(elementName));
        chart.draw(data, options);
    }
    $(window).resize(function(){
    drawChart()
    });
}