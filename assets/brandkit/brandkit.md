# Conf42 family media kit

Machine-readable index: https://www.conf42.com/assets/brandkit/brandkit.json (every file with url, size, px, sha256, mime).

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
| Primary | `#2C3FB0` | 44 63 176 | 75 64 0 31 |
| Ink | `#0F1A3D` | 15 26 61 | 75 57 0 76 |
| Dark | `#16205A` | 22 32 90 | 76 64 0 65 |
| Light | `#E2E6F8` | 226 230 248 | 9 7 0 3 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- [Wordmark, black (SVG)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.svg)
- [Wordmark, black (PDF)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.pdf)
- [Wordmark, black (EPS)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.eps)
- [Wordmark, black (PNG, 2000x531)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-black.png)
- [Wordmark, white (SVG)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.svg)
- [Wordmark, white (PDF)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.pdf)
- [Wordmark, white (EPS)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.eps)
- [Wordmark, white (PNG, 2000x531)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-white.png)
- [Wordmark, colour (SVG)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-color.svg)
- [Wordmark, color (PDF)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-color.pdf)
- [Wordmark, color (EPS)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-color.eps)
- [Wordmark, colour (PNG, 2000x531)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-color.png)
- [Wordmark on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-on-light.png)
- [Wordmark on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-wordmark-on-dark.png)
- [Mark (42), black (SVG)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.svg)
- [Mark (42), black (PDF)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.pdf)
- [Mark (42), black (EPS)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.eps)
- [Mark (42), black (PNG, 2000x2091)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-black.png)
- [Mark (42), white (SVG)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.svg)
- [Mark (42), white (PDF)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.pdf)
- [Mark (42), white (EPS)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.eps)
- [Mark (42), white (PNG, 2000x2091)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-white.png)
- [Mark (42), colour (SVG)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-color.svg)
- [Mark (42), color (PDF)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-color.pdf)
- [Mark (42), color (EPS)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-color.eps)
- [Mark (42), colour (PNG, 2000x2091)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-color.png)
- [Mark (42) on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-on-light.png)
- [Mark (42) on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/conf42/logos/conf42-mark-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/conf42/social/conf42-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/conf42/avatars/conf42-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 2000x2000)](https://www.conf42.com/assets/brandkit/conf42/stickers/conf42-sticker.png)

### Mascots

- [Corgi (404) (PNG, 467x720)](https://www.conf42.com/assets/brandkit/conf42/mascots/conf42-corgi-404.png)
- [Bear with us (PNG, 480x675)](https://www.conf42.com/assets/brandkit/conf42/mascots/conf42-bear-with-us.png)

### Artwork

- [Illustration, hero (PNG, 7809x4076)](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-hero.png)
- [Illustration, blog (PNG, 7470x4317)](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-blog.png)
- [Illustration, podcast (PNG, 7854x4013)](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-podcast.png)
- [Illustration, sponsors (PNG, 7516x3853)](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-illustration-sponsors.png)
- [Space banner (PNG, 2550x1440)](https://www.conf42.com/assets/brandkit/conf42/artwork/conf42-space-banner.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/conf42/colours/conf42-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/conf42/colours/conf42-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/conf42/colours/conf42-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/conf42/colours/conf42-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/conf42/colours/conf42-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/conf42/conf42-about.txt)

## SREday

SREday is where Site Reliability Engineers, DevOps practitioners and cloud architects meet face to face: talks from people running production at scale, hosted in the offices of companies like Harness, ING and Google.

Name: SREday (SRE in capitals, day in lower case). Website: https://www.sreday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#7B3FE4` | 123 63 228 | 46 72 0 11 |
| Ink | `#1D1240` | 29 18 64 | 55 72 0 75 |
| Dark | `#2D0E62` | 45 14 98 | 54 86 0 62 |
| Light | `#E9E0FB` | 233 224 251 | 7 11 0 2 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- [Logo, black (SVG)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.svg)
- [Logo, black (PDF)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.pdf)
- [Logo, black (EPS)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.eps)
- [Logo, black (PNG, 2000x1966)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-black.png)
- [Logo, white (SVG)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.svg)
- [Logo, white (PDF)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.pdf)
- [Logo, white (EPS)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.eps)
- [Logo, white (PNG, 2000x1966)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-white.png)
- [Logo, colour (SVG)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.svg)
- [Logo, color (PDF)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.pdf)
- [Logo, color (EPS)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.eps)
- [Logo, colour (PNG, 2000x1966)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-color.png)
- [Logo on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-on-light.png)
- [Logo on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/sreday/logos/sreday-logo-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/sreday/social/sreday-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/sreday/avatars/sreday-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 2000x2000)](https://www.conf42.com/assets/brandkit/sreday/stickers/sreday-sticker.png)

### Mascots

- [Monkey (PNG, 2048x2048)](https://www.conf42.com/assets/brandkit/sreday/mascots/sreday-monkey.png)
- [Monkey (404) (PNG, 580x720)](https://www.conf42.com/assets/brandkit/sreday/mascots/sreday-monkey-404.png)

### Artwork

- [Logo, round (PNG, 1500x1500)](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-logo-round.png)
- [Logo, horizontal (PNG, 1500x750)](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-logo-horizontal.png)
- [Brand gradient (JPG, 2848x4272)](https://www.conf42.com/assets/brandkit/sreday/artwork/sreday-brand-gradient.jpg)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/sreday/colours/sreday-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/sreday/colours/sreday-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/sreday/colours/sreday-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/sreday/colours/sreday-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/sreday/colours/sreday-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/sreday/sreday-about.txt)

## LLMday

LLMday brings AI engineers, ML engineers and data scientists together in person to share what actually works with LLMs and agents in production: evaluation, RAG, guardrails, cost and everything in between.

Name: LLMday (LLM in capitals, day in lower case). Website: https://www.llmday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#1F9D6B` | 31 157 107 | 80 0 32 38 |
| Ink | `#0C2B20` | 12 43 32 | 72 0 26 83 |
| Dark | `#135E40` | 19 94 64 | 80 0 32 63 |
| Light | `#E1F9F0` | 225 249 240 | 10 0 4 2 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- [Logo, black (SVG)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.svg)
- [Logo, black (PDF)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.pdf)
- [Logo, black (EPS)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.eps)
- [Logo, black (PNG, 2000x1654)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-black.png)
- [Logo, white (SVG)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.svg)
- [Logo, white (PDF)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.pdf)
- [Logo, white (EPS)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.eps)
- [Logo, white (PNG, 2000x1654)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-white.png)
- [Logo, colour (SVG)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.svg)
- [Logo, color (PDF)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.pdf)
- [Logo, color (EPS)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.eps)
- [Logo, colour (PNG, 2000x1654)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-color.png)
- [Logo on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-on-light.png)
- [Logo on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/llmday/logos/llmday-logo-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/llmday/social/llmday-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/llmday/avatars/llmday-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 2000x2000)](https://www.conf42.com/assets/brandkit/llmday/stickers/llmday-sticker.png)

### Mascots

- [Baby llama (PNG, 2048x2048)](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-baby-llama.png)
- [Llama (PNG, 816x928)](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-llama.png)
- [Llama (404) (PNG, 498x720)](https://www.conf42.com/assets/brandkit/llmday/mascots/llmday-llama-404.png)

### Artwork

- [Brand gradient (PNG, 1024x1536)](https://www.conf42.com/assets/brandkit/llmday/artwork/llmday-brand-gradient.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/llmday/colours/llmday-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/llmday/colours/llmday-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/llmday/colours/llmday-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/llmday/colours/llmday-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/llmday/colours/llmday-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/llmday/llmday-about.txt)

## PLATFORMday

PLATFORMday is for the people who build and run internal platforms: developer experience, infrastructure, golden paths and the tooling that ties them together, in person.

Name: PLATFORMday (PLATFORM in capitals, day in lower case). Website: https://www.platformday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#E2971D` | 226 151 29 | 0 33 87 11 |
| Ink | `#2A1C06` | 42 28 6 | 0 33 86 84 |
| Dark | `#62420E` | 98 66 14 | 0 33 86 62 |
| Light | `#FBF0E0` | 251 240 224 | 0 4 11 2 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- [Logo, black (SVG)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.svg)
- [Logo, black (PDF)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.pdf)
- [Logo, black (EPS)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.eps)
- [Logo, black (PNG, 2000x1990)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-black.png)
- [Logo, white (SVG)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.svg)
- [Logo, white (PDF)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.pdf)
- [Logo, white (EPS)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.eps)
- [Logo, white (PNG, 2000x1990)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-white.png)
- [Logo, colour (SVG)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.svg)
- [Logo, color (PDF)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.pdf)
- [Logo, color (EPS)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.eps)
- [Logo, colour (PNG, 2000x1990)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-color.png)
- [Logo on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-on-light.png)
- [Logo on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/platformday/logos/platformday-logo-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/platformday/social/platformday-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/platformday/avatars/platformday-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 4096x4096)](https://www.conf42.com/assets/brandkit/platformday/stickers/platformday-sticker.png)

### Mascots

- [Baby platypus (PNG, 2048x2048)](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-baby-platypus.png)
- [Platypus (PNG, 1080x1080)](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-platypus.png)
- [Platypus (404) (PNG, 585x720)](https://www.conf42.com/assets/brandkit/platformday/mascots/platformday-platypus-404.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/platformday/colours/platformday-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/platformday/colours/platformday-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/platformday/colours/platformday-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/platformday/colours/platformday-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/platformday/colours/platformday-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/platformday/platformday-about.txt)

## Prompt Engineering Conference

The Prompt Engineering Conference grew from its online beginnings in 2023 to a full day in London, co-located with LLMday London: the craft of prompting, agents and AI-assisted work.

Name: Prompt Engineering Conference (short: PEC). Website: https://promptengineering.rocks/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#D9467A` | 217 70 122 | 0 68 44 15 |
| Ink | `#1E1530` | 30 21 48 | 37 56 0 81 |
| Dark | `#5D132D` | 93 19 45 | 0 80 52 64 |
| Light | `#F9E1EA` | 249 225 234 | 0 10 6 2 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- [Logo, black (SVG)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.svg)
- [Logo, black (PDF)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.pdf)
- [Logo, black (EPS)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.eps)
- [Logo, black (PNG, 2000x734)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-black.png)
- [Logo, white (SVG)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.svg)
- [Logo, white (PDF)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.pdf)
- [Logo, white (EPS)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.eps)
- [Logo, white (PNG, 2000x729)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-white.png)
- [Logo, colour (SVG)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.svg)
- [Logo, color (PDF)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.pdf)
- [Logo, color (EPS)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.eps)
- [Logo, colour (PNG, 2000x766)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-color.png)
- [Logo on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-on-light.png)
- [Logo on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/pec/logos/pec-logo-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/pec/social/pec-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/pec/social/pec-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/pec/social/pec-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/pec/social/pec-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/pec/social/pec-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/pec/social/pec-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/pec/social/pec-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/pec/social/pec-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/pec/avatars/pec-avatar-round-400.png)

### Stickers

- [Logo, original (PNG, 2229x918)](https://www.conf42.com/assets/brandkit/pec/stickers/pec-sticker.png)

### Mascots

- [Avatar (PNG, 650x650)](https://www.conf42.com/assets/brandkit/pec/mascots/pec-avatar.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/pec/colours/pec-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/pec/colours/pec-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/pec/colours/pec-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/pec/colours/pec-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/pec/colours/pec-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/pec/pec-about.txt)

## DevOps Not Dead

DevOps Not Dead is an in-person event series co-created with Harness: practitioners talking honestly about delivering software, in London and New York.

Name: DevOps Not Dead (short: DND). Website: https://www.devopsnotdead.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#2E9AD8` | 46 154 216 | 79 29 0 15 |
| Ink | `#14202B` | 20 32 43 | 53 26 0 83 |
| Dark | `#12435F` | 18 67 95 | 81 29 0 63 |
| Light | `#E1F0F9` | 225 240 249 | 10 4 0 2 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/devopsnotdead/social/devopsnotdead-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/devopsnotdead/avatars/devopsnotdead-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/devopsnotdead/avatars/devopsnotdead-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/devopsnotdead/avatars/devopsnotdead-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/devopsnotdead/avatars/devopsnotdead-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 7851x5441)](https://www.conf42.com/assets/brandkit/devopsnotdead/stickers/devopsnotdead-sticker.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/devopsnotdead/colours/devopsnotdead-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/devopsnotdead/colours/devopsnotdead-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/devopsnotdead/colours/devopsnotdead-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/devopsnotdead/colours/devopsnotdead-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/devopsnotdead/colours/devopsnotdead-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/devopsnotdead/devopsnotdead-about.txt)

## Reliaburger

Reliaburger is a container orchestrator in Rust by Miko Pawlikowski: one binary, a complete container platform, zero assembly. Source, design notes and a free book on GitHub.

Name: Reliaburger (one word). Website: https://reliaburger.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#A83B15` | 168 59 21 | 0 65 87 34 |
| Ink | `#181B19` | 24 27 25 | 11 0 7 89 |
| Dark | `#62240E` | 98 36 14 | 0 63 86 62 |
| Light | `#FBE7E0` | 251 231 224 | 0 8 11 2 |
| Paper | `#FFF7EF` | 255 247 239 | 0 3 6 0 |

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/reliaburger/social/reliaburger-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/reliaburger/avatars/reliaburger-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 2048x2048)](https://www.conf42.com/assets/brandkit/reliaburger/stickers/reliaburger-sticker.png)

### Artwork

- [Logo (v1) (JPG, 1024x1024)](https://www.conf42.com/assets/brandkit/reliaburger/artwork/reliaburger-logo-v1.jpg)
- [Burger (WEBP, 720x892)](https://www.conf42.com/assets/brandkit/reliaburger/artwork/reliaburger-burger.webp)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/reliaburger/colours/reliaburger-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/reliaburger/colours/reliaburger-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/reliaburger/colours/reliaburger-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/reliaburger/colours/reliaburger-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/reliaburger/colours/reliaburger-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/reliaburger/reliaburger-about.txt)

## CFP Ninja

CFP Ninja is the open Call for Papers platform every Conf42, SREday and LLMday CFP runs on. Speakers find open calls and submit once; organisers review in one place.

Name: CFP Ninja (cfp.ninja as the address). Website: https://cfp.ninja/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#C8262C` | 200 38 44 | 0 81 78 22 |
| Ink | `#1C2A12` | 28 42 18 | 33 0 57 84 |
| Dark | `#5E1215` | 94 18 21 | 0 81 78 63 |
| Light | `#F9E1E2` | 249 225 226 | 0 10 9 2 |
| Paper | `#FFFFFF` | 255 255 255 | 0 0 0 0 |

### Logos

- [Mark, black (SVG)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-black.svg)
- [Mark, black (PDF)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-black.pdf)
- [Mark, black (EPS)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-black.eps)
- [Mark, black (PNG, 2000x1296)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-black.png)
- [Mark, white (SVG)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-white.svg)
- [Mark, white (PDF)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-white.pdf)
- [Mark, white (EPS)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-white.eps)
- [Mark, white (PNG, 2000x1296)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-white.png)
- [Mark, colour (PNG, 1331x861)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-color.png)
- [Mark on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-on-light.png)
- [Mark on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/cfpninja/logos/cfpninja-mark-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/cfpninja/social/cfpninja-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/cfpninja/avatars/cfpninja-avatar-round-400.png)

### Stickers

- [Sticker (PNG, 2048x1934)](https://www.conf42.com/assets/brandkit/cfpninja/stickers/cfpninja-sticker.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/cfpninja/colours/cfpninja-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/cfpninja/colours/cfpninja-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/cfpninja/colours/cfpninja-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/cfpninja/colours/cfpninja-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/cfpninja/colours/cfpninja-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/cfpninja/cfpninja-about.txt)

## Certified FYI

Certified FYI issues verifiable certificates of achievement: organisers issue them, speakers collect them on a public profile.

Name: Certified FYI (certified.fyi as the address). Website: https://certified.fyi/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#22A339` | 34 163 57 | 79 0 65 36 |
| Ink | `#1B1F23` | 27 31 35 | 23 11 0 86 |
| Dark | `#135D20` | 19 93 32 | 80 0 66 64 |
| Light | `#E1F9E6` | 225 249 230 | 10 0 8 2 |
| Paper | `#F4F7F4` | 244 247 244 | 1 0 1 3 |

### Logos

- [Logo, black (SVG)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.svg)
- [Logo, black (PDF)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.pdf)
- [Logo, black (EPS)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.eps)
- [Logo, black (PNG, 2000x1115)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-black.png)
- [Logo, white (SVG)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.svg)
- [Logo, white (PDF)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.pdf)
- [Logo, white (EPS)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.eps)
- [Logo, white (PNG, 2000x1115)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-white.png)
- [Logo, colour (PNG, 1936x1079)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-color.png)
- [Logo on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-on-light.png)
- [Logo on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/certifiedfyi/logos/certifiedfyi-logo-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/certifiedfyi/social/certifiedfyi-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/certifiedfyi/avatars/certifiedfyi-avatar-round-400.png)

### Stickers

- [Logo, original (PNG, 2214x1272)](https://www.conf42.com/assets/brandkit/certifiedfyi/stickers/certifiedfyi-sticker.png)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/certifiedfyi/colours/certifiedfyi-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/certifiedfyi/colours/certifiedfyi-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/certifiedfyi/colours/certifiedfyi-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/certifiedfyi/colours/certifiedfyi-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/certifiedfyi/colours/certifiedfyi-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/certifiedfyi/certifiedfyi-about.txt)

## Badger

Badger prints attendee badges at the door of every SREday, LLMday and PLATFORMday; Snout by Badger is its sponsor lead scanner.

Name: Badger (Snout by Badger for the lead scanner). Website: https://scan.sreday.com/

| Colour | HEX | RGB | CMYK |
|---|---|---|---|
| Primary | `#F26B1D` | 242 107 29 | 0 56 88 5 |
| Ink | `#151515` | 21 21 21 | 0 0 0 92 |
| Dark | `#622D0E` | 98 45 14 | 0 54 86 62 |
| Light | `#FBEAE0` | 251 234 224 | 0 7 11 2 |
| Paper | `#F6F4F1` | 246 244 241 | 0 1 2 4 |

### Logos

- [Badger, black (SVG)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.svg)
- [Badger, black (PDF)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.pdf)
- [Badger, black (EPS)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.eps)
- [Badger, black (PNG, 2000x564)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-black.png)
- [Badger, white (SVG)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.svg)
- [Badger, white (PDF)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.pdf)
- [Badger, white (EPS)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.eps)
- [Badger, white (PNG, 2000x564)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-white.png)
- [Badger, colour (PNG, 1565x440)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-color.png)
- [Badger on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-on-light.png)
- [Badger on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/badger/logos/badger-badger-on-dark.png)
- [Snout by Badger, black (SVG)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.svg)
- [Snout by Badger, black (PDF)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.pdf)
- [Snout by Badger, black (EPS)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.eps)
- [Snout by Badger, black (PNG, 2000x630)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-black.png)
- [Snout by Badger, white (SVG)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.svg)
- [Snout by Badger, white (PDF)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.pdf)
- [Snout by Badger, white (EPS)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.eps)
- [Snout by Badger, white (PNG, 2000x630)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-white.png)
- [Snout by Badger, colour (PNG, 1245x393)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-color.png)
- [Snout by Badger on light (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-on-light.png)
- [Snout by Badger on dark (PNG, 2400x1350)](https://www.conf42.com/assets/brandkit/badger/logos/badger-snout-on-dark.png)

### Social

- [LinkedIn company page cover (PNG, 1512x256)](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-company-1512x256.png)
- [LinkedIn company page cover, sharp (6:1) (PNG, 4200x700)](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-company-hd-4200x700.png)
- [LinkedIn profile banner (PNG, 1584x396)](https://www.conf42.com/assets/brandkit/badger/social/badger-linkedin-profile-1584x396.png)
- [X (Twitter) header (PNG, 1500x500)](https://www.conf42.com/assets/brandkit/badger/social/badger-x-header-1500x500.png)
- [Bluesky banner (PNG, 3000x1000)](https://www.conf42.com/assets/brandkit/badger/social/badger-bluesky-banner-3000x1000.png)
- [Facebook cover (PNG, 1640x624)](https://www.conf42.com/assets/brandkit/badger/social/badger-facebook-cover-1640x624.png)
- [YouTube channel banner (PNG, 2560x1440)](https://www.conf42.com/assets/brandkit/badger/social/badger-youtube-banner-2560x1440.png)
- [Link preview (Open Graph) (PNG, 1200x630)](https://www.conf42.com/assets/brandkit/badger/social/badger-og-image-1200x630.png)
- [Zoom / Teams / Meet background (PNG, 1920x1080)](https://www.conf42.com/assets/brandkit/badger/social/badger-video-background-1920x1080.png)
- [Email signature banner (PNG, 1200x300)](https://www.conf42.com/assets/brandkit/badger/social/badger-email-signature-1200x300.png)

### Avatars

- [Avatar, square, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-square-1000.png)
- [Avatar, square, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-square-400.png)
- [Avatar, round, 1000 px (PNG, 1000x1000)](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-round-1000.png)
- [Avatar, round, 400 px (PNG, 400x400)](https://www.conf42.com/assets/brandkit/badger/avatars/badger-avatar-round-400.png)

### Stickers

- [Logo, original (WEBP, 1600x451)](https://www.conf42.com/assets/brandkit/badger/stickers/badger-sticker.webp)

### Colours

- [Palette (PNG, 2000x700)](https://www.conf42.com/assets/brandkit/badger/colours/badger-palette.png)
- [Palette, JSON (JSON)](https://www.conf42.com/assets/brandkit/badger/colours/badger-palette.json)
- [Palette, CSS variables (CSS)](https://www.conf42.com/assets/brandkit/badger/colours/badger-palette.css)
- [Palette, GIMP / Inkscape (GPL)](https://www.conf42.com/assets/brandkit/badger/colours/badger-palette.gpl)
- [Design tokens (W3C) (JSON)](https://www.conf42.com/assets/brandkit/badger/colours/badger-tokens.json)

### Press

- [About text (boilerplate) (TXT)](https://www.conf42.com/assets/brandkit/badger/badger-about.txt)
