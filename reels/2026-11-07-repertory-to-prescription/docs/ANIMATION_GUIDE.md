# Animation guide
## Tokens
--ink #070C1F · --jade #10B880 · --jade-deep #06805A · --jade-on-dark #5FD6AC · --tint #E8F8F1 · --card #FFFFFF · --line #CDEFE0 · --muted #6A7385
Radius: card 32, chip 999, row 18. Shadow: raised (design.md).
## Easing set
- glide: cubic-bezier(.22,1,.36,1) (easeOutQuint) — cards entering, 500–700 ms
- snap: easeOutBack(1.4) — chips/ticks landing, 300–400 ms
- settle: easeInOutCubic — layout shifts, 400 ms
- exit: easeInCubic — 250–300 ms, 80 px travel
## Durations
Type-on 45 ms/char · row stagger 90 ms · bar fill 600 ms · kinetic word stagger 120 ms.
## Patterns
- Card glide: translateY 120→0, opacity 0→1, slight scale .98→1; parallax background layer moves 0.4× foreground.
- Tick: circle stroke draw 250 ms, then check snap.
- Match cut: UI state A's key element ends at the same screen position as state B's start.
- At most one push-in (scale ≤ 1.04) per shot.
## Safe zones (Reels)
Top 220 px and bottom 420 px kept free of essential text; side margins 72 px. Captions sit at y 1180–1420.
