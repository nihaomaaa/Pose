# 安全 / Security

Pose is a single-user desktop application. Do not expose its loopback HTTP server to a LAN or the internet.

Electron renderers use sandbox and contextIsolation without Node integration. IPC validates the main window and its allowed page. HTTP writes require the correct Host, Origin and session token. Remote API endpoints require HTTPS. Model/runtime downloads use fixed hashes; downloaded Python plugins and unsafe pickle weights are not enabled.

本地生成不上传照片。可选云端模式会向明确配置的服务传输必要输入；请参考 docs/PRIVACY.md。API 密钥使用 Windows 用户安全存储加密，更改地址时不会默默复用旧密钥。服务商返回的图片链接不会收到 API 密钥。

No security measure protects against malicious software that already controls your Windows user account. Custom endpoints and ComfyUI workflows must be trusted. Do not expose arbitrary workflow execution to untrusted parties.

Please remove photos, names, credentials and private paths from reports. Use GitHub private vulnerability reporting if enabled. If it is unavailable, open an issue containing only a request for a private reporting channel, without exploit details or personal data.
