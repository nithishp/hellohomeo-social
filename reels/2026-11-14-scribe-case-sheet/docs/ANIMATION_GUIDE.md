# Animation guide
## Tokens
--ink #070C1F · --jade #10B880 · --jd #06805A · --jod #5FD6AC · --tint #E8F8F1 · --line #CDEFE0 · --muted #6A7385 · --txt #0B1220
Radius: card 32, field 20, chip 12, pill 999. Shadow: raised (design.md).
## Easing set
- glide: easeOutQuint — cards/heads entering, 450–600 ms, 120–140 px travel, scale .98→1
- snap: easeOutBack(1.4) — chips, "Sent" button, 300–350 ms
- settle: easeInOutCubic — remedy board re-rank, 1.6 s
- exit: easeInCubic — 250–350 ms
## Durations
Type-on: field values ≈ 45–60 chars/s; Hindi line 1.5 s; chip stagger 80 ms (first 3), 400 ms (rest).
## Patterns
- Field fill: field appears with tint background + caret while typing; "✓ just written" on the newest complete field (as in the real Scribe UI).
- Match cuts: hook case sheet → P2 case sheet (same card); P1 patient bubble drops toward the Modalities field; "Sent to consultation" button → clip B2 (doctor looks up at patient).
- Loop: last 0.75 s the case-sheet card glides back to its frame-0 state (same field progress), so frame 899 → frame 0 is seamless.
- At most one push-in per shot (clip A has an in-camera push; no UI push-ins).
## Safe zones
Text kept between y 250 and 1500; side margins 72 px. Captions at y 1390.
