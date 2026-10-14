# ---- v3 de-slop pass: content (exec'd after v2.py, before pages) ----
MATT='In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.'
def quote(t,c,cls='scripture'): return f'<!-- wp:quote {{"className":"{cls}"}} --><blockquote class="wp-block-quote {cls}"><!-- wp:paragraph --><p>{t}</p><!-- /wp:paragraph --><cite>{c}</cite></blockquote><!-- /wp:quote -->'
def link(t,u): return pc('more',f'<a href="{u}">{t}</a>')
def colsN(items,cls=''):
  return f'<!-- wp:columns {{"className":"{cls}"}} --><div class="wp-block-columns {cls}">'+''.join(f'<!-- wp:column --><div class="wp-block-column">{x}</div><!-- /wp:column -->' for x in items)+'</div><!-- /wp:columns -->'
def card(inner): return gi('m-card', inner)
hero = g('m-hero', gw('hero-grid',
   gi('hero-text', hc('hero-title','Let your light shine.',1)
     + pc('lead','M516 is a Christ-centered ministry designed to reach the corners of the earth with the redeeming message of the Gospel for all people.')
     + bts(btn('Book your next event','/booking/','is-style-light'),btn('Learn more about M516','/about/','is-style-text')))
   + im(U+'2015/08/Falls-Creek-2023-3.jpg','Ryan Young preaching to students at Falls Creek','hero-photo')))
statement = g('m-section m-intro',
   quote(MATT,'Matthew 5:16','scripture is-large')
   + pc('','This is the core concept of The 516 Movement. We want to see a movement of God unlike anything we have ever seen before. If followers of Christ would live a Matthew 5:16 life, we believe that revival would break out.')
   + pc('','We need to not just pray for revival, we need to live for revival.'))
trio = g('m-section is-paper',
   gw('trio-wrap', hc('section-title','Ministry, missions, movement')
     + colsN([hc('',t,3)+pc('',d) for t,d in [
       ('Ministry','The spiritual work or service of any Christian or a group of Christians, especially evangelism.'),
       ('Missions','The calling of a Christian organization to go into the world and spread its faith.'),
       ('Movement','A group of people working together to advance their shared ideas.')]],'trio')
     + pc('trio-note','We would love to show your students or congregation how to effectively minister to others, to live a lifestyle of missions, and to join the movement of the Holy Spirit in this world. '+'<a href="/our-values/">Read our values</a>')))
ryan = g('m-section',
   gw('editorial', im(U+'2015/08/Family-Photo-2023-2.jpg','Ryan Young with his wife Karistin and their children, Annslee and Cross','editorial__photo')
     + gi('editorial__body', hc('section-title','Meet Ryan Young')
       + pc('','Ryan has surrendered his life to Jesus Christ. He is married to his amazing wife, Karistin. They have a beautiful daughter, Annslee, and a handsome son, Cross.')
       + pc('','He has served in student ministry for 20 years and has led mission teams locally, nationally and internationally. Missions isn’t just an international concept. Where there are people, there are mission opportunities.')
       + link('More about Ryan','/about-ryan/'))))
collage = g('m-section is-paper',
   gw('gallery-wrap', hc('section-title','Ministry in action')
     + gw('photo-grid', ''.join(f'<!-- wp:image {{"className":"p{i+1}"}} --><figure class="wp-block-image p{i+1}"><img src="{U}2015/08/{f}" alt="{a}"/><figcaption class="wp-element-caption">{a}</figcaption></figure><!-- /wp:image -->' for i,(f,a) in enumerate([('Falls-Creek-2023-2-2.jpg','Worship at Falls Creek'),('Japan-2023-2-2.jpg','Mission trip to Japan'),('Duncan-2025-2.jpg','Duncan, Oklahoma')])))))
answer = g('m-section m-answer',
   hc('section-title','Jesus is the answer')
   + pc('','Putting your faith in Jesus Christ is the most important decision that you will ever make.')
   + quote('I am the way, the truth, and the life. No one comes to the Father except through me.','John 14:6')
   + pc('more','<a href="/the-answer/">Read The Answer</a> &nbsp;·&nbsp; <a href="/armor-up/">Armor Up, a daily prayer</a>'))
cta = g('m-band', gw('band', hc('band__title','Bring M516 to your church, camp, or event')
   + pc('','Even if Ryan isn’t available, he may be able to recommend someone who would be perfect for your event. He will do everything he can to work within your budget.')
   + bts(btn('Book your next event','/booking/','is-style-light'),btn('Support the ministry','/donate/','is-style-text'))))
home = hero+statement+trio+ryan+collage+answer+cta
