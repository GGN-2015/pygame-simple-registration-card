# pygame-simple-registration-card

使用 Pygame 显示全屏定位卡：屏幕正中央绘制矩形边框，背景色、线条颜色和线宽可配置，默认白底黑线。

## 运行

安装 [uv](https://docs.astral.sh/uv/getting-started/installation/) 后，在项目目录执行：

```powershell
uv run python -m regcard 800 600
```

两个位置参数分别为矩形的宽度和高度，单位为像素，均须为正整数。uv 会自动创建虚拟环境并安装依赖。

项目默认使用 Python 3.13，支持 Python 3.10–3.13。

可选参数设置背景色，以及矩形边框与内部连线的颜色和线宽，例如使用深灰色背景、红色线条、3 像素线宽：

```powershell
uv run python -m regcard 800 600 --linecolor 255 0 0 --lineweight 3 --bgcolor 32 32 32
```

- `--linecolor R G B`：RGB 三个分量均为 0–255 的整数；普通模式默认 `0 0 0`（黑色），`--showblank` 模式默认 `255 255 255`（白色圆形）。
- `--lineweight PIXELS`：线宽，单位为像素，必须为正整数，默认 `1`。
- `--bgcolor R G B`：背景色，RGB 三个分量均为 0–255 的整数，默认 `255 255 255`（白色），矩形内部与外部背景颜色一致。
- `--showblank`：显示全屏黑色画面，并在屏幕中心绘制实心圆；圆半径为 `min(width, height) / 2` 的整数像素值，默认白色，设置 `--linecolor` 后使用该颜色。该模式隐藏鼠标，忽略 `--lineweight` 和 `--bgcolor`，按回车不改变画面，按 **Esc** 退出。

纯黑屏模式：

```powershell
uv run python -m regcard 800 600 --showblank
```

指定黑屏模式圆形颜色：

```powershell
uv run python -m regcard 800 600 --showblank --linecolor 255 0 0
```

- 全屏使用当前显示器分辨率，矩形保持指定像素尺寸。
- 初始矩形左边中点与上边中点之间有一条连线，与边框颜色和线宽一致，随矩形整体旋转。
- 按 **Enter**（包括小键盘回车）绕矩形中心逆时针旋转 90°，中心始终与屏幕中心重合。
- 按 **Esc** 退出程序。
- 矩形超出屏幕的部分会被裁切，不会缩放。

项目使用 `pyproject.toml` 声明依赖，使用 `uv.lock` 锁定依赖版本。
