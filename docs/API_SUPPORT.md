# 图片 API 能力与验证范围 / Image API capabilities

Reviewed 2026-10-29. Presets are editable because provider model access and naming can change.

**验证范围：** 所有适配按官方协议实现并有模拟协议测试。没有各家的真实付费密钥，尚未逐家执行收费出图。连接检测使用 HEAD，不触发生图，也不验证计费与权限。

**Validation:** adapters have mocked contract tests, not live paid-provider certification. Reachability is not successful authentication or generation. A provider can change or retire a model independently of Pose.

| 服务 / Provider | 当前适配 / Capability | 默认模型 / Preset | 来源 / Source |
| --- | --- | --- | --- |
| Seedream · 豆包 / 火山方舟 | 多图编辑 / Multi-reference | doubao-seedream-4-5-251128 | [官方说明 / Docs](https://docs.volcengine.com/docs/ark/image-generation-api) |
| 通义万相 · Wan | 多图编辑 / Multi-reference | wan2.6-image | [官方说明 / Docs](https://help.aliyun.com/zh/model-studio/wan-image-generation-api-reference) |
| Qwen-Image · 千问 | 多图编辑 / Multi-reference | qwen-image-2.0-pro | [官方说明 / Docs](https://help.aliyun.com/zh/model-studio/qwen-image-edit-api) |
| 腾讯混元 · Hunyuan | 多图编辑 / Multi-reference | hy-image-v3 | [官方说明 / Docs](https://intl.cloud.tencent.com/zh/document/product/1300/83708) |
| CogView · 智谱 | 仅文字 / Text only | cogview-4-250304 | [官方说明 / Docs](https://docs.bigmodel.cn/api-reference/模型-api/图像生成) |
| 文心一格 / 千帆 · Baidu | 仅文字 / Text only | ernie-image-turbo | [官方说明 / Docs](https://cloud.baidu.com/doc/qianfan-api/s/Imo9g5a6a) |
| DeepSeek | 不可直接接入 / Not an image endpoint | User supplied | [官方说明 / Docs](https://api-docs.deepseek.com/guides/vision/) |
| OpenAI · GPT Image / DALL·E | 多图编辑 / Multi-reference | gpt-image-2.5-sunburst | [官方说明 / Docs](https://developers.openai.com/api/reference/resources/images/methods/edit) |
| Stability AI | 仅文字 / Text only | core | [官方说明 / Docs](https://platform.stability.ai/docs/api-reference) |
| FLUX · Black Forest Labs | 多图编辑 / Multi-reference | flux-2-klein-9b | [官方说明 / Docs](https://docs.bfl.ml/quick_start/generating_images) |
| Google Gemini · Nano Banana | 多图编辑 / Multi-reference | gemini-3.1-flash-image | [官方说明 / Docs](https://ai.google.dev/gemini-api/docs/image-generation) |
| Google Imagen | 仅文字 / Text only | imagen-4.0-generate-001 | [官方说明 / Docs](https://ai.google.dev/gemini-api/docs/imagen) |
| Recraft | 仅文字 / Text only | recraftv3 | [官方说明 / Docs](https://external.api.recraft.ai/doc/ui/) |
| Ideogram | 多图编辑 / Multi-reference | ideogram-4-5 | [官方说明 / Docs](https://developer.ideogram.ai/api-reference/images/precise-edit/ideogram-4-5) |
| fal.ai | 多图编辑 / Multi-reference | fal-ai/flux-2/klein/9b/edit | [官方说明 / Docs](https://fal.ai/models/fal-ai/flux-2/klein/9b/edit/api) |
| Replicate | 多图编辑 / Multi-reference | black-forest-labs/flux-2-klein-9b | [官方说明 / Docs](https://replicate.com/black-forest-labs/flux-2-klein-9b/api) |
| SiliconFlow · 硅基流动 | 仅文字 / Text only | Qwen/Qwen-Image | [官方说明 / Docs](https://docs.siliconflow.cn/docs/userguide/capabilities/images) |
| ModelsLab | 仅文字 / Text only | flux | [官方说明 / Docs](https://docs.modelslab.com/image-generation/community-models/dreambooth-text-to-image) |
| Hugging Face Inference Endpoints | 仅文字 / Text only | User supplied | [官方说明 / Docs](https://huggingface.co/docs/inference-endpoints/guides/test_endpoint) |
| ComfyUI | 用户工作流 / Workflow | User supplied | [官方说明 / Docs](https://docs.comfy.org/development/comfyui-server/comms_routes) |
| Automatic1111 | 仅文字 / Text only | User supplied | [官方说明 / Docs](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) |
| Xinference | 仅文字 / Text only | User supplied | [官方说明 / Docs](https://inference.readthedocs.io/en/latest/models/image/index.html) |
| OneDiff | 不可直接接入 / Not an image endpoint | User supplied | [官方说明 / Docs](https://github.com/siliconflow/onediff) |
| Text-Generation-Inference | 不可直接接入 / Not an image endpoint | User supplied | [官方说明 / Docs](https://huggingface.co/docs/text-generation-inference/index) |
| OpenAI-compatible · 自定义兼容接口 | 多图编辑 / Multi-reference | User supplied | [官方说明 / Docs](https://developers.openai.com/api/reference/resources/images/methods/edit) |

## 实际协议 / Protocol details

- Seedream: images/generations with an ordered image array. A, B and pose stay distinct; provider watermark is retained.
- Qwen / Wan: DashScope multimodal-generation content entries contain image references followed by text. The preset does not implement arbitrary asynchronous Wan video APIs.
- Hunyuan: the international TokenHub hy-image-v3 generation endpoint and images array. Tencent’s Chinese-region signed TC3 API and v3.5 chat/SSE protocol are different and are not interchangeable with this preset.
- GPT Image / custom OpenAI-compatible: JSON images/edits with images[{image_url}]. Custom servers must implement that exact edit contract; merely supporting chat/completions is insufficient. DALL·E is retired; older GPT Image presets may also be unavailable.
- Gemini / Nano Banana: generateContent with inlineData references and image response parts. Imagen is a separate text-to-image predict endpoint.
- BFL: input_image, input_image_2 and input_image_3, followed by the returned polling URL.
- Ideogram 4.5: precise-edit multipart image plus reference_images; text generation uses the model-specific generation path.
- fal.ai: a queued edit model with image_urls; status and result endpoints are polled. Replicate: a model prediction with input_images. These presets depend on the selected model’s schema, not any arbitrary model hosted by those companies.
- CogView, Baidu ERNIE Image, Recraft, SiliconFlow and Xinference: their documented text-generation image endpoints. Pose’s current adapters do not offer multi-person photo editing for these presets.
- Stability: Stable Image Core multipart text generation, with binary output.
- ModelsLab: community-model text2img followed by images/fetch when processing. Moderation remains enabled.
- Hugging Face: a dedicated text-to-image endpoint that accepts inputs/parameters and returns image bytes. Custom handlers using different request/output formats need their own adapter.
- Automatic1111: an already running server started with API support; sdapi/v1/txt2img and base64 output. This version does not configure ControlNet/IP-Adapter automatically.
- ComfyUI: image upload, prompt submission, history polling and output view. Import a trusted API workflow and map inputs in the UI. See [workflow guide](MODELS_AND_WORKFLOWS.md).
- Xinference: an already deployed image model UID, using its image-generation endpoint. Pose does not deploy the server or download its models.
- OneDiff is an acceleration library: connect the accelerated ComfyUI server instead. TGI serves language-model text; it is not an image synthesis endpoint. DeepSeek’s official vision interface describes image understanding, not public image output; Janus research weights are not a compatible hosted DeepSeek image API.

## 内容、费用与数据 / Content, charges and data

服务商可能因安全审核、额度、地区或账号权限拒绝请求。软件会提前提示并显示失败原因，不绕过审核，不轮换账号重试，不切换到未授权服务。请求超时或取消不保证云端计算和计费停止。

Photos and prompts leave the computer only for your selected API, after cloud consent. Two-person edits send A, B and pose in that order. Text-to-image mode sends no subject photos. Results are downloaded from the provider or its CDN and saved locally; credentials are not forwarded to result-image URLs.

Remote custom endpoints require HTTPS. Plain HTTP is limited to loopback addresses. API keys are encrypted in Windows storage and excluded from task files and renderer configuration. No cloud key, credit or subscription is bundled with Pose.
