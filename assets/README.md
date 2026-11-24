# README assets

The profile README serves these images from the repo instead of third-party icon services, so they stay current.

- `icons/` has one 256×256 tile per skill, in the skillicons.dev dark style (rounded 60px corners).
- `skills/` has the six "Tech Stack" rows. Each row is built from `icons/` by `python3 scripts/build-skill-rows.py`. To add, remove or reorder an icon, change `ROWS` in that script and run it again.
- `badges/` has the source marks that are base64-embedded in the shields.io badges at the top of the README.

## Where the logos come from

The tiles below were rebuilt from each brand's own files (checked 2026-11-24):

| Tile / badge | Official source |
|---|---|
| `apple` | apple.com global-nav mark (monochrome, white on dark tile) |
| `androidstudio` | developer.android.com/static/studio/images/android-studio-stable.svg |
| `nodejs` | nodejs.org/static/logos/jsIconGreen.svg (#5FA04E) |
| `ts` | typescriptlang.org/branding/typescript-design-assets.zip, `ts-logo-128.svg` (#3178C6) |
| `jquery` | brand.jquery.org/resources/jquery-foundation-logos-eps.zip, mark in white on jQuery Primary Blue #0769AD |
| `figma` | static.figma.com/app/icon/2/favicon.svg (#FF3737 #FF7237 #874FFF #00B6FF #24CB71) |
| `mongodb` | mongodb.com/brand-resources logo-marks SVG (Spring Green #00ED64 on Slate #001E2B) |
| `redis` | redis.io/icon.png (the current site icon) |
| `firebase` | firebase.google.com/brand-guidelines, firebase-brand-assets.zip, `Logomark_Full Color.svg` |
| `googlecloud` | gstatic.com/cgc/super_cloud_gradient.png (the gradient cloud on cloud.google.com) |
| `docker` | docker.com/app/uploads/brand/logo/docker-mark-ether.svg on Docker blue #6172FF, as in Docker's own favicon (2026-11-19 rebrand) |
| `idea` | resources.jetbrains.com/storage/logos/web/intellij-idea/intellij-idea.svg |
| `badges/linkedin-inbug-white.png` | brand.linkedin.com/downloads, `in-logo.zip`, `InBug-White.png` (trimmed, 64px high) |
| `badges/stackoverflow-symbol-white.svg` | stackoverflow.design/docs/public/brand/logo/symbol.svg (2025 identity), recoloured white |

All other tiles are copied unchanged from [skillicons.dev](https://github.com/tandpfun/skill-icons) (MIT). All logos are trademarks of their owners.
