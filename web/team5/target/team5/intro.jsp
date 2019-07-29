<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html style="height: 100%">

<head>
    <meta charset="utf-8">

    <title>CLUSTER2-05</title>
    <!-- Twitter Bootstrap -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/default.css">
    <link rel="stylesheet" href="css/bootstrap-vertical-menu.css">
    <link href="https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- 引入 echarts.js -->
    <script src="./src/jquery.min.js"></script>
</head>
<body style="height: 100%;margin: 0">
<div id="sidebar">
    <jsp:include page="sidebar.jsp"/>
</div>
<div id="main" style="height: 100%;text-align: center">
    <figure id="eg6" >
        <img id="mainPic" src="./pic/SWS3001_CLUSTER2-05.png" alt="mainPage" title="Vote Team 5!" style="height: 45%;width:35%"/>
<%--        <figcaption>An awesome picture caption!</figcaption>--%>
    </figure>
</div>
<div id="3001" style="position:absolute;top:0;right : -1px;z-index: 999">
    <img src="./pic/3001.png" alt = "3001"/>
</div>
</body>