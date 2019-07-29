
//wyj：另一种用ajax传json的尝试，先把数据传过来，再生成表格，but failed
$(document).ready(function(){
    $('#LMTable').bootstrapTable({
        ajax: function (request) {
            $.ajax({
                type: "GET",
                url:"",
                // url: Feng.ctxPath + "/dataQuery/list" + "/" + sql + "/" + connectInfo,
                contentType: "application/json;charset=utf-8",
                dataType: "json",
                json: 'callback',
                success:function (result){

                },
                error:function () {
                    alert("SQL查询错误，请输入正确的SQL语句！");
                    location.reload();
                }
            });
        }
    });
});