# Review log
## Round 1 (stills, 17 times)
Scores: hook 7 · readability@360 6 · product clarity 8 · motion 7 · composition 6 · depth 6 · sound sync n/a · polish 6
Gates: claims ✓ sources.md · PII ✓ (demo doctor only; scripted demo patient's name never shown) · garbled UI ✓ (all UI rebuilt in HTML) · safe zones ✗ (captions over remedy board and Send button)
Top problems: 1) UI type too small at 360 px; 2) captions collide with cards; 3) "In any of 10 languages." wraps into the card, "Not the patient." overlaps line 1.
Fixes: UI values 38–41 px, captions to y 1390, headline shortened to "In their language.", kinetic line moved, ghost card added for depth.
## Round 2 (stills + first full render, frame every 3 s)
Scores: hook 8 · readability@360 8 · product clarity 9 · motion 8 · composition 8 · depth 8 · sound sync 8 · polish 8
Gates: all ✓. Problems: 1) hook didn't show the Hindi→English idea in frame 1; 2) room card empty for ~0.5 s after the cut; 3) clips are 720p upscaled (slightly soft).
Fixes: Hindi patient line above the filling case sheet from frame 0 (and in the loop end); room bubbles enter 0.15/0.6 s after the cut.
## Round 3 (final render, frames 0,3,…,27,29.9 + last frame, loop_check.mp4)
Scores: hook 9 · readability@360 8 · product clarity 9 · motion 8 · composition 8 · depth 8 · sound sync 8 · polish 8
Gates: claims ✓ · PII ✓ · garbled UI ✓ · safe zones ✓ (text between y 250 and 1500) · product acting in frame 1 ✓ (Location field typing, "just written" tick)
Audio: −14.2 LUFS integrated, −1.2 dBFS peak; music ducked under VO (sidechain); Whisper (base.en) re-transcription of the mix reads the VO cleanly; music has no vocals.
Remaining known issues: Higgsfield clips are 720p upscaled; SFX synthesised locally; cuts sit within ≤0.15 s of the music beats.
