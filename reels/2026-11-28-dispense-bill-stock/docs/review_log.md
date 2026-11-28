# Review log
## Round 1 (stills 0, 1.5, 4.5, 9.8, 13.8, 17.8, 20.5, 27.5, 29.9)
Scores: hook 7, readability@360 6, product clarity 8, motion 8, composition 7, depth 7, sound sync 8, polish 7.
Gates: claims in sources.md ✔; PII ✔ (fictional patient; no captured screen used); garbled UI ✔ (all UI is live HTML); safe zones ✔.
Top problems: (1) card text too small at 360 px (26–32 px labels, 4-column field grid wrapping); (2) result tiles used invented labels ("Dispensed today", "Unbilled visits") not on any real screen; (3) frame 1 showed a static number.
Fixes: 2×2 field grid, card text 30–48 px; result tiles switched to the real Billing Dashboard labels (Today's Revenue, This Month, Outstanding, Total Invoices); stock number already rolling in frame 1.
## Round 2 (full render; frames every 3 s + loop pair)
Scores: hook 8, readability@360 8, product clarity 9, motion 8, composition 8, depth 8 (added ghost-panel parallax at 14 px/s over the 6 px/s dot grid), sound sync 8, polish 8.
Gates all pass. Loop: last frame (29.9) matches frame 0 (same card, same 48 ml state). Shipped.
