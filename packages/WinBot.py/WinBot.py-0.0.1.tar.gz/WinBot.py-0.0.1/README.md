## AiBot 使用方法说明

### 下载安装

```shell
pip install WinBot.py
```

### 使用 AiBot 编写脚本

```python
# 1. 导入 AiBotMain 类
from WinBot import WinBotMain

def main():
    # 1. 构建实例，传入监听的端口
    driver = WinBotMain.build(3000)
    
    # 2. 调用 API
    # 查询窗口句柄
    result = driver.find_window("TXGuiFoundation")
    print(result)  # 1050010
    
    # 移动鼠标
    driver.move_mouse("1050010", 100, 100, False)
    
    # 隐藏窗口
    driver.show_window("1050010", False)

if __name__ == '__main__':
    # 执行脚本
    main()
```
> 教程中仅演示部分 api，更多 api 请自行查阅 [WinBot 官方文档](http://www.ai-bot.net/android.html) 。
