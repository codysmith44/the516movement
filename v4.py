# ---- v4: v2 design minus specific tells (content) ----
import re as _re
_EB = _re.compile(r'<!-- wp:paragraph \{"className":"eyebrow[^"]*"\} --><p class="eyebrow[^"]*">.*?</p><!-- /wp:paragraph -->')
def noeb(s): return _EB.sub('', s)
def squote(t,c,cls='scripture'): return f'<!-- wp:quote {{"className":"{cls}"}} --><blockquote class="wp-block-quote {cls}"><!-- wp:paragraph --><p>{t}</p><!-- /wp:paragraph --><cite>{c}</cite></blockquote><!-- /wp:quote -->'
MATT='In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.'
hero = noeb(hero).replace('<!-- wp:group {"className":"hero-stats"', squote(MATT,'Matthew 5:16','scripture hero-verse')+'<!-- wp:group {"className":"hero-stats"',1)
trio = noeb(trio)
ryan = noeb(ryan).replace('<!-- wp:quote {"className":"pull"}', hc('section-title is-light','Meet Ryan Young')+'<!-- wp:quote {"className":"pull"}',1)
collage = noeb(collage)
answer = noeb(answer).replace('<!-- wp:buttons', squote('I am the way, the truth, and the life. No one comes to the Father except through me.','John 14:6','scripture is-centered')+'<!-- wp:buttons',1)
cta = noeb(cta)
home = hero+statement+trio+ryan+collage+answer+cta
