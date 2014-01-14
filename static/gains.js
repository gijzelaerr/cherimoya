
var url = 'http://localhost/render?from=1389700090&until=1389701100&target=GAINS.*.*.*&format=json';
var items = new Object();
var series = [];
var time;

$.getJSON(url, function( data ) {
    $.each( data, function( index, metric ) {
        var target = metric.target;
        var splitted = target.split('.');
        var axes = splitted.pop();
        var name = splitted.join('.');

        var value;
        $.each( metric.datapoints, function( index2, datapoint ) {
            if (!time || datapoint[1] >= time) {
                time = datapoint[1];
                value = datapoint[0];
            }
        });

        if (!(name in items)) {
            items[name] = [];
        }
        items[name][axes] = value;
    });
    $.each(items, function(key, value) {
        series.push({'name': key, 'data': [[value['real'], value['imag']]]});
    });
    $('#gainplot').highcharts({
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: 'All gains for antenna 0 on ' + Highcharts.dateFormat('%Y %b %e %H:%M', time * 1000)
        },
        xAxis: {
            title: {
                enabled: true,
                text: 'Real'
            },
            startOnTick: true,
            endOnTick: true,
            showLastLabel: true
        },
        yAxis: {
            title: {
                text: 'Imag'
            }
        },
        series: series
    });
});