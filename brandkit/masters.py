# brand kit masters (Marek 2026-11-09): the best local originals, found by the inventory of Dropbox + repos
DB = '/Users/marek/Library/CloudStorage/Dropbox'
GH = '/Users/marek/Documents/GitHub'
# mono: which logos get one-colour variants (flat marks only), and how ink is found:
#   'alpha'  - every opaque pixel is ink;  'alpha-light' - opaque AND not near-white (white details become holes)
LOGOS = {
 'conf42':      dict(src=GH + '/conf42/docs/assets/brandkit/conf42/logos/conf42-wordmark-black.png', mono='alpha', label='Wordmark'),
 'conf42-mark': dict(src=DB + '/Conf42/_OVERLAYS/C42_MINI_WHITE.png', mono='alpha', label='Mark (42)'),
 'sreday':      dict(src=DB + '/_misc/sreday square.png', mono='alpha', label='Logo'),
 'llmday':      dict(src=DB + '/_misc/LLMDAY LOGO.png', mono='alpha', label='Logo'),
 'platformday': dict(src=DB + '/_misc/PLATFORMday LOGO.png', mono='alpha', label='Logo'),
 'pec':         dict(src=DB + '/_misc/PEC logo.png', mono='alpha-light', label='Logo'),
 'certifiedfyi':dict(src=DB + '/_misc/certified fyi.png', mono='alpha-light', label='Logo'),
 'badger':      dict(src=GH + '/badger/snout/assets/badger-logo.webp', mono='alpha', label='Logo'),
 'snout':       dict(src=GH + '/badger/snout/assets/snout-logo.png', mono='alpha', label='Logo'),
 'dnd':         dict(src=GH + '/website/home/assets/sister dnd.png', mono=None, label='Logo'),
 'cfpninja':    dict(src=DB + '/_misc/cfpninja bigga logo.png', mono=None, label='Logo'),
 'cfpninja-mark': dict(src=DB + '/_misc/cfpninja MINI.png', mono='alpha-light', label='Mark'),
}
