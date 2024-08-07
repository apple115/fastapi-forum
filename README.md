```{=org}
#+filetags:   :项目:
```
```{=org}
#+identifier: 20240331T190249
```
# 使用 nextjs + fastapi + mysql + redis 的论坛

## fastapi

设计一个简单的论坛系统

## 需求

### 用户注册和登录

### 用户资料管理

### 创建和管理主题

### 发布和回复帖子

### 浏览和搜索主题和帖子

### 用户权限管理

帖子是一段话限制一下(字数小于100) 可以添加图片,等

帖子回复帖子:

## 用户角色和权限

定义系统中的不同用户角色及其权限。 超级管理员 (root): 拥有系统的全部权限
管理员 (admin): 管理用户、主题和帖子 普通用户 (user):
创建主题、发布帖子和回复帖子

## 数据库设置

先设计一个用户原类 level 0(root) 1(admin) 2(user) User: id 主键 name
create~at~ email password~hash~ level

Post: id: user~id~: content: topic~id~: reply~id~:

topic: id time title description creator~id~

## api的设计

### 用户相关API

1.  用户注册

    -   POST /register: 用户注册(做完)

    TODO root 密码应该开始的时候就有

    -   GET /verify/{token}: 验证这个(注册)

    1.用户提交注册信息：
    用户填写注册表单并提交用户名、邮箱,密码,和确认密码

    2.生成唯一令牌：
    使用安全的随机生成器创建一个唯一的令牌，这个令牌将用于验证用户的邮箱。

    3.存储注册信息和令牌： 将用户的注册信息和令牌存储在缓存系统（如
    Redis）中，设置一个合理的过期时间。

    4.发送包含验证链接的邮件：
    向用户发送一封包含验证链接的邮件，链接中包含生成的令牌。

    5.创建验证端点：
    在您的应用程序中创建一个验证端点，当用户点击邮件中的链接时，将访问此端点。

    6.验证令牌：
    在验证端点中，检查缓存中是否存在对应的令牌，并验证令牌的有效性。

    7.将用户信息添加到数据库：
    如果令牌验证成功，从缓存中删除注册信息和令牌，并将用户信息添加到数据库中。

    8.设置登录状态： 用户此时可以被设置为已验证，并可以正常登录。

2.  用户登录

    -   POST /login: 用户登录(done)
    -   GET /users/{user~id~}: 获取用户信息(done)

3.  用户忘记密码(TODO)

4.  用户更改密码(TODO)

    <https://emacs-china.org/t/xref-backend-functions-function-list/22297/10>
    这个url 指向一个帖子 22297 指向的是一个主题 10
    指向这个这个主题下的一个帖子

### 主题相关API

-   POST /topics: 创建主题
-   GET /topics: 获取所有主题
-   GET /topics/{topic~id~}: 获取单个主题
-   Patch /posts/{post~id~}/like: 点赞加一

### 帖子相关API

例子

-   POST /posts: 创建帖子
-   GET /posts: 获取所有帖子
-   GET /posts/{post~id~}: 获取单个帖子

### 全局内容设置

## 前端设计

### 首页

-   显示所有主题

### 注册和登录页面

-   提供用户注册和登录功能

### 主题详情页

-   显示主题内容及其下的所有帖子
-   提供发布新帖和回复帖子的功能

### 用户资料页面

-   显示和编辑用户个人信息
