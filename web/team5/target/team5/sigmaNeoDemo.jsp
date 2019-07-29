<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <%--    <title>Neo4j and Sigma.js Example</title>--%>
    <!-- Twitter Bootstrap -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">

    <link rel="stylesheet" href="css/bootstrap-vertical-menu.css">
    <link href="https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script type="text/javascript" src="./src/sigma.min.js"></script>
    <script type="text/javascript" src="./src/sigma.parseGexf.js"></script>
    <script type="text/javascript" src="./src/sigma.forceatlas2.js"></script>
    <link type="text/css" rel="stylesheet" href="./css/neo_sigma.css"/>
    <%--    <link rel="stylesheet" type="text/css" href="css/default.css">--%>
</head>
<body style="height: 100%;margin: 0;background-color: #222">  <%--TAT--%>

<div id="sidebar">
    <jsp:include page="sidebar.jsp"/>
</div>
<div class="buttons-container" style="left: 7%;z-index: 50;position: absolute">
    <button class="btn" id="stop-layout">Stop Layout</button>
    <%--    <button class="btn" id="rescale-graph">Rescale Graph</button>--%>
</div>
<div class="span12 sigma-parent" id="sigma-example-parent">
    <div class="sigma-expand" id="sigma-example" style="background-color: #f9f7f6"></div>
</div>
<script type="text/javascript" src="./src/neo_sigma.js"></script>
<div id="step1" style="position:absolute;top:0;right : -1px;z-index: 999">
    <img src="./pic/step1.png" alt = "step1"/>
</div>

</body>
</html>