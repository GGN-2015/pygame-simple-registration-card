# pygame-simple-registration-card

使用 Pygame 显示全屏定位卡：白色背景，屏幕正中央绘制黑色矩形边框。

## 运行

安装 [uv](https://docs.astral.sh/uv/getting-started/installation/) 后，在项目目录执行：

```powershell
uv run python -m regcard 800 600
```

两个位置参数分别为矩形的宽度和高度，单位为像素，均须为正整数。uv 会自动创建虚拟环境并安装依赖。

项目默认使用 Python 3.13，支持 Python 3.10–3.13。

- 全屏使用当前显示器分辨率，矩形保持指定像素尺寸，边框宽度为 1 像素。
- 按 **Enter**（包括小键盘回车）绕矩形中心逆时针旋转 90°，中心始终与屏幕中心重合。
- 按 **Esc** 退出程序。
- 矩形超出屏幕的部分会被裁切，不会缩放。

项目使用 `pyproject.toml` 声明依赖，使用 `uv.lock` 锁定依赖版本。
