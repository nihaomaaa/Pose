# 隐私说明 / Privacy

Pose 0.3.0 · 2026-10-29

## 本机数据 / Local data

本地模式的照片、提示词与结果仅由本机引擎处理。上传照片、生成作品、任务元数据、日志、模型与 Python 环境保存在所选数据目录，默认是 Windows LOCALAPPDATA 下的 PoseAtelier。应用偏好与加密凭据在 Electron 的 Windows 用户数据目录；开发测试可以另行指定隔离目录。

Local mode processes photos and prompts on this computer. The chosen data folder contains uploads, outputs, job metadata, logs, models and the Python environment. Preferences and encrypted credentials use Electron’s per-user Windows data directory. No analytics or advertising service is built in.

## 网络请求 / Network requests

安装需要连接 Astral、PyTorch、PyPI、Hugging Face、GitHub 及所选镜像。它们会接收正常网络请求信息，如 IP、所请求文件路径；下载来源选择不会把照片上传到镜像。受限模型的 Hugging Face 下载令牌只发给官方域名。

Cloud generation sends the prompt and required images to your chosen API endpoint. Returned image URLs may be hosted on the provider’s CDN. Text-only mode sends no subject photos. Input files may contain EXIF or other metadata; remove sensitive metadata before choosing a cloud provider. Provider retention, training, international transfers and deletion are governed by its own terms. Read them before consenting.

云端服务费用由用户自行承担。应用不会在失败后悄悄把照片切换到另一家服务。停止本地等待不保证云端任务、照片留存或计费一同停止。

## 凭据 / Credentials

API 与 Hugging Face 密钥通过 Electron safeStorage 调用 Windows 用户保护机制加密；不会返回给网页渲染层或写入任务元数据。密钥仍需在调用服务时短暂存在内存中。此保护无法抵御已控制当前 Windows 用户账户的恶意程序。

Changing an API endpoint requires re-entering or clearing the saved key. GitHub starring tokens are used for the requested star once and are not stored. Opening GitHub does not submit a star automatically without authorization.

## 保存、备份与删除 / Retention

卸载保留作品与模型；没有自动到期删除。删除一件作品会移除该作品与任务文件，但不会同时删除上传的原图，也不会请求服务商删除其副本。可从“查看数据文件夹”进入目录，在退出应用并备份所需内容后自行处理。更改存储位置不会迁移旧目录。

Keep backups of important work. Never attach credentials, private photos or complete data folders to a public GitHub issue. Review logs for private information before sharing. Report security issues through the repository’s private security-reporting facility when available; do not publish secrets.

## 联系 / Contact

Project: https://github.com/nihaomaaa/Pose

本说明不替代适用的数据保护法律，也不承诺任何服务商的处理行为。 / This notice does not replace applicable data-protection law or guarantee a provider’s conduct.
