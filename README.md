[README-Pose.md](https://github.com/user-attachments/files/34163683/README-Pose.md)
# Pose

**换一个姿势，保留你的样子。 · A different pose. Still you.**

Windows 人物姿势 AI 创作工具 / An AI pose-editing studio for Windows.

[简体中文](#简体中文) · [English](#english) · [项目主页 / Repository](https://github.com/nihaomaaa/Pose) · [版本发布 / Releases](https://github.com/nihaomaaa/Pose/releases) · [问题反馈 / Issues](https://github.com/nihaomaaa/Pose/issues)

> **版本 / Version：0.3.0 · Windows 10 / 11 x64**  
> **发布状态 / Publication status（2026-10-30）：**本地安装包已构建；GitHub 尚未发布 Release，公开下载以 Releases 页实际附件为准。 / The local installer has been built. No GitHub Release is published yet; public downloads depend on the assets actually available on the Releases page.

---

## 简体中文

### Pose 是什么？

Pose 将人物照片、姿势图库和 AI 生图整合在一个桌面界面中。上传照片，从图库选择姿势，再点击生成，即可在软件内预览、下载和继续创作，无需来回复制提示词或手动上传姿势参考图。

它适合个人非商业创作练习、人物姿势研究、绘画参考和 AI 图像编辑实验。模型会尝试保留人物的脸部、发型、服装、体型与整体外貌，同时改变姿态和必要视角；**身份与细节保持是生成目标，不能保证每张结果完全一致。**

### 主要功能

- **照片换姿势：**上传人物照片，选择姿势并生成，支持预览、下载、历史记录和重新生成。
- **双人独立参考：**普通双人姿势默认分别上传人物 A、B 的照片，并显示角色对应关系；只有主动选择“同一人物分饰两角”才复用一个人物。
- **完整图库浏览：**按原项目分类整理 288 个姿势、1,439 张视图，支持搜索、分类筛选、拍摄角度、收藏及多视角浏览。全部视图可浏览，实际可生成范围见下文。
- **免费本地模型：**根据硬件推荐运行方式，自动准备独立环境、下载模型与图库并校验文件。
- **自己的 API：**可连接已适配的云端图片服务或本机推理服务，提供图片编辑与独立文字生图模式。
- **中文与英语：**界面内切换语言；采用简洁的 Apple 风格设计、圆角菜单及适量磨砂效果。
- **可见的下载状态：**支持暂停续传、重试，下载时显示可测量的实时速度与预计剩余时间。

### 安装与第一次使用

1. 在 [Releases](https://github.com/nihaomaaa/Pose/releases) 有正式附件后，下载 **Pose-Setup-0.3.0-x64.exe**，双击安装。其他版本请以对应 Release 的文件名为准。
2. 从桌面或开始菜单打开 **Pose**，阅读首次使用协议，可选择中文或 English。
3. 选择生成方式：
   - **本地生成：**选择“自动推荐”，确认保存位置，点击“开始自动配置”。程序准备运行环境、模型与图库，完成校验和真实出图自检后进入创作台。
   - **API 生成：**打开“设置 → API 连接”，配置自己的服务商、模型、地址与密钥，阅读云端传输和费用提示后保存。此模式准备图库，不安装本地模型与 Python。
4. 上传一张清晰的人物照片，从图库选中姿势。双人姿势需分别上传 A、B，可按角色说明交换两张照片。
5. 点击“生成图片”，等待完成，再放大预览、下载或选择其他姿势继续生成。

普通用户无需使用命令行，也无需自行安装 Python 或 CUDA Toolkit；NVIDIA 显卡驱动仍需正常安装。首次配置会下载较大文件，本地环境完成准备后可离线生成。

当前安装包未进行 Windows 代码签名，系统可能显示未知发布者。下载时请核对发布渠道及同一 Release 提供的 SHA-256 校验文件，不要关闭系统安全防护。

### 电脑配置与模型选择

当前只提供 **Windows x64** 安装包；没有 macOS、Linux、Windows ARM64 安装包。能打开界面不代表电脑满足本地生图要求。

| 使用方式 | 配置参考 | 磁盘空间 |
| --- | --- | --- |
| 4B 显卡模式 | NVIDIA CUDA 架构 7.0+，至少 6 GiB 显存、24 GiB 内存；通常使用 NF4 降低显存占用 | 至少预留 45 GB |
| 4B 完整精度 | 至少 24 GiB 显存、48 GiB 内存 | 至少预留 45 GB |
| 4B CPU 模式 | 至少 48 GiB 内存；速度可能很慢 | 至少预留 55 GB |
| 9B 显卡模式 | 建议至少 8 GB 显存、32 GB 内存 | 至少预留 65 GB |
| 9B CPU 模式 | 至少 64 GiB 内存；速度可能很慢 | 至少预留 65 GB |
| API 模式 | 不需要满足本地模型的显存门槛；仍需服务连接及图库存储空间 | 不下载本地模型权重 |

上述是程序的配置参考，实际兼容性以驱动、可用内存和出图自检为准。**暂未适配 AMD / Intel GPU 加速**，不满足本地要求时可选择 API 模式。

| 偏好选项 | 实际行为 |
| --- | --- |
| 自动推荐 | 使用 FLUX.2 klein 4B，按硬件选择 NF4 或完整精度。4B 为 Apache 2.0 模型，无需模型账号。 |
| 节省空间 | 选择较小的 4B 家族，优先降低显存占用。权重下载仍约 17 GB；NF4 在加载时量化，不会缩小原始下载文件。 |
| 更好效果 | 使用 FLUX.2 klein 9B，权重约 35 GB；需本人在 Hugging Face 接受官方非商业许可并提供具备读取权限的令牌。不能保证每张图片都优于 4B。 |
| 自定义模型 | 粘贴兼容的 Hugging Face 蒸馏版 Flux2KleinPipeline / Diffusers 仓库链接，检查后下载。 |

自定义模型不支持任意单文件 checkpoint、LoRA、GGUF、非蒸馏基础模型或可执行 Python 插件。应用检查配置、固定下载版本并校验文件，不运行模型仓库附带的远程 Python 代码。兼容格式也不等于一定适合当前电脑。

**验证范围：**50 项自动测试已通过；RTX 4060 8 GB / 32 GB 内存上完成过 4B 双人真实出图，单次测试约 65 秒。此数据不是速度承诺；9B、CPU 和其他硬件配置尚未全部实机验证。

### 下载源、网络与存储

- “自动 / 大陆网络优先”使用 HF Mirror、jsDelivr、清华 PyPI 等来源，并保留官方源回退；也可选择官方源。
- Python、PyTorch / CUDA 组件仍需访问其官方分发服务，不能保证所有网络环境都能直连。支持 Windows 系统 HTTP 代理。
- 受限模型的 Hugging Face 下载令牌只发往官方域名，不发送到镜像。账号访问许可需由每位用户自行取得。
- 支持续传、失败重试、长度及 SHA-256 / Git blob 校验。网速和剩余时间仅在可测量的下载阶段显示；依赖安装、校验和首次出图可能无法准确估时。
- 默认数据目录为 Windows 本地应用数据目录下的 **PoseAtelier**。可在设置中打开数据文件夹，并在首次配置阶段选择其他位置。
- 更改保存位置不会自动迁移原目录。模型、照片、作品与环境会占用持续增长的空间，应用不会擅自删除已下载模型。

### API 与工作流支持

API 模式使用你自己的账号、地址、模型权限与额度。**本地免费生成不需要 API；云端服务可能单独收费。ChatGPT Plus 会员不能直接充当本应用的图片 API 授权。**

| 服务或项目 | Pose 0.3.0 当前适配范围 |
| --- | --- |
| 火山引擎方舟 / 豆包 Seedream | 多图编辑 |
| 通义万相 Wan、Qwen-Image | 多图编辑 |
| 腾讯混元生图 | 多图编辑；当前预设面向国际 TokenHub 接口 |
| OpenAI GPT Image（DALL·E 类服务入口） | 多图编辑；使用 GPT Image 预设，不保证旧模型可用 |
| Google Gemini / Nano Banana | 多图编辑 |
| FLUX / Black Forest Labs、Ideogram、fal.ai、Replicate | 所选适配模型的多图编辑 |
| CogView、文心 / 百度千帆、Stability AI、Google Imagen | 当前适配仅文字生图 |
| Recraft、SiliconFlow、ModelsLab、Hugging Face Inference Endpoints | 当前适配仅文字生图；HF 需兼容的专用端点 |
| Automatic1111、Xinference | 当前适配仅文字生图，需已运行的兼容服务 |
| ComfyUI | 导入可信 API 工作流，在界面中映射人物 A、人物 B、姿势及提示词输入 |
| 自定义 OpenAI 兼容接口 | 必须实现当前适配器要求的图片编辑协议；仅兼容聊天接口不足以接入 |
| DeepSeek 官方 API、OneDiff、Text-Generation-Inference | 未作为独立图片生成端点接入；界面会说明能力限制 |

“已适配服务”不代表该服务的任意模型、任意地区、任意接口都通用。OneDiff 可用于你另行部署的加速服务，例如通过 ComfyUI 连接；Pose 不会自动部署这些外部服务器及其模型。

**配置步骤：**进入 API 连接页，选择服务，填写对应地址、模型及密钥，确认数据传输和费用说明后保存。双人编辑需服务本身支持 A、B 与姿势三个参考输入。文字模式不会发送人物照片，也不承诺身份保持。

ComfyUI 需先准备能够处理人物与姿势的 API 格式工作流。Pose 提供节点映射和后续自动传图，不会把普通文字生图工作流自动变为人物换姿势工作流，也不会静默安装自定义节点。

连接检测只验证服务器可达性，不会付费生图，也不证明密钥、余额或模型访问权限有效。各适配器经过模拟协议测试，**尚未使用每一家付费账号逐一验证真实生图**。服务商可能因审核、额度、地区或权限拒绝请求；停止本地等待不一定停止远端计算或计费。软件不绕过审核，也不在失败后悄悄更换服务商。

### 隐私与数据处理

| 场景 | 数据去向 |
| --- | --- |
| 本地生成 | 人物照片、提示词和生成过程由本机引擎处理，不上传给云端图片服务。 |
| 安装与下载 | 连接运行环境、模型、图库及镜像服务器，对方接收 IP、文件请求路径等常规网络信息。 |
| 云端图片编辑 | 在确认后，将提示词及必要的人物、姿势参考发送给你配置的服务；结果可能从服务商 CDN 下载。 |
| 文字生图 | 发送提示词与生成参数，不发送人物照片。 |

- 不内置广告、分析统计或遥测。
- 原图、作品、任务信息、日志、模型与环境保存于本地，直到你主动处理；没有自动到期删除。
- API / Hugging Face 密钥通过 Windows 用户级安全机制加密，调用时仍需短暂存在内存中。该保护无法抵御已控制当前 Windows 用户账户的恶意程序。
- 修改已保存 API 地址时，需要重新输入或清除旧密钥；密钥不会被转发给结果图片的下载地址。
- 照片可能包含 EXIF 等元数据；选择云端前请自行处理不希望传出的信息，并查看服务商的留存、训练、跨境传输与删除政策。
- 更新和卸载默认保留本地数据。删除历史作品不会同时删除原图，也无法删除服务商留存的副本。重要作品请自行备份。
- 不要把密钥、私密照片、完整数据目录或未检查的日志上传至公开 Issue。

### 使用声明与许可

**非商业用途。** Pose 原创代码采用 **PolyForm Noncommercial 1.0.0**，用于符合许可证的非商业学习、研究和交流。不得销售软件、出售访问权限、经营付费生图服务，或将本项目用于商业牟利。完整许可见项目 LICENSE 文件；本段不替代许可原文。该许可证不属于 OSI 认可的开源许可证，因此本项目应准确称为“源码公开 / source-available”。

**第三方权利。** 组件、模型、图库各自适用独立许可。本项目的代码许可不会扩大第三方素材的使用权。FLUX.2 klein 4B 自身采用 Apache 2.0，并不意味着使用整个 Pose 项目可以忽略其非商业限制；9B 仍须遵循官方模型条款。

**图片与人物授权。** 仅使用拥有合法处理权限的照片，并取得被拍摄人物对相关处理的必要同意。尊重著作权、肖像、隐私、名誉及其他合法权益。禁止未经同意的私密影像、涉及未成年人的性内容、诈骗、冒充、诽谤及其他违法用途。

**图库生成边界。** 全部图库可搜索浏览；仅已核验的普通双人动作支持人物照片生成。露骨性行为参考为浏览用途，不能用于人物照片生成，不提供解除限制或绕过服务商审核的功能。

**结果与标识。** AI 可能改变人物身份、衣着、体型、手指、肢体与画面细节。请逐张检查，勿将生成结果当作真实事件的证明。对外发布时应按适用法律与平台规则声明 AI 生成，不得恶意删除、伪造或隐匿服务商水印及来源标识。

**责任与适用法律。** 软件按现状提供，在法律允许的范围内不保证特定结果、无错误或持续可用；不排除依法不得免除的责任或用户法定权利。“仅供学习交流”不能自动免除侵权责任。本说明不构成法律意见或合规保证。界面语言不决定适用法律，相关要求需结合使用者、被拍摄人物及传播地区判断。

应用的中文协议提供中国大陆相关法律参考；英文协议提供注明地区的美国纽约州肖像 / 隐私及欧盟 AI 透明度、数据保护资料。它们是地区性参考，并非适用于所有国家的统一规则。

### 常见问题

**必须购买 ChatGPT 会员或 API 吗？**  
不需要。符合硬件要求时可以使用免费本地模型。可选 API 使用用户自己的账号，费用由服务商决定，软件不附赠额度。

**为什么选择“节省空间”仍需下载十几 GB？**  
4B 相比 9B 更小，但 NF4 主要降低运行时显存占用。当前不提供预先量化的小体积权重包，不会把原始下载文件伪装成更小模型。

**下载没有网速，是不是卡住？**  
可能正在解压、安装依赖、校验模型或执行首次出图。先查看当前阶段；下载阶段失败时可暂停续传或更换来源。不同网络的连通性无法保证。

**我的电脑没有 NVIDIA 显卡怎么办？**  
有足够内存时可使用较慢的 CPU 模式，或连接自己的 API。AMD / Intel GPU 暂无加速适配。

**9B 为什么要求登录 Hugging Face？**  
这是官方模型的访问和许可要求。每位用户需自行授权，软件不会共享作者令牌或代替用户接受模型许可。

**为什么人物不完全一样，或姿势不够准确？**  
生成模型不是确定性的姿态或身份复制工具。请使用清晰、无遮挡、尽量完整的人物照片，核对 A/B 角色，尝试其他种子或姿势，并检查结果。换用更大模型也不保证完全一致。

**删除记录或卸载会删除所有照片吗？**  
不会。删除作品与删除原图是不同操作；卸载默认保留数据目录。退出应用、备份所需内容后，可自行清理本地目录。

### 开发、构建与反馈

普通用户无需执行本节。开发者使用 Windows x64、Node.js 24，在包含 package.json 的项目目录运行：

~~~bash
npm ci
npm test
npm start
# 构建 Windows 安装程序
npm run build
~~~

构建产物位于 dist/。准备脚本下载固定版本的 uv 并校验 SHA-256；图标由项目 SVG 生成。可通过 POSE_DESKTOP_DATA、POSE_CONFIG_DIR 指定隔离测试目录，POSE_SHOW_SETUP=1 强制显示设置页。不要将个人模型缓存、照片、密钥、代理配置或私有路径提交到仓库。

问题反馈请使用 [GitHub Issues](https://github.com/nihaomaaa/Pose/issues)，注明版本、Windows / 显卡 / 内存、所用模型或服务及复现步骤，并提供已脱敏的错误信息。发现凭据泄露或安全问题时，不要在公开 Issue 发布敏感细节；优先使用仓库提供的私密报告渠道（如可用）。

“关于”页提供项目链接与 Star 按钮。打开 GitHub 会显示感谢提示；在网页上是否点赞由用户决定。可选的自动 Star 需要本人一次授权，仅在 GitHub 确认后显示成功，不保存该次令牌。

### 致谢

**源自于 [anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh) 支持。** 原始姿势素材作者：ギア；中文汉化：Anhao。

上游代码与图片、姿势数据的授权范围不同：图片和数据保留原作者权利，并遵守其非商业要求，不因上游代码采用 MIT 就获得任意商用权。EXE 和源码仓库不包含模型权重或图库图片，由首次配置下载固定版本并校验。

感谢 Black Forest Labs、Hugging Face、Electron / Chromium / Node.js、Astral uv、PyTorch 及相关模型与工具的贡献者。各组件仍受自身许可约束。界面风格与 Apple 公司无关联，也不意味着获得其背书；本项目与所列云端服务商亦无隶属或背书关系。

---

## English

### What is Pose?

Pose brings subject photos, a pose library and AI image generation into one Windows desktop interface. Upload a photo, select a pose, then generate, preview and download without copying prompts or manually moving reference images between applications.

It is intended for personal, noncommercial creative practice, pose studies, drawing references and AI editing experiments. The model attempts to preserve a person's face, hairstyle, clothing, body shape and appearance while changing posture and necessary camera angles. **Identity and detail preservation are goals, not guarantees.**

### Features

- Photo-based pose editing with preview, download, history and regeneration.
- Separate photos for person A and person B in ordinary couple poses, with role descriptions and swapping. One person is reused only when explicitly selected.
- A searchable library of 288 poses and 1,439 views, organized by the upstream categories, with angles and favorites. Browsing access does not mean every reference is available for generation.
- Free local generation with hardware detection, an isolated runtime, verified downloads and a real generation self-test.
- Optional image APIs and already running local inference servers, including a separate text-to-image mode.
- Chinese and English interfaces, rounded controls and restrained frosted surfaces.
- Resumable downloads, retries, measurable transfer speed and remaining-download estimates.

### Install and start

1. When installer assets are published on [Releases](https://github.com/nihaomaaa/Pose/releases), download **Pose-Setup-0.3.0-x64.exe** and install it. Use the corresponding filename for a different version.
2. Launch **Pose**, read the first-run terms and select your language.
3. Choose a generation method:
   - **Local:** choose Automatic, confirm storage and start setup. Pose prepares the runtime, model and gallery, verifies files and runs a generation self-test.
   - **API:** open Settings → API connections, configure your provider, model, endpoint and key, acknowledge data transmission and billing, then save. This prepares the gallery without local model weights or Python.
4. Upload a clear photo and choose a pose. Couple poses require separate A/B photos; follow the role descriptions and swap them if necessary.
5. Generate, inspect the result, download it or try another pose.

Ordinary users do not need commands, a separate Python installation or CUDA Toolkit. A working NVIDIA driver is still required for GPU mode. Initial downloads are large; local generation works offline after setup.

The current installer is unsigned, so Windows may show an unknown publisher. Use the project's release channel and verify the accompanying SHA-256 checksums. Do not disable system security protections.

### Hardware and models

Only **Windows 10/11 x64** is packaged. There are no macOS, Linux or Windows ARM64 installers. Being able to open the interface does not establish local-generation compatibility.

| Mode | Hardware guidance | Free disk |
| --- | --- | --- |
| 4B GPU | NVIDIA CUDA architecture 7.0+, at least 6 GiB VRAM and 24 GiB RAM; usually NF4 | At least 45 GB |
| 4B full precision | At least 24 GiB VRAM and 48 GiB RAM | At least 45 GB |
| 4B CPU | At least 48 GiB RAM; potentially very slow | At least 55 GB |
| 9B GPU | Recommended at least 8 GB VRAM and 32 GB RAM | At least 65 GB |
| 9B CPU | At least 64 GiB RAM; potentially very slow | At least 65 GB |
| API | Does not require local-model VRAM; needs a working service and gallery storage | No local model weights |

Actual compatibility depends on drivers, available memory and the generation self-test. **AMD and Intel GPU acceleration are not implemented.** API mode is an option when local requirements are not met.

| Preference | Behavior |
| --- | --- |
| Automatic | FLUX.2 klein 4B; NF4 or full precision according to hardware. The 4B model is ungated and licensed under Apache 2.0. |
| Smaller footprint | The smaller 4B family, favoring lower VRAM use. It still downloads roughly 17 GB of weights: runtime NF4 quantization does not shrink the original download. |
| Quality first | FLUX.2 klein 9B, roughly 35 GB of weights. Each user must accept the official noncommercial model license on Hugging Face and supply an authorized read token. Better results are not guaranteed for every image. |
| Custom model | A compatible, distilled Flux2KleinPipeline repository in Diffusers format on Hugging Face, checked before downloading. |

Arbitrary single-file checkpoints, LoRAs, GGUF files, base/non-distilled variants and executable Python plugins are unsupported. Pose validates metadata, pins revisions and verifies files without executing remote repository Python code. Format compatibility does not guarantee memory fit or quality.

**Validation:** 50 automated tests passed. Real 4B two-person generation completed on an RTX 4060 8 GB / 32 GB RAM machine in approximately 65 seconds in one test. This is not a performance guarantee. 9B, CPU and other hardware profiles have not all been tested on real machines.

### Downloads and storage

Automatic/mainland-first sources prefer HF Mirror, jsDelivr and Tsinghua PyPI, with official fallbacks. Official-only sources are also available. Python and PyTorch/CUDA still require their official distributions; network availability is not guaranteed. Windows system HTTP proxy settings are supported.

Gated-model tokens go only to the official Hugging Face domain, never a mirror. Each user must obtain their own model access. Downloads support resume, retries, length checks and SHA-256 / Git blob verification. Speed and ETA cover measurable transfers; installation, verification and first generation may not have reliable estimates.

Data normally lives under **PoseAtelier** in Windows local application data. Open the folder from settings or choose another location during initial setup. Changing the location does not migrate old data. Models, uploads, results and runtime files consume disk space; Pose does not silently remove installed models.

### APIs and workflows

Bring your own service account, endpoint, model permissions and credits. **Local generation needs no API. Cloud services may charge separately; a ChatGPT Plus subscription cannot serve as this app's image API authorization.**

| Service or project | Current Pose 0.3.0 adapter |
| --- | --- |
| Volcengine Ark / Doubao Seedream | Multi-reference editing |
| Alibaba Wan and Qwen-Image | Multi-reference editing |
| Tencent Hunyuan | Multi-reference editing through the international TokenHub preset |
| OpenAI GPT Image / DALL·E-family service entry | Multi-reference editing using the GPT Image preset; legacy model availability is not guaranteed |
| Google Gemini / Nano Banana | Multi-reference editing |
| FLUX / Black Forest Labs, Ideogram, fal.ai, Replicate | Multi-reference editing for the selected compatible model |
| CogView, Baidu Qianfan, Stability AI, Google Imagen | Text-to-image only in current adapters |
| Recraft, SiliconFlow, ModelsLab, Hugging Face Inference Endpoints | Text-to-image only; HF requires a compatible dedicated endpoint |
| Automatic1111 and Xinference | Text-to-image only, through an already running compatible server |
| ComfyUI | Import a trusted API workflow and map subject A, subject B, pose and prompt inputs |
| Custom OpenAI-compatible endpoint | Must implement the adapter's image-editing contract; chat compatibility alone is insufficient |
| DeepSeek's official API, OneDiff, Text-Generation-Inference | Not integrated as standalone image-generation endpoints; capability limits are explained in the app |

A provider preset does not support every model, region or protocol that company offers. OneDiff may accelerate a separately deployed server, such as ComfyUI; Pose does not deploy these external servers or their models.

Choose Settings → API connections, enter the provider-specific endpoint, model and key, acknowledge transmission and billing, then save. Couple editing requires support for three distinct references: A, B and the pose. Text mode sends no subject photos and does not promise identity preservation.

ComfyUI requires an existing multi-reference API-format workflow. Pose maps inputs and automates later uploads; it cannot turn a text-only workflow into an identity/pose editor or silently install custom nodes.

The connection check tests reachability without paid generation. It does not verify credentials, balance or model access. Adapters have mocked contract tests; **live paid generation has not been verified with every provider.** Moderation, credits, regional limits or account permissions can cause rejection. Stopping locally may not stop remote computation or billing. Pose does not bypass filters or silently switch providers after failure.

### Privacy and data

| Activity | Data handling |
| --- | --- |
| Local generation | Photos, prompts and generation are processed by the local engine, without upload to a cloud image provider. |
| Setup and downloads | Runtime, model, gallery and mirror servers receive normal network information such as IP addresses and requested paths. |
| Cloud image editing | After acknowledgment, prompts and required subject/pose references go to your chosen endpoint. Results may download from its CDN. |
| Text-to-image | Sends prompts and generation parameters, without subject photos. |

- No built-in advertising, analytics or telemetry.
- Uploads, results, job information, logs, models and runtimes remain locally until you remove them; there is no automatic retention expiry.
- API and Hugging Face keys are encrypted with Windows user protection and briefly exist in memory during requests. This cannot protect against malware controlling the current Windows account.
- Changing a saved endpoint requires re-entering or clearing its key. Credentials are not forwarded to result-image download URLs.
- Photos can contain EXIF or other metadata. Remove information you do not want transmitted and review your provider's retention, training, international-transfer and deletion policies before cloud use.
- Updates and uninstalling preserve data by default. Deleting a result does not delete the original upload or a provider's copies. Back up important work.
- Never attach keys, private photos, full data directories or unreviewed logs to public issues.

### Usage declarations and license

**Noncommercial use.** Original Pose code is licensed under **PolyForm Noncommercial 1.0.0** for permitted noncommercial learning, research and sharing. Do not sell the software or access to it, operate paid generation services with it, or use the project for commercial profit. The complete project LICENSE governs; this summary does not replace it. This is a **source-available** project, not software under an OSI-approved open-source license.

**Third-party rights.** Dependencies, models and gallery assets retain their separate terms. Pose's code license does not expand third-party rights. The 4B model's own Apache 2.0 license does not override Pose's noncommercial terms; 9B remains subject to its official model license.

**Images and consent.** Use photos you have permission to process, including the necessary consent of depicted people. Respect copyright, likeness, privacy, reputation and other protected interests. Nonconsensual intimate imagery, sexual content involving minors, fraud, impersonation, defamation and other unlawful uses are prohibited.

**Generation boundaries.** All library views can be browsed. Only verified ordinary couple poses support photo-based generation. Explicit sexual references are browse-only and cannot be used for subject-photo generation. No restriction removal or provider-filter bypass is offered.

**Results and disclosure.** AI can change identity, clothing, body shape, hands, anatomy and other details. Inspect every result. Do not present generated images as evidence of real events. Disclose AI generation under applicable law and platform rules; do not maliciously remove, falsify or hide provider watermarks or provenance labels.

**Responsibility and applicable law.** The software is provided as available, without guarantees of a particular outcome, error-free operation or continued availability, to the extent permitted by law. Nothing excludes liability that cannot lawfully be excluded or limits statutory rights. A learning-only notice does not excuse infringement. This documentation is not legal advice or a guarantee of compliance. Interface language does not determine jurisdiction; relevant requirements depend on users, depicted people and distribution locations.

Chinese terms include mainland Chinese references. English terms use region-labeled New York, US likeness/privacy and EU AI transparency/data-protection references. These are regional examples, not universal rules for every country.

### FAQ

**Do I need ChatGPT Plus or a paid API?**  
No. Compatible hardware can use free local generation. Optional APIs use your own accounts and provider pricing; no credits are bundled.

**Why does the smaller option still download many gigabytes?**  
4B is smaller than 9B, while NF4 mainly saves runtime VRAM. This version does not supply a smaller prequantized weight package.

**Is setup stuck when speed is zero?**  
It may be unpacking, installing dependencies, verifying files or running the first generation. Check the current stage. Failed transfers can be resumed or retried through another source; network availability varies.

**What if I have no NVIDIA GPU?**  
Use the slower CPU mode if sufficient RAM is available, or connect your own API. AMD and Intel GPU acceleration are not supported.

**Why does 9B require Hugging Face authorization?**  
The official repository has access and license requirements. Each user must authorize access; the application does not share the maintainer's token or accept model terms on a user's behalf.

**Why is identity or posture imperfect?**  
Generation is not a deterministic identity or posture copy. Use clear, unobstructed photos, check A/B mapping and try another seed or pose. A larger model still cannot guarantee an exact match.

**Does uninstalling erase every photo?**  
No. Outputs and source uploads are separate; uninstalling preserves data by default. Quit the app, back up what you need and manage the data folder yourself.

### Development and support

Ordinary users can skip this section. Developers need Windows x64 and Node.js 24. Run the following from the directory containing package.json:

~~~bash
npm ci
npm test
npm start
# Build the Windows installer
npm run build
~~~

Build output goes to dist/. Preparation downloads a pinned, SHA-256-verified uv build; icons are generated from the project SVG. POSE_DESKTOP_DATA and POSE_CONFIG_DIR select isolated test directories; POSE_SHOW_SETUP=1 forces setup to appear. Do not commit personal model caches, photos, keys, proxy settings or private paths.

Use [GitHub Issues](https://github.com/nihaomaaa/Pose/issues) for bugs, including version, Windows/GPU/RAM, model or service, reproduction steps and sanitized errors. For credential leaks or vulnerabilities, avoid public sensitive details and use private reporting where the repository makes it available.

About Pose links to the project and its Star button. Opening GitHub shows thanks; starring on the website remains the user's choice. Optional automatic starring requires one-time user authorization, reports success only after GitHub confirms it and does not save that token.

### Acknowledgments

**Based on and supported by [anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh).** Original artwork: ギア. Chinese localization: Anhao.

The upstream code and artwork/data have different licensing scopes. Artwork and pose data retain their original rights and noncommercial restrictions; an MIT license on upstream code does not grant unrestricted commercial rights to those assets. The EXE and source repository do not bundle model weights or gallery images; setup retrieves and verifies pinned files.

Thanks to Black Forest Labs, Hugging Face, Electron/Chromium/Node.js, Astral uv, PyTorch and contributors to the underlying tools and models. Each component retains its own license. Apple-inspired interface styling does not imply affiliation or endorsement by Apple, and the project is not affiliated with or endorsed by the listed cloud providers.
