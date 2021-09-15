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
