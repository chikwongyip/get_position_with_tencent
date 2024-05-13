# txmap

#### 介绍
使用腾讯地图WebService API获取经纬度坐标

#### Python版本
3.7.6(3.6以上均可)

#### 相关依赖
- python-dotenv: 使用环境变量配置key键值
- requests: 发送GET请求
- openpyxl: 操作xlsx表格

#### 使用方法
手动在项目根目录下创建`.env`文件,内容编辑为下面格式(使用腾讯地图KEY进行替换)

```ini
KEY=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
```

安装依赖

```shell script
pip install -r requirements.txt
```

运行主程序

```shell script
python main.py
```