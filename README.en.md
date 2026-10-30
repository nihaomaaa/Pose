# Pose

[简体中文](README.md) · [Download for Windows](https://github.com/nihaomaaa/Pose/releases/latest) · [API support](docs/API_SUPPORT.md)

A desktop studio for AI pose editing. Upload a person, browse 1,439 pose views, and generate, preview and download in one place. Ordinary couple poses require a separate reference photo for each person.

Local generation is free and needs no ChatGPT subscription or API key. Optional cloud providers use your own API account and may charge separately. ChatGPT Plus does not include image API access for this app.

## Start creating

1. Download **Pose-Setup-0.3.0-x64.exe** from Releases and install it on Windows 10/11 x64.
2. Open Pose, read the terms, and choose English or Chinese in the upper-right corner.
3. Choose Automatic and start setup. Pose detects hardware, installs its own runtime, downloads and verifies assets, and runs a real image-generation check.
4. Upload a photo, choose a pose and generate. Couple references require different photos for A and B unless you explicitly enable the same person in both roles.
5. Preview, download or revisit your locally saved work. Local generation works offline after setup.

No command line, Python experience or CUDA Toolkit is needed. You still need a working GPU driver. The installer is unsigned; Windows may show an unknown publisher. Use this repository’s Releases and verify SHA-256. Do not disable Windows security protections.

## Models and hardware

| Preference | Behavior |
| --- | --- |
| Automatic | FLUX.2 klein 4B, NF4 or full precision according to hardware; ungated, Apache 2.0 |
| Save space | Uses the smaller 4B family and prefers NF4 for VRAM; still downloads the same roughly 17 GB of weights |
| Higher quality | FLUX.2 klein 9B, roughly 35 GB of weights; requires accepting BFL’s noncommercial license and an HF read token; quality gains are not guaranteed for every image |
| Custom | A compatible, distilled Flux2KleinPipeline Diffusers repository on Hugging Face; not an arbitrary checkpoint, LoRA, GGUF or executable plugin |
| API | Downloads the gallery, without local model weights or Python; performance and charges depend on the provider |

Default GPU mode requires NVIDIA CUDA architecture 7.0+, at least 6 GiB VRAM, 24 GiB RAM and 45 GB free disk. Full precision is selected with at least 24 GiB VRAM and 48 GiB RAM. CPU fallback requires 48 GiB RAM and 55 GB free disk and can be very slow. AMD and Intel GPU acceleration are not implemented.

9B targets at least 8 GB VRAM, 32 GB RAM and 65 GB free disk; CPU needs 64 GiB RAM. These thresholds are guidance, not universal compatibility guarantees. The setup self-test is the final check. 4B two-person generation was tested on an RTX 4060 8 GB / 32 GB RAM system. 9B, CPU and other hardware profiles have not all been tested on real devices.

## Downloads

Pause/resume, retries, size checks and cryptographic verification are built in. Actual speed and remaining download time are shown when measurable. Dependency installation, verification and the first generation do not show invented speed or ETA.

Automatic/mainland-first downloads prefer HF Mirror, jsDelivr and Tsinghua PyPI, with official fallbacks. Gated model credentials only go to the official Hugging Face host. Python and PyTorch/CUDA still use official distributions; availability depends on your network. Windows HTTP proxy settings are supported. You can choose official-only downloads.

Choose another data folder before opening the workbench. Changing the location does not move existing data.

## Your own APIs

Choose Settings → API connections, select a provider, enter its model, base endpoint and key, then acknowledge transmission and billing. Pose handles reference uploads and result retrieval. See the [capability matrix](docs/API_SUPPORT.md) for multi-reference editing, text-only endpoints, and local workflows.

DeepSeek’s public API, OneDiff and TGI are not standalone image-generation endpoints for this application; Pose explains this instead of presenting nonfunctional adapters. Retired DALL·E models are replaced by the GPT Image preset. Text-only adapters use a separate mode and do not send subject photos or promise identity preservation.

Keys are encrypted with Windows user protection. Changing the endpoint requires re-entering or clearing the old key. The connection check only tests reachability, not credentials, credits or model access. Adapters have offline contract tests; live paid generation has not been verified for every provider. Moderation can reject requests. Stopping locally may not cancel remote processing or billing. No filter bypass or silent provider switching is implemented.

## Privacy and licensing

Local generation keeps photos on your computer. Cloud generation sends necessary inputs to your explicitly configured service after confirmation. There are no built-in ads, analytics or telemetry. Models, photos, results and runtime files normally live in the Windows local application-data folder under PoseAtelier. Updating/uninstalling preserves data; removing a result does not delete its source photo.

Original Pose code is **source-available under [PolyForm Noncommercial 1.0.0](LICENSE)**. Commercial use is prohibited by the license. This is not an OSI open-source license. Dependencies retain their own terms.

The gallery is based on [anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh), with artwork by ギア and Chinese localization by Anhao. Artwork and pose data retain the original rights and noncommercial restrictions. Neither model weights nor gallery artwork are bundled in the EXE/source repository; setup retrieves pinned upstream files.

All gallery views remain browsable. Verified ordinary couple poses support photo editing; explicit sexual references are browse-only. Use photos you have permission to process. AI can alter identity, anatomy and clothing. Disclose AI generation when sharing and preserve provider provenance/watermarks.

[Terms](docs/TERMS.en.md) · [Privacy](docs/PRIVACY.md) · [Third-party notices](THIRD_PARTY_NOTICES.md)

English legal references identify New York, US and EU jurisdictions. Interface language does not determine which law applies. A learning-only notice does not excuse infringement.

## Support and development

About Pose links to this repository and the upstream gallery. Opening GitHub shows a frosted thank-you toast. Optional automatic starring needs your explicit, one-time GitHub Starring authorization; the token is not saved and success is shown only after GitHub confirms it.

Developers need Windows x64 and Node.js 24:

    npm ci
    npm test
    npm run build

The prepare script obtains a pinned, SHA-256-verified uv build from Astral. Icons are built from the project SVG. Output is written to dist/. Use npm start for development. Release automation builds a Windows installer and checksums from a version tag or a manual workflow run.

Use POSE_DESKTOP_DATA and POSE_CONFIG_DIR for isolated tests, and POSE_SHOW_SETUP=1 to show setup. No personal paths, proxy configuration, photos, keys or model caches are included in releases.

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Custom models and ComfyUI](docs/MODELS_AND_WORKFLOWS.md)
