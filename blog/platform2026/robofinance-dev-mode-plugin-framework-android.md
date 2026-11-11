# The smallest internal platform: a plugin-based Dev Mode for Android

Conf42 Blog, 2026-10-19, updated 2026-11-09. https://www.conf42.com/blog/platform2026/robofinance-dev-mode-plugin-framework-android

In short: Denis Galkin (Robofinance) at Conf42 Platform Engineering 2026 on turning scattered debug menus into a plugin-based Dev Mode framework inside the app.

Every mobile app grows a hidden button on the profile screen, a debug menu in settings and a secret gesture somewhere else. At Conf42 Platform Engineering 2026, Denis Galkin, Android engineer at Robofinance, showed how his team treated those internal tools as a platform product from the start: a plugin-based Dev Mode framework where the framework owns the shell and the app owns every tool inside it.

It's a platform talk at the scale of one binary, and the lessons travel well beyond Android.

## Split the shell from the content

The classic platform problem, Denis argues, happens inside one app too: people build the same thing many times, differently, and nobody owns the result. Developers redo navigation for each new tool, QA has to remember where every tool lives (or interrupt a developer), and each app ends up with its own debug menu.

Dev Mode's core idea is a hard split. The framework owns activation, the Dev Mode screen, the list of tools and navigation between them. The app owns which tools exist, their screens, view models, repositories and settings. The framework has no idea what *mock date* or *test push* means; to it, every tool is a name and a screen. Denis compares it to Backstage: a small core with everything useful in plugins.

Why bother? Because the two halves change at different speeds. The shell almost never changes once it works; the content changes every sprint. Keep them apart and the shared code stays quiet.

## No `when` statement in the framework

The walkthrough is concrete. Activation is one line in the app: `initDevModeListener` on a View, or a `Modifier.devModeClickable` in Jetpack Compose. A Dev Mode Runner inside the framework counts taps (five by default, with a timer that resets the count) and opens Dev Mode Activity.

That activity depends on one interface, `IDevModePluginEntriesProvider`, whose single method returns entries for Navigation 3, Google's new navigation library. The app implements it, registering screens like `TestPushesDevPluginScreen` and `MockDatePluginScreen`. A second small interface supplies the menu: an index, a title and a screen key per plugin. The router takes a key and navigates. Denis's favourite detail: there's no Kotlin `when` anywhere in the framework deciding which tool to open. The framework builds the route; the app decides where it leads.

Adding a tool (say, a feature flag switcher) is four steps, all inside the app: screen plus view model, navigation key, registration, menu item. The framework isn't touched. In his phrasing, the cost of a new tool should be the cost of the tool, not the platform around it.

## Adopted without a migration

The adoption story is the part platform teams should study. Nobody was told to use Dev Mode, and there was no migration. Denis gives three reasons. Timing: the framework arrived before ad-hoc tools spread, so there was nothing to move and no owners to persuade. The easy way was the right way: registering a plugin beats building your own debug screen. And ownership follows the feature: whoever builds a feature builds its test plugin in the same task.

Users turned out to be broader than *dev* suggests. QA sets up dates and pushes without a special build; managers check app behaviour on their own. With weekly releases, that's everyday work, not an edge case.

## What he'd do differently

Two honest regrets. Measure from day one (time to prepare a test scenario, how often QA needs a developer), because preventing a problem leaves you no *before* chart to show anyone. And name an owner for the core before plugin screens drift apart and dead tools pile up in the list. For small or short-lived apps he'd skip the full framework but keep one rule: a single entry point for all internal tools.

## Who should watch

Mobile leads with more than one debug menu, and platform engineers who want a clean, small example of a golden path that people choose without being told. If you think platform engineering only means Kubernetes, this is a good corrective.

## Related Conf42 talks

- [Development, Customization, and Maintenance of White-Label Android Applications](https://www.conf42.com/Chaos_Engineering_2025_Dmitrii_Nikitin_development_maintenance_applications) by Dmitrii Nikitin (Quadcode)
- [Modularizing a 10-Year Monolith: The Architecture, The People, and the Pain](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith) by Victor Lyuboslavsky (Fleet Device Management)
- [Engineering Reliable Mobile Applications](https://www.conf42.com/Site_Reliability_Engineering_2021_Pranjal_Deo_reliable_mobile_applications) by Pranjal Deo (Google)

[Watch Denis's talk](https://www.conf42.com/Platform_Engineering_2026_Denis_Galkin_mobile_plugin_framework)

[Watch the talk on YouTube](https://youtu.be/pptgG5RPpgg).

## Watch the talk

[Building an Internal Mobile Platform: A Plugin-Based Dev Mode Framework](https://www.conf42.com/Platform_Engineering_2026_Denis_Galkin_mobile_plugin_framework) at Conf42 Platform Engineering 2026.
