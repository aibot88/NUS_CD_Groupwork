<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html style="height: 100%">

<head>
    <meta charset="utf-8">
    <title>TEAM 5</title>
    <link href="http://cdn.bootcss.com/font-awesome/4.4.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- Twitter Bootstrap -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/default.css">
    <link rel="stylesheet" href="css/bootstrap-vertical-menu.css">
    <link href="https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- 引入 echarts.js -->
    <script src="./src/jquery.min.js"></script>
    <script type="text/javascript" src="./src/echarts/echarts.min.js"></script>
    <script type="text/javascript" src="./src/echarts/echarts-gl.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
    <script type="text/javascript"
            src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
    <script type="text/javascript"
            src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>

</head>
<body style="height: 100%;margin: 0">
<div id="sidebar">
    <jsp:include page="sidebar.jsp"/>
</div>
<div id="main" style="height: 100%">
    <script type="text/javascript">  //;background-color: #404d5b
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));
        var option;
        myChart.showLoading();
        $.get('partitiondepressedsingleedge004.json', function (webkitDep) {
            myChart.hideLoading();
            option = {
                // color: "#404d5b",
                title: {
                    text: 'TEAM5',
                    subtext: 'Default layout',
                    top: 'bottom',
                    left: 'right'
                },
                tooltip: {
                    trigger: 'item',
                    // formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                    data: ['0', '1', '2', '3','4','5','6','7','8','9']
                },
                series: [{
                    type: 'graph',
                    layout: 'force',
                    animation: true,
                    label: {
                        normal: {
                            fontSize: 17,
                            position: 'right',
                            formatter: '{b}'
                        }
                    },

                    draggable: true,
                    roam: true,
                    focusNodeAdjacency: true,
                    // wyj: 这种方法行不通,报错 this._rawData.getSource is not a function
                    // data: {
                    //     name :webkitDep.nodes.name,   // wyj: name具有唯一性
                    //     // x : webkitDep.nodes.x,
                    //     // y : webkitDep.nodes.y,
                    //     // category : webkitDep.nodes.category
                    //     // itemStyle: {
                    //     //     color: webkitDep.nodes.color
                    //     // }
                    // },

                    // wyj: 下面是官方的方法
                    data: webkitDep.nodes.map(function (node, name) {
                        node.id = name;
                        return node;
                    }),
                    categories: webkitDep.categories,
                    force: {
                        initLayout: 'circular',
                        // repulsion: 20,
                        layoutAnimation : true,
                        edgeLength: 20, //10
                        repulsion: 10, //3
                        gravity: 0
                    },
                    symbolSize: 8,
                    edges: webkitDep.links,
                    lineStyle: {
                        color: 'rgba(128, 128, 128, 0.3)'

                    },
                    animationThreshold: 110,
                    animationEasing: "cubicIn",            //wyj : cubicIn
                    animationEasingUpdate: "circularOut" //wyj：数据更新的缓动效果
                    // animationDelay : 300
                }]
            };
            myChart.setOption(option);
        });
        if (option && typeof option === "object") {
            myChart.setOption(option, true);
        }
    </script>
</div>
<div id="depre" style="position:absolute;top:0;right : -1px;z-index: 999">
    <img src="./pic/depre.png" alt = "depre"/>
</div>
</body>