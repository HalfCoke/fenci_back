# 基于 Python 3.9 镜像构建
FROM python:3.9

# 设置工作目录
WORKDIR /app

COPY . .

# 安装依赖包
RUN pip install -r requirements.txt

# 暴露 5000 端口
EXPOSE 5000

# 运行 Flask 应用
CMD ["python", "server.py"]