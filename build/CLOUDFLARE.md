# Cloudflare settings (dashboard, not in git)

The site is GitHub Pages behind Cloudflare. These rules make pages fast on venue
wifi **without ever serving an old schedule**. Set them once per zone
(conf42.com) under the zone's **Rules**.

## 1. HTML: always check for the latest version
*Rules → Transform Rules → Modify Response Header → Create rule*
- When: `(not http.request.uri.path contains ".") or ends_with(http.request.uri.path, ".html")`
- Then: **Set static** `Cache-Control` = `no-cache`

Browsers then always ask before reusing a page (an unchanged page costs a ~300-byte
`304`). Today GitHub sends `max-age=600`, so a browser can show a schedule up to
10 minutes old.

## 2. Versioned assets: cache for a year
The `asset` filter in `build/generate.py` adds `?v=<content hash>` to local CSS and JS URLs, so a changed file always gets a new URL and these can be cached forever.

*Rules → Cache Rules → Create rule*
- When: `http.request.uri.query contains "v="`
- Then: Eligible for cache. Edge TTL: 1 month. Browser TTL: **override, 1 year**.

*Transform Rules → Modify Response Header* (same condition):
- **Set static** `Cache-Control` = `public, max-age=31536000, immutable`

## 3. Leave alone
- Don't cache HTML at the edge (no "Cache Everything" on pages): schedules change at
  the last minute.
- No service worker.

## Check
```sh
curl -sI https://www.conf42.com/devsecops2026 | grep -i cache-control      # no-cache
curl -sI "https://www.conf42.com/assets/css/theme.bundle.css?v=x" | grep -i cache-control   # max-age=31536000, immutable
```

## Not covered here
Headshots, podcast covers and slides come from conf42.github.io/static (GitHub Pages, no
Cloudflare): those use `.webp` files made by `make_webp.py` in the static repo.
