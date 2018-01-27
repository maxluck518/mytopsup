# 答题辅助 (百度 OCR Version)

本工程修改自[Skyexu](https://github.com/Skyexu) ，仅供个人娱乐学习使用，原生版本应移步 https://github.com/Skyexu/TopSup 

## 使用步骤（仅Android可用）

有关baidu OCR，请移步详细帮助，[链接](/baidu)

#### 1. 安装 ADB

下载地址：https://adb.clockworkmod.com/
安装完后插入安卓设备且安卓已打开 USB 调试模式，终端输入 `adb devices` ，显示设备号则表示成功。
#### 2. 安装 python 3
#### 3. 安装所需 python 包

命令行：
```
pip install pytesseract
pip install pillow  
pip install requests
```
#### 4. 在 `./baidu/GetWordsBaiduAndroid.py` 中加入相应 key

```
百度OCR API
api_key = ''
api_secret = ''
```

#### 5. 运行脚本

##### 辅助策咯：

    1.  打开浏览器查询
    2.  词频搜索

##### 使用方法：

1. 在`./config/settings.py`中修改增加可支持的app参数（region,pos）

   ```
    # 添加app
    SUPPORT_APP_TYPE = ["youku","uc","dabai"]
    # 定义答题框范围
    REGION_DICT = {
            'youku':(75, 350, 990, 1300),
            'uc' : (75, 400, 990, 1220),
            'dabai' : (75, 400, 990, 1220),
            'default' : (75, 350, 990, 1200)
            }
    # choices起始位置，避免选项前缀干扰
    POS_DICT = {
            'youku' : 2 ,
            'uc' : 2 ,
            'dabai' : 1 ,
            'default' : 0
            }
   ```

2. 命令行下运行：

   西瓜，冲顶，芝士超人，命令行下输入：

   ```
   python RunAndroid.py
   ```

   支持UC浏览器答题软件，命令行下输入：

   ```
   python mjwGetQuestionTessAndroid.py uc
   ```
   支持优酷答题软件，命令行下输入：

   ```
   python RunAndroid.py youku
   ```
