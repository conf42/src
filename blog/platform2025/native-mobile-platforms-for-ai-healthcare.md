# Healthcare apps need native code, on-device AI and HIPAA by design

Conf42 Blog, 2025-08-13, updated 2026-11-09. https://www.conf42.com/blog/platform2025/native-mobile-platforms-for-ai-healthcare

In short: Srikanth Puram of General Motors at Conf42 Platform Engineering 2025 on native mobile platforms with embedded AI for HIPAA-compliant, offline-ready healthcare.

When a patient's heart rate drops, a loading spinner is not an acceptable state. At Conf42 Platform Engineering 2025, Srikanth Puram, a senior software engineer at General Motors, made the case that healthcare apps should be built as platforms on native mobile code with embedded AI, so they stay fast, private and useful even when the network isn't there.

The talk is a broad tour rather than a code walkthrough, and each section is anchored by a real-world example from a different country.

## Platforms, not one-off apps

Srikanth's starting point is pressure on health systems: ageing populations, more chronic illness and stretched capacity. Building isolated apps doesn't scale, so he argues for platforms of reusable components, standardised interfaces for hospitals, devices and insurers, and architectures that handle millions of patients. Reliability, observability and maintainability matter even more in a domain that needs safe, auditable systems.

His example is a UK hospital network that built one shared platform for appointments, telemedicine and vaccination tracking and reused components across apps, cutting development time.

## Why native

Native development, in his framing, is about performance and reliability: real-time responsiveness for alerts, deeper OS-level security with encryption and secure storage, direct integration with glucose monitors, ECGs and blood pressure cuffs, and offline capability for rural areas with poor connectivity.

The example is an Android diabetes app connected directly to Bluetooth glucose monitors. Patients get instant alerts on abnormal readings and doctors get accurate, secure data streams. He argues that immediacy would have been hard with a hybrid app.

## AI on the device

Embedded AI shifts care from reactive to predictive. With frameworks like TensorFlow Lite, models run on the phone, so sensitive data stays local and analysis is faster. Uses include early warning of deterioration, personalised care recommendations and clinical decision support.

His examples range widely: a mobile eye-care app in India detecting diabetic retinopathy from smartphone images in clinics without eye specialists, connected ECG patches in Japan flagging abnormal rhythms, and an oncology decision-support system suggesting chemotherapy options while doctors keep the final call.

## Compliance is architecture

On HIPAA his line is that compliance is foundational, not optional: encryption at rest and in transit, role-based access with biometrics and multi-factor authentication, and audit trails for every data interaction. The best platforms bake these in so every app built on them gets them automatically. He cites a US telemedicine provider that restricted test results to physicians only, which helped with HIPAA and with patient trust.

## Rolling it out safely

The implementation section is the most grounded. Agile adapted for regulatory cycles, clinical validation with diverse patient groups, pilots in controlled settings, and real change management with staff training. His favourite example is a US children's hospital that piloted an asthma app with 50 families, refined it, then expanded to 10,000 patients.

Accessibility gets attention too: large fonts, voice input, high-contrast modes, translation and content tuned to literacy levels. Looking ahead he points to federated learning, AR in surgery and voice-first interfaces.

## Who should watch

Mobile engineers moving into health tech, and platform teams who need a checklist of what regulated, device-connected mobile apps require. Expect breadth over depth.

## Related Conf42 talks

- [Nisheedh Raveendran on managing regulatory incidents in HIPAA, GDPR and DMA environments](https://www.conf42.com/Incident_Management_2025_Nisheedh_Raveendran_compliance_hipaa_gdpr) covers what happens when compliance meets an incident.
- [Meghana Rao and Ananya M Gowda on attacking Bluetooth LE in mobile and wearables](https://www.conf42.com/Web_30_2022_Meghana_Rao_Ananya_M_Gowda_bluetooth_mobile_wearables_ecosystems) is the security flip side of device integration.
- [Ramakrishna Ambati on secure IoT edge architecture for medical diagnostic systems](https://www.conf42.com/Internet_of_Things_IoT_2025_Ramakrishna_Ambati_maintenance_predictive_medical) applies edge AI to medical hardware.

[Watch Srikanth Puram's talk](https://www.conf42.com/Platform_Engineering_2025_Srikanth_Puram_mobile_healthcare_powered)

[Watch the talk on YouTube](https://youtu.be/2jXid_Sqja0).

## Watch the talk

[Platform Engineering for AI-Powered Healthcare: Native Mobile Architecture](https://www.conf42.com/Platform_Engineering_2025_Srikanth_Puram_mobile_healthcare_powered) at Conf42 Platform Engineering 2025.
