# BLOG
django project blog
配置开发环境
数据库
    mariadb
    第三方库 pymysql
python virtualenv
    python3.6.1

1.创建项目
    django-admin startproject blog
    python-

blog model 结构
    1.artitle table
        1.title 题目
        2.author 作者
        3.desc 文章简介
        4.content 文章内容
        5.created 创作时间
        6.upddate 更新时间
        7.draft  是否发表
        8.category 分类
        9.tag 标签
        10.agreed 点赞
        11.disagreed 反对
        12.visited 浏览数
    2.comment table 评论
        1.content 内容
        2.author 作者
        3.artical 评论的文章
        4.created 发表时间
        5.commentid 父级评论
        6.agreed
        7.disagreed
    3.user table
        1.头像
        2.phone
        3.email
        4.name
        5.password




