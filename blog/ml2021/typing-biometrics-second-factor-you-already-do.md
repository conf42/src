# Typing biometrics, the second factor you are already doing

Conf42 Blog, 2021-07-29. https://www.conf42.com/blog/ml2021/typing-biometrics-second-factor-you-already-do

In short: Madalina Burci (TypingDNA) at Conf42 Machine Learning 2021 on keystroke dynamics as a second factor, with a live Postman demo of the TypingDNA API

Your password can be shoulder-surfed; the rhythm you type it in cannot. That is the pitch [Madalina Burci](https://www.conf42.com/Machine_Learning_2021_Madalina_Burci_Security_at_your_fingertips), Developer Ambassador at TypingDNA, made at Conf42 Machine Learning 2021: keystroke dynamics, the timing of how you press and release keys, is a second authentication factor that asks the user to do nothing they were not already doing. The talk is half theory, half live demo, and the demo includes the satisfying moment where a colleague's attempt to type the same phrase gets rejected.

It is a vendor talk showing TypingDNA's own products, and it says so.

## Where does keystroke dynamics come from?

Further back than you would guess. During World War II, military intelligence used a method called the fist of the sender: the rhythm of a Morse code operator's dots and dashes was distinctive enough to tell an allied operator from an enemy one. As written communication took over, the same idea moved to keyboards, and authentication became the most developed use.

## How does it compare with other factors?

She splits authentication factors into three groups and grades each on security and user experience:

- **Knowledge** (a PIN, a password, your mother's maiden name): the friendliest, because everyone is used to it, and the weakest, because once leaked or reused it is trivial to break.
- **Possession** (a phone, an email address, a token that receives a one-time code): more secure, but a lost or stolen phone locks you out exactly when you need your bank.
- **Biometrics**, either physiological (fingerprint, face) or behavioural (how you walk, talk or type): the most secure on paper, but often heavier for the user, and never a clean yes or no. A biometric match is a confidence score against a threshold.

Her case for typing as the behavioural pick is that it is hard to mimic, accepted as a second factor under the EU's PSD2 rules for online payments, needs no extra hardware, and keeps adapting as the user's typing changes. Madalina Burci said at Conf42 Machine Learning 2021: "Even though somebody is next to you and sees what your password is, they cannot replicate how you type it."

The use cases she lists are e-learning and proctoring (checking that the person who started an exam is the one who finished it, and the one who took the course), financial services meeting PSD2's second-factor requirement, and identity and access management, with drop-in integrations for widgets such as ForgeRock and Azure AD B2C.

## How does the pipeline work?

Four steps: behaviour recording, data engineering, machine learning, authentication. An open source recorder captures key-press and key-release times, special keys, movement between keys, mouse movement and, on mobile, how the phone is held. Data engineering keeps only the most useful signals. The user types two or three times to enrol, much like registering a fingerprint on a new phone. After that, each login is compared against the stored profile, and a match above the threshold passes.

## What does the demo show?

First the ready-made widget, TypingDNA Verify. She signs up with an email address, which doubles as the root of trust and the fallback if you, say, break your arm. Enrolment takes the short phrase typed three times plus a one-time code; the next login is four short words and done.

Then the API, from Postman. The collection imports from TypingDNA's site, credentials go in as basic auth, and almost everything runs through one auto endpoint: it enrols the first three patterns, verifies after that, and adds any high-quality pattern it verifies to the profile so it stays current. A typing pattern viewer on the website generates patterns to paste in. Two details are worth knowing before you build on it:

- **Same text or any text.** Same text means the user types an identical phrase every time and gets away with fewer characters; any text accepts whatever they type but needs more of it. Her test phrase, picked because it gives good accuracy with few characters, is Make yourself necessary to somebody.
- **Replays are an attack signal.** Madalina Burci said at Conf42 Machine Learning 2021 that "no two typing patterns are identical, not even for the same user", so sending an identical pattern twice is flagged as a possible fraud attempt.

She also warns that desktop and mobile keyboards behave differently, so a user enrolled on desktop needs a separate mobile profile. Send a user ID, never personal data, as the identifier. The finale is the impostor test: a colleague typed the same phrase before the talk, the API returns a result of zero, and nothing is enrolled.

## What else can typing tell you?

She closes on e-health. Startups are researching whether typing patterns can flag or track brain-related conditions over time, and TypingDNA itself had just launched Focus, a free productivity app that infers mood from how you type and suggests when to take a break.

## Who should watch?

Developers adding a second factor who are tired of SMS codes, and anyone curious how behavioural biometrics behave in practice: thresholds, enrolment counts, replay detection, device profiles. The Postman section is a usable walkthrough on its own.

## Related Conf42 talks

- [Python for passwordless authentication with FIDO2 and WebAuthn](https://www.conf42.com/Python_2025_Sairam_Durgaraju_fido2_webauthn) at Conf42 Python 2025.
- [Voice biometrics in healthcare](https://www.conf42.com/Incident_Management_2025_Sreenivasul_Reddy_Meegada_healthcare_biometrics_security) at Conf42 Incident Management 2025.
- [Strokes vs keystrokes: causal AI on developer performance](https://www.conf42.com/Quantum_Computing_2024_Alex_Harris_strokes_keystrokes) at Conf42 Quantum Computing 2024.

[Watch the talk on YouTube](https://youtu.be/25IY3PZruvQ).

## From TypingDNA

- TypingDNA: [typingdna.com](https://www.typingdna.com/)
- TypingDNA Verify, the widget from the demo: [typingdna.com/verify](https://www.typingdna.com/verify)

## Watch the talk

[Security at your fingertips: from Theory to Practice!](https://www.conf42.com/Machine_Learning_2021_Madalina_Burci_Security_at_your_fingertips) at Conf42 Machine Learning 2021.
