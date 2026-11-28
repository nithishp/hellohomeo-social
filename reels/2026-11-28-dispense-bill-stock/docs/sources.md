# Sources for every on-screen claim
| on-screen | source (nithishp/hellohomeo) |
|---|---|
| Dispense once. Stock updates. / "Available now", "deducts … from stock", "Mark as Dispensed", "Pending Dispensing" | public/docs/pharmacist-prescription-detail.webp (screen text); MARKETING_SUMMARY.md §5 "Prescription-driven dispensing … inventory tracking and stock alerts" (line 16) |
| Dispense from the prescription. | MARKETING_SUMMARY.md §5 "pharmacist sees exactly what to dispense per consultation" |
| Running low? It's flagged. / Low Stock count / low stock alert | MARKETING_SUMMARY.md §5 "low-stock alerts"; public/docs/inventory-dashboard.webp ("Low Stock", "Total Items"); inventory-alerts.webp ("Low Stock" tab) |
| Batches, oldest expiry "used first" | MARKETING_SUMMARY.md §5 "items, batches" and "Multi-batch dispensing with FIFO logic" |
| The bill is ready (consultation + prescription item) | MARKETING_SUMMARY.md §7 "Auto-generated invoices from completed appointments"; documents/BILLING_MODULE_DOCUMENTATION.md "Prescription Items Addition … Uses inventory selling price" |
| Paid by UPI; Cash/Card/UPI/Bank | MARKETING_SUMMARY.md §7 "Multiple payment methods: Cash, Card, UPI, Bank Transfer…"; public/docs/billing-quick-bill.webp |
| Today's Revenue / This Month / Outstanding / Total Invoices | public/docs/billing-dashboard.webp (tile labels); values are demo values |
| 30-day free trial. Full access to all features. | app/page.js FAQ "Every new clinic gets a 30-day free trial with full access to all features." |
Demo values (Arnica 51 ml, min 50, ₹300/₹150, ₹4,350 etc.) are illustrative demo-clinic numbers on rebuilt UI, not statistics or claims.
