<!DOCTYPE html>
<html style="height: 100%">
<head>
    <meta charset="utf-8">
    <!-- Twitter Bootstrap -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/default.css">
    <link rel="stylesheet" href="css/bootstrap-vertical-menu.css">
    <link href="https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- 引入 echarts.js -->
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-gl/echarts-gl.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
    <script type="text/javascript"
            src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
    <%--       <script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=xfhhaTThl11qYVrqLZii6w8qE5ggnhrY&__ec_v__=20190126"></script>--%>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>
    <%--<div style="float: right"><span></span></div>--%>

</head>
<body style="height: 100%; margin: 0">
<div id="sidebar">
    <jsp:include page="sidebar.jsp"/>
</div>
<div id="container" style="height: 100%"></div>

<script type="text/javascript">
    var dom = document.getElementById("container");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    option = {
        title: {
            text: 'Number of Posts in Different Periods during a Day',// Number of Weibo posts in different period during a day
            // subtext: 'from：Louvain',
            left : '4.5%'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
        },
        toolbox: {
            show: true,
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: [
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                0,
                1,
                2,
                3,
                4,
                5
            ]
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value} Pieces'
            },
            axisPointer: {
                snap: true
            }
        },
        visualMap: {
            show: false,
            dimension: 0,
            pieces: [{
                lte: 6,
                color: 'green'
            }, {
                gt: 5,
                lte: 8,
                color: 'red'
            }, {
                gt: 8,
                lte: 16,
                color: 'green'
            }, {
                gt: 16,
                lte: 19,
                color: 'red'
            }, {
                gt: 19,
                color: 'green'
            }]
        },
        series: [
            {
                name: 'Pieces of Posts',
                type: 'line',
                smooth: true,
                data: [
                    1,
                    1,
                    1,
                    4,
                    2,
                    1,
                    7,
                    5,
                    5,
                    3,
                    4,
                    3,
                    4,
                    7,
                    9,
                    10,
                    15,
                    19,
                    30,
                    21,
                    3,
                    1,
                    0,
                    0
                ], markArea: {
                    data: [[{
                        name: 'The Peak at Night',
                        // fontsize:15,
                        xAxis: '22'
                    }, {
                        xAxis: '1'
                    }], [{
                        name: 'The Peak at Noon',
                        xAxis: '12'
                    }, {
                        xAxis: '14'
                    }]]
                }
            }
        ]
    };
    ;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
</script>
</body>
</html>