# make_pages.py: writes the /mediakit/ template into every site (Marek 2026-11-09: "make the media kit look similar
# (button designs, liquid glass shards, etc.)"). One body (mk.css + mk.js), two wrappers:
#   sister sites (SREday, LLMday, PLATFORMday, PEC, DND): {% extends "_base.html" %}, the home page's ink-sweep glow +
#   .lg-glass cards + Bootstrap theme buttons, the brand band like Past events;
#   conf42.com: {% extends "base.html" %}, the event-page dark hero (ev-chip, ev-btn-glass) + Landkit cards and buttons.
# Each generate.py renders it through Jinja with mk_home = the site's brand key. Run: python3 brandkit/page/make_pages.py
import os
HERE = os.path.dirname(os.path.abspath(__file__)); GH = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CSS = open(os.path.join(HERE, 'mk.css')).read(); JS = open(os.path.join(HERE, 'mk.js')).read()
KIT = 'https://www.conf42.com/assets/brandkit/'

# per site: (glow accent, its rgb, the home page's four sweep colours) - copied from each home/_templates/index.html
GLOW = {'sreday': ('#713660', '113,54,96', '#713660 #098dcf #c46aa0 #5fb8e6'), 'llmday': ('#26986A', '38,152,106', '#26986A #098dcf #8fdc6a #2ec4b6'),
        'platformday': ('#E2971D', '226,151,29', '#E2971D #d0562b #f5c84c #415b78'), 'pec': ('#6b40d8', '107,64,216', '#6b40d8 #e8507a #f2a93b #2bb3c0'),
        'devopsnotdead': ('#2e9ad8', '46,154,216', '#2e9ad8 #098dcf #5fb8e6 #415b78'), 'conf42': ('#335eea', '51,94,234', '#335eea #7c69ef #42ba96 #7ea2d2')}
SITES = {'website': 'sreday', 'llmday': 'llmday', 'platformday': 'platformday', '2026.promptengineering.rocks': 'pec', 'devopsnotdead': 'devopsnotdead'}

def sweep(c):
    a, b, d, e = c.split()
    return ('linear-gradient(115deg, transparent 4%%, color-mix(in srgb, %s 38%%, transparent) 14%%, transparent 26%%),\n'
            '  linear-gradient(115deg, transparent 30%%, color-mix(in srgb, %s 34%%, transparent) 42%%, transparent 54%%),\n'
            '  linear-gradient(115deg, transparent 56%%, color-mix(in srgb, %s 40%%, transparent) 68%%, transparent 80%%),\n'
            '  linear-gradient(115deg, transparent 80%%, color-mix(in srgb, %s 30%%, transparent) 92%%, transparent 100%%)') % (a, b, d, e)
NOISE = """url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .55 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")"""
GLASS = """.lg-glass { position: relative; border-radius: 24px !important;
  background: linear-gradient(140deg, rgba(255,255,255,.62) 0%, rgba(255,255,255,.28) 45%, rgba(255,255,255,.42) 100%) !important;
  -webkit-backdrop-filter: blur(14px) saturate(160%); backdrop-filter: blur(14px) saturate(160%);
  border: 1px solid rgba(255,255,255,.7) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.95), inset 0 -1px 0 rgba(255,255,255,.25), 0 1px 2px rgba(20,28,37,.06), 0 12px 32px -8px rgba(var(--mk-accent-rgb),.22);
  transition: box-shadow .35s ease; }
.lg-glass::after { content: ""; position: absolute; inset: -1px; border-radius: inherit; pointer-events: none; padding: 1px; z-index: 2;
  background: linear-gradient(160deg, rgba(255,255,255,.95), rgba(255,255,255,0) 35%, rgba(var(--mk-accent-rgb),.35) 100%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude; }
.lg-glass:hover { box-shadow: inset 0 1px 0 rgba(255,255,255,.95), inset 0 -1px 0 rgba(255,255,255,.25), 0 2px 4px rgba(20,28,37,.06), 0 22px 48px -10px rgba(var(--mk-accent-rgb),.38); }"""
# shards lean up to 1 degree towards the cursor, like the home page's event cards (desktop mouse only, off for reduced motion)
TILT = """(function () {
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var on = null;
  document.addEventListener('pointermove', function (e) {
    var c = e.target.closest ? e.target.closest('#mk .mk-item, #mk .sw, #mk .bt') : null;
    if (on && on !== c) on.style.transform = '';
    on = c; if (!c) return;
    var r = c.getBoundingClientRect(), m = Math.min(3, Math.max(1, 600 / r.width));
    c.style.transform = 'perspective(900px) rotateX(' + (-((e.clientY - r.top) / r.height - .5) * m * 2).toFixed(2) + 'deg) rotateY(' + (((e.clientX - r.left) / r.width - .5) * m * 2).toFixed(2) + 'deg)';
  }, { passive: true });
})();"""

HEAD = """<meta name="description" content="Logos, colours, banners, profile pictures, mascots, animations and event artwork for Conf42, SREday, LLMday, PLATFORMday, Prompt Engineering Conference and friends.">
<link rel="alternate" type="application/json" href="%(kit)sbrandkit.json" title="Media kit index (JSON)">
<link rel="alternate" type="text/markdown" href="%(kit)sbrandkit.md" title="Media kit index (Markdown)">"""
SEARCH = """<label class="search"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
        <input id="q" type="search" placeholder="What do you need? Try: logo, white logo, LinkedIn banner, llama..." aria-label="Search the media kit" autocomplete="off"></label>
      <div class="tries"><span>Try:</span>%s</div>"""
TRIES = ['logo', 'white logo', 'LinkedIn banner', 'profile picture', 'mascots', 'colours', 'event splash', 'zoom background']
BODY = """  <div class="container mk-body">
    <h2 class="step">Pick a brand</h2>
    <div class="brands" id="brands"></div>
    <nav class="mk-nav" id="nav"></nav>
    <div id="out"></div>
    <p class="empty" id="none" hidden>Nothing found. Try a simpler word, like "logo" or "banner".</p>
  </div>
  <section class="mk-cli %(cli)s">
    <div class="glow-bg"></div>
    <div class="container">
      <h3 class="section-heading text-center mb-3">For developers &amp; AI agents</h3>
      <p class="intro">Every file has a fixed URL. The index lists them all with size, pixels, SHA-256 and type, so scripts, CI jobs and AI agents can fetch exactly what they need.</p>
      <div class="cmds">
        <div class="cmd"><span>Index (JSON)</span><code data-k="json"></code><button class="copy" type="button">copy</button></div>
        <div class="cmd"><span>Index (Markdown)</span><code data-k="md"></code><button class="copy" type="button">copy</button></div>
        <div class="cmd"><span>For LLMs</span><code data-k="llms"></code><button class="copy" type="button">copy</button></div>
        <div class="cmd"><span>One logo</span><code data-k="one"></code><button class="copy" type="button">copy</button></div>
        <div class="cmd"><span>A whole brand</span><code data-k="brand"></code><button class="copy" type="button">copy</button></div>
        <div class="cmd"><span>Every white SVG logo</span><code data-k="white"></code><button class="copy" type="button">copy</button></div>
        <div class="cmd"><span>Brand colours</span><code data-k="colors"></code><button class="copy" type="button">copy</button></div>
      </div>
    </div>
  </section>
  <div class="mk-toast" id="toast"></div>
</div>
<script>window.MK = %(mk)s;</script>
<script>
{%% raw %%}
%(js)s
%(tilt)s
{%% endraw %%}
</script>"""
NOTE = '{# /mediakit/ (Marek 2026-11-09): the whole family\'s media kit, the same page on every site with that site\'s brand first (mk_home);\n   every file and the index live on conf42.com/assets/brandkit/. GENERATED by conf42/brandkit/page/make_pages.py: edit there, not here. #}\n'

def sister(key):
    acc, rgb, sw = GLOW[key]; tries = ''.join('<button type="button" class="mk-chip">%s</button>' % t for t in TRIES)
    css = """#home.hero-block, .stats-block { display: none !important; }   /* like /ambassadorship/: no inherited hero or stats bar */
#mk { --mk-accent: %(acc)s; --mk-accent-rgb: %(rgb)s; position: relative; isolation: isolate; background: #f0f6fa; clip-path: inset(0); }
#mk > .glow-bg { position: fixed; inset: 0; z-index: -1; pointer-events: none; opacity: .55; background:
  %(sweep)s; }
#mk .glow-bg::after { content: ""; position: absolute; inset: 0; opacity: .12; background-image: %(noise)s; }
#mk .mk-cli { background: %(acc)s; }   /* the brand band, like Past events on the home page */
#mk .mk-cli > .glow-bg { position: absolute; inset: 0; z-index: 0; opacity: .35; pointer-events: none; background: linear-gradient(115deg, transparent 20%%, rgba(255,255,255,.25) 45%%, transparent 70%%); }
#mk .mk-cli > .container { position: relative; z-index: 1; }
#mk .mk-chip { border: 1px solid rgba(255,255,255,.9); background: rgba(255,255,255,.6); -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px); color: #2a3644;
  border-radius: 999px; padding: 6px 13px; font-weight: 700; font-size: .85rem; cursor: pointer; box-shadow: inset 0 1px 0 #fff, 0 6px 16px -8px rgba(var(--mk-accent-rgb),.35); transition: background .2s, color .2s; }
#mk .mk-chip:hover { background: #fff; color: var(--mk-accent); }
#mk .btn-sm { font-size: .85rem; padding: .4rem .8rem; }
%(glass)s
""" % dict(acc=acc, rgb=rgb, sweep=sweep(sw), noise=NOISE, glass=GLASS)
    mk = '{"main": "btn btn-primary", "alt": "btn btn-secondary", "item": "lg-glass"}'   # the hero's CFP + Sponsor pair (the theme's .btn has no border, so no outline buttons)
    return (NOTE + '{% extends "_base.html" %}\n\n{% block head_extra %}\n' + HEAD % dict(kit=KIT) + '\n<style>\n' + css + CSS + '</style>\n{% endblock %}\n\n{% block content %}\n'
            + '<div id="mk" data-kit="%s" data-home="{{ mk_home }}">\n  <div class="glow-bg"></div>\n  <section class="mk-hero">\n    <div class="container">\n'
              '      <div class="mk-eyebrow">Conf42 family</div>\n      <h1 class="section-heading">Media kit</h1>\n'
              '      <p class="mk-lead">Logos, colours, banners, profile pictures, mascots and event artwork for all our brands. Pick a brand, find what you need, click PNG or SVG.</p>\n      ' % KIT
            + SEARCH % tries + '\n    </div>\n  </section>\n' + BODY % dict(cli='', mk=mk, js=JS, tilt=TILT) + '\n{% endblock %}\n')

def conf42():
    acc, rgb, sw = GLOW['conf42']; tries = ''.join('<button type="button" class="btn btn-sm ev-btn ev-btn-glass">%s</button>' % t for t in TRIES)
    css = """#mk { --mk-accent: %(acc)s; --mk-accent-rgb: %(rgb)s; background: #f9fbfd; }
#mk .mk-hero { color: #fff; overflow: hidden; isolation: isolate; background: linear-gradient(160deg, #161c2d 0%%, #1b2a4e 60%%, #22357a 100%%); padding-bottom: 56px; margin-bottom: 30px; }
#mk .mk-hero > .glow-bg, #mk .mk-cli > .glow-bg { position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: .75; background:
  %(sweep)s; }
#mk .mk-hero h1 { font-family: "Plus Jakarta Sans", sans-serif; color: #fff; text-shadow: 0 2px 18px rgba(0,0,0,.12); }
#mk .mk-hero .search input { background: rgba(255,255,255,.94); }
#mk .mk-hero .tries .btn { border-radius: .7rem; font-weight: 600; padding: .35rem .8rem; }
#mk .mk-cli { background: #161c2d; isolation: isolate; }
#mk .mk-item, #mk .sw, #mk .bt, #mk .bhead, #mk .about { border-radius: 1rem !important; border: 0; }
#mk .bhead, #mk .about { flex-direction: row; }
#mk .bhead { position: relative; }
#mk .mk-nav { background: rgba(255,255,255,.86); }
#mk .lift:hover { transform: translate3d(0, -3px, 0); }
""" % dict(acc=acc, rgb=rgb, sweep=sweep(sw))
    mk = '{"main": "btn btn-primary shadow lift", "alt": "btn btn-primary-soft", "item": "card shadow-light-lg lift"}'
    tilt = ''   # Landkit cards lift on hover instead of tilting
    return (NOTE + '{% extends "base.html" %}\n\n{% block head %}\n' + HEAD % dict(kit=KIT) + '\n<style>\n' + css + CSS + '</style>\n{% endblock %}\n\n{% block content %}\n'
            + '<div id="mk" data-kit="%s" data-home="{{ mk_home }}">\n  <section class="mk-hero">\n    <div class="glow-bg"></div>\n    <div class="container">\n'
              '      <div class="ev-eyebrow"><span class="ev-chip">Conf42 family</span><span class="ev-chip">9 brands</span><span class="ev-chip">PNG · SVG · ZIP</span></div>\n'
              '      <h1>Media kit</h1>\n      <p class="mk-lead">Logos, colours, banners, profile pictures, mascots and event artwork for all our brands. Pick a brand, find what you need, click PNG or SVG.</p>\n      ' % KIT
            + SEARCH % tries + '\n    </div>\n  </section>\n' + BODY % dict(cli='', mk=mk, js=JS, tilt=tilt) + '\n{% endblock %}\n')

open(os.path.join(GH, 'conf42', '_templates', 'mediakit.html'), 'w').write(conf42()); print('conf42')
for repo, key in SITES.items():
    t = sister(key)
    if key == 'devopsnotdead':   # DND's _base.html has no head_extra block: the head bits open the content block instead
        h0 = t.index('{% block head_extra %}\n'); h1 = t.index('{% endblock %}\n\n{% block content %}\n')
        t = t[:h0] + '{% block content %}\n' + t[h0 + len('{% block head_extra %}\n'):h1] + t[h1 + len('{% endblock %}\n\n{% block content %}\n'):]
    open(os.path.join(GH, repo, 'home', '_templates', 'mediakit.html'), 'w').write(t); print(repo, key)
