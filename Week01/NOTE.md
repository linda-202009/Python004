## 第一周学习笔记

### 1. 用requests写一个简单的爬虫
>**学习知识要点:**

> requests 官方文档链接： https://requests.readthedocs.io/zh_CN/latest/

>1.1 任务实现4步骤：（提出需求、编码、代码run、完善和修复）;

>1.2 headers主要作用：模拟浏览器，主要防止服务器被阻止掉，所以需要增加http里面的头部信息，传入user_agent浏览器相关信息，还可以传入账户密码、token放入headers认证；

>1.3 浏览器的基本上操作.
     
### 2. 使用BeautifulSoup解析爬取到的网页
>**学习知识要点:**

>Beautiful Soup 官方文档链接： https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

>2.1 Chrom浏览器调试功能快捷键：`command + option + i` ;

>2.2 `from bs4 import BeautifulSoup as bs`  as 切记重名函数或者包一定不要重名；

>2.3 BeautifulSoup 内置默认解析方式--THML, 缺点：解析效果不高；

>2.4 `bs_info.find_all('div', attrs={'class': 'hd'})` 查找div元素,以及div下面的 class属性下的，名称等于hd的;

>2.5 `atag.find('span').text` 查找span标签下的text内容,了解了find_all，find之间的区别;
    
>2.6 `atag.get('href')` 获取href链接;

### 3. 使用XPath解析网页 -- 获取详情页的相关信息
>**学习知识要点:**

>3.1 Chrom浏览器快捷键搜索栏：`command + f` ;

>3.2 Chrom 复制XPath信息到搜索栏;

>3.3 `selector.xpath('//*[@id="info"]/span[10]/text()')` /text 获取当前的内容；

>3.4 pandas  `pd.DataFrame` 对数据进行保存；

>3.5 保存到csv文件，字符编码`utf8`，如果是windows需要使用`gbk`字符集。

### 4. 实现爬虫的自动翻页功能
>**学习知识要点:**

>4.1 元组推导式：`tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))` ;

>4.2 page 实现翻页.


### 5. Python基础语法回顾
>**学习知识要点:**

>5.1 python 基础语法

> + Python 简介: https://docs.python.org/zh-cn/3.7/tutorial/introduction.html

> + Python 数据结构: https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html

> + Python 其他流程控制工具 : https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html

> + Python 中的类: https://docs.python.org/zh-cn/3.7/tutorial/classes.html

> + Python 定义函数: https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions

### 6. 前端基础：HTML基本结构
>**学习知识要点:**

>6.1 W3C 标准官方文档: https://www.w3.org/standards/

>6.2 HTTP请求是指什么❓

> + 客户端通过发送 HTTP 请求向服务器请求对资源的访问。 它向服务器传递了一个数据块，也就是请求信息，HTTP 请求由三部分组成：请求行、请求头和请求正文。

>6.3 工作原理

> + 1.由HTTP客户端发起一个请求，建立一个到服务器指定端口（默认是`80`端口）的`TCP`连接，

> + 2.HTTP服务器则在那个端口监听客户端发送过来的请求；

> + 3.服务器（向客户端）发回一个状态行，比如"HTTP/1.1 `200 OK`"，和（响应的）消息，消息的消息体可能是请求的文件、错误消息、或者其它一些信息； 

> + 4.客户端接收服务器所返回的信息通过浏览器显示在用户的显示屏上，然后客户端与服务器断开连接。

>6.3 HTTP协议请求与返回头部

> + 1、HTTP协议请求方式

> + 1 ) `GET或POST`：请求类型，后接请求资源、协议和版本

> + 2 ) `Host`：主机和端口

> + 3 ) `Connection`：是否使用持续连接

> + 4 ) `User-Agent`：客户端浏览器的名称

> + 5 ) `Accept`：浏览器可接受的MIME类型

> + 6 ) `Accept-Encoding`：浏览器知道如何解码的数据编码类型

> + 7 ) `Accept-Language`：浏览器指定的语言

> + 8 ) `Accept-Charset`：浏览器支持的字符编码

> + 9 ) `Cookie`：保存的Cookie对象

> + 2、HTTP响应头

> >　响应头用于指示客户端如何处理响应体，告诉浏览器响应的类型、字符编码和字节大小等信息。

> + 1 ) `Allow`：服务器支持哪些请求方法（如GET、POST等）

> + 2 ) `Content-Encoding`：文档的编码（Encode）类型。只有在解码之后才可以得到Content-Type头指定的内容类型

> + 3 ) `Content-Length`：内容长度。只有当浏览器使用持久HTTP连接时才需要这个数据

> + 4 ) `Content-Type`：表示后面的文档属于什么MIME类型

> + 5 ) `Date`：当前的时间

> + 6 ) `Expires`：文档过期时间

> + 7 ) `Refresh`：表示浏览器应该在多少时间之后刷新文档，以秒计

> + 8 ) `Server`：服务器名称

> + 9 ) `Set-Cookie`：设置与页面关联的Cookie

> + 10 ) `WWW-Authenticate`：客户应该在Authorization头中提供的授权信息类型

> + 3、HTTP响应体

> >　响应头之后紧跟着一个空行，然后接响应体。响应体就是Web服务器发送到客户端的实际内容。除网页外，响应体还可以是诸如Word、Excel或PDF等其他类型的文档，具体是哪种文档类型由`Content-Type`指定的MIME类型决定。


### 7. 前端基础：HTTP协议
>**学习知识要点:**

>7.1 参考文档: https://www.cnblogs.com/ranyonsue/p/5984001.html

>7.2 HTTP响应状态

> + 1 ) `1xx`消息: 请求已被服务器接收，继续处理

> + 2 ) `2xx`成功: 请求已成功被服务器接收、理解、并接受

> + 3 ) `3xx`重定向: 需要后续操作才能完成这一请求

> + 4 ) `4xx`客户端错误: 请求有语法错误或请求无法实现

> + 5 ) `5xx`服务器错误: 服务器在处理某个正确请求时发生错误

> > 常见状态码：

> > `200 OK` 客户端请求成功

> > `400 Bad Request` 客户端请求有语法错误，不能被服务器所理解

> > `401 Unauthorized` 请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用

> > `403 Forbidden` 服务器收到请求，但是拒绝提供服务

> > `404 Not Found` 请求资源不存在，eg：输入了错误的URL

> > `500 Internal Server Error` 服务器发生不可预期的错误

> > `503 Server Unavailable`        //服务器当前不能处理客户端的请求，一段时间后可能恢复正常

> 7.3 HTTP请求方法

> >根据HTTP标准，HTTP请求可以使用多种请求方法。

> > >HTTP1.0定义了三种请求方法：`GET`, `POST` 和 `HEAD`方法。

> > > HTTP1.1新增了五种请求方法：`OPTIONS`, `PUT`, `DELETE`, `TRACE` 和 `CONNECT` 方法。

> > 常见请求方法：

> > `GET` 请求指定的页面信息，并返回实体主体。

> > `HEAD` 类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头

> > `POST` 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。

> > `PUT` 从客户端向服务器传送的数据取代指定的文档的内容。

> > `DELETE1` 请求服务器删除指定的页面。

> > `CONNECT` HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。

> > `OPTIONS` 允许客户端查看服务器的性能。

> > `TRACE` 回显服务器收到的请求，主要用于测试或诊断。