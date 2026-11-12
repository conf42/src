# Seven browser APIs that let a web app act like a native one

Conf42 Blog, 2021-10-27. https://www.conf42.com/blog/js2021/browser-apis-close-native-gap

In short: Francesco Leardini (Trivadis) at Conf42 JavaScript 2021 on browser APIs from Screen Wake Lock to Contact Picker that close the gap with native apps

A recipe site whose screen goes dark while your hands are covered in dough is a solved problem, and most web apps still have it. At Conf42 JavaScript 2021, [Francesco Leardini](https://www.conf42.com/JavaScript_2021_Francesco_Leardini_browser_web_APIs), Senior Consultant and Angular Trainer at Trivadis, demos seven browser APIs that give web apps capabilities that used to belong to native apps, each one with a live demo, often on his phone, and the code behind it.

The demo app is built with Angular and Angular Material, but every API he shows is framework agnostic: React, Vue.js or plain JavaScript work the same. The code is on GitHub with comments throughout, and each demo page carries a browser compatibility section, which matters for the experimental ones.

He opens with the SpaceX Dragon 2 console, whose touch screens run on Chromium and JavaScript. Francesco Leardini said at Conf42 JavaScript 2021: "or at least I would not try it with Internet Explorer eleven".

## Which ones work everywhere today?

**Page Visibility** is the old, widely supported one. Listen for the visibilitychange event, check document.hidden, and react: pause a video when the tab loses focus and resume from the same second, stop a product carousel, or stop polling the server while nobody is looking, which saves traffic for mobile users.

**Web Share** hands a title, text and URL to the device's native share sheet, so the user can pick WhatsApp, email or anything else installed. Only one of the three fields is required, but he recommends setting all of them, because you do not know which app the user will choose: an email client uses the title as the subject, a chat app ignores it. Chrome had recently added it on desktop too, and a second level of the API shares files such as images.

**Vibration** takes an array of alternating vibrate and pause durations in milliseconds, so any pattern is possible. His quiz demo buzzes three short times for a right answer and once, long, for a wrong one. It needs hardware that can vibrate, so a laptop will not.

## Which ones are newer but worth it?

**Screen Wake Lock** is his favourite and the recipe demo above. It needs a secure connection and a user gesture to request a sentinel with the screen type, the only value left after system was removed. The lock is released when the page loses focus, so his demo adds a second checkbox that requests it again automatically when the user comes back. Release it when the component is destroyed.

**File System Access** offers showOpenFilePicker and showSaveFilePicker, and returns a file handle. Keep the handle and every later save writes straight to the same file on disk, no dialog and no download, which makes autosave possible. Chrome shows an icon in the address bar when the page has read or write permission.

## And the experimental ones?

**Ambient Light Sensor** is part of the Sensor APIs and needed a Chrome flag at the time. His demo reads the illuminance value and switches the whole interface to dark mode below a threshold, the way a native maps app does at night; roughly 10 to 50 counts as a dark room in his example. Check for support first and either explain, fall back, or skip the feature silently.

**Contact Picker** lets the user pick contacts and share name, email, phone, address and icon with the page. Because the data is sensitive it requires HTTPS and a user gesture, and at the time it worked mainly in Chrome for Android, the Android browser and Opera Mobile. Design the UI for missing fields, since not every contact has all of them.

## Who should watch?

Front-end developers building progressive web apps or mobile-first sites who want to see what the platform already does before they reach for a native wrapper. The talk is demo-heavy and short on theory, and the repository is the real takeaway; check current browser support before shipping the experimental APIs.

## Related Conf42 talks

- Michael Solati on [building a progressive web app](https://www.conf42.com/JavaScript_2020_Michael_Solati_progressive_web_app) at Conf42 JavaScript 2020.
- Francesco Sciuti on [browsers made by others](https://www.conf42.com/JavaScript_2023_Francesco_Sciuti_browsers_made_by_others) at Conf42 JavaScript 2023.
- Mohamad Shiralizadeh on [built-in AI in browsers](https://www.conf42.com/JavaScript_2024_Mohamad_Shiralizadeh_40_aibrowsers_builtin_future) at Conf42 JavaScript 2024.

[Watch Francesco Leardini's talk](https://www.conf42.com/JavaScript_2021_Francesco_Leardini_browser_web_APIs), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Trivadis

Trivadis is an IT consultancy based in Switzerland, covering a wide range of technologies; Francesco Leardini works there as a senior consultant and Angular trainer.

- [Trivadis website](https://www.trivadis.com/en/index.html)

[Watch the talk on YouTube](https://youtu.be/3iVnmIBWCIo).

## Watch the talk

[Wait...can my browser do that?](https://www.conf42.com/JavaScript_2021_Francesco_Leardini_browser_web_APIs) at Conf42 JavaScript 2021.
