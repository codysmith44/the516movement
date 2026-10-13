# ---- v2 art direction: system (exec'd after theme files written) ----
shutil.copy('node_modules/@fontsource-variable/fraunces/files/fraunces-latin-wght-italic.woff2', T/'assets/fonts/fraunces-latin-wght-italic.woff2')
shutil.copy('node_modules/@fontsource-variable/fraunces/LICENSE', T/'assets/fonts/FRAUNCES-OFL.txt')
theme['settings']['color']['palette']=[
 {"slug":"primary","name":"M516 Blue","color":"#0f75bc"},{"slug":"navy","name":"Navy","color":"#0b3e63"},
 {"slug":"night","name":"Night","color":"#05121f"},{"slug":"accent","name":"Red","color":"#c3272f"},
 {"slug":"glow","name":"Glow","color":"#f4b860"},{"slug":"ink","name":"Ink","color":"#14202b"},
 {"slug":"muted","name":"Slate","color":"#4a545a"},{"slug":"paper","name":"Paper","color":"#f6f2ea"},
 {"slug":"light","name":"Light","color":"#ece6da"},{"slug":"base","name":"White","color":"#ffffff"}]
theme['settings']['color']['gradients']=[{"slug":"night-glow","name":"Night glow","gradient":"radial-gradient(120% 80% at 80% 0%, rgba(244,184,96,.35) 0%, rgba(11,62,99,0) 45%), linear-gradient(180deg,#0b3e63 0%,#05121f 100%)"}]
theme['settings']['typography']['fontFamilies'].append({"slug":"accent","name":"Fraunces Italic","fontFamily":"Fraunces, Georgia, serif","fontFace":[{"fontFamily":"Fraunces","fontWeight":"300 900","fontStyle":"italic","fontDisplay":"swap","src":["file:./assets/fonts/fraunces-latin-wght-italic.woff2"]}]})
theme['settings']['typography']['fontSizes']=[
 {"slug":"small","name":"Small","size":"0.875rem"},{"slug":"medium","name":"Body","size":"1.0625rem","fluid":{"min":"1rem","max":"1.125rem"}},
 {"slug":"large","name":"Large","size":"1.5rem","fluid":{"min":"1.25rem","max":"1.5rem"}},
 {"slug":"x-large","name":"XL","size":"2.75rem","fluid":{"min":"2rem","max":"2.75rem"}},
 {"slug":"xx-large","name":"XXL","size":"4.5rem","fluid":{"min":"2.75rem","max":"4.5rem"}},
 {"slug":"huge","name":"Display","size":"8.5rem","fluid":{"min":"3.4rem","max":"8.5rem"}}]
theme['settings']['spacing']['spacingSizes']=[{"slug":s,"name":n,"size":v} for s,n,v in [("20","2XS","0.5rem"),("30","XS","1rem"),("40","S","1.5rem"),("50","M","clamp(2rem,4vw,3rem)"),("60","L","clamp(3rem,6vw,5rem)"),("70","XL","clamp(4.5rem,9vw,8rem)"),("80","2XL","clamp(6rem,12vw,11rem)")]]
theme['settings']['layout']={"contentSize":"720px","wideSize":"1280px"}
st=theme['styles']
st['color']={"background":"var(--wp--preset--color--base)","text":"var(--wp--preset--color--ink)"}
st['spacing']={"blockGap":"var(--wp--preset--spacing--40)","padding":{"left":"clamp(1.25rem,5vw,3rem)","right":"clamp(1.25rem,5vw,3rem)"}}
st['elements']['heading']={"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","fontWeight":"600","lineHeight":"1.05","letterSpacing":"-0.01em","textTransform":"uppercase"},"color":{"text":"var(--wp--preset--color--navy)"}}
st['elements']['h1']={"typography":{"fontSize":"var(--wp--preset--font-size--xx-large)"}}
st['elements']['h2']={"typography":{"fontSize":"var(--wp--preset--font-size--x-large)"}}
st['elements']['h3']={"typography":{"fontSize":"var(--wp--preset--font-size--large)","letterSpacing":"0.01em"}}
st['elements']['button']={"color":{"background":"var(--wp--preset--color--navy)","text":"#fff"},"border":{"radius":"999px"},"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","fontWeight":"500","fontSize":"0.95rem","textTransform":"uppercase","letterSpacing":"0.08em"},"spacing":{"padding":{"top":"1rem","bottom":"1rem","left":"1.75rem","right":"1.75rem"}},":hover":{"color":{"background":"var(--wp--preset--color--night)"}},":focus":{"outline":{"width":"3px","style":"solid","color":"var(--wp--preset--color--glow)","offset":"3px"}}}
st['blocks']['core/quote']={"border":{"left":{"color":"var(--wp--preset--color--accent)","width":"3px"}},"spacing":{"padding":{"left":"1.5rem"}},"typography":{"fontFamily":"var(--wp--preset--font-family--accent)","fontStyle":"italic","fontSize":"var(--wp--preset--font-size--large)","lineHeight":"1.35"}}
w('theme.json', json.dumps(theme, indent=2))
w('functions.php', """<?php
add_action('wp_enqueue_scripts', function(){
  $v = wp_get_theme()->get('Version');
  wp_enqueue_style('the516movement', get_stylesheet_uri(), [], $v);
  wp_enqueue_script('the516movement-reveal', get_theme_file_uri('assets/reveal.js'), [], $v, ['strategy'=>'defer','in_footer'=>true]);
});
add_action('wp_head', function(){ echo "<script>document.documentElement.classList.add('js');</script>\\n"; }, 1);
add_action('init', function(){
  register_block_pattern_category('the516movement',['label'=>'The 516 Movement']);
  foreach (['light'=>'Light (glow)','ghost'=>'Ghost','text'=>'Text link'] as $k=>$l) register_block_style('core/button',['name'=>$k,'label'=>$l]);
});
""")
w('assets/reveal.js', """(function(){var els=document.querySelectorAll('.reveal');
if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches){els.forEach(function(e){e.classList.add('in')});return;}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{rootMargin:'0px 0px -10% 0px',threshold:0.05});
els.forEach(function(e){io.observe(e)});})();""")
w('parts/header.html', """<!-- wp:group {"tagName":"div","className":"site-header","layout":{"type":"constrained","contentSize":"1280px"}} -->
<div class="wp-block-group site-header"><!-- wp:group {"className":"site-header__inner","layout":{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap"}} -->
<div class="wp-block-group site-header__inner"><!-- wp:html --><a class="m516-logo" href="/" rel="home"><img src="https://the516movement.com/wp-content/themes/the-516-movement/images/516-logo.png" alt="M516 – The 516 Movement, home" width="410" height="182"/></a><!-- /wp:html -->
<!-- wp:group {"className":"site-header__nav","layout":{"type":"flex","flexWrap":"nowrap"}} --><div class="wp-block-group site-header__nav"><!-- wp:navigation {"overlayMenu":"mobile","textColor":"base","overlayTextColor":"base","overlayBackgroundColor":"night","layout":{"type":"flex","justifyContent":"right"}} /-->
<!-- wp:buttons {"className":"header-cta"} --><div class="wp-block-buttons header-cta"><!-- wp:button {"className":"is-style-light"} --><div class="wp-block-button is-style-light"><a class="wp-block-button__link wp-element-button" href="/booking/">Book Ryan</a></div><!-- /wp:button --></div><!-- /wp:buttons --></div><!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->""")
w('parts/footer.html', """<!-- wp:group {"tagName":"div","className":"site-footer grain","layout":{"type":"constrained","contentSize":"1280px"}} -->
<div class="wp-block-group site-footer grain"><!-- wp:paragraph {"className":"footer-mark"} --><p class="footer-mark">Let your <em>light</em> shine.</p><!-- /wp:paragraph -->
<!-- wp:columns {"className":"footer-cols"} --><div class="wp-block-columns footer-cols"><!-- wp:column {"width":"40%"} --><div class="wp-block-column" style="flex-basis:40%"><!-- wp:html --><img class="footer-logo" src="https://the516movement.com/wp-content/themes/the-516-movement/images/516-logo.png" alt="M516" width="410" height="182" loading="lazy"/><!-- /wp:html -->
<!-- wp:paragraph --><p>A Christ-centered ministry designed to reach the corners of the earth with the redeeming message of the Gospel for all people.</p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column --><div class="wp-block-column"><!-- wp:heading {"level":2,"className":"footer-h"} --><h2 class="wp-block-heading footer-h">Connect</h2><!-- /wp:heading -->
<!-- wp:paragraph --><p>M516, Inc. · Ryan Young<br>PO Box 1728<br>Elk City, OK 73648<br><a href="tel:5803030499">580-303-0499</a></p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column --><div class="wp-block-column"><!-- wp:heading {"level":2,"className":"footer-h"} --><h2 class="wp-block-heading footer-h">Explore</h2><!-- /wp:heading -->
<!-- wp:paragraph {"className":"footer-links"} --><p class="footer-links"><a href="/about/">About</a><a href="/about-ryan/">About Ryan</a><a href="/the-answer/">The Answer</a><a href="/the-marathon/">The Marathon</a><a href="/contact/">Contact</a></p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column --><div class="wp-block-column"><!-- wp:heading {"level":2,"className":"footer-h"} --><h2 class="wp-block-heading footer-h">Follow</h2><!-- /wp:heading -->
<!-- wp:social-links {"iconColor":"base","iconColorValue":"#ffffff","className":"is-style-logos-only"} --><ul class="wp-block-social-links has-icon-color is-style-logos-only"><!-- wp:social-link {"url":"https://x.com/RyanYoung516","service":"x","label":"@RyanYoung516 on X"} /--><!-- wp:social-link {"url":"https://instagram.com/RyanYoung516","service":"instagram","label":"@RyanYoung516 on Instagram"} /--><!-- wp:social-link {"url":"https://facebook.com/The516Movement","service":"facebook","label":"The516Movement on Facebook"} /--></ul><!-- /wp:social-links -->
<!-- wp:paragraph --><p>#The516Movement</p><!-- /wp:paragraph --></div><!-- /wp:column --></div><!-- /wp:columns -->
<!-- wp:paragraph {"className":"footer-legal"} --><p class="footer-legal"><span>© 2026 The 516 Movement · M516, Inc.</span><span>A 501(c)3 non-profit organization</span></p><!-- /wp:paragraph --></div>
<!-- /wp:group -->""")
H2='<!-- wp:template-part {"slug":"header","tagName":"header","className":"site-header-wrap"} /-->\n'
main2=lambda inner:H2+'<!-- wp:group {"tagName":"main","className":"site-main","layout":{"type":"constrained"}} -->\n<main class="wp-block-group site-main">'+inner+'</main>\n<!-- /wp:group -->'+F
w('templates/page.html', main2('<!-- wp:group {"align":"full","className":"page-hero grain","layout":{"type":"constrained","contentSize":"1280px"}} --><div class="wp-block-group alignfull page-hero grain"><!-- wp:paragraph {"className":"eyebrow"} --><p class="eyebrow">The 516 Movement</p><!-- /wp:paragraph --><!-- wp:post-title {"level":1,"className":"page-hero__title"} /--></div><!-- /wp:group -->'
  +'<!-- wp:post-content {"className":"entry","layout":{"type":"constrained"}} /-->'
  +'<!-- wp:pattern {"slug":"the516movement/cta-booking"} /-->'))
w('templates/page-no-title.html', main2('<!-- wp:post-content {"align":"full","className":"entry is-home","layout":{"type":"constrained"}} /-->'))
w('templates/front-page.html', main2('<!-- wp:post-content {"align":"full","className":"entry is-home","layout":{"type":"constrained"}} /-->'))
w('patterns/cta-booking.php', "<?php\n/**\n * Title: Booking statement band\n * Slug: the516movement/cta-booking\n * Categories: the516movement, call-to-action\n */\n?>\n"+cta)
w('patterns/home.php', "<?php\n/**\n * Title: Home page\n * Slug: the516movement/home\n * Categories: the516movement\n * Block Types: core/post-content\n */\n?>\n"+home)
w('patterns/hero.php', "<?php\n/**\n * Title: Light-in-darkness hero\n * Slug: the516movement/hero\n * Categories: the516movement, banner\n */\n?>\n"+hero)
w('patterns/numbered-trio.php', "<?php\n/**\n * Title: Numbered trio\n * Slug: the516movement/numbered-trio\n * Categories: the516movement\n */\n?>\n"+trio)
w('patterns/editorial-split.php', "<?php\n/**\n * Title: Editorial split with pull quote\n * Slug: the516movement/editorial-split\n * Categories: the516movement\n */\n?>\n"+ryan)
w('patterns/collage.php', "<?php\n/**\n * Title: Photo collage\n * Slug: the516movement/collage\n * Categories: the516movement, gallery\n */\n?>\n"+collage)
# nicer form placeholders
def field(l,t='text',full=False): return f'<label class="{"full" if full else ""}"><span>{l}</span>'+('<span class="field-box is-area"></span>' if t=='area' else '<span class="field-box"></span>')+'</label>'
def mock(title,fields,note): return '<!-- wp:html --><div class="form-mock" role="group" aria-label="'+title+' (preview)"><p class="form-mock__tag">Preview · form plugin goes here</p><h3>'+title+'</h3><div class="form-mock__grid">'+''.join(fields)+'</div><span class="form-mock__btn" aria-hidden="true">Submit</span><p class="form-mock__note">'+note+'</p></div><!-- /wp:html -->\n'
import re
bk=mock('Booking questionnaire',[field('Contact name'),field('Phone','tel'),field('Email','email'),field('Sponsoring organization'),field('Event name'),field('Event date','date'),field('Event location & closest airport',full=True),field('Brief event description','area',True)],'[PLACEHOLDER] The live site uses Gravity Forms. Rebuild it with a form plugin and embed it here.')
pages['Booking']=(pages['Booking'][0], re.sub(r'<!-- wp:group \{"className":"m-card".*?<!-- /wp:group -->', lambda m: bk, pages['Booking'][1], count=1, flags=re.S))
ct=mock('Send a message',[field('Name'),field('Email','email'),field('Phone','tel',True),field('Your message','area',True)],'[PLACEHOLDER] Contact form: embed a form plugin here.')
c=pages['Contact'][1]; i=c.rfind('<!-- wp:group {"className":"m-card"')
pages['Contact']=(pages['Contact'][0], c[:i]+ct)
dn=mock('Give online',[field('Amount ($25 · $50 · $100 · $250 · $500 · custom)',full=True),field('First name'),field('Email','email')],'[PLACEHOLDER] GiveWP + Stripe donation form goes here.')
d=pages['Donate'][1]; i=d.rfind('<!-- wp:group {"className":"m-card"'); j=d.find('<!-- /wp:group -->',i)+len('<!-- /wp:group -->')
pages['Donate']=(pages['Donate'][0], d[:i]+dn+d[j:])
w('style.css', (T/'style.css').read_text().split('*/')[0]+'*/\n'+open('v2.css').read())
