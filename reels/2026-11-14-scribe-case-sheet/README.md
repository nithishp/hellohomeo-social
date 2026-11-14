# 2026-W46 Reel — The case sheet writes itself (Scribe AI)
30 s, 1080×1920, 30 fps. Theme: Scribe AI turns a Hindi consultation into an English case sheet with live repertorisation (the "Vita autofilling a case sheet" family).
- comp/index.html: the composition (deterministic `seek(t)`); comp/render.js renders transparent PNG overlay frames (serve comp/ on :8765, `node render.js range frames 0 30 30`).
- Base layer: ink + Higgsfield clips A (src 0.3–3.9 → reel 2.0–5.6) and B2 (src 1.9–4.8 → reel 20.3–23.2), upscaled 720p→1080p.
- Audio: VO take 1 split into 11 phrases at 1.08× (tools/vo.py), music1 (src 3.4→, intro looped under the tail), local SFX; sidechain duck; loudnorm −14 LUFS.
- Outputs: out/final.mp4, out/loop_check.mp4, out/poster.png, out/contact.png, out/captions.srt.
- Footage: captured live 2026-11-14 (demo-clinic doctor, Scribe built-in demo replay; no patient data); UI rebuilt in HTML from those captures and lib/vita-demo-script.js.
