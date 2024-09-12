FROM python:3.12 
# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY pyproject.toml poetry.lock /app/

# 安装 Poetry
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple poetry

# 根据参数安装依赖
RUN poetry install

# 复制脚本和应用程序代码
COPY ./scripts/ /app/
COPY ./app /app/
