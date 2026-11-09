# Conf42 family media kit

Machine-readable index: https://www.conf42.com/assets/brandkit/brandkit.json (every file with url, size, px, sha256, mime, alpha).

```sh
# every SREday file
curl -s https://www.conf42.com/assets/brandkit/brandkit.json | jq -r '.items[] | select(.brand=="sreday") | .url' | xargs -n1 curl -sO
# one logo
curl -O https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.svg
```

## Conf42

Conf42 is where it started, online, in 2020: 30+ online conferences a year on everything from SRE and Kubernetes to Python, Rust and AI. Every talk is free on YouTube, with transcripts and slides at conf42.com.

Name: Conf42 (capital C, no space). Website: https://www.conf42.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Blue | `#335EEA` | 51 94 234 | 78 60 0 8 |
| Navy | `#1B2A4E` | 27 42 78 | 65 46 0 69 |
| Midnight | `#161C2D` | 22 28 45 | 51 38 0 82 |
| Sky | `#7EA2D2` | 126 162 210 | 40 23 0 18 |
| Corgi | `#EA8A5A` | 234 138 90 | 0 41 62 8 |
| Coral | `#DF4759` | 223 71 89 | 0 68 60 13 |
| Mint | `#42BA96` | 66 186 150 | 65 0 19 27 |
| Paper | `#F9FBFD` | 249 251 253 | 2 1 0 1 |

### Logos

- Wordmark in black: [SVG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.svg), [PDF](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.eps), [PNG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.png)
- Mark (42) in black: [SVG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.svg), [PDF](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.eps), [PNG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.png)
- Wordmark in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.svg), [PDF](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.eps), [PNG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.png)
- Mark (42) in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.svg), [PDF](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.eps), [PNG](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.png)
- Wordmark, original vector (Adobe Illustrator): [AI](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-original.ai)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/social/conf42-email-signature-1200x300.svg)

### Stickers

- Sticker: [PNG](https://www.conf42.com/assets/brandkit/conf42/stickers/conf42-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/stickers/conf42-sticker.svg)

### Mascots & pets

- Corgi (404): [PNG](https://www.conf42.com/assets/brandkit/conf42/mascots/conf42-corgi-404.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/mascots/conf42-corgi-404.svg)
- Bear with us: [PNG](https://www.conf42.com/assets/brandkit/conf42/mascots/conf42-bear-with-us.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/mascots/conf42-bear-with-us.svg)

### Animations

- Hero animation: [WEBP](https://www.conf42.com/assets/brandkit/conf42/animations/conf42-hero-animation.webp), [MP4](https://www.conf42.com/assets/brandkit/conf42/animations/conf42-hero-animation.mp4)

### Illustrations

- Illustration, hero: [PNG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-hero.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-hero.svg)
- Illustration, blog: [PNG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-blog.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-blog.svg)
- Illustration, podcast: [PNG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-podcast.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-podcast.svg)
- Illustration, sponsors: [PNG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-sponsors.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-sponsors.svg)
- Space banner: [PNG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-space-banner.png), [SVG](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-space-banner.svg)

### Event splashes

- Conf42 AI Agents 2027: [PNG](https://www.conf42.com/assets/splash/AGENTS2027_Event_Splash.png)
- Conf42 Chaos Engineering 2027: [PNG](https://www.conf42.com/assets/splash/CE2027_Event_Splash.png)
- Conf42 Cloud Native 2027: [PNG](https://www.conf42.com/assets/splash/CLOUD2027_Event_Splash.png)
- Conf42 Database DevOps 2027: [PNG](https://www.conf42.com/assets/splash/DBD2027_Event_Splash.png)
- Conf42 DevOps 2027: [PNG](https://www.conf42.com/assets/splash/DEVOPS2027_Event_Splash.png)
- Conf42 DevSecOps 2027: [PNG](https://www.conf42.com/assets/splash/DEVSECOPS2027_Event_Splash.png)
- Conf42 Feature Flags 2027: [PNG](https://www.conf42.com/assets/splash/FEATUREFLAGS2027_Event_Splash.png)
- Conf42 FinOps 2027: [PNG](https://www.conf42.com/assets/splash/FINOPS2027_Event_Splash.png)
- Conf42 Golang 2027: [PNG](https://www.conf42.com/assets/splash/GOLANG2027_Event_Splash.png)
- Conf42 Large Language Models (LLMs) 2027: [PNG](https://www.conf42.com/assets/splash/LLM2027_Event_Splash.png)
- Conf42 MLOps 2027: [PNG](https://www.conf42.com/assets/splash/MLOPS2027_Event_Splash.png)
- Conf42 Machine Learning 2027: [PNG](https://www.conf42.com/assets/splash/ML2027_Event_Splash.png)
- Conf42 Observability 2027: [PNG](https://www.conf42.com/assets/splash/OBS2027_Event_Splash.png)
- Conf42 Platform Engineering 2027: [PNG](https://www.conf42.com/assets/splash/PLATFORM2027_Event_Splash.png)
- Conf42 Prompt Engineering 2027: [PNG](https://www.conf42.com/assets/splash/PROMPT2027_Event_Splash.png)
- Conf42 Remix 2027: [PNG](https://www.conf42.com/assets/splash/REMIX2027_Event_Splash.png)
- Conf42 Site Reliability Engineering (SRE) 2027: [PNG](https://www.conf42.com/assets/splash/SRE2027_Event_Splash.png)
- Conf42 Tokenomics 2027: [PNG](https://www.conf42.com/assets/splash/TOKENOMICS2027_Event_Splash.png)
- Conf42 AI Agents 2026: [PNG](https://www.conf42.com/assets/splash/AGENTS2026_Event_Splash.png)
- Conf42 Chaos Engineering 2026: [PNG](https://www.conf42.com/assets/splash/CE2026_Event_Splash.png)
- Conf42 Cloud Native 2026: [PNG](https://www.conf42.com/assets/splash/CLOUD2026_Event_Splash.png)
- Conf42 Database DevOps 2026: [PNG](https://www.conf42.com/assets/splash/DBD2026_Event_Splash.png)
- Conf42 DevOps 2026: [PNG](https://www.conf42.com/assets/splash/DEVOPS2026_Event_Splash.png)
- Conf42 DevSecOps 2026: [PNG](https://www.conf42.com/assets/splash/DEVSECOPS2026_Event_Splash.png)
- Conf42 Feature Flags 2026: [PNG](https://www.conf42.com/assets/splash/FEATUREFLAGS2026_Event_Splash.png)
- Conf42 Golang 2026: [PNG](https://www.conf42.com/assets/splash/GOLANG2026_Event_Splash.png)
- Conf42 Incident Management 2026: [PNG](https://www.conf42.com/assets/splash/INCIDENT2026_Event_Splash.png)
- Conf42 Kube Native 2026: [PNG](https://www.conf42.com/assets/splash/KUBE2026_Event_Splash.png)
- Conf42 Large Language Models (LLMs) 2026: [PNG](https://www.conf42.com/assets/splash/LLM2026_Event_Splash.png)
- Conf42 MLOps 2026: [PNG](https://www.conf42.com/assets/splash/MLOPS2026_Event_Splash.png)
- Conf42 Machine Learning 2026: [PNG](https://www.conf42.com/assets/splash/ML2026_Event_Splash.png)
- Conf42 Observability 2026: [PNG](https://www.conf42.com/assets/splash/OBS2026_Event_Splash.png)
- Conf42 Platform Engineering 2026: [PNG](https://www.conf42.com/assets/splash/PLATFORM2026_Event_Splash.png)
- Conf42 Prompt Engineering 2026: [PNG](https://www.conf42.com/assets/splash/PROMPT2026_Event_Splash.png)
- Conf42 Python 2026: [PNG](https://www.conf42.com/assets/splash/PYTHON2026_Event_Splash.png)
- Conf42 Quantum Computing 2026: [PNG](https://www.conf42.com/assets/splash/QUANTUM2026_Event_Splash.png)
- Conf42 Remix 2026: [PNG](https://www.conf42.com/assets/splash/REMIX2026_Event_Splash.png)
- Conf42 Robotics 2026: [PNG](https://www.conf42.com/assets/splash/ROBOTICS2026_Event_Splash.png)
- Conf42 Site Reliability Engineering (SRE) 2026: [PNG](https://www.conf42.com/assets/splash/SRE2026_Event_Splash.png)
- Conf42 Chaos Engineering 2025: [PNG](https://www.conf42.com/assets/splash/CE2025_Event_Splash.png)
- Conf42 Cloud Native 2025: [PNG](https://www.conf42.com/assets/splash/CLOUD2025_Event_Splash.png)
- Conf42 DevOps 2025: [PNG](https://www.conf42.com/assets/splash/DEVOPS2025_Event_Splash.png)
- Conf42 DevSecOps 2025: [PNG](https://www.conf42.com/assets/splash/DEVSECOPS2025_Event_Splash.png)
- Conf42 Golang 2025: [PNG](https://www.conf42.com/assets/splash/GOLANG2025_Event_Splash.png)
- Conf42 Incident Management 2025: [PNG](https://www.conf42.com/assets/splash/INCIDENT2025_Event_Splash.png)
- Conf42 Internet of Things (IoT) 2025: [PNG](https://www.conf42.com/assets/splash/IOT2025_Event_Splash.png)
- Conf42 JavaScript 2025: [PNG](https://www.conf42.com/assets/splash/JS2025_Event_Splash.png)
- Conf42 Kube Native 2025: [PNG](https://www.conf42.com/assets/splash/KUBE2025_Event_Splash.png)
- Conf42 Large Language Models (LLMs) 2025: [PNG](https://www.conf42.com/assets/splash/LLM2025_Event_Splash.png)
- Conf42 MLOps 2025: [PNG](https://www.conf42.com/assets/splash/MLOPS2025_Event_Splash.png)
- Conf42 Machine Learning 2025: [PNG](https://www.conf42.com/assets/splash/ML2025_Event_Splash.png)
- Conf42 Observability 2025: [PNG](https://www.conf42.com/assets/splash/OBS2025_Event_Splash.png)
- Conf42 Platform Engineering 2025: [PNG](https://www.conf42.com/assets/splash/PLATFORM2025_Event_Splash.png)
- Conf42 Prompt Engineering 2025: [PNG](https://www.conf42.com/assets/splash/PROMPT2025_Event_Splash.png)
- Conf42 Python 2025: [PNG](https://www.conf42.com/assets/splash/PYTHON2025_Event_Splash.png)
- Conf42 Quantum Computing 2025: [PNG](https://www.conf42.com/assets/splash/QUANTUM2025_Event_Splash.png)
- Conf42 Robotics 2025: [PNG](https://www.conf42.com/assets/splash/ROBOTICS2025_Event_Splash.png)
- Conf42 Rustlang 2025: [PNG](https://www.conf42.com/assets/splash/RUST2025_Event_Splash.png)
- Conf42 Site Reliability Engineering (SRE) 2025: [PNG](https://www.conf42.com/assets/splash/SRE2025_Event_Splash.png)
- Conf42 Aiml 2024: [PNG](https://www.conf42.com/assets/splash/AIML2024_Event_Splash.png)
- Conf42 Chaos Engineering 2024: [PNG](https://www.conf42.com/assets/splash/CE2024_Event_Splash.png)
- Conf42 Cloud Native 2024: [PNG](https://www.conf42.com/assets/splash/CLOUD2024_Event_Splash.png)
- Conf42 DevOps 2024: [PNG](https://www.conf42.com/assets/splash/DEVOPS2024_Event_Splash.png)
- Conf42 DevSecOps 2024: [PNG](https://www.conf42.com/assets/splash/DEVSECOPS2024_Event_Splash.png)
- Conf42 Golang 2024: [PNG](https://www.conf42.com/assets/splash/GOLANG2024_Event_Splash.png)
- Conf42 Incident Management 2024: [PNG](https://www.conf42.com/assets/splash/INCIDENT2024_Event_Splash.png)
- Conf42 Internet of Things (IoT) 2024: [PNG](https://www.conf42.com/assets/splash/IOT2024_Event_Splash.png)
- Conf42 JavaScript 2024: [PNG](https://www.conf42.com/assets/splash/JS2024_Event_Splash.png)
- Conf42 Kube Native 2024: [PNG](https://www.conf42.com/assets/splash/KUBE2024_Event_Splash.png)
- Conf42 Large Language Models (LLMs) 2024: [PNG](https://www.conf42.com/assets/splash/LLM2024_Event_Splash.png)
- Conf42 Machine Learning 2024: [PNG](https://www.conf42.com/assets/splash/ML2024_Event_Splash.png)
- Conf42 Observability 2024: [PNG](https://www.conf42.com/assets/splash/OBS2024_Event_Splash.png)
- Conf42 Platform Engineering 2024: [PNG](https://www.conf42.com/assets/splash/PLATFORM2024_Event_Splash.png)
- Conf42 Prompt Engineering 2024: [PNG](https://www.conf42.com/assets/splash/PROMPT2024_Event_Splash.png)
- Conf42 Python 2024: [PNG](https://www.conf42.com/assets/splash/PYTHON2024_Event_Splash.png)
- Conf42 Quantum Computing 2024: [PNG](https://www.conf42.com/assets/splash/QUANTUM2024_Event_Splash.png)
- Conf42 Rustlang 2024: [PNG](https://www.conf42.com/assets/splash/RUST2024_Event_Splash.png)
- Conf42 Site Reliability Engineering (SRE) 2024: [PNG](https://www.conf42.com/assets/splash/SRE2024_Event_Splash.png)
- Conf42 Chaos Engineering 2023: [PNG](https://www.conf42.com/assets/splash/CE2023_Event_Splash.png)
- Conf42 Cloud Native 2023: [PNG](https://www.conf42.com/assets/splash/CLOUD2023_Event_Splash.png)
- Conf42 DevOps 2023: [PNG](https://www.conf42.com/assets/splash/DEVOPS2023_Event_Splash.png)
- Conf42 DevSecOps 2023: [PNG](https://www.conf42.com/assets/splash/DEVSECOPS2023_Event_Splash.png)
- Conf42 Golang 2023: [PNG](https://www.conf42.com/assets/splash/GOLANG2023_Event_Splash.png)
- Conf42 Incident Management 2023: [PNG](https://www.conf42.com/assets/splash/INCIDENT2023_Event_Splash.png)
- Conf42 Internet of Things (IoT) 2023: [PNG](https://www.conf42.com/assets/splash/IOT2023_Event_Splash.png)
- Conf42 JavaScript 2023: [PNG](https://www.conf42.com/assets/splash/JS2023_Event_Splash.png)
- Conf42 Kube Native 2023: [PNG](https://www.conf42.com/assets/splash/KUBE2023_Event_Splash.png)
- Conf42 Machine Learning 2023: [PNG](https://www.conf42.com/assets/splash/ML2023_Event_Splash.png)
- Conf42 Mobile 2023: [PNG](https://www.conf42.com/assets/splash/MOBILE2023_Event_Splash.png)
- Conf42 Observability 2023: [PNG](https://www.conf42.com/assets/splash/OBS2023_Event_Splash.png)
- Conf42 Platform Engineering 2023: [PNG](https://www.conf42.com/assets/splash/PLATFORM2023_Event_Splash.png)
- Conf42 Python 2023: [PNG](https://www.conf42.com/assets/splash/PYTHON2023_Event_Splash.png)
- Conf42 Quantum Computing 2023: [PNG](https://www.conf42.com/assets/splash/QUANTUM2023_Event_Splash.png)
- Conf42 Rustlang 2023: [PNG](https://www.conf42.com/assets/splash/RUST2023_Event_Splash.png)
- Conf42 Site Reliability Engineering 2023: [PNG](https://www.conf42.com/assets/splash/SRE2023_Event_Splash.png)
- Conf42 Web 3.0 2023: [PNG](https://www.conf42.com/assets/splash/WEB32023_Event_Splash.png)
- Conf42 Chaos Engineering 2022: [PNG](https://www.conf42.com/assets/splash/CE2022_Event_Splash.png)
- Conf42 Cloud Native 2022: [PNG](https://www.conf42.com/assets/splash/CLOUD2022_Event_Splash.png)
- Conf42 DevSecOps 2022: [PNG](https://www.conf42.com/assets/splash/DEVSECOPS2022_Event_Splash.png)
- Conf42 Golang 2022: [PNG](https://www.conf42.com/assets/splash/GOLANG2022_Event_Splash.png)
- Conf42 Incident Management 2022: [PNG](https://www.conf42.com/assets/splash/INCIDENT2022_Event_Splash.png)
- Conf42 JavaScript 2022: [PNG](https://www.conf42.com/assets/splash/JS2022_Event_Splash.png)
- Conf42 Kube Native 2022: [PNG](https://www.conf42.com/assets/splash/KUBE2022_Event_Splash.png)
- Conf42 Machine Learning 2022: [PNG](https://www.conf42.com/assets/splash/ML2022_Event_Splash.png)
- Conf42 Mobile 2022: [PNG](https://www.conf42.com/assets/splash/MOBILE2022_Event_Splash.png)
- Conf42 Python 2022: [PNG](https://www.conf42.com/assets/splash/PYTHON2022_Event_Splash.png)
- Conf42 Quantum Computing 2022: [PNG](https://www.conf42.com/assets/splash/QUANTUM2022_Event_Splash.png)
- Conf42 Rustlang 2022: [PNG](https://www.conf42.com/assets/splash/RUST2022_Event_Splash.png)
- Conf42 Site Reliability Engineering 2022: [PNG](https://www.conf42.com/assets/splash/SRE2022_Event_Splash.png)
- Conf42 Web 3.0 2022: [PNG](https://www.conf42.com/assets/splash/WEB32022_Event_Splash.png)
- Conf42 JavaScript 2010: [PNG](https://www.conf42.com/assets/splash/JS2010_Event_Splash.png)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/conf42/conf42-about.txt)

## SREday

SREday is where Site Reliability Engineers, DevOps practitioners and cloud architects meet face to face: talks from people running production at scale, hosted in the offices of companies like Harness, ING and Google.

Name: SREday (SRE in capitals, day in lower case). Website: https://www.sreday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Plum | `#713660` | 113 54 96 | 0 52 15 56 |
| Sticker violet | `#5A4E72` | 90 78 114 | 21 32 0 55 |
| Blue | `#098DCF` | 9 141 207 | 96 32 0 19 |
| Coral | `#EC645E` | 236 100 94 | 0 58 60 7 |
| Orchid | `#C46AA0` | 196 106 160 | 0 46 18 23 |
| Monkey orange | `#EA9244` | 234 146 68 | 0 38 71 8 |
| Ink | `#141C25` | 20 28 37 | 46 24 0 85 |
| Mist | `#F0F6FA` | 240 246 250 | 4 2 0 2 |

### Logos

- Logo in colour: [SVG](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.svg), [PDF](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.pdf), [EPS](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.eps), [PNG](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.png)
- Logo in black: [SVG](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.svg), [PDF](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.eps), [PNG](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.png)
- Logo in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.svg), [PDF](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.eps), [PNG](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/social/sreday-email-signature-1200x300.svg)

### Stickers

- Sticker: [PNG](https://www.conf42.com/assets/brandkit/sreday/stickers/sreday-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/stickers/sreday-sticker.svg)

### Mascots & pets

- Monkey: [PNG](https://www.conf42.com/assets/brandkit/sreday/mascots/sreday-monkey.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/mascots/sreday-monkey.svg)
- Monkey (404): [PNG](https://www.conf42.com/assets/brandkit/sreday/mascots/sreday-monkey-404.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/mascots/sreday-monkey-404.svg)

### Animations

- Boardroom monkeys: [WEBP](https://www.conf42.com/assets/brandkit/sreday/animations/sreday-monkeys.webp), [MP4](https://www.conf42.com/assets/brandkit/sreday/animations/sreday-monkeys.mp4)
- Monkey dance: [WEBP](https://www.conf42.com/assets/brandkit/sreday/animations/sreday-monkey-dance.webp), [MP4](https://www.conf42.com/assets/brandkit/sreday/animations/sreday-monkey-dance.mp4)

### Illustrations

- Logo, round: [PNG](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-logo-round.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-logo-round.svg)
- Logo, horizontal: [PNG](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-logo-horizontal.png), [SVG](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-logo-horizontal.svg)
- Brand gradient: [JPG](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-brand-gradient.jpg), [SVG](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-brand-gradient.svg)

### Event splashes

- SREday Katowice 2027 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2027-katowice-q2.png)
- SREday London 2027 Q1: [PNG](https://sreday.com/assets/images/events/sreday-2027-london-q1.png)
- SREday Warsaw 2027 Q1: [PNG](https://sreday.com/assets/images/events/sreday-2027-warsaw-q1.png)
- SREday Amsterdam 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-amsterdam-q4.png)
- SREday Austin 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-austin-q2.png)
- SREday Bangalore 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-bangalore-q2.png)
- SREday Barcelona 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-barcelona-q2.png)
- SREday Campinas 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-campinas-q4.png)
- SREday Chennai 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-chennai-q4.png)
- SREday Cologne 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-cologne-q2.png)
- SREday Dallas 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-dallas-q4.png)
- SREday Hyderabad 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-hyderabad-q2.png)
- SREday Lisbon 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-lisbon-q2.png)
- SREday London 2026 Q1: [PNG](https://sreday.com/assets/images/events/sreday-2026-london-q1.png)
- SREday London 2026 Q3: [PNG](https://sreday.com/assets/images/events/sreday-2026-london-q3.png)
- SREday Munich 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-munich-q2.png)
- SREday NYC 2026 Q1: [PNG](https://sreday.com/assets/images/events/sreday-2026-nyc-q1.png)
- SREday NYC 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-nyc-q2.png)
- SREday NYC 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-nyc-q4.png)
- SREday Paris 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-paris-q2.png)
- SREday Sanfrancisco 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-sanfrancisco-q2.png)
- SREday Sanfrancisco 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-sanfrancisco-q4.png)
- SREday Seattle 2026 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2026-seattle-q2.png)
- SREday Warsaw 2026 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2026-warsaw-q4.png)
- SREday Amsterdam 2025 Q2: [PNG](https://sreday.com/assets/images/events/sreday-2025-amsterdam-q2.png)
- SREday Amsterdam 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-amsterdam-q4.png)
- SREday Campinas 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-campinas-q4.png)
- SREday Chennai 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-chennai-q4.png)
- SREday Cologne 2025 Q2: [JPEG](https://sreday.com/assets/images/events/sreday-2025-cologne-q2.jpeg)
- SREday Cologne 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-cologne-q4.png)
- SREday Lisbon 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-lisbon-q4.png)
- SREday London 2025 Q1: [JPEG](https://sreday.com/assets/images/events/sreday-2025-london-q1.jpeg)
- SREday London 2025 Q3: [PNG](https://sreday.com/assets/images/events/sreday-2025-london-q3.png)
- SREday NYC 2025 Q1: [JPEG](https://sreday.com/assets/images/events/sreday-2025-nyc-q1.jpeg)
- SREday Paris 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-paris-q4.png)
- SREday Redmond 2025 Q2: [JPEG](https://sreday.com/assets/images/events/sreday-2025-redmond-q2.jpeg)
- SREday Sanfrancisco 2025 Q2: [JPEG](https://sreday.com/assets/images/events/sreday-2025-sanfrancisco-q2.jpeg)
- SREday Sanfrancisco 2025 Q4: [PNG](https://sreday.com/assets/images/events/sreday-2025-sanfrancisco-q4.png)
- SREday Amsterdam 2024: [JPEG](https://sreday.com/assets/images/events/sreday-2024-amsterdam.jpeg)
- SREday London 2024: [JPEG](https://sreday.com/assets/images/events/sreday-2024-london.jpeg)
- SREday Sanfrancisco 2024: [JPEG](https://sreday.com/assets/images/events/sreday-2024-sanfrancisco.jpeg)
- SREday Sanfrancisco 2024 Q4: [JPEG](https://sreday.com/assets/images/events/sreday-2024-sanfrancisco-q4.jpeg)
- SREday London 2023: [JPEG](https://sreday.com/assets/images/events/sreday-2023-london.jpeg)
- SREday London 2022: [JPEG](https://sreday.com/assets/images/events/sreday-2022-london.jpeg)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/sreday/sreday-about.txt)

## LLMday

LLMday brings AI engineers, ML engineers and data scientists together in person to share what actually works with LLMs and agents in production: evaluation, RAG, guardrails, cost and everything in between.

Name: LLMday (LLM in capitals, day in lower case). Website: https://www.llmday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Green | `#26986A` | 38 152 106 | 75 0 30 40 |
| Leaf | `#4BCB81` | 75 203 129 | 63 0 36 20 |
| Lime | `#8FDC6A` | 143 220 106 | 35 0 52 14 |
| Teal | `#2EC4B6` | 46 196 182 | 77 0 7 23 |
| Blue | `#098DCF` | 9 141 207 | 96 32 0 19 |
| Coral | `#EC645E` | 236 100 94 | 0 58 60 7 |
| Black | `#000000` | 0 0 0 | 0 0 0 100 |
| Ink | `#141C25` | 20 28 37 | 46 24 0 85 |
| Mist | `#F0F6FA` | 240 246 250 | 4 2 0 2 |

### Logos

- Logo in colour: [SVG](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.svg), [PDF](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.pdf), [EPS](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.eps), [PNG](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.png)
- Logo in black: [SVG](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.svg), [PDF](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.eps), [PNG](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.png)
- Logo in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.svg), [PDF](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.eps), [PNG](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/social/llmday-email-signature-1200x300.svg)

### Stickers

- Sticker: [PNG](https://www.conf42.com/assets/brandkit/llmday/stickers/llmday-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/stickers/llmday-sticker.svg)

### Mascots & pets

- Baby llama: [PNG](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-baby-llama.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-baby-llama.svg)
- Llama: [PNG](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-llama.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-llama.svg)
- Llama (404): [PNG](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-llama-404.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-llama-404.svg)

### Animations

- Llama: [WEBP](https://www.conf42.com/assets/brandkit/llmday/animations/llmday-llama.webp), [MP4](https://www.conf42.com/assets/brandkit/llmday/animations/llmday-llama.mp4)
- Llama conspiracy: [WEBP](https://www.conf42.com/assets/brandkit/llmday/animations/llmday-llama-conspiracy.webp), [MP4](https://www.conf42.com/assets/brandkit/llmday/animations/llmday-llama-conspiracy.mp4)

### Illustrations

- Brand gradient: [PNG](https://www.conf42.com/assets/brandkit/llmday/artwork/llmday-brand-gradient.png), [SVG](https://www.conf42.com/assets/brandkit/llmday/artwork/llmday-brand-gradient.svg)

### Event splashes

- LLMday Austin 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-austin-q2.png)
- LLMday Austin 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-austin-q4.png)
- LLMday Bangalore 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-bangalore-q2.png)
- LLMday Hamburg 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-hamburg-q2.png)
- LLMday Hamburg 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-hamburg-q4.png)
- LLMday Lisbon 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-lisbon-q2.png)
- LLMday London 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-london-q2.png)
- LLMday London 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-london-q4.png)
- LLMday Montevideo 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-montevideo-q4.png)
- LLMday NYC 2026 Q1: [PNG](https://llmday.com/assets/images/events/llmday-2026-nyc-q1.png)
- LLMday NYC 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-nyc-q2.png)
- LLMday NYC 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-nyc-q4.png)
- LLMday San Francisco 2026 Q2: [PNG](https://llmday.com/assets/images/events/llmday-2026-san-francisco-q2.png)
- LLMday San Francisco 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-san-francisco-q4.png)
- LLMday Tel Aviv 2026 Q4: [PNG](https://llmday.com/assets/images/events/llmday-2026-tel-aviv-q4.png)
- LLMday Warsaw 2026 Q1: [PNG](https://llmday.com/assets/images/events/llmday-2026-warsaw-q1.png)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/llmday/llmday-about.txt)

## PLATFORMday

PLATFORMday is for the people who build and run internal platforms: developer experience, infrastructure, golden paths and the tooling that ties them together, in person.

Name: PLATFORMday (PLATFORM in capitals, day in lower case). Website: https://www.platformday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Orange | `#E2971D` | 226 151 29 | 0 33 87 11 |
| Ember | `#D0562B` | 208 86 43 | 0 59 79 18 |
| Sun | `#F5C84C` | 245 200 76 | 0 18 69 4 |
| Platypus | `#7B5947` | 123 89 71 | 0 28 42 52 |
| Slate | `#415B78` | 65 91 120 | 46 24 0 53 |
| Blue | `#098DCF` | 9 141 207 | 96 32 0 19 |
| Coral | `#EC645E` | 236 100 94 | 0 58 60 7 |
| Black | `#000000` | 0 0 0 | 0 0 0 100 |
| Ink | `#141C25` | 20 28 37 | 46 24 0 85 |
| Mist | `#F0F6FA` | 240 246 250 | 4 2 0 2 |

### Logos

- Logo in colour: [SVG](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.svg), [PDF](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.pdf), [EPS](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.eps), [PNG](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.png)
- Logo in black: [SVG](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.svg), [PDF](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.eps), [PNG](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.png)
- Logo in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.svg), [PDF](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.eps), [PNG](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/social/platformday-email-signature-1200x300.svg)

### Stickers

- Sticker: [PNG](https://www.conf42.com/assets/brandkit/platformday/stickers/platformday-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/stickers/platformday-sticker.svg)

### Mascots & pets

- Baby platypus: [PNG](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-baby-platypus.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-baby-platypus.svg)
- Platypus: [PNG](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-platypus.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-platypus.svg)
- Platypus (404): [PNG](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-platypus-404.png), [SVG](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-platypus-404.svg)

### Event splashes

- PLATFORMday London 2027 Q2: [PNG](https://platformday.com/assets/images/events/platformday-2027-london-q2.png)
- PLATFORMday Austin 2026 Q4: [PNG](https://platformday.com/assets/images/events/platformday-2026-austin-q4.png)
- PLATFORMday San Francisco 2026 Q4: [PNG](https://platformday.com/assets/images/events/platformday-2026-san-francisco-q4.png)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/platformday/platformday-about.txt)

## Prompt Engineering Conference

The Prompt Engineering Conference grew from its online beginnings in 2023 to a full day in London, co-located with LLMday London: the craft of prompting, agents and AI-assisted work.

Name: Prompt Engineering Conference (short: PEC). Website: https://promptengineering.rocks/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Violet | `#6B40D8` | 107 64 216 | 50 70 0 15 |
| Pink | `#E8507A` | 232 80 122 | 0 66 47 9 |
| Amber | `#F5AD37` | 245 173 55 | 0 29 78 4 |
| Red | `#EF4448` | 239 68 72 | 0 72 70 6 |
| Sky | `#29B7EC` | 41 183 236 | 83 22 0 7 |
| Green | `#6CDE7C` | 108 222 124 | 51 0 44 13 |
| Teal | `#2BB3C0` | 43 179 192 | 78 7 0 25 |
| Ink | `#141C25` | 20 28 37 | 46 24 0 85 |
| Mist | `#F0F6FA` | 240 246 250 | 4 2 0 2 |

### Logos

- Logo in colour: [SVG](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.svg), [PDF](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.pdf), [EPS](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.eps), [PNG](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.png)
- Logo in black: [SVG](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.svg), [PDF](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.eps), [PNG](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.png)
- Logo in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.svg), [PDF](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.eps), [PNG](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/pec/social/pec-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/pec/social/pec-email-signature-1200x300.svg)

### Stickers

- Logo, original: [PNG](https://www.conf42.com/assets/brandkit/pec/stickers/pec-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/pec/stickers/pec-sticker.svg)

### Mascots & pets

- Avatar: [PNG](https://www.conf42.com/assets/brandkit/pec/mascots/pec-avatar.png), [SVG](https://www.conf42.com/assets/brandkit/pec/mascots/pec-avatar.svg)

### Event splashes

- Prompt Engineering Conference London 2026 Q4: [JPG](https://promptengineering.rocks/assets/images/events/pec-2026-london-q4.jpg)
- Prompt Engineering Conference London 2025 Q4: [JPG](https://promptengineering.rocks/assets/images/events/pec-2025-london-q4.jpg)
- Prompt Engineering Conference Online 2024: [JPG](https://promptengineering.rocks/assets/images/events/pec-2024-online.jpg)
- Prompt Engineering Conference Online 2023: [JPG](https://promptengineering.rocks/assets/images/events/pec-2023-online.jpg)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/pec/pec-about.txt)

## Reliaburger

Reliaburger is a container orchestrator in Rust by Miko Pawlikowski: one binary, a complete container platform, zero assembly. Source, design notes and a free book on GitHub.

Name: Reliaburger (one word). Website: https://reliaburger.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Lettering pink | `#EA1E4E` | 234 30 78 | 0 87 67 8 |
| Bun orange | `#F68A1E` | 246 138 30 | 0 44 88 4 |
| Lettuce | `#5ABA42` | 90 186 66 | 52 0 65 27 |
| Sauce | `#DE2A96` | 222 42 150 | 0 81 32 13 |
| Patty | `#7E421E` | 126 66 30 | 0 48 76 51 |
| Rust | `#A83B15` | 168 59 21 | 0 65 87 34 |
| Peach | `#F49463` | 244 148 99 | 0 39 59 4 |
| Ink | `#181B19` | 24 27 25 | 11 0 7 89 |
| Sage | `#E4E9E3` | 228 233 227 | 2 0 3 9 |

### Logos

- Logo in colour: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-color.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-color.svg)
- Logo in black: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-black.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-black.svg), [PDF](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-black.eps)
- Logo in white (for dark backgrounds): [PNG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-white.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-white.svg), [PDF](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-white.eps)
- Lettering (text only) in colour: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-lettering.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-lettering.svg)
- Logo on yellow (original): [PNG](https://www.conf42.com/assets/brandkit/reliaburger/logos/reliaburger-burger-logo-on-yellow.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-email-signature-1200x300.svg)

### Stickers

- Sticker: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/stickers/reliaburger-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/stickers/reliaburger-sticker.svg)

### Mascots & pets

- Capybara: [PNG](https://www.conf42.com/assets/brandkit/reliaburger/mascots/reliaburger-capybara.png), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/mascots/reliaburger-capybara.svg)

### Animations

- Burger loop: [WEBP](https://www.conf42.com/assets/brandkit/reliaburger/animations/reliaburger-burger-loop.webp), [MP4](https://www.conf42.com/assets/brandkit/reliaburger/animations/reliaburger-burger-loop.mp4)

### Illustrations

- Logo (v1): [JPG](https://www.conf42.com/assets/brandkit/reliaburger/artwork/reliaburger-logo-v1.jpg), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/artwork/reliaburger-logo-v1.svg)
- Burger: [WEBP](https://www.conf42.com/assets/brandkit/reliaburger/artwork/reliaburger-burger.webp), [SVG](https://www.conf42.com/assets/brandkit/reliaburger/artwork/reliaburger-burger.svg)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/reliaburger/reliaburger-about.txt)

## CFP Ninja

CFP Ninja is the open Call for Papers platform every Conf42, SREday and LLMday CFP runs on. Speakers find open calls and submit once; organisers review in one place.

Name: CFP Ninja (cfp.ninja as the address). Website: https://cfp.ninja/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Bandana red | `#A21E1E` | 162 30 30 | 0 81 81 36 |
| Frog green | `#96BA4E` | 150 186 78 | 19 0 58 27 |
| Moss | `#728A36` | 114 138 54 | 17 0 61 46 |
| Laptop | `#4D5454` | 77 84 84 | 8 0 0 67 |
| Cream | `#F6F5DD` | 246 245 221 | 0 0 10 4 |
| Ink | `#000000` | 0 0 0 | 0 0 0 100 |

### Logos

- Mark in colour: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-color.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-email-signature-1200x300.svg)

### Stickers

- Sticker: [PNG](https://www.conf42.com/assets/brandkit/cfpninja/stickers/cfpninja-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/cfpninja/stickers/cfpninja-sticker.svg)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/cfpninja/cfpninja-about.txt)

## Certified FYI

Certified FYI issues verifiable certificates of achievement: organisers issue them, speakers collect them on a public profile.

Name: Certified FYI (certified.fyi as the address). Website: https://certified.fyi/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Green | `#158C0F` | 21 140 15 | 85 0 89 45 |
| Ink | `#151515` | 21 21 21 | 0 0 0 92 |
| White | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- Logo in colour: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-color.png)
- Logo in black: [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.svg), [PDF](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.eps), [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.png)
- Logo in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.svg), [PDF](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.eps), [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-email-signature-1200x300.svg)

### Stickers

- Logo, original: [PNG](https://www.conf42.com/assets/brandkit/certifiedfyi/stickers/certifiedfyi-sticker.png), [SVG](https://www.conf42.com/assets/brandkit/certifiedfyi/stickers/certifiedfyi-sticker.svg)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/certifiedfyi/certifiedfyi-about.txt)

## Badger

Badger prints attendee badges at the door of every SREday, LLMday and PLATFORMday; Snout by Badger is its sponsor lead scanner.

Name: Badger (Snout by Badger for the lead scanner). Website: https://scan.sreday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Orange | `#EA722A` | 234 114 42 | 0 51 82 8 |
| Ink | `#151515` | 21 21 21 | 0 0 0 92 |
| White | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- Badger in colour: [PNG](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-color.png)
- Snout by Badger in colour: [PNG](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-color.png)
- Badger in black: [SVG](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.svg), [PDF](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.eps), [PNG](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.png)
- Snout by Badger in black: [SVG](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.svg), [PDF](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.pdf), [EPS](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.eps), [PNG](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.png)
- Badger in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.svg), [PDF](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.eps), [PNG](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.png)
- Snout by Badger in white (for dark backgrounds): [SVG](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.svg), [PDF](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.pdf), [EPS](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.eps), [PNG](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.png)

### Profile pictures

- Avatar, square, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-square-1000.png), [SVG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-square-1000.svg)
- Avatar, square, 400 px: [PNG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-square-400.png), [SVG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-square-400.svg)
- Avatar, round, 1000 px: [PNG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-round-1000.png), [SVG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-round-1000.svg)
- Avatar, round, 400 px: [PNG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-round-400.png), [SVG](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-round-400.svg)

### Banners & covers

- LinkedIn company page cover: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-company-1512x256.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-company-1512x256.svg)
- LinkedIn company page cover, sharp (6:1): [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-company-hd-4200x700.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-company-hd-4200x700.svg)
- LinkedIn profile banner: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-profile-1584x396.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-profile-1584x396.svg)
- X (Twitter) header: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-x-header-1500x500.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-x-header-1500x500.svg)
- Bluesky banner: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-bluesky-banner-3000x1000.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-bluesky-banner-3000x1000.svg)
- Facebook cover: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-facebook-cover-1640x624.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-facebook-cover-1640x624.svg)
- YouTube channel banner: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-youtube-banner-2560x1440.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-youtube-banner-2560x1440.svg)
- Link preview (Open Graph): [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-og-image-1200x630.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-og-image-1200x630.svg)
- Zoom / Teams / Meet background: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-video-background-1920x1080.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-video-background-1920x1080.svg)
- Email signature banner: [PNG](https://www.conf42.com/assets/brandkit/badger/social/badger-email-signature-1200x300.png), [SVG](https://www.conf42.com/assets/brandkit/badger/social/badger-email-signature-1200x300.svg)

### Stickers

- Logo, original: [WEBP](https://www.conf42.com/assets/brandkit/badger/stickers/badger-sticker.webp), [SVG](https://www.conf42.com/assets/brandkit/badger/stickers/badger-sticker.svg)

### About text

- About text (boilerplate): [TXT](https://www.conf42.com/assets/brandkit/badger/badger-about.txt)
