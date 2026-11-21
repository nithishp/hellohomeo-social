# Animation guide
- Canvas 1080×1920 @30 fps; transparent overlay PNG frames over ffmpeg base (ink or clip).
- Safe zones: all text between y 250 and y 1580; captions at y 1430; nothing in top 250 / bottom 340.
- Side margins 72 px; cards 936 px wide.
- Tokens: see style_guide.md (CSS vars --ink --jade --jd --jod --tint --txt --muted).
- Easing set: quint-out (enter), back-out 1.4 (pops, chips), cubic-in (exit), cubicIO (morphs).
- Durations: enter 0.5–0.6 s; exit 0.25–0.35 s; stagger 0.15–0.2 s; typing 14–18 chars/s.
- Components: .card (white UI card), .head (2-line headline, 2nd line jade), .kin (kinetic over footage), .bub (chat bubble), .chip (reminder chip), #cap (captions, rgba ink pill).
- Deterministic: window.seek(t) renders any time; no CSS animations or timers.
