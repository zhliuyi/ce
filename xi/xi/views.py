from django.http import HttpResponse
from django.template import Template,Context

def weide(request):
    html='''
    <html>
        <head>
        </head>
        <body>
            <h1>我是h1标签<h1>
            <h2>我是{{name}}</h2>
            <p>{{content}}</p>
        </body>
    </html>
    '''
    #1.构建模板结构
    template_obj=Template(html)
    #2.创建渲染模板
    params=dict(name="韦德大爷",content="好几个总冠军")#构建数据结构
    content_obj=Context(params)#模板加载数据
    #3.进行数据渲染
    result=template_obj.render(content_obj)
    return  HttpResponse(result)

#调用模板第一种方法
from django.shortcuts import render
def indextmp(request):
    name='哈士奇'
    return render(request,'index.html',{'name':name})

#调用模板的第二种方法
from django.shortcuts import render_to_response
def abc(request):
    name="abc,enne"
    return render_to_response("abc.html",{"name":name})

#调用模板的第三种方法
from django.template.loader import get_template
def abc(request):
    template=get_template("abc.html")
    name="hello"
    result=template.render({'name':name})
    return  HttpResponse(result)

def tpltest(request,age):
    class Say(object):
        def say(self):
            return "hello"
    name="zhangsan"
    age=19
    hobby=["eat","sing","pingpang"]
    score={"shuxue":89,"yingyu":90,"yuwen":100}
    say=Say()
    myjs="""
    <script>
    alert("hello")
    </script>
    """
    # return render(request,"tpltest.html",{"name":name,"age":age,"hobby":hobby,"score":score})
    #使用locals（）方法，作用将当前视图函数的所有局部变量返回
    return render(request,"tpltest.html",locals())
def statictest(request):
    return render(request,'statictest.html')
def staticdemo(request):
    params=[
        {"name":"麦迪","img":"maidi.jpg","url":"https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7%E9%BA%A6%E6%A0%BC%E9%9B%B7%E8%BF%AA/6118977?fromtitle=%E9%BA%A6%E8%BF%AA&fromid=136057&fr=aladdin"},
        {"name":"科比","img":"kb.jpg","url":"https:www.baidu.com"},
        {"name": "姚明", "img": "ym.jpg", "url": "https:www.sina.com"},
        {"name": "易建联", "img": "yjl.jpg", "url": "https:www.taobao.com"},
    ]
    return  render(request,"staticdemo.html",locals())
def staticdemo3(request):
    params=[
        {"name":"麦迪","img":"maidi.jpg","url":"https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7%E9%BA%A6%E6%A0%BC%E9%9B%B7%E8%BF%AA/6118977?fromtitle=%E9%BA%A6%E8%BF%AA&fromid=136057&fr=aladdin"},
        {"name":"科比","img":"kb.jpg","url":"https:www.baidu.com"},
        {"name": "姚明", "img": "ym.jpg", "url": "https:www.sina.com"},
        {"name": "易建联", "img": "yjl.jpg", "url": "https:www.taobao.com"},
    ]
    return  render(request,"staticdemo3.html",locals())