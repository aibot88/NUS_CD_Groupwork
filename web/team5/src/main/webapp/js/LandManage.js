
$(document).ready(function(){
    $('#LMTable').bootstrapTable({
        contentType: "application/x-www-form-urlencoded;charset=UTF-8",
        url: "action.LandManage",
        toolbar: '#toolbar', //工具按钮用哪个容器
        method: 'post',
        cache: false,
        pagination: false, //是否显示分页
        // sidePagination: "client",
         sortable: false, //是否启用排序
        // sortOrder: "asc", //排序方式
        // pageSize: 10, //每页的记录行数（*）
        // pageList: [10, 25, 50, 100], //可供选择的每页的行数（*）
         search: false,
        showRefresh: true, //是否显示刷新按钮
        clickToSelect: true, //是否启用点击选中行
        dataType: "json",
        uniqueId : "ID",
        locale: "zh-CN",
        /*queryParams: function (params) {//自定义参数，这里的参数是传给后台的，我这是是分页用的
            return {//这里的params是table提供的
                offset: params.offset,//从数据库第几条记录开始
                limit: params.limit//找多少条
            };
        },*/
        columns: [{
            field: 'id',
            title: '序号id'
        }, {
            field: 'district',
            title: '地区District'
        }, {
            field: 'mark',
            title: '地标mark'
        }, {
            field: 'block',
            title: '地块block'
        }, {
            field: 'place',
            title: '地位place'
        }, {
            field: 'name',
            title: '作物名称name'
        }, {
            field: 'area',
            title: '面积area'
        }, {
            field: 'stat',
            title: '状态stat'
        }, {
            field: 'manager',
            title: '管理员manager'
        }],
/*        responseHandler:function(res) {
            //动态渲染表格之前获取有后台传递的数据时,用于获取出除去本身渲染所需的数据的额外参数
            //详见此函数参数的api
            return res;
        },*/
        data: [{

            name: 'Item 1',

        }, {
            id: 2,
            name: 'Item 2',
        }]
    })
});