# Sources for every on-screen claim
| claim / text | source file |
|---|---|
| "Schedule Follow-up" dialog: "Book the next visit for … They will get a confirmation and reminders automatically.", Date / Time / "Reason / notes (optional)", "Review response to remedy", Cancel / Schedule Follow-up | app/c/[clinicSlug]/doctor/consultation/[id]/page.jsx (modal markup); live capture 2026-11-21 |
| Toast "Follow-up scheduled - patient notified 🎉" | same file, handleScheduleFollowUp; live capture (POST stubbed) |
| Reminders 24 h and 1 h before on WhatsApp | app/features/page.jsx ("appointment reminders (24h & 1h)"); app/api/doctor/appointments/[id]/follow-up/route.js comment ("24h+1h WhatsApp reminders") |
| 24 h reminder text "⏰ Appointment Reminder … you have an appointment tomorrow. 📅 Date … 🕐 Time … 🔹 Mode: 🏥 In-Person" | lib/whatsapp/templates.js appointmentReminder24h |
| 1 h reminder text "⏰ Appointment in 1 Hour … 📍 Please make your way to the clinic." | lib/whatsapp/templates.js appointmentReminder1h |
| Patients reschedule over WhatsApp; "✅ Appointment Rescheduled! … Our team will review the change and confirm shortly." | app/page.js FAQ ("check appointment status, cancel, or reschedule"); lib/whatsapp/templates.js rescheduleSuccess |
| "My appointments", "Every consultation assigned to you.", Follow-up tag, Pending pill | live capture appointments.png (2026-11-21) |
| 30-day free trial, full access to all features | app/page.js FAQ "Is there a free trial?" |
| "Less chasing. Home on time." | narrative line (no number or guarantee); not a product claim |
Patient names are pseudonyms (Asha Rao, Vikram Iyer, Meera Nair, Divya Shah); no real patient data.
