# 自定义模型与工作流 / Custom models and workflows

## 本地模型链接 / Local model links

在设置中选择“自定义”，粘贴 Hugging Face 仓库链接，再点击检查。支持链接形如 https://huggingface.co/black-forest-labs/FLUX.2-klein-4B 或带 /tree/版本 的仓库链接。

The local engine supports **distilled Flux2KleinPipeline repositories in Diffusers layout**. The downloader checks model_index.json, pins the repository revision, allows only model/config/tokenizer assets, and verifies file hashes. It does not run a downloaded repository’s Python code or use trust_remote_code. Incompatible architecture, standalone safetensors, GGUF, LoRA and base/non-distilled variants are rejected. A compatible class name still does not guarantee that arbitrary custom weights fit your memory or produce good results.

9B uses the pinned official BFL repository. The user must accept its noncommercial license on Hugging Face and provide a read token. Authorized metadata is fetched before downloading, because the public unauthenticated file list hides gated weight hashes. No token is sent to a mirror. Your token and license acceptance do not travel with the public EXE.

“节省空间”选择 4B 家族，NF4 是加载时的显存量化，不会把已下载的原始权重文件变小。要省磁盘，不必同时安装 4B 和 9B；应用不会擅自删除已有模型。

## ComfyUI 图形化配置 / Visual ComfyUI mapping

ComfyUI is for users who already operate a compatible server and multi-reference workflow. Pose does not silently install ComfyUI, custom nodes or extra model families.

1. 在 ComfyUI 中准备已经能够处理人物与姿势参考的工作流，导出 API 格式 JSON。普通画布格式不是 API 工作流。
2. 在 Pose 的 API 连接页选择 ComfyUI，填服务地址。本机默认 http://127.0.0.1:8188；远程服务需 HTTPS。
3. 导入可信工作流文件。用下拉菜单选择人物 A、人物 B、姿势参考对应的图片输入节点，以及正向提示词节点。双人生成要有三个独立图片输入。
4. 保存，进入创作台。此后每次上传、选姿势和生成都由 Pose 自动送入相应节点，无需手动复制提示词或参考图。

The mapping UI replaces image/text inputs with placeholders and supplies the job seed. It cannot turn a text-only workflow into a pose/identity editing workflow. Pose detects string image inputs and text/prompt inputs; specialized custom nodes with other input names need a workflow prepared by its author.

Advanced workflow authors can use these exact string values in API node inputs: {{PERSON_A}}, {{PERSON_B}}, {{POSE}}, {{PROMPT}}, {{SEED}}. All required photo bindings are checked before submitting a pose job. Text-to-image workflows need the prompt binding; image-editing workflows should not be used in text-only mode.

Do not import untrusted workflows. They execute through the server and its installed nodes under that server’s permissions. OneDiff can accelerate a separately configured ComfyUI server; Pose talks to the ComfyUI protocol, not an invented OneDiff REST endpoint.
