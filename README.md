# learning_log

## 激活环境

`source ll_env/bin/activate`

## 添加环境激活脚本

1. 给脚本加权限 `chmod 777 run.sh`
2. 执行脚本 `. run.sh`

## 迁移数据库

```
python3 manage.py makemigrations learning_logs
python3 manage.py migrate
```

## Django shell

`python3 manage.py shell`

## 创建包含包列表的文件 `requirements.txt`

`pip freeze > requirements.txt`

命令 `freeze` 让 `pip` 将项目中当前安装的所有包的名称都写入到文件 `requirements.txt` 中

## 启动 Procfile 进程

`heroku local`
