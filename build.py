import json, os, pathlib
T = pathlib.Path('theme/the516movement'); 
import shutil
for d in ['templates','parts','patterns','assets/fonts']: (T/d).mkdir(parents=True, exist_ok=True)
for fam,files in [('oswald',['oswald-latin-wght-normal.woff2']),('inter',['inter-latin-wght-normal.woff2','inter-latin-wght-italic.woff2'])]:
  for f in files: shutil.copy(f'node_modules/@fontsource-variable/{fam}/files/{f}', T/'assets/fonts'/f)
  shutil.copy(f'node_modules/@fontsource-variable/{fam}/LICENSE', T/f'assets/fonts/{fam.upper()}-OFL.txt')
U='https://the516movement.com/wp-content/uploads/'
def w(p,s): (T/p).write_text(s)
w('style.css', """/*
Theme Name: The 516 Movement
Theme URI: https://github.com/codysmith44/the516movement
Author: Cody Smith
Description: Modern block theme rebuild for M516, Inc. (The 516 Movement) - a Christ-centered ministry. Trial build.
Version: 0.5.0
Requires at least: 6.5
Requires PHP: 7.4
License: GPLv2 or later
Text Domain: the516movement
*/
""")
w('functions.php', """<?php
add_action('wp_enqueue_scripts', function(){ wp_enqueue_style('the516movement', get_stylesheet_uri(), [], wp_get_theme()->get('Version')); });
add_action('init', function(){ register_block_pattern_category('the516movement',['label'=>'The 516 Movement']); });
""")
theme = {
 "$schema":"https://schemas.wp.org/trunk/theme.json","version":3,
 "settings":{"appearanceTools":True,"useRootPaddingAwareAlignments":True,"layout":{"contentSize":"760px","wideSize":"1200px"},
  "color":{"palette":[
   {"slug":"primary","name":"M516 Blue","color":"#0f75bc"},
   {"slug":"navy","name":"Navy","color":"#0b3e63"},
   {"slug":"accent","name":"Red","color":"#c3272f"},
   {"slug":"ink","name":"Ink","color":"#212121"},
   {"slug":"muted","name":"Slate","color":"#4a545a"},
   {"slug":"light","name":"Light","color":"#f5f5f5"},
   {"slug":"base","name":"White","color":"#ffffff"}]},
  "typography":{"fluid":True,"fontFamilies":[
   {"slug":"heading","name":"Oswald","fontFamily":"Oswald, system-ui, sans-serif","fontFace":[{"fontFamily":"Oswald","fontWeight":"500 700","fontStyle":"normal","fontDisplay":"swap","src":["file:./assets/fonts/oswald-latin-wght-normal.woff2"]}]},
   {"slug":"body","name":"Inter","fontFamily":"Inter, system-ui, sans-serif","fontFace":[{"fontFamily":"Inter","fontWeight":"100 900","fontStyle":"normal","fontDisplay":"swap","src":["file:./assets/fonts/inter-latin-wght-normal.woff2"]},{"fontFamily":"Inter","fontWeight":"100 900","fontStyle":"italic","fontDisplay":"swap","src":["file:./assets/fonts/inter-latin-wght-italic.woff2"]}]}],
   "fontSizes":[{"slug":"small","size":"0.9rem","name":"Small"},{"slug":"medium","size":"1.125rem","name":"Medium"},
    {"slug":"large","size":"1.6rem","name":"Large","fluid":{"min":"1.35rem","max":"1.6rem"}},
    {"slug":"x-large","size":"2.4rem","name":"XL","fluid":{"min":"1.8rem","max":"2.4rem"}},
    {"slug":"huge","size":"3.75rem","name":"Huge","fluid":{"min":"2.4rem","max":"3.75rem"}}]},
  "spacing":{"units":["px","rem","%","vw"]}},
 "styles":{"color":{"background":"var(--wp--preset--color--base)","text":"var(--wp--preset--color--ink)"},
  "typography":{"fontFamily":"var(--wp--preset--font-family--body)","fontSize":"var(--wp--preset--font-size--medium)","lineHeight":"1.7"},
  "spacing":{"blockGap":"1.5rem","padding":{"left":"1.25rem","right":"1.25rem"}},
  "elements":{
   "heading":{"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","fontWeight":"600","lineHeight":"1.15"},"color":{"text":"var(--wp--preset--color--navy)"}},
   "link":{"color":{"text":"var(--wp--preset--color--primary)"},":hover":{"color":{"text":"var(--wp--preset--color--navy)"}},":focus":{"outline":{"width":"2px","style":"solid","color":"var(--wp--preset--color--accent)","offset":"2px"}}},
   "button":{"color":{"background":"var(--wp--preset--color--primary)","text":"#fff"},"border":{"radius":"6px"},"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","fontWeight":"700","textTransform":"uppercase","letterSpacing":"0.04em"},"spacing":{"padding":{"top":".8rem","bottom":".8rem","left":"1.6rem","right":"1.6rem"}},
     ":hover":{"color":{"background":"var(--wp--preset--color--navy)"}},":focus":{"outline":{"width":"3px","style":"solid","color":"var(--wp--preset--color--accent)","offset":"2px"}}}},
  "blocks":{"core/navigation":{"typography":{"fontFamily":"var(--wp--preset--font-family--heading)","textTransform":"uppercase","fontSize":"0.95rem","letterSpacing":"0.03em"}},
   "core/quote":{"border":{"left":{"color":"var(--wp--preset--color--accent)","width":"4px"}},"spacing":{"padding":{"left":"1.25rem"}},"typography":{"fontStyle":"italic"}}}},
 "templateParts":[{"name":"header","title":"Header","area":"header"},{"name":"footer","title":"Footer","area":"footer"}],
 "customTemplates":[{"name":"page-no-title","title":"Page (no title)","postTypes":["page"]}]}
w('theme.json', json.dumps(theme, indent=2))
w('parts/header.html', f"""<!-- wp:group {{"tagName":"header","style":{{"spacing":{{"padding":{{"top":"0.75rem","bottom":"0.75rem"}}}},"position":{{"type":"sticky","top":"0px"}}}},"backgroundColor":"navy","textColor":"base","className":"site-header","layout":{{"type":"constrained","contentSize":"1200px"}}}} -->
<header class="wp-block-group site-header has-base-color has-navy-background-color has-text-color has-background" style="padding-top:0.75rem;padding-bottom:0.75rem"><!-- wp:group {{"layout":{{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap"}}}} -->
<div class="wp-block-group"><!-- wp:html --><a class="m516-logo" href="/" rel="home"><img src="https://the516movement.com/wp-content/themes/the-516-movement/images/516-logo.png" alt="The 516 Movement home" width="180" height="60" style="height:64px;width:auto;display:block"/></a><!-- /wp:html -->
<!-- wp:navigation {{"overlayMenu":"mobile","textColor":"base","backgroundColor":"navy","overlayTextColor":"base","overlayBackgroundColor":"navy","layout":{{"type":"flex","justifyContent":"right"}}}} /--></div>
<!-- /wp:group --></header>
<!-- /wp:group -->""")
w('parts/footer.html', """<!-- wp:group {"tagName":"footer","style":{"spacing":{"padding":{"top":"3rem","bottom":"2rem"}},"elements":{"link":{"color":{"text":"#ffffff"}},"heading":{"color":{"text":"#ffffff"}}}},"backgroundColor":"navy","textColor":"base","layout":{"type":"constrained","contentSize":"1200px"}} -->
<footer class="wp-block-group has-base-color has-navy-background-color has-text-color has-background has-link-color" style="padding-top:3rem;padding-bottom:2rem"><!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":2,"fontSize":"large"} --><h2 class="wp-block-heading has-large-font-size">Connect</h2><!-- /wp:heading -->
<!-- wp:paragraph --><p><strong>M516, Inc.</strong> &middot; Ryan Young<br>PO Box 1728, Elk City, OK 73648<br><a href="tel:5803030499">580-303-0499</a></p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":2,"fontSize":"large"} --><h2 class="wp-block-heading has-large-font-size">Follow</h2><!-- /wp:heading -->
<!-- wp:social-links {"iconColor":"base","iconColorValue":"#ffffff","className":"is-style-logos-only"} --><ul class="wp-block-social-links has-icon-color is-style-logos-only"><!-- wp:social-link {"url":"https://x.com/RyanYoung516","service":"x","label":"@RyanYoung516 on X"} /--><!-- wp:social-link {"url":"https://instagram.com/RyanYoung516","service":"instagram","label":"@RyanYoung516 on Instagram"} /--><!-- wp:social-link {"url":"https://facebook.com/The516Movement","service":"facebook","label":"The516Movement on Facebook"} /--></ul><!-- /wp:social-links -->
<!-- wp:paragraph --><p>Use the hashtag <strong>#The516Movement</strong> on social media.</p><!-- /wp:paragraph --></div><!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":2,"fontSize":"large"} --><h2 class="wp-block-heading has-large-font-size">Get Involved</h2><!-- /wp:heading -->
<!-- wp:buttons --><div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"accent"} --><div class="wp-block-button"><a class="wp-block-button__link has-accent-background-color has-background wp-element-button" href="/booking/">Book an Event</a></div><!-- /wp:button --><!-- wp:button {"className":"is-style-outline","textColor":"base"} --><div class="wp-block-button is-style-outline"><a class="wp-block-button__link has-base-color has-text-color wp-element-button" href="/donate/">Donate</a></div><!-- /wp:button --></div><!-- /wp:buttons --></div><!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- wp:paragraph {"align":"center","fontSize":"small"} --><p class="has-text-align-center has-small-font-size">The 516 Movement &copy; 2026 All Rights Reserved &middot; M516, Inc. is a 501(c)3 non-profit organization.</p><!-- /wp:paragraph --></footer>
<!-- /wp:group -->""")
H='<!-- wp:template-part {"slug":"header","tagName":"header"} /-->\n'
F='\n<!-- wp:template-part {"slug":"footer","tagName":"footer"} /-->'
main=lambda inner:H+'<!-- wp:group {"tagName":"main","layout":{"type":"constrained"}} -->\n<main class="wp-block-group">'+inner+'</main>\n<!-- /wp:group -->'+F
hero_title='<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"3.5rem","bottom":"3rem"}},"elements":{"heading":{"color":{"text":"#ffffff"}}}},"backgroundColor":"navy","textColor":"base","layout":{"type":"constrained"}} -->\n<div class="wp-block-group alignfull has-base-color has-navy-background-color has-text-color has-background" style="padding-top:3.5rem;padding-bottom:3rem"><!-- wp:post-title {"level":1,"fontSize":"huge"} /--></div>\n<!-- /wp:group -->'
content='<!-- wp:post-content {"layout":{"type":"constrained"},"style":{"spacing":{"padding":{"top":"2.5rem","bottom":"3rem"}}}} /-->'
w('templates/page.html', main(hero_title+content))
w('templates/page-no-title.html', main('<!-- wp:post-content {"align":"full","layout":{"type":"constrained"}} /-->'))
w('templates/front-page.html', main('<!-- wp:post-content {"align":"full","layout":{"type":"constrained"}} /-->'))
w('templates/index.html', main('<!-- wp:query {"query":{"inherit":true}} --><div class="wp-block-query"><!-- wp:post-template --><!-- wp:post-title {"isLink":true} /--><!-- wp:post-excerpt /--><!-- /wp:post-template --><!-- wp:query-pagination /--></div><!-- /wp:query -->'))
w('templates/404.html', main('<!-- wp:heading {"level":1} --><h1 class="wp-block-heading">Page not found</h1><!-- /wp:heading --><!-- wp:paragraph --><p>Try the menu above, or <a href="/">return home</a>.</p><!-- /wp:paragraph -->'))

# ---- page content (block markup) ----
def p(t): return f'<!-- wp:paragraph --><p>{t}</p><!-- /wp:paragraph -->\n'
def h(t,l=2): return f'<!-- wp:heading {{"level":{l}}} --><h{l} class="wp-block-heading">{t}</h{l}><!-- /wp:heading -->\n'
def q(t,c): return f'<!-- wp:quote --><blockquote class="wp-block-quote"><!-- wp:paragraph --><p>{t}</p><!-- /wp:paragraph --><cite>{c}</cite></blockquote><!-- /wp:quote -->\n'
def img(src,alt): return f'<!-- wp:image {{"sizeSlug":"large","style":{{"border":{{"radius":"10px"}}}}}} --><figure class="wp-block-image size-large has-custom-border"><img src="{src}" alt="{alt}" style="border-radius:10px"/></figure><!-- /wp:image -->\n'
def btns(*bs):
  s='<!-- wp:buttons --><div class="wp-block-buttons">'
  for i,(t,u) in enumerate(bs):
    if i: s+=f'<!-- wp:button {{"className":"is-style-outline"}} --><div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{u}">{t}</a></div><!-- /wp:button -->'
    else: s+=f'<!-- wp:button --><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{u}">{t}</a></div><!-- /wp:button -->'
  return s+'</div><!-- /wp:buttons -->\n'
def cols(items):
  s='<!-- wp:columns --><div class="wp-block-columns">'
  for it in items: s+='<!-- wp:column --><div class="wp-block-column">'+it+'</div><!-- /wp:column -->'
  return s+'</div><!-- /wp:columns -->\n'
def card(inner): return '<!-- wp:group {"style":{"spacing":{"padding":{"top":"1.5rem","bottom":"1.5rem","left":"1.5rem","right":"1.5rem"}},"border":{"radius":"10px"}},"backgroundColor":"light","layout":{"type":"default"}} --><div class="wp-block-group has-light-background-color has-background" style="border-radius:10px;padding:1.5rem">'+inner+'</div><!-- /wp:group -->'
cta = ('<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"3rem","bottom":"3rem"}},"elements":{"heading":{"color":{"text":"#ffffff"}}}},"backgroundColor":"primary","textColor":"base","layout":{"type":"constrained"}} --><div class="wp-block-group alignfull has-base-color has-primary-background-color has-text-color has-background" style="padding-top:3rem;padding-bottom:3rem">'
 +'<!-- wp:heading {"textAlign":"center"} --><h2 class="wp-block-heading has-text-align-center">Bring M516 to your church, camp, or event</h2><!-- /wp:heading -->'
 +'<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} --><div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"accent"} --><div class="wp-block-button"><a class="wp-block-button__link has-accent-background-color has-background wp-element-button" href="/booking/">Book Your Next Event</a></div><!-- /wp:button --><!-- wp:button {"backgroundColor":"base","textColor":"navy"} --><div class="wp-block-button"><a class="wp-block-button__link has-navy-color has-base-background-color has-text-color has-background wp-element-button" href="/donate/">Donate</a></div><!-- /wp:button --></div><!-- /wp:buttons --></div><!-- /wp:group -->\n')
home = ('<!-- wp:cover {"url":"'+U+'2015/08/Falls-Creek-2023-3.jpg","dimRatio":70,"overlayColor":"navy","minHeight":78,"minHeightUnit":"vh","align":"full","layout":{"type":"constrained"}} --><div class="wp-block-cover alignfull" style="min-height:78vh"><span aria-hidden="true" class="wp-block-cover__background has-navy-background-color has-background-dim-70 has-background-dim"></span><img class="wp-block-cover__image-background" alt="" src="'+U+'2015/08/Falls-Creek-2023-3.jpg" data-object-fit="cover"/><div class="wp-block-cover__inner-container">'
 +'<!-- wp:paragraph {"style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.15em","fontWeight":"700"}},"textColor":"base"} --><p class="has-base-color has-text-color" style="font-weight:700;letter-spacing:0.15em;text-transform:uppercase">Matthew 5:16</p><!-- /wp:paragraph -->'
 +'<!-- wp:heading {"level":1,"textColor":"base","fontSize":"huge"} --><h1 class="wp-block-heading has-base-color has-text-color has-huge-font-size">Let your light shine.</h1><!-- /wp:heading -->'
 +'<!-- wp:paragraph {"textColor":"base","fontSize":"large"} --><p class="has-base-color has-text-color has-large-font-size">M516 is a Christ-centered ministry designed to reach the corners of the earth with the redeeming message of the Gospel for all people.</p><!-- /wp:paragraph -->'
 +'<!-- wp:buttons --><div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"accent"} --><div class="wp-block-button"><a class="wp-block-button__link has-accent-background-color has-background wp-element-button" href="/booking/">Book Your Next Event</a></div><!-- /wp:button --><!-- wp:button {"backgroundColor":"base","textColor":"navy"} --><div class="wp-block-button"><a class="wp-block-button__link has-navy-color has-base-background-color has-text-color has-background wp-element-button" href="/about/">Learn More About M516</a></div><!-- /wp:button --></div><!-- /wp:buttons --></div></div><!-- /wp:cover -->\n'
 +'<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"4rem","bottom":"3rem"}}},"layout":{"type":"default"}} --><div class="wp-block-group alignwide" style="padding-top:4rem;padding-bottom:3rem">'
 +'<!-- wp:heading {"textAlign":"center"} --><h2 class="wp-block-heading has-text-align-center">Ministry. Missions. Movement.</h2><!-- /wp:heading -->'
 +cols([card(h('Ministry',3)+p('The spiritual work or service of any Christian or a group of Christians, especially evangelism.')),
        card(h('Missions',3)+p('The calling of a Christian organization to go into the world and spread its faith.')),
        card(h('Movement',3)+p('A group of people working together to advance their shared ideas.'))])
 +btns(('Our Values','/our-values/'))[:-1].replace('<div class="wp-block-buttons">','<div class="wp-block-buttons" style="justify-content:center;display:flex">')+'</div><!-- /wp:group -->\n'
 +'<!-- wp:media-text {"align":"wide","mediaType":"image","verticalAlignment":"center"} --><div class="wp-block-media-text alignwide is-stacked-on-mobile is-vertically-aligned-center"><figure class="wp-block-media-text__media"><img src="'+U+'2015/08/Family-Photo-2023-2.jpg" alt="Ryan Young with his family"/></figure><div class="wp-block-media-text__content">'
 +h('Meet Ryan Young')+p('Ryan has served in student ministry for 20 years and will always have a passion for younger generations to live their lives to positively impact The Kingdom. Ryan is a dynamic communicator of the Gospel of Jesus Christ.')+btns(('About Ryan','/about-ryan/'))
 +'</div></div><!-- /wp:media-text -->\n'
 +'<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"3rem","bottom":"3rem"}}},"layout":{"type":"default"}} --><div class="wp-block-group alignwide" style="padding-top:3rem;padding-bottom:3rem">'+h('Ministry in Action')
 +'<!-- wp:gallery {"columns":3,"linkTo":"none"} --><figure class="wp-block-gallery has-nested-images columns-3 is-cropped">'
 +''.join(f'<!-- wp:image --><figure class="wp-block-image"><img src="{U}2015/08/{f}" alt="{a}"/></figure><!-- /wp:image -->' for f,a in [('Falls-Creek-2023-2-2.jpg','Ryan preaching at Falls Creek'),('Japan-2023-2-2.jpg','Mission trip to Japan'),('Duncan-2025-2.jpg','Event in Duncan, Oklahoma'),('Falls-Creek-Response-Time-2023-2.jpg','Response time at Falls Creek'),('Japan-2023-3.jpg','Ministry in Japan'),('Ryan-Dallas-Jersey-2.jpg','Ryan Young')])
 +'</figure><!-- /wp:gallery --></div><!-- /wp:group -->\n'
 +'<!-- wp:group {"style":{"spacing":{"padding":{"bottom":"3rem"}}},"layout":{"type":"constrained"}} --><div class="wp-block-group" style="padding-bottom:3rem">'+h('Jesus is The Answer')+p('Putting your faith in Jesus Christ is the most important decision that you will ever make.')+btns(('Read The Answer','/the-answer/'),('Armor Up Prayer','/armor-up/'))+'</div><!-- /wp:group -->\n'+cta)
exec(open('v2.py').read())
exec(open('v4.py').read())
pages = {
 'Home': ('home', home),
 'About': ('about', img(U+'2015/08/Falls-Creek-2023-2-2.jpg','Students worshiping at a M516 event')+h('About M516')+p('Have you ever wanted to be a part of something that is bigger than yourself? Those who follow Christ are given that opportunity every day!')+q('In the same way, let your light shine before others, so that they may see your deeds and glorify your Father in heaven.','Matthew 5:16')+p('This is the core concept of The 516 Movement. We want to see a movement of God unlike anything we have ever seen before. If followers of Christ would live a Matthew 5:16 life, we believe that revival would break out. We desperately need <strong>revival</strong>! We need to not just pray for revival, we need to live for revival.')+p('We meet people every day that are looking for something — we want to help point these people to the Cross with our actions, with our words, and with our lives. We either point people <em>to</em> the Cross or we point people <em>away from</em> the Cross. We want to be light in our world and to point as many people to the Cross as we can!')+p('<strong>Let the movement begin!</strong>')+btns(('Book Your Next Event','/booking/'),('Donate','/donate/'))),
 'Our Values': ('our-values', cols([card(h('Ministry',3)+p('The spiritual work or service of any Christian or a group of Christians, especially evangelism.')),card(h('Missions',3)+p('The calling of a Christian organization to go into the world and spread its faith.')),card(h('Movement',3)+p('A group of people working together to advance their shared ideas.'))])+q('In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.','Matthew 5:16')+p('We would love to show your students or congregation how to effectively minister to others, to live a lifestyle of missions, and to join the movement of the Holy Spirit in this world.')+btns(('Book Your Next Event','/booking/'))),
 'About Ryan': ('about-ryan', cols([img(U+'2025/01/Ryan-300x240.jpg','Ryan Young'),img(U+'2025/01/Family-300x240.jpg','Ryan, Karistin, Annslee and Cross')])+p('Ryan has surrendered his life to Jesus Christ. He is married to his amazing wife, Karistin. They have a beautiful daughter, Annslee, and a handsome son, Cross.')+p('Ryan has served in student ministry for 20 years and will always have a passion for younger generations to live their lives to positively impact The Kingdom.')+p('Ryan has a deep love for missions. Missions isn’t just an international concept. Where there are people, there are mission opportunities. He has led mission teams locally, nationally and internationally. It is his heart to present the Gospel to anyone and everyone, no matter what nation they belong to.')+p('Ryan also desperately wants the church to experience true revival that could lead to a spiritual awakening that this nation needs. Ryan is a dynamic communicator of the Gospel of Jesus Christ.')+btns(('Book Ryan','/booking/'))),
 'The Answer': ('the-answer', p('<strong>Putting your faith in Jesus Christ is the most important decision that you will ever make. Jesus is The Answer.</strong>')
   +''.join(card(h(a,3)+p(b))+'\n' for a,b in [
   ('1. God loves you','God loves you and has a great plan for your life! He created you for a purpose: to have a personal relationship with Him. <em>Genesis 1:27</em> He wants you to experience a full and abundant life – right here on earth. Jesus said: “My purpose is to give life in all its fullness.” <em>John 10:10b</em>'),
   ('2. Sin separates us','Because of sin in your life, you are separated from God. We are ALL sinners. <em>Romans 3:23</em> The price for sin is death. <em>Romans 6:23</em> (Eternal separation from God)'),
   ('3. The price is already paid','“God showed His great love for us by sending Christ to die for us while we were still sinners.” <em>Romans 5:8</em>'),
   ('4. It’s free!','Eternal salvation is a free gift. <em>Ephesians 2:8-9</em> You can’t be saved by good works, morality, religion, or Bible knowledge. You can’t earn your way to heaven.'),
   ('5. JESUS is the Answer','“I am the way, the truth, and the life. No one comes to the Father except through me.” <em>John 14:6</em>'),
   ('6. It’s up to you','You must decide for yourself if you are willing to turn from your sins and ask Jesus into your heart to be your Lord and Savior! <em>Romans 10:9; John 1:12</em>')])
   +h('Will you receive Christ today?')+p('Pray this prayer:')+q('Jesus, I surrender my life to You completely. Please forgive me, change me, and be my Lord and Savior. Thank you for saving me from my sins. I want to live my life daily to bring glory to You and to You alone. In Jesus name. Amen.','')+p('Congratulations for making the best decision that you will ever make in your life! If you prayed to receive Christ we would like to know about it so we can help you and pray for you as you begin this new journey with Christ.')+btns(('Tell Us','/contact/'))),
 'Armor Up': ('armor-up', p('<strong>A daily prayer for you during the course of your life.</strong> “The battle is on, and it belongs to the Lord” — Ephesians 6:10-18')+q('Therefore put on the full armor of God, so that when the day of evil comes, you may be able to stand your ground, and after you have done everything, to stand.','Ephesians 6:13')
   +''.join(card(h(a,3)+p(b))+'\n' for a,b in [('The belt of truth','Lord, I put on the belt of truth. I choose a lifestyle of honesty and integrity. Show me the truths I so desperately need today. Expose the lies I’m not even aware I’m believing.'),('The breastplate of righteousness','And yes Lord, I wear your righteousness today against all condemnation and corruption. Fit me with your holiness and purity—defend me from all assaults against my heart.'),('The gospel of peace','I do choose to live for the gospel at any moment. Show me where the larger story is unfolding.'),('The shield of faith','Jesus, I lift against every lie and every assault the confidence that you are good, and that you have good in store for me. Nothing is coming today that can overcome me because You are with me.'),('The helmet of salvation','Thank you, Lord, for my salvation. I receive it in a new and fresh way from you, and I declare that nothing can separate me now from the love of Christ.'),('The sword of the Spirit','Holy Spirit, show me specifically today the truths of the Word of God that I will need to counter the assaults and the snares of the Enemy. Bring them to mind throughout the day.')])
   +p('Finally, Holy Spirit, I agree to walk in step with you in everything—in all prayer as my spirit communes with you throughout the day. In Jesus Name I pray, Amen.')),
 'Booking': ('booking', p('Thank you for considering us for your event or conference. Please take a moment and fill out the brief questionnaire which will help Ryan and M516, Inc. gain a greater understanding of the work that God is doing in your ministry and through your event.')+p('Even if he isn’t available, Ryan may be able to provide a referral for someone who would be perfect for your event, or would happily consider a future date if there is a conflict. Ryan will do everything he can to work within your event’s budget.')
   +card(h('Booking questionnaire',3)+p('<strong>[PLACEHOLDER]</strong> The live site uses a Gravity Forms questionnaire (contact name, phone, email, organization, event name/date/location, closest airport, audience age, speaking times, honorarium budget, worship leader). Install a form plugin and embed the form here.'))+'\n'+btns(('Contact Us','/contact/'))),
 'Donate': ('donate', p('There are several ways that you can support M516, Inc.!')
   +cols([card(h('Pray',3)+p('First and foremost is your prayer support. We would consider it an honor for you to consistently pray for us as we strive to point people to the Cross of Christ!')),card(h('Share',3)+p('You can support us by telling others/churches about M516, Inc. We would be grateful to have the opportunity to minister to whoever and wherever we can.')),card(h('Give',3)+p('You can support M516, Inc. with your financial contributions. Donate online, or send a check (payable to <strong>M516, Inc.</strong>) to PO Box 1728, Elk City, OK 73648.'))])
   +p('We are a 501(c)3 non-profit organization.')+card(p('<strong>[PLACEHOLDER]</strong> Online giving form (live site uses GiveWP + Stripe) goes here.'))+'\n'+btns(('Learn About The Marathon','/the-marathon/'))),
 'The Marathon': ('the-marathon', img(U+'2025/01/Marathon-Page.jpg','The Marathon fundraiser')+h('It’s a Marathon!')+p('As we step into 2025, we are reminded that this ministry is not a 50-yard dash but a marathon—a journey of faith. This year marks a decade of full-time travel ministry, and we stand in awe of how the Lord has worked through these ten years of service.')+p('One of the most remarkable aspects of M516’s ministry is that, in nearly 10 years, we have never declined a ministry opportunity due to finances. This is a testament to God’s provision and the generosity of His people.')+p('As part of The Marathon campaign, we are thrilled to introduce a commemorative coin for each donor. These coins will serve as a tangible reminder to pray for M516 and symbolize your partnership with us.')+h('Partnership levels',3)
   +'<!-- wp:table --><figure class="wp-block-table"><table><thead><tr><th>Partnership</th><th>Annual giving</th></tr></thead><tbody>'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in [('Participating','$100–$599'),('Pioneer','$600–$1,199'),('Promoter','$1,200–$2,499'),('Patron','$2,500–$4,999'),('Pacesetter','$5,000–$9,999'),('Premium','$10,000–$19,999'),('Platinum','$20,000–$29,999'),('Pinnacle','$30,000 and beyond')])+'</tbody></table></figure><!-- /wp:table -->\n'
   +p('We hope you will consider joining The Marathon and partnering with us to take the Gospel to the ends of the earth.')+btns(('Join The Marathon','/donate/'))),
 'Contact': ('contact', p('Below you’ll find several ways to get in touch. If you’re interested in booking an event, please use our <a href="/booking/">booking form</a>. We look forward to hearing from you!')
   +cols([card(h('Phone',3)+p('<a href="tel:5803030499">580-303-0499</a>')),card(h('Mailing Address',3)+p('PO Box 1728<br>Elk City, OK 73648')),card(h('Email',3)+p('<strong>[PLACEHOLDER]</strong> Ryan’s email (obfuscated on live site; confirm with client).'))])
   +card(p('<strong>[PLACEHOLDER]</strong> Contact form (name, email, phone, message) – embed form plugin here.'))),
}
# pattern for home hero
w('patterns/cta-booking.php', "<?php\n/**\n * Title: Booking / Donate CTA\n * Slug: the516movement/cta-booking\n * Categories: the516movement, call-to-action\n */\n?>\n"+cta)
w('patterns/values-cards.php', "<?php\n/**\n * Title: Values cards\n * Slug: the516movement/values-cards\n * Categories: the516movement\n */\n?>\n"+pages['Our Values'][1].split('<!-- wp:quote')[0])
w('patterns/home.php', "<?php\n/**\n * Title: Home page\n * Slug: the516movement/home\n * Categories: the516movement\n * Block Types: core/post-content\n */\n?>\n"+home)
w('style.css', (T/'style.css').read_text()+"""
.site-header{z-index:50;box-shadow:0 2px 8px rgba(0,0,0,.25)}
.site-header .wp-block-navigation a,.site-header .wp-block-navigation button{color:#fff}
.site-header .wp-block-navigation .wp-block-navigation-item__content{padding:.35rem .15rem;border-bottom:2px solid transparent}
.site-header .wp-block-navigation .wp-block-navigation-item__content:hover,.site-header .current-menu-item>.wp-block-navigation-item__content{border-bottom-color:#c3272f;text-decoration:none}
.site-header .wp-block-navigation a:focus-visible,.site-header .wp-block-navigation button:focus-visible,.m516-logo:focus-visible{outline:3px solid #fff;outline-offset:3px;border-radius:2px}
.site-header .wp-block-navigation__submenu-container{background:#072a44!important;color:#fff!important;border:0!important;border-radius:6px;box-shadow:0 8px 20px rgba(0,0,0,.3);padding:.4rem 0}
.site-header .wp-block-navigation__submenu-container .wp-block-navigation-item__content{padding:.55rem 1.1rem!important;border-bottom:0}
.site-header .wp-block-navigation__submenu-container .wp-block-navigation-item__content:hover,.site-header .wp-block-navigation__submenu-container .wp-block-navigation-item__content:focus-visible{background:#0f75bc}
.site-header .wp-block-navigation__responsive-container.is-menu-open{background:#0b3e63!important;color:#fff!important}
.site-header .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__submenu-container{background:transparent!important;box-shadow:none}
.site-header .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item__content{font-size:1.15rem}
.wp-block-gallery.is-cropped img{border-radius:8px}
.wp-block-table th{background:var(--wp--preset--color--navy);color:#fff;text-align:left}
.wp-block-table td,.wp-block-table th{padding:.6rem .9rem}
.skip-link:focus{position:fixed;top:0;left:0;z-index:999;background:#fff;padding:.5rem 1rem}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important}}
""")
# ---- blueprint ----
exec(open('v2post.py').read())
exec(open('v4post.py').read())
order=['Home','About','Our Values','About Ryan','The Answer','Armor Up','Booking','Donate','The Marathon','Contact']
php = "<?php require '/wordpress/wp-load.php';\n$pages = json_decode(base64_decode('%s'), true);\n" % __import__('base64').b64encode(json.dumps({k:{'slug':pages[k][0],'content':pages[k][1]} for k in order}).encode()).decode()
php += r"""$ids=[]; $i=0;
foreach($pages as $title=>$pg){ $ids[$title]=wp_insert_post(['post_type'=>'page','post_status'=>'publish','post_title'=>$title,'post_name'=>$pg['slug'],'post_content'=>wp_slash($pg['content']),'menu_order'=>$i++]); }
update_post_meta($ids['Home'],'_wp_page_template','page-no-title');
update_option('show_on_front','page'); update_option('page_on_front',$ids['Home']);
update_option('blogname','The 516 Movement'); update_option('blogdescription','Let your light shine — Matthew 5:16');
update_option('permalink_structure','/%postname%/'); flush_rewrite_rules();
$l=function($t,$id){return '<!-- wp:navigation-link {"label":"'.$t.'","type":"page","id":'.$id.',"url":"'.get_permalink($id).'","kind":"post-type"} /-->';};
$sub=function($t,$kids)use($l,$ids){$s='<!-- wp:navigation-submenu {"label":"'.$t.'","url":"'.get_permalink($ids[$kids[0]]).'","kind":"post-type","type":"page","id":'.$ids[$kids[0]].'} -->';foreach($kids as $k)$s.=$l($k,$ids[$k]);return $s.'<!-- /wp:navigation-submenu -->';};
$nav=$l('Home',$ids['Home']).$sub('M516',['About','Our Values','About Ryan']).$sub('Resources',['The Answer','Armor Up']).$l('Booking',$ids['Booking']).$sub('Donate',['Donate','The Marathon']).$l('Contact',$ids['Contact']);
wp_insert_post(['post_type'=>'wp_navigation','post_status'=>'publish','post_title'=>'Main Menu','post_content'=>wp_slash($nav)]);
"""
def bp(theme_step):
  return {"$schema":"https://playground.wordpress.net/blueprint-schema.json","landingPage":"/","preferredVersions":{"php":"8.2","wp":"latest"},
   "features":{"networking":True},"login":True,
   "steps":[theme_step,{"step":"runPHP","code":php}]}
json.dump(bp({"step":"installTheme","themeData":{"resource":"url","url":"https://raw.githubusercontent.com/codysmith44/the516movement/main/the516movement-theme.zip?v=6"},"options":{"activate":True}}), open('blueprint.json','w'), indent=2)
json.dump(bp({"step":"activateTheme","themeFolderName":"the516movement"}), open('blueprint.local.json','w'), indent=2)
