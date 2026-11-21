# 2026-W47 Reel — Book once. Reminders go out. (follow-ups & reminders)
30 s, 1080×1920, 30 fps. Theme: schedule the follow-up from the consultation; WhatsApp reminders 24 h and 1 h before; patients reschedule on WhatsApp.
- comp/index.html: deterministic composition (`seek(t)`); comp/render.js renders transparent overlay frames (serve comp/ on :8765, `node render.js range ../out/frames 0 30 30`).
- tools/compose.sh: ink base + Higgsfield clip A (src 0.1→ reel 2.25–7.0) and clip B (src 0.9→ reel 21.625–25.0), upscaled 720p→1080p, overlay frames, mix.
- Audio: VO take 1 (eleven_v4, Amit) split into 9 phrases on the beat grid (tools/mix.py); local music (tools/music.py, 106.7 BPM, lift 7.0, resolve 25.0); local SFX (tools/sfx.py); sidechain duck; loudnorm −14 LUFS.
- Footage: captured live 2026-11-21 (demo-clinic doctor; follow-up POST stubbed, no booking written; names/phones pseudonymised from the doctor appointments roster). UI rebuilt in HTML from those captures; WhatsApp messages use the exact template text in lib/whatsapp/templates.js.
