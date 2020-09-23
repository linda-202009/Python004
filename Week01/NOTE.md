## 第一周学习笔记

### 1. 用requests写一个简单的爬虫
    学习知识要点：
    requests 官方文档链接： https://requests.readthedocs.io/zh_CN/latest/
    1.1 任务实现4步骤：（提出需求、编码、代码run、完善和修复）；
    1.2 headers主要作用：模拟浏览器，主要防止服务器被阻止掉，所以需要增加http里面的头部信息，传入user_agent浏览器相关信息，还可以传入账户密码、token放入headers认证；
    1.3 浏览器的基本上操作；
     
### 2. 使用BeautifulSoup解析爬取到的网页
    学习知识要点：
    Beautiful Soup 官方文档链接： https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
    2.1 Chrom浏览器调试功能快捷键：command + option + i 
    2.2 from bs4 import BeautifulSoup as bs  /  as 切记重名函数或者包一定不要重名；
    2.3 BeautifulSoup 内置默认解析方式--THML,缺点：解析效果不高；
    2.4 bs_info.find_all('div', attrs={'class': 'hd'}) 查找div元素,以及div下面的 class属性下的，名称等于hd的
    2.5 atag.find('span').text 查找span标签下的text内容
    2.6 atag.get('href') 获取href链接

### 3. 使用XPath解析网页 -- 获取详情页的相关信息
    >        <strong>学习知识要点</strong>
    3.1 Chrom浏览器快捷键搜索栏：command + f
    3.2 Chrom 复制XPath信息到搜索栏
    3.3 selector.xpath('//*[@id="info"]/span[10]/text()') /text 获取当前的内容；
    3.4 pandas  pd.DataFrame 对数据进行保存；
    3.5 保存到csv文件，字符编码utf8，如果是windows需要使用gbk字符集。

### 4. 实现爬虫的自动翻页功能
