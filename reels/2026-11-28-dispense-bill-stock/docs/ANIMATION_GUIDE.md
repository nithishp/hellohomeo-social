# Animation guide
- Canvas 1080×1920, 30 fps; deterministic `window.seek(t)` in comp/index.html; overlay rendered transparent and composited over ink + Higgsfield clips in ffmpeg.
- Tokens: --ink #070C1F, --jade #10B880, --jd #06805A, --jod #5FD6AC, --tint #E8F8F1, --txt #0B1220, amber #D97706.
- Easing set: quint-out (glides, 0.5 s), back-out 1.4 (alert pop), cubic-in (exits), linear for counters through quint.
- Durations: entrances 0.5 s, staggers 0.1–0.25 s, exits 0.3–0.35 s on a beat; state swaps are hard cuts on ticks.
- Components: Prescription card (#rx, shared hook/P1/loop = match cut), stat tiles (.st, .warn), alert + batch rows, invoice card with payment chips, CTA stack.
- Safe zones: nothing essential above y=250 or below y=1580 (Reels UI); headlines at top 250; cards 560–1500; side margins 72.
