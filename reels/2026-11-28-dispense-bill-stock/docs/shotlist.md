# Shot list (30 s, 30 fps, 106.67 BPM grid; bar = 2.25 s from 0.25)
No voiceover this week (ElevenLabs free tier: 19 characters left until the monthly reset), so the on-screen headlines carry the script. Text column = burned-in caption.

| # | time | frames | picture / camera | on-screen text | SFX | source |
|---|---|---|---|---|---|---|
| 1 HOOK | 0.00–2.25 | 0–67 | Prescription Details card already ticked in frame 1; "Available now" rolls 51 → 46 ml; pill flips Pending → Dispensed at 0.9 s; very slow push (1.2%) | Dispense once. / Stock updates. | ticks 0.05, 0.3, 0.9 | rebuilt from public/docs/pharmacist-prescription-detail.webp |
| 2 PAIN | 2.25–7.00 | 67–210 | Higgsfield clip A: pharmacist counting bottles into a paper stock register, then a bill pad; gentle push-in | Stock register. / Bill book. / Every evening. | whoosh 2.1 | Higgsfield prompt A (docs/spend.md) |
| 3 PAYOFF 1 | 7.00–11.50 | 210–345 | Same card glides back up (match on card); box ticks 8.6, button press 9.3, pill → Dispensed 9.5, stock rolls 51→46 | Dispense from / the prescription. | whoosh 6.85, tick 8.6, pop 9.5 | pharmacist-prescription-detail.webp |
| 4 PAYOFF 2 | 11.50–15.44 | 345–463 | Inventory stat cards (Total Items 40, Low Stock 0→1 amber), alert card pops: Arnica Montana 30C low stock 46 ml (min 50); two batches, oldest-expiry "used first" | Running low? / It's flagged. | whoosh 11.35, pop 12.5, ticks 13.4, 13.65 | inventory-dashboard.webp, inventory-alerts.webp; MARKETING_SUMMARY §5 |
| 5 PAYOFF 3 | 15.44–19.00 | 463–570 | Invoice card: Consultation ₹300 + Arnica 5 ml ₹150 = ₹450; UPI chip selects 17.2; pill pending → paid 17.8 | The bill is ready. / Paid by UPI. | whoosh 15.3, ticks lines, chime 17.8 | billing-invoice-create.webp, billing-quick-bill.webp; MARKETING_SUMMARY §7; BILLING_MODULE_DOCUMENTATION |
| 6 RESULT | 19.00–21.63 | 570–649 | Calm billing dashboard tiles count up (Today's Revenue, This Month, Outstanding ₹0, Total Invoices) | Stock and bills. / Done by closing. | whoosh 18.85 | billing-dashboard.webp labels |
| 7 HOME | 21.63–25.00 | 649–750 | Higgsfield clip B: doctor and pharmacist smile; doctor leaves; static drift | Counter closed. / On time. | whoosh 21.5 (soft) | Higgsfield prompt B |
| 8 CTA | 25.00–30.00 | 750–900 | Logo, HelloHomeo, hellohomeo.in, "30-day free trial / Full access to all features."; at 29.3 the prescription card glides back in = frame 1 (loop) | as shown | chime 25.0 | app/page.js FAQ |
