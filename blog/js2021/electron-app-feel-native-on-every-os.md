# Your Electron app feels off because of eight small details

Conf42 Blog, 2021-10-27. https://www.conf42.com/blog/js2021/electron-app-feel-native-on-every-os

In short: Kilian Valkhof (Polypane) at Conf42 JavaScript 2021 on the eight details that make an Electron app feel native on Windows, macOS and Linux.

An Electron app rarely feels wrong because of its big design decisions. It feels wrong because the window flashes white on launch, the app quits when you close it on a Mac, or Cmd+A highlights the toolbar. At [Conf42 JavaScript 2021](https://www.conf42.com/js2021), Kilian Valkhof of Polypane, a member of the Electron governance team, walked through eight such details and the code that fixes each one. The takeaway: you don't need native widgets or a redesign, you need to respect the platform's habits.

## Why doesn't a custom UI doom an Electron app?

His starting point is that users have become tolerant of custom interfaces, thanks to web apps and mobile. Gmail as a Mac app would have been dismissed, he argues, while Superhuman shipped a very custom interface 13 years later and did fine. Slack's fully custom UI is even a plus: it is the same on every platform, so it is easier to learn. What makes or breaks the app is whether that custom UI also adopts each operating system's customs. Kilian has shipped dozens of Electron apps after earlier attempts with Qt and GTK, which were cross-platform in theory but too opaque to build and package in practice.

## Launch like an app, not a web page

A web page loads in public: white screen, things popping in. An app appears fully formed after the dock icon bounces. Electron does the former by default, so flip it: create the BrowserWindow with show set to false, wait for the ready-to-show event, then show and focus the window. Also set a background color on the window that matches your app instead of the default white. If loading is slow, show a skeleton screen early; the wait may be the same, but it feels shorter.

## Closing is a platform question

On Windows and Linux the window is the app; close it and the app quits. On macOS the window is an instance of the app, which stays alive in the dock. So check for darwin before quitting when all windows close, move window creation into a function, and recreate the window on the activate event when the dock icon is clicked.

## Remember what the user told you

Desktop apps have meta preferences the web never needed: window size, position, which monitor, whether it was maximized. The trap is the maximized state: save that it was maximized, but not the maximized geometry, because native apps restore to the user's last size. And you can only maximize a window after it is shown. The electron-window-state package handles this, including a window last seen on a monitor that is no longer connected; electron-settings works for storing your own values. The same courtesy applies to file dialogs: store the last folder after a successful save or open, never after a cancel.

## Menus, selection and context menus

Older Electron versions shipped no default application menu, which on macOS meant no cut, copy and paste. Kilian found out the hard way. "Guess who found that out after shipping a note taking app?" Kilian Valkhof said at Conf42 JavaScript 2021. Electron now provides a default, but it is Mac-centric, so he wrote electron-create-menu, which builds platform-appropriate menus from one structure with per-item platform flags.

Two CSS and event details follow. Put user-select none on the body so Select All doesn't highlight your buttons; Chromium keeps inputs selectable. And build a context menu from Electron's context-menu event, which tells you whether the target is editable, a link, selected text, an image or a video; electron-context-menu covers the basics.

## Shortcuts, fonts and the memory question

Write CmdOrCtrl in accelerators and Electron picks Command on macOS and Control elsewhere. For type, the CSS system-ui keyword gives Segoe UI on Windows, San Francisco on Mac and Ubuntu's font on Ubuntu, where long GitHub-style font stacks miss the Linux fonts. If you use a custom font, ship it with the app.

On memory he is unapologetic: about 100 MB of base memory is not far from other GUI-heavy apps. The real risk is leaks, because an app lives far longer than a web page. Record a performance profile in Chromium DevTools with memory checked; if memory and listener counts only go up, a listener isn't being cleared. For the Node side, start Electron with the inspect flag and attach from chrome://inspect.

## Who should watch

Anyone shipping an Electron app, or porting a web app to one. It is a practical checklist with code, about 20 minutes, and each item is a small fix. Pair it with:

- [Julian Jandl on JavaScript heap memory leaks](https://www.conf42.com/JavaScript_2023_Julian_Jandl_js_heap_memory_leaks) at Conf42 JavaScript 2023.
- [Kilian Valkhof on moving features from JavaScript to CSS and HTML](https://www.conf42.com/JavaScript_2023_Kilian_Valkhof_moving_features_css_html) at Conf42 JavaScript 2023.
- [Martin Alvarez-Espinar on Quick Apps](https://www.conf42.com/JavaScript_2021_Martin_AlvarezEspinar_Quick_Apps_frictionless_UX) at Conf42 JavaScript 2021.

[Watch Kilian Valkhof's talk](https://www.conf42.com/JavaScript_2021_Kilian_Valkhof_Electron_App) from Conf42 JavaScript 2021.

## From Polypane

Polypane is the company behind this talk; its speaker builds desktop software with Electron.

- [Polypane website](https://polypane.app)

[Watch the talk on YouTube](https://youtu.be/p4PyzDzppiY).

## Watch the talk

[Make Your Electron App Feel at Home Everywhere](https://www.conf42.com/JavaScript_2021_Kilian_Valkhof_Electron_App) at Conf42 JavaScript 2021.
