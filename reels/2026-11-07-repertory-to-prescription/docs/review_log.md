# Review log
## Round 1 (stills every 1.5 s)
Scores: hook 8 · readability@360 6 · product clarity 8 · motion 7 · composition 6 · depth 7 · sound sync n/a · polish 7
Gates: claims ✓ sources.md · PII ✓ none · garbled UI ✓ none (all UI rebuilt in HTML) · safe zones ✗ (cards overlapped caption band)
Top problems: 1) UI cards too tall, overlap captions; 2) "Patient waiting." low contrast over clip; 3) UI text too small at 360 px.
Fixes: trimmed cards (2 result rows, 3 remedies, 3 table rows), moved captions to y 1310, larger UI type, stronger top shade + text shadow.
## Round 2 (final render, frame every 3 s + loop check)
Scores: hook 8 · readability@360 8 · product clarity 9 · motion 8 · composition 8 · depth 8 · sound sync 8 · polish 8
Gates: claims ✓ · PII ✓ (no patient names/phones in reel; Vita prompt generic) · garbled UI ✓ · safe zones ✓ (text between y 250 and 1420)
Remaining problems: 1) background dot-grid loop offset (fixed: 16 px/s = exactly 10 tiles in 30 s); 2) Higgsfield clips are 720p upscaled (slightly soft); 3) tick SFX synthesised locally because ElevenLabs was busy.
Audio: −13.8 LUFS integrated, −1.5 dBTP; music ducked under VO by sidechain; Whisper re-transcription of the final mix reads the VO cleanly.
