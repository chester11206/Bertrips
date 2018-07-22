KindEditor.ready(function (k) {
    //這個地方需要注意；模型類中使用 text = models.TextField()的話id就是id_text。
    // 如果是提前字段類型可以到瀏覽器中檢查，獲取到需要使用富文本編輯器的元素的id

    KE = k.create('#id_content',{
    	langType:'en',
        resizeType:1,
        allowPreviewEmoticons : false,
        allowImageRemote : false,
        uploadJson : '/upload/kindeditor', //這個是上傳圖片後台處理的url
        width:'100%',
        height:'800px',
        // KE.dialog({width:600px,}),
        afterBlur: function(){ this.sync(); }, //编辑器失去焦点(blur)时执行的回调函数（将编辑器的HTML数据同步到textarea）
        afterUpload : function(url, data, name) { //上传文件后执行的回调函数，必须为3个参数
            if(name=="image" || name=="multiimage"){ //单个和批量上传图片时
                var img = new Image(); img.src = url;
                img.onload = function(){ //图片必须加载完成才能获取尺寸
                    KE.html(KE.html().replace('<img src="' + url + '"','<img src="' + url + '" width="400" '))
                }
            }
        }
     });
})