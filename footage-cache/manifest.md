# Footage cache manifest
Pseudonymised captures from the demo clinic (doctor login). Captured 1600×900 @2x. PII gate passed (patient names/emails/phones replaced from the admin roster; files below contain no patient data).

| file | what it shows | captured (IST) |
|---|---|---|
| 2026-11-04/doctor-dashboard.png | Doctor portal dashboard (Dr. Doctor demo account, quickstart checklist) | 2026-11-04 |
| 2026-11-04/repertory-search-typed.png | Repertory Search with "flatulence" typed | 2026-11-04 |
| 2026-11-04/repertory-results-flatulence.png | Results (295) for "flatulence": ABDOMEN - FLATULENCE added | 2026-11-04 |
| 2026-11-04/repertory-sheet-remedy-analysis.png | Repertory Sheet: ABDOMEN - FLATULENCE → Remedy Analysis (aloe, am-m., arg-n., ars., calc., score 3) | 2026-11-04 |
| 2026-11-04/vita-compare-nux-lyco.png | Vita AI answer: Nux Vomica vs Lycopodium for digestive complaints, comparison table (conversation list cropped out) | 2026-11-04 |
| 2026-11-14/scribe-idle.png | Doctor portal → Scribe (Consultation scribe), idle, before the demo starts | 2026-11-14 |
| 2026-11-14/scribe-demo-30s.png | Scribe demo "Chronic migraine · Hindi" at 0:30: The room (Hindi + English gloss), Case sheet 6 of 17 fields, Live repertorisation 8 rubrics (nat-m 18) | 2026-11-14 |
| 2026-11-14/scribe-demo-end.png | Scribe demo complete: Case sheet 13 of 17 fields, 14 rubrics, nat-m 36 (14/14) | 2026-11-14 |
Note: 2026-11-14 captures show only the app's built-in scripted Scribe demo (fictional patient, name not visible in these frames) and the demo doctor account; no real patient data. /api/admin/patients returned 401 for the doctor role, so the roster walk had nothing to replace.
| 2026-11-21/followup-modal-filled.png | Consultation → Schedule Follow-up dialog (cropped to the dialog): date, 11:30 AM, "Review response to remedy"; patient name is a pseudonym | 2026-11-21 |
| 2026-11-21/followup-toast.png | Toast "Follow-up scheduled - patient notified 🎉" (follow-up POST was stubbed; nothing booked) | 2026-11-21 |
| 2026-11-21/doctor-appointments.png | Doctor portal → My appointments (96 total; Follow-up/Chronic tags, Pending status); names and phones pseudonymised | 2026-11-21 |
Note: 2026-11-21 roster came from /api/doctor/appointments (admin roster returns 401 for the doctor). The full consultation page was NOT cached: it shows a street address that is not in the roster.
