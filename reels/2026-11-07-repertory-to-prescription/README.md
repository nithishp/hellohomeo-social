# 2026-W45 Reel — Repertory to rubrics to prescription
30 s, 1080×1920, 30 fps. Theme: repertory → rubrics → prescription.
- comp/index.html: the composition (deterministic `seek(t)`), comp/render.js renders the PNG overlay frames (served from comp/ over http).
- Base layer: ink colour + Higgsfield clips (A 2.00–7.00, B 21.42–24.31); overlay frames composited with ffmpeg (see commands in docs/README notes below).
- Audio: VO take1 (+2.0 s), music m4 (head trim 2.25 s, ducked), SFX; loudnorm −14 LUFS / −1.5 dBTP.
- Outputs: out/final.mp4, out/loop_check.mp4, out/poster.png, out/contact.png, out/captions.srt.
- Footage: captured live 2026-11-04 from the demo clinic (doctor login), pseudonymised; UI beats rebuilt as HTML from those captures.
