# 第三方组件与素材

应用原创代码采用 PolyForm Noncommercial 1.0.0；其他组件分别遵循其原始许可，本文件不替换这些许可。

| 组件 | 许可 / 来源 | 分发方式 |
| --- | --- | --- |
| Electron / Chromium / Node.js | Electron MIT、Chromium BSD 类及其他；https://www.electronjs.org/ | EXE 内含运行时；完整第三方文本在安装目录 LICENSES.chromium.html、LICENSE.electron.txt |
| uv 0.13.6 | MIT 或 Apache 2.0；https://github.com/astral-sh/uv | EXE 包含 uv.exe；附 licenses/uv-MIT.txt |
| CPython (python-build-standalone) | PSF 等；https://github.com/astral-sh/python-build-standalone | 首次启动由 uv 下载官方构建 |
| PyTorch / torchvision | BSD 类；https://pytorch.org/ | 首次启动由官方 wheel 安装，依赖各有许可 |
| CUDA wheel 组件 | NVIDIA 组件许可；https://developer.nvidia.com/cuda-toolkit | 随官方 PyTorch wheel 下载；遵循其独立许可 |
| diffusers / transformers / accelerate / bitsandbytes | Apache 2.0 / 各发行包许可；https://huggingface.co/ | 首次启动从 PyPI 安装 |
| FLUX.2 klein 4B | Apache 2.0；https://huggingface.co/black-forest-labs/FLUX.2-klein-4B | 下载锁定版本的权重与 LICENSE.md，未随 EXE 或本仓库分发 |
| FLUX.2 klein 9B | BFL 非商业许可；https://huggingface.co/black-forest-labs/FLUX.2-klein-9B | 可选下载，必须由用户自行接受官方许可；不随软件分发 |
| 姿势图库 | https://github.com/anhao/ai-pose-gallery-zh | 首次启动下载锁定版本；非商业素材 |

## 原始图库

原作：ギア。汉化：Anhao。请阅读 [上游声明](licenses/gallery-UPSTREAM.txt)。原项目的 MIT 许可仅覆盖 HTML/CSS/JavaScript 等代码，**图片、姿势数据不在 MIT 授权范围内**，保留原作者权利，仅供非商业使用。

本仓库不包含上游图片或原始 pose-zh.json / meta-zh.json。文件清单保留上游版本与 Git 校验值；派生姿势说明/英文动作词也不扩大上游素材的使用许可。请不要把应用开源理解为图库可自由商用。

## 字体和图标

界面使用用户系统已安装的字体，无外发 Apple 字体；Pose 标识与应用图标为项目绘制的 SVG/几何图形。Apple 风格表示界面设计方向，与 Apple 公司无关联。
