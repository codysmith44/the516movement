# ---- v3 de-slop pass: system ----
fd=T/'assets/fonts'
for f in fd.iterdir(): f.unlink()
for fam,files in [('newsreader',['newsreader-latin-opsz-normal.woff2','newsreader-latin-opsz-italic.woff2']),('source-sans-3',['source-sans-3-latin-wght-normal.woff2','source-sans-3-latin-wght-italic.woff2'])]:
  for f in files: shutil.copy(f'node_modules/@fontsource-variable/{fam}/files/{f}', fd/f)
  shutil.copy(f'node_modules/@fontsource-variable/{fam}/LICENSE', fd/f'{fam.upper()}-OFL.txt')
(T/'assets/reveal.js').unlink(missing_ok=True)
ty=theme['settings']['typography']
ty['fontFamilies']=[
 {"slug":"heading","name":"Newsreader","fontFamily":"Newsreader, Georgia, 'Times New Roman', serif","fontFace":[
   {"fontFamily":"Newsreader","fontWeight":"200 800","fontStyle":"normal","fontDisplay":"swap","src":["file:./assets/fonts/newsreader-latin-opsz-normal.woff2"]},
   {"fontFamily":"Newsreader","fontWeight":"200 800","fontStyle":"italic","fontDisplay":"swap","src":["file:./assets/fonts/newsreader-latin-opsz-italic.woff2"]}]},
 {"slug":"body","name":"Source Sans 3","fontFamily":"'Source Sans 3', 'Segoe UI', Arial, sans-serif","fontFace":[
   {"fontFamily":"Source Sans 3","fontWeight":"200 900","fontStyle":"normal","fontDisplay":"swap","src":["file:./assets/fonts/source-sans-3-latin-wght-normal.woff2"]},
   {"fontFamily":"Source Sans 3","fontWeight":"200 900","fontStyle":"italic","fontDisplay":"swap","src":["file:./assets/fonts/source-sans-3-latin-wght-italic.woff2"]}]}]
ty['fontSizes']=[{"slug":"small","name":"Small","size":"0.9375rem"},{"slug":"medium","name":"Body","size":"1.1875rem","fluid":{"min":"1.0625rem","max":"1.1875rem"}},
 {"slug":"large","name":"Large","size":"1.5rem","fluid":{"min":"1.3rem","max":"1.5rem"}},{"slug":"x-large","name":"XL","size":"2.5rem","fluid":{"min":"1.9rem","max":"2.5rem"}},
 {"slug":"xx-large","name":"XXL","size":"3.75rem","fluid":{"min":"2.5rem","max":"3.75rem"}},{"slug":"huge","name":"Display","size":"5.25rem","fluid":{"min":"3rem","max":"5.25rem"}}]
theme['settings']['color']['gradients']=[]
theme['settings']['color']['palette']=[
 {"slug":"primary","name":"M516 Blue","color":"#0f75bc"},{"slug":"navy","name":"Navy","color":"#0b3e63"},
 {"slug":"accent","name":"Red","color":"#c3272f"},{"slug":"ink","name":"Ink","color":"#1d2329"},
 {"slug":"muted","name":"Slate","color":"#525b62"},{"slug":"paper","name":"Paper","color":"#f5f2ec"},
 {"slug":"rule","name":"Rule","color":"#dcd6cb"},{"slug":"base","name":"White","color":"#ffffff"}]
st=theme['styles']
st['typography']={"fontFamily":"var(--wp--preset--font-family--body)","fontSize":"var(--wp--preset--font-size--medium)","lineHeight":"1.6"}
st['elements']['heading']={"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","fontWeight":"500","lineHeight":"1.12","letterSpacing":"-0.01em"},"color":{"text":"var(--wp--preset--color--ink)"}}
st['elements']['h1']={"typography":{"fontSize":"var(--wp--preset--font-size--huge)","lineHeight":"1.02"}}
st['elements']['h2']={"typography":{"fontSize":"var(--wp--preset--font-size--xx-large)"}}
st['elements']['h3']={"typography":{"fontSize":"var(--wp--preset--font-size--large)","fontWeight":"600"}}
st['elements']['link']={"color":{"text":"var(--wp--preset--color--navy)"},"typography":{"textDecoration":"underline"},":hover":{"color":{"text":"var(--wp--preset--color--accent)"}},":focus":{"outline":{"width":"2px","style":"solid","color":"var(--wp--preset--color--primary)","offset":"2px"}}}
st['elements']['button']={"color":{"background":"var(--wp--preset--color--navy)","text":"#fff"},"border":{"radius":"3px"},"typography":{"fontFamily":"var(--wp--preset--font-family--body)","fontWeight":"600","fontSize":"1.0625rem","textTransform":"none","letterSpacing":"0"},"spacing":{"padding":{"top":"0.85rem","bottom":"0.85rem","left":"1.4rem","right":"1.4rem"}},":hover":{"color":{"background":"#072c47"}},":focus":{"outline":{"width":"3px","style":"solid","color":"var(--wp--preset--color--primary)","offset":"2px"}}}
st['blocks']['core/navigation']={"typography":{"fontFamily":"var(--wp--preset--font-family--body)","fontSize":"1.0625rem","fontWeight":"500"}}
st['blocks']['core/quote']={"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","fontStyle":"italic","fontSize":"var(--wp--preset--font-size--large)","lineHeight":"1.4"},"border":{"left":{"width":"0px","style":"none"}},"spacing":{"padding":{"left":"0"}}}
w('theme.json', json.dumps(theme, indent=2))
w('functions.php', """<?php
add_action('wp_enqueue_scripts', function(){
  wp_enqueue_style('the516movement', get_stylesheet_uri(), [], wp_get_theme()->get('Version'));
});
add_action('init', function(){
  register_block_pattern_category('the516movement',['label'=>'The 516 Movement']);
  foreach (['light'=>'On dark','text'=>'Text link'] as $k=>$l) register_block_style('core/button',['name'=>$k,'label'=>$l]);
});
""")
w('parts/footer.html', """<!-- wp:group {"tagName":"div","className":"site-footer","layout":{"type":"constrained","contentSize":"1280px"}} -->
<div class="wp-block-group site-footer"><!-- wp:columns {"className":"footer-cols"} --><div class="wp-block-columns footer-cols"><!-- wp:column {"width":"42%"} --><div class="wp-block-column" style="flex-basis:42%"><!-- wp:html --><img class="footer-logo" src="https://the516movement.com/wp-content/themes/the-516-movement/images/516-logo.png" alt="M516" width="410" height="182" loading="lazy"/><!-- /wp:html -->
<!-- wp:paragraph --><p>A Christ-centered ministry designed to reach the corners of the earth with the redeeming message of the Gospel for all people.</p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column --><div class="wp-block-column"><!-- wp:heading {"level":2,"className":"footer-h"} --><h2 class="wp-block-heading footer-h">Contact</h2><!-- /wp:heading -->
<!-- wp:paragraph --><p>M516, Inc.<br>PO Box 1728<br>Elk City, OK 73648<br><a href="tel:5803030499">580-303-0499</a></p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column --><div class="wp-block-column"><!-- wp:heading {"level":2,"className":"footer-h"} --><h2 class="wp-block-heading footer-h">Pages</h2><!-- /wp:heading -->
<!-- wp:paragraph {"className":"footer-links"} --><p class="footer-links"><a href="/about/">About M516</a><a href="/about-ryan/">About Ryan</a><a href="/the-answer/">The Answer</a><a href="/the-marathon/">The Marathon</a><a href="/contact/">Contact</a></p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column --><div class="wp-block-column"><!-- wp:heading {"level":2,"className":"footer-h"} --><h2 class="wp-block-heading footer-h">Follow</h2><!-- /wp:heading -->
<!-- wp:paragraph {"className":"footer-links"} --><p class="footer-links"><a href="https://x.com/RyanYoung516">@RyanYoung516 on X</a><a href="https://instagram.com/RyanYoung516">Instagram</a><a href="https://facebook.com/The516Movement">Facebook</a></p><!-- /wp:paragraph -->
<!-- wp:paragraph --><p>Share with #The516Movement</p><!-- /wp:paragraph --></div><!-- /wp:column --></div><!-- /wp:columns -->
<!-- wp:paragraph {"className":"footer-legal"} --><p class="footer-legal">© 2026 M516, Inc. The 516 Movement is a 501(c)3 non-profit organization.</p><!-- /wp:paragraph --></div>
<!-- /wp:group -->""")
w('templates/page.html', main2('<!-- wp:group {"align":"full","className":"page-hero","layout":{"type":"constrained","contentSize":"1280px"}} --><div class="wp-block-group alignfull page-hero"><!-- wp:post-title {"level":1,"className":"page-hero__title"} /--></div><!-- /wp:group -->'
  +'<!-- wp:post-content {"className":"entry","layout":{"type":"constrained"}} /-->'
  +'<!-- wp:pattern {"slug":"the516movement/cta-booking"} /-->'))
for f in ['hero','numbered-trio','editorial-split','collage']: (T/f'patterns/{f}.php').unlink(missing_ok=True)
w('patterns/hero.php', "<?php\n/**\n * Title: Hero with photo\n * Slug: the516movement/hero\n * Categories: the516movement, banner\n */\n?>\n"+hero)
w('patterns/intro-scripture.php', "<?php\n/**\n * Title: Scripture introduction\n * Slug: the516movement/intro-scripture\n * Categories: the516movement\n */\n?>\n"+statement)
w('patterns/three-columns.php', "<?php\n/**\n * Title: Three text columns\n * Slug: the516movement/three-columns\n * Categories: the516movement\n */\n?>\n"+trio)
w('patterns/photo-and-text.php', "<?php\n/**\n * Title: Photo and text\n * Slug: the516movement/photo-and-text\n * Categories: the516movement\n */\n?>\n"+ryan)
w('patterns/photo-grid.php', "<?php\n/**\n * Title: Photo grid with captions\n * Slug: the516movement/photo-grid\n * Categories: the516movement, gallery\n */\n?>\n"+collage)
(T/'patterns/values-cards.php').unlink(missing_ok=True)
w('style.css', (T/'style.css').read_text().split('*/')[0]+'*/\n'+open('v3.css').read())
w('parts/header.html', (T/'parts/header.html').read_text().replace('"overlayBackgroundColor":"night"','"overlayBackgroundColor":"navy"'))
w('parts/footer.html', (T/'parts/footer.html').read_text().replace('"contentSize":"1200px"','"contentSize":"1280px"'))
