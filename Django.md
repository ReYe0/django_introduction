# 1、django基础命令



创建项目 django-admin startproject django_introduction
运行项目 python manage.py runserver
创建应用 python manage.py startapp blog

# 2、数据迁移
方法一：

生成迁移文件 python manage.py makemigrations
运行迁移文件，把表结构同步到数据库（如mysql）中去 python manage.py migrate

方法二：

python manage.py dumpdata > data.json
python manage.py loaddata data.json

# 3、创建超级管理员


Django shell 进入面向过程编程，可以查看数据库 python manage.py shell

创建Django Admin模块超级管理员 python manage.py createsuperuser

# 4、部署到linux服务器上



### 1、用pycharm导出项目依赖包
```shell
pip install pipreqs

# 进入到项目所在目录，在执行下面的命令
$> pipreqs . --encoding=utf8 --force	#或者用pip3 freeze > requirements.txt命令
 
# “.” 指的是将导出依赖包的文件放在当前目录下
# “--encoding=utf8” 指的是存放文件的编码为utf-8,否则会报错
# “--force”  --force 强制执行，当生成目录下的requirements.txt存在时强制覆盖
```

### 2、打包为docker镜像
    dockerfile放在源代码目录下
    DockerFile 文件如下

```shell script
# 使用官方的 Python 镜像作为基础镜像
FROM python:3.7.9 

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y gcc 

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 暴露端口
EXPOSE 800

# 运行 Django 开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

```
打包命令 docker build -t my_django_app .
完成后运行：docker run -p 8000:8000 my_django_app
前端vue，Nginx 配置




### 3、vue同理
Dockerfile
```shell script
# 使用官方的 Node.js 镜像作为基础镜像
FROM node:14

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package*.json ./

# 安装项目依赖
RUN npm install

# 复制所有文件到工作目录
COPY . .

# 构建 Vue 项目
RUN npm run build

# 安装 Express
RUN npm install express

# 暴露端口
EXPOSE 8080

# 启动 Node.js 服务器
CMD ["node", "server.js"]

```

# 5、django 测试全部方法命令



命令：` python manage.py test polls`，polls是应用名

## 5.1 数据库api

django 两model，有一个是另一个外键的情况下， 可以相互取对方的对象实例

```Python shell
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

```Python shell
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```