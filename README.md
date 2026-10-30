# Pose

[English](README.en.md) · [下载安装包](https://github.com/nihaomaaa/Pose/releases/latest) · [API 支持表](docs/API_SUPPORT.md)

Windows 上的人物姿势创作工具。上传人物照片，从 1,439 张姿势视图中挑选参考，在同一个界面中生成、预览和下载。普通双人姿势使用两个人各自的照片。

**免费本地生成，无需 ChatGPT 会员或 API Key。** 也可以连接自己的云端图片 API。云端服务可能收费，ChatGPT Plus 不等于图片 API 额度。

## 安装与开始

1. 从 Releases 下载 **Pose-Setup-0.3.0-x64.exe**，双击安装。需要 Windows 10/11 x64。
2. 打开 Pose，阅读使用协议。在右上角选择中文或 English。
3. 选择“自动推荐”，点击“开始自动配置”。程序检测硬件、安装独立运行环境、下载并校验模型与图库，再执行一次真实出图自检。
4. 进入创作台，上传照片，选择姿势并生成。双人参考默认要求人物 A、B 两张不同照片；只有主动勾选“同一人物分饰两角”才复用照片。
5. 结果保存于本机，可放大、下载、查看历史，或继续选择其他姿势。

首次下载较大；安装完成后的本地模式可离线使用。不需要命令行、Python 安装经验或 CUDA Toolkit。显卡驱动需已正确安装。

本版本未购买 Windows 代码签名证书，系统可能显示“未知发布者”。请从本仓库 Releases 获取安装包并核对 SHA-256，不要关闭系统安全防护。

## 模型与电脑配置

| 偏好 | 模型及要求 |
| --- | --- |
| 自动推荐 | FLUX.2 klein 4B，按硬件选择 NF4 或完整精度；免账号，Apache 2.0 |
| 节省空间 | 同一 4B 模型，优先 NF4 节省显存；磁盘下载仍约 17 GB，不是假装更小的权重文件 |
| 更好效果 | FLUX.2 klein 9B，权重约 35 GB；需自行接受 BFL 非商业许可并提供 Hugging Face 读取令牌；不保证每张都优于 4B |
| 自定义 | 粘贴兼容的 Hugging Face **蒸馏版 Flux2KleinPipeline / Diffusers 仓库**链接，先检查再下载；不接受任意 checkpoint、LoRA、GGUF 或 Python 插件 |
| API 模式 | 不下载本地模型和 Python，只准备图库；速度、效果、费用和限制取决于所选服务 |

默认本地 GPU 模式建议 NVIDIA CUDA 架构 7.0+、至少 6 GiB 显存和 24 GiB 内存，至少预留 45 GB 磁盘。24 GiB 显存 / 48 GiB 内存可使用完整精度。无合适 NVIDIA GPU 时，需要至少 48 GiB 内存、55 GB 磁盘才能使用很慢的 CPU 模式。AMD / Intel GPU 暂无本机加速适配。

9B 建议至少 8 GB 显存、32 GB 内存、65 GB 空余磁盘；CPU 模式至少 64 GiB 内存。配置门槛不代表所有机器都能稳定运行，安装后的出图自检会确认实际兼容性。已在 RTX 4060 8 GB / 32 GB RAM 上验证 4B 双人真实出图；9B、CPU 和其他 GPU 配置未全部实机验证。

## 下载与大陆网络

支持暂停续传、失败重试、文件长度与 SHA-256 / Git blob 校验。下载阶段显示实际网络传输速度与预计剩余时间；解压、依赖安装和出图自检没有可信进度时会明确显示无法估时。

“自动 / 大陆网络优先”使用 HF Mirror、jsDelivr 和清华 PyPI，并保留官方源回退；也可选择只使用官方源。受许可保护的模型只向 Hugging Face 官方发送令牌。Python、PyTorch/CUDA 组件仍使用官方分发，不能保证任何地区或网络下都能直连。可使用 Windows 系统 HTTP 代理。镜像故障时切换来源或稍后续传。

首次设置可以更改数据保存位置，切换目录不会自动搬移旧数据。模型文件下载完成后会做完整哈希校验，因此“网速为零”不一定是卡住。

## API 连接

在“设置 → API 连接”中选择服务商，填写自己的模型、基础地址和密钥，确认传输与费用提示，再保存。预设包含豆包 Seedream、通义 / Qwen、腾讯混元、Gemini / Nano Banana、GPT Image、FLUX、Ideogram、fal.ai、Replicate 等多图编辑适配；其他服务的文字生图和本机工作流能力见 [完整支持表](docs/API_SUPPORT.md)。

**不能把所有服务名称都视为同一种生图 API。** DeepSeek 官方接口、OneDiff、Text-Generation-Inference 不提供本项目所需的独立图片生成协议，界面明确说明并阻止误配。DALL·E 已退役，OpenAI 预设使用当前 GPT Image 编辑接口。只支持文字生图的适配进入独立文字模式，不发送人物照片，也不承诺人物身份保持。

密钥由 Windows 用户安全机制加密保存在本机；修改 API 地址时需要重新填写或清除原密钥，避免误发。连接检测只检查服务器是否可达，不会付费生图，也不证明密钥、额度或模型权限有效。协议适配有离线模拟测试，尚未用各家付费账号逐一实测。服务商可能拒绝内容、收费或变更模型；停止等待不一定能停止云端任务和计费。Pose 不绕过审核、不自动切换其他服务。

## 隐私、许可与限制

- 本地生成不会把照片传往云端；云端模式在确认后向你选择的服务传递必要输入。无内置统计、广告或遥测。
- 照片、作品、模型和环境默认保存于 Windows 用户本地应用数据目录下的 **PoseAtelier**。安装、更新和卸载默认保留这些数据。删除历史作品不同时删除原图。
- Pose 原创代码采用 [PolyForm Noncommercial 1.0.0](LICENSE)，仅供合法、非商业使用。**这是源码公开项目，并非允许商业使用的 OSI 开源许可证。** 第三方组件各自的许可证不变。
- 姿势图库源自于 [anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh) 支持；原作ギア、汉化 Anhao。图片与数据保留原作者权利，遵守上游非商业要求。EXE 和源码仓库不打包图库图片或模型权重，而从固定上游版本下载并校验。
- 全部图库可搜索浏览；已核验的普通双人动作可生成。露骨性行为参考仅供浏览，不能用于人物照片生成。请使用有处理授权的人物照片。
- AI 不能保证完全保留身份、衣服、手指与身体细节。发布结果应明确说明 AI 生成，不得冒充真实事件或移除服务商来源标识。

[中文协议](docs/TERMS.zh-CN.md) · [English terms](docs/TERMS.en.md) · [隐私说明 / Privacy](docs/PRIVACY.md) · [第三方声明](THIRD_PARTY_NOTICES.md)

英文协议链接采用注明地区的美国纽约州肖像 / 隐私权及欧盟法律参考。界面语言不决定适用法律，“仅供学习”也不是免除侵权责任的依据。

## 关于与支持

关于页面提供项目和上游链接。Star 按钮打开 GitHub 并显示磨砂感谢提示；如选择自动点赞，需要本人提供仅用于当次操作的 GitHub Starring 读写授权。打开网页不会冒充点赞成功，令牌不会保存。

## 开发与构建

普通用户无需执行以下步骤。开发者使用 Windows x64 与 Node.js 24：

    npm ci
    npm test
    npm run build

prepare 脚本从 Astral 官方下载固定版本 uv 并验证 SHA-256；图标由项目 SVG 构建。输出在 dist/。npm start 启动开发版。工作流在版本标签或手动运行时构建并发布 Windows 安装包和校验值。

POSE_DESKTOP_DATA、POSE_CONFIG_DIR 可指定隔离测试目录；POSE_SHOW_SETUP=1 显示设置页。发行版不预置个人路径、代理、照片、密钥或模型缓存。

[贡献指南](CONTRIBUTING.md) · [安全说明](SECURITY.md) · [模型 / 工作流接入](docs/MODELS_AND_WORKFLOWS.md)
