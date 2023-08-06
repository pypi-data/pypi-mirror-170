# Paperl📃
![](https://img.shields.io/pypi/wheel/Paperl?style=flat-square)
![](https://img.shields.io/pypi/v/Paperl?style=flat-square)
![](https://img.shields.io/pypi/l/Paperl?style=flat-square)
![](https://img.shields.io/pypi/pyversions/Paperl?style=flat-square)
![](https://img.shields.io/pypi/dm/Paperl?style=flat-square)
![](https://img.shields.io/pypi/dd/Paperl?style=flat-square)
![](https://img.shields.io/pypi/pyversions/Paperl?style=flat-square)
![](https://img.shields.io/pypi/format/Paperl?style=flat-square)

一个使用众多扩展库与个人研究合并而成的tkinter超级扩展库。

---

## 示例🪧
按下s键可以切换主题
```bash
python -m Paperl
```

---

## 教程🥏

### 安装
首先安装Paperl库，如果需要体验最新内容，可以加上`--pre`选项
```bash
pip install Paperl
```
接下来你可以加入`--upgrade`选项开始更新。
```bash
pip install Paperl --upgrade
```

### 快速开始
先来一个最简单的示例文件。
```python
from Paperl import Application, Window


App = Application()
Window = Window()
App.run(Window)
```

---

### Paperl.Paperui.Widgets 基本组件库
#### Widget
所有组件的父类

- `useStyleSunValley(self, theme: Literal["light", "dark", "auto"] = "auto")`

`theme` 主题，可设置为light浅色模式，dark暗黑模式，auto自动模式

启用太阳谷主题

- `getId(self)`

获取组件的Id

- `gethWnd(self)`

获取组件的窗柄（仅Windows系统）

- `showToast(self, title: str = "", message: str = "Message", appName: str = "Python", appIcon: str = "", timeOut: int = 0)`

`title`通知的标题

`message`通知的文本消息

`appName` 显示通知的应用名

`appIcon` 显示通知的图标文件

`timeOut`通知的显示时间

显示通知

---

#### Application
应用程序，用于调用窗口运行等各种选项

- `alwaysUpdate(self, window)`

`window`表示需要调用的窗口

一直刷新窗口，直到此窗口被销毁。
- `runAsync(self, window)`

`window`表示需要调用的窗口

异步运行窗口，需安装`async_tkinter_loop`库
- `run(self, window)`

`window`表示需要调用的窗口

正常运行窗口，直到主窗口被销毁

```python
from Paperl import Application, Window


App = Application()
Window = Window()
App.run(Window)
```

---

#### Window
窗口组件

---

#### Button
按钮组件

![](./README/Button.png)

- `__init__(self, parent: Widget, text: str = "")` 

`parent` 为组件父组件

`text` 为按钮组件的文本

- `setText(self, text: str)`

`text` 组件的文本属性

设置按钮的文本属性

- `getText(self)`

获取按钮的文本属性

- `onCommand(self, eventFunc: None = ...)`

`eventFunc` 被绑定的事件函数。

绑定按钮被点击后触发的事件

`buttonUseDafaultStyle(self)`

将按钮主题设置为默认

`buttonUseSunValleyAccentStyle(self)`

设置按钮主题为太阳谷主题的Accent状态。

```python
from Paperl import Application, Window, Button


Application = Application()

Window = Window()

Button = Button(Window)
Button.setText("Hello World")
Button.pack()

Application.run(Window)
```

---

## 版本
VER代表版本，后面三个数字代表版本号，最后这个数字代表更新内容的序列

![](./README/Version.svg)

### 0.0.1 

`VER0011` -> 稳定初始版本发布。

---

### 0.0.2 
`VER0020` -> 添加Padevel库，使用ctypes开发无需其他环境，节省安装过程

`VER0021` -> 优化`HeaderBar`，标题也能获得标题栏同样的效果

`VER0022` -> 去除`Window.useStyleSunValley`提示安装tkdev4的信息

`VER0023` -> 加入`TreeView`、`ListBox`组件

`VER0024` -> 为Paperl示例添加热键，按下s键即可切换主题

`VER0025` -> 为`Application`和`Window`组件添加`alwaysUpdate`方法

`VER0026` -> 将Paperl示例程序的标题栏背景材质设为`MainWindow`（仅限Windows11 22H2）

`VER0027` -> 在`Padevel.Windows.Dwmapi`里添加`dwmExtendFrameIntoClientArea`组件（仅限Windows11 21H2）

`VER0028` -> 为`Window`组件添加`positionCenter`方法，用于居中窗口

`VER0029` -> 因为已经将`SunValley`主题纳入依赖库，所以去除使用主题时的提示

`VER00210` -> 将`Padevel.Windows.core`命名为`Core`

`VER00211` -> 完善文档

`VER00212` -> 添加`ToolBar`组件

`VER00213` -> 添加`BreadcrumbBar`组件

`VER00214` -> 添加`PanedWindow`组件

`VER00215` -> 添加`InfoBar`组件

`VER00216` -> 为`Entry`组件加入`setInvalid`方法和`setNotInvalid`方法

---

### 0.0.3
`VER0030` -> 改进对`Python3.9`的支持。

`VER0031` -> 为`Padevel.Winuser`加入更多方法

## 笔记📓
开发时遇到了一些问题，使用ScrollText时，使用createHeaderBarEx设置的标题栏拖动窗口时，会导致程序错误，不知道为什么

---
