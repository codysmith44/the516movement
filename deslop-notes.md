# De-slop checklist: common "AI / template" design tells and how to fix them

Use this as a review pass on any generated or templated site. The aim is restraint: the content and photos should carry the page, not decoration.

## Typography
| Tell | Fix |
|---|---|
| ALL CAPS headings, nav, buttons | Sentence case everywhere. Reserve caps for real acronyms. |
| Small, letter-spaced uppercase "eyebrow" labels above headings (often with a short colored rule) | Delete them. If context is needed, say it in the heading or the first sentence. |
| Condensed grotesk display fonts (Oswald, Bebas, Anton) used to look "bold" | Choose a typeface that fits the voice: a literary serif for headings (Newsreader, Source Serif, Literata) and a humanist sans for text (Source Sans, Fira Sans). |
| An italic serif "accent word" in a sans headline | Italics only where the language needs emphasis, or within the same family. |
| Huge display type at 0.85 line-height everywhere | One large moment at most. Normal leading (1.05–1.2 for headings) and a clear but modest scale. |
| Over-tracked or negatively tracked text | Default tracking; use optical sizing (`font-optical-sizing:auto`) where the font supports it. |
| Widows or ragged headlines | `text-wrap: balance` on headings, `pretty` on paragraphs. |

## Layout and components
| Tell | Fix |
|---|---|
| Three cards in a row with a colored top border, rounded corners and a tinted fill | Plain text columns separated by whitespace or a single hairline. |
| Everything in a card or box | Use boxes only when they mean something (a form, a callout). |
| Outlined or giant numerals (01 / 02 / 03) | Drop the numbers unless the order matters. |
| A "stats strip" of big numbers with tiny captions | Put the facts in a sentence. |
| Offset or outline frames behind photos, overlapping "polaroid" insets | Show the photo plainly, at a good crop and size. |
| Masonry or staggered collages | A simple, even grid with honest captions. |
| A centered hero over a darkened full-bleed photo | Text beside the photo, or the photo shown un-darkened. |
| Alternating dark/light bands on every section | Two or three background tones total; let whitespace separate sections. |
| A "statement band" in the accent color with a huge watermark number | A plain section in the brand color, with a clear heading and one action. |
| Footer with an oversized slogan | Logo, contact, links, legal. |

## Decoration and effects
| Tell | Fix |
|---|---|
| Glow blobs, radial "light" gradients, mesh gradients | Flat brand colors. |
| Grain or noise overlays | Remove them. Real photography provides texture. |
| Duotone or grayscale-plus-blend photo treatments by default | Show photos as they are; adjust only where it helps. |
| Watermark text or giant faded numerals | Remove. |
| Gradient text, glassmorphism (blur) headers | A solid header. |
| Accent color sprinkled on rules, bullets, quote marks and buttons | Use the accent once or twice per page, where it signals something. |

## Motion and interaction
| Tell | Fix |
|---|---|
| Every section fades or slides in on scroll | No scroll animation, or one subtle one. Always respect `prefers-reduced-motion`. |
| Buttons that lift, glow and slide an arrow on hover | Change color or underline on hover; that's enough. |
| Pill-shaped buttons with tracked caps and arrows | Small radius (2–4px), sentence case, plain label. |
| Animated nav underlines | A static underline for hover and the current page. |

## Content
| Tell | Fix |
|---|---|
| Labels instead of language (e.g. a verse reference as a tag) | Quote the source text properly: set it as a quotation with a plain citation ("— Book 1:1"). |
| Made-up taglines and punchy fragments | Use the client's real words; edit them lightly. |
| Generic CTAs ("Learn more →") repeated everywhere | Specific links ("More about Ryan", "Read our values"). |
| Placeholder forms styled to look finished | Mark them clearly and keep them simple. |

## Review routine
1. Take full-page screenshots at about 1440px and 390px wide.
2. Squint test: is the hierarchy clear without the decoration?
3. Search the CSS for `uppercase`, `letter-spacing`, `gradient`, `blur`, `box-shadow`, `transform`, `::before`/`::after` decorations and `animation`, and justify each one.
4. Check alignment: every block's left edge should line up with the logo or the text column. Beware `margin:0` overriding the auto-centering margins of constrained layouts.
5. Check text contrast against WCAG AA and visible focus outlines on every interactive element.
6. Repeat until nothing reads as a template.
