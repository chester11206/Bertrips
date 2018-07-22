from django.contrib import admin

# Register your models here.
from .models import Post

# class TestTinymce_Admin(admin.ModelAdmin):

#     class Media:
#         js = [
#             '/static/tinymce/js/jquery.min.js',   # 必须首先加载的jquery，手动添加文件
#             '/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
#             '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
#             '/static/tinymce/js/tinymce/textarea.js',   # 手动添加文件，用户初始化参数
#         ]

# admin.site.register(Post, TestTinymce_Admin)



class userAdmin(admin.ModelAdmin):
    class Media:
            # 在管理後台的HTML文檔中加入js文檔, 每一個路徑都會追加STATIC_URL/
        js = [
                '/static/js/kindeditor/kindeditor-all-min.js',
                #'/static/js/kindeditor/zh_CN.js',
                '/static/js/kindeditor/config.js',
            ]
#使用admin.site.register
admin.site.register(Post,userAdmin)

