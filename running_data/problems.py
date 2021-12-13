problemslist = \
[{
    "theme": "code",
    "text": "使用python的<code>reversed()</code>函数出现一个问题，假设对列表list1进行反转后，得到list2即<code>list2=reversed(list1)</code>，此时得到的list2是一个反向迭代器对象而不是一个list，所以不能使用print()函数直接打印"
},
    {
        "theme": "code",
        "text": "想要快速获取两个日期的时间差，python并没有特定的函数。使用date()方法可以快速解决，获取系统时间<code>date2 = time.strptime(date2,'%Y-%m-%d')</code>，假设date1为‘2017-2-1’其格式需要与date2相同。然后对date1，date2格式化，<code>date1 = datetime.datetime(date1[0],date1[1],date1[2])</code>最终的时间差就是(date2-date1)"
    },
    {
        "theme": "flask",
        "text": "想要在网页按钮按下时提交一个表单，但是flask默认重定向会刷新全部网页，所以想使用Ajax来处理表单达到局部刷新的目的。然而在测试时一切正常但是在服务器上运行时就会发生服务器崩溃..."
    },
    {
        "theme": "linux",
        "text": "vsftpd在运行的时候线程数是动态变化的，上传任务过多过大的时候后台居然有十几个进程，因为读取问题centos的磁盘管理在ftp线程过多时会禁止其他进程写入。"
    },
    {
        "theme": "docker",
        "text": "远程仓库的tag就是仓库名，而本地的tag是用来区分新旧的标签名。"
    },
    {
        "theme": "flask",
        "text": "flask的默认静态文件加载目录是<code>static</code>，然而经常一堆模板的css链接写的是<code>/css/main.css</code>通过浏览器解析就变成了<code>http://localhost:5000/css/main.css</code>了，不能正确加载static目录下的静态文件。所以使用全局配置参数<code>app = Flask(__name__,static_path_for='')</code>这样默认加载的静态文件目录就会从<code>'/'</code>开始"
    },
    {
        "theme": "flask",
        "text": "flask的实现通过app.py传入字符串，在html页面里被渲染为html块元素。用到javascript脚本，使用css过滤器筛选需要显示的块，使用innerText提取文本，使用innerHTML()方法将传入的字符串重新渲染。具体的方法研究参考<a href='http://landers1037.top/2019/07/30/flask-2-html/'>博客</a>"
    },
    {
        "theme": "flask",
        "text": "普通的div元素怎么变成正方形使其高度等于宽度，除了给定其高度和宽度值还需要其自适应网页大小，用到了<code>padding-top(bottom)</code>属性<br><pre><code>{<br> width: 100%;<br>  height: 0;<br>  padding-top: 100%;<br> }</code></pre>这样就能满足高度随着宽度的改变而改变并且始终等于宽度。"
    },
    {
        "theme": "code",
        "text": "解决全局变量的列表数值无法自动清空的方法，有一种就是把列表放在一个字典里，每次新值更新时把字典对应的列表键直接赋值，通过字典键值的更新解决全局列表不会刷新的问题。"
    },
    {
        "theme": "code",
        "text": "大部分的居中偏移问题是padding默认有问题"
    },
    {
        "theme": "flask",
        "text": "使用Gunicorn代理flask应用优化配置：默认worker应该为(cpu数*2+1)，<code>gunicorn -w 4 -b 127.0.0.1:5000 -t 500 app:app --reload</code>"
    },
    {
        "theme": "flask",
        "text": "使用jquery使echarts的图表自适应网页大小<code>$(window).resize(function() {myChart.resize();});</code>"
    },
    {
        "theme": "linux",
        "text": "linux查看端口的占用情况，使用netstat<br><pre>netstat -ntlp 查看全部端口<br>netstat -ntulp|grep 8080 查看8080端口占用<br>netstat -anp|grep 60 查看60端口的进程 </pre>"
    },
    {
        "theme": "code",
        "text": "python对html字符转义使用html.unescape(str)方法"
    },
    {
        "theme": "code",
        "text": "python对url链接地址的编解码使用urlib库的parse类<br><pre>str1 = parse.quote(str)<br>str2 = parse.unquote(str)</pre>"
    },
    {
        "theme": "code",
        "text": "re模块的扩展语法<br><pre>re.I 匹配对大小写不敏感<br>re.S 匹配包括换行符<br>re.M 多行匹配<br>re.U 根据Unicode编码解析字符<br>re.X 灵活解析<br>re.L 做本地化识别</pre>"
    },
    {
        "theme": "flask",
        "text": "使用link引入css时，rel不注明stylesheet竟然引入后不会被使用"
    },
    {
        "theme": "code",
        "text": "css定义margin-top属性的时候，假如有父子两个div容器，子容器的margin无法作用反而直接作用于父容器上，这种情况一般是由于父容器的padding属性没有设置"
    },
    {
        "theme": "code",
        "text": "跨域问题太恐怖了，就算是有nginx代理添加请求头还是会请求失败，放弃了"
    },
    {
        "theme": "flask",
        "text": "一种a标签内img垂直居中的方案，<pre>a{display: table-cell;vertical-align:middle;}</pre>最简单的处理方法还是<pre>img{position:relative;top:50%;left:50%;}</pre>"
    },
    {
        "theme": "flask",
        "text": "pre标签内文字的自动换行，作用不是很大，效果不如允许自由滑动<pre>word-break: break-all;<br>word-wrap: break-word;<br>white-space: pre-wrap!important;<br>*white-space:normal!important;</pre>"
    },
    {
        "theme": "code",
        "text": "使用jQuery对页面的某个div进行局部刷新的时候，使用的锚点前面一定要加<strong>空格</strong><br><pre>$(\"#ajax_refresh\").load(location.href+' #row');</pre>"
    },
    {
        "theme":"flask",
        "text": "Jinja2模板和javascript语法冲突时，在模板里添加块<br><code>{% verbatim myblock %} {% endverbatim myblock %}</code>被包括区域不会被渲染"
    }
]