# ---- v2 art direction: content (exec'd before pages dict) ----
def g(cls, inner, tag='section', layout='constrained', extra=''):
  return f'<!-- wp:group {{"tagName":"{tag}","align":"full","className":"{cls}","layout":{{"type":"{layout}"}}}} --><{tag} class="wp-block-group alignfull {cls}">{inner}</{tag}><!-- /wp:group -->\n'
def gi(cls, inner, layout='default'):
  return f'<!-- wp:group {{"className":"{cls}","layout":{{"type":"{layout}"}}}} --><div class="wp-block-group {cls}">{inner}</div><!-- /wp:group -->'
def gw(cls, inner, layout='default'):
  return f'<!-- wp:group {{"align":"wide","className":"{cls}","layout":{{"type":"{layout}"}}}} --><div class="wp-block-group alignwide {cls}">{inner}</div><!-- /wp:group -->'
def pc(cls,t): return f'<!-- wp:paragraph {{"className":"{cls}"}} --><p class="{cls}">{t}</p><!-- /wp:paragraph -->'
def hc(cls,t,l=2): return f'<!-- wp:heading {{"level":{l},"className":"{cls}"}} --><h{l} class="wp-block-heading {cls}">{t}</h{l}><!-- /wp:heading -->'
def btn(t,u,cls=''):
  c=f' {cls}' if cls else ''
  a=f'{{"className":"{cls}"}} ' if cls else ''
  return f'<!-- wp:button {a}--><div class="wp-block-button{c}"><a class="wp-block-button__link wp-element-button" href="{u}">{t}</a></div><!-- /wp:button -->'
def bts(*b): return '<!-- wp:buttons --><div class="wp-block-buttons">'+''.join(b)+'</div><!-- /wp:buttons -->'
def card(inner): return gi('m-card', inner)
def cols2(a,b,cls=''): return f'<!-- wp:columns {{"className":"{cls}"}} --><div class="wp-block-columns {cls}"><!-- wp:column --><div class="wp-block-column">{a}</div><!-- /wp:column --><!-- wp:column --><div class="wp-block-column">{b}</div><!-- /wp:column --></div><!-- /wp:columns -->'
def im(src,alt,cls=''): return f'<!-- wp:image {{"className":"{cls}"}} --><figure class="wp-block-image {cls}"><img src="{src}" alt="{alt}"/></figure><!-- /wp:image -->'
ARROW=' <span aria-hidden="true">→</span>'
hero = ('<!-- wp:cover {"url":"'+U+'2015/08/Falls-Creek-2023-3.jpg","dimRatio":0,"minHeight":92,"minHeightUnit":"vh","align":"full","className":"m-hero grain","layout":{"type":"constrained"}} --><div class="wp-block-cover alignfull m-hero grain" style="min-height:92vh"><span aria-hidden="true" class="wp-block-cover__background has-background-dim-0 has-background-dim"></span><img class="wp-block-cover__image-background" alt="" src="'+U+'2015/08/Falls-Creek-2023-3.jpg" data-object-fit="cover"/><div class="wp-block-cover__inner-container">'
 + pc('eyebrow','Matthew 5:16')
 + hc('display','Let your <em>light</em><br>shine.',1)
 + pc('lead','M516 is a Christ-centered ministry designed to reach the corners of the earth with the redeeming message of the Gospel for all people.')
 + bts(btn('Book Your Next Event'+ARROW,'/booking/','is-style-light'),btn('Learn More About M516','/about/','is-style-ghost'))
 + gi('hero-stats', pc('stat','<strong>10</strong><span>years of full-time travel ministry</span>')+pc('stat','<strong>20</strong><span>years serving students</span>')+pc('stat','<strong>0</strong><span>opportunities declined due to finances</span>'),'flex')
 + '</div></div><!-- /wp:cover -->\n')
trio = g('m-section is-paper reveal',
  gw('split', gi('split__aside', pc('eyebrow on-light','What we are about')+hc('section-title','Ministry.<br>Missions.<br><em>Movement.</em>')+pc('muted','We would love to show your students or congregation how to effectively minister to others, to live a lifestyle of missions, and to join the movement of the Holy Spirit in this world.')+bts(btn('Our Values'+ARROW,'/our-values/','is-style-text')))
   + gi('split__main numbered', ''.join(gi('num-item', pc('num',n)+hc('',t,3)+pc('',d)) for n,t,d in [
     ('01','Ministry','The spiritual work or service of any Christian or a group of Christians, especially evangelism.'),
     ('02','Missions','The calling of a Christian organization to go into the world and spread its faith.'),
     ('03','Movement','A group of people working together to advance their shared ideas.')]))))
statement = g('m-statement is-paper reveal', pc('statement','Have you ever wanted to be a part of something that is <em>bigger than yourself?</em>')+pc('statement-sub','Those who follow Christ are given that opportunity every day.'))
ryan = g('m-section is-dark grain reveal',
  gw('editorial', gi('editorial__media', im(U+'2015/08/Ryan-Dallas-Jersey-2.jpg','Ryan Young preaching','frame-main')+im(U+'2015/08/Family-Photo-2023-2.jpg','Ryan Young with his family','frame-inset'))
   + gi('editorial__body', pc('eyebrow','Meet Ryan Young')
     + '<!-- wp:quote {"className":"pull"} --><blockquote class="wp-block-quote pull"><!-- wp:paragraph --><p>Where there are people, there are mission opportunities.</p><!-- /wp:paragraph --></blockquote><!-- /wp:quote -->'
     + pc('','Ryan has served in student ministry for 20 years and will always have a passion for younger generations to live their lives to positively impact The Kingdom. He has led mission teams locally, nationally and internationally. Ryan is a dynamic communicator of the Gospel of Jesus Christ.')
     + bts(btn('About Ryan'+ARROW,'/about-ryan/','is-style-light')))))
collage = g('m-section is-paper reveal',
  gw('section-head', pc('eyebrow on-light','Ministry in action')+hc('section-title','Camps, churches &amp; <em>the nations.</em>'),'flex')
  + gw('collage', ''.join(im(U+'2015/08/'+f,a,'c'+str(i+1)) for i,(f,a) in enumerate([('Falls-Creek-2023-2-2.jpg','Students worshiping at Falls Creek'),('Japan-2023-2-2.jpg','Mission trip to Japan'),('Falls-Creek-Response-Time-2023-2.jpg','Response time at Falls Creek'),('Duncan-2025-2.jpg','Ministry event in Duncan, Oklahoma'),('Japan-2023-3.jpg','Ministry in Japan')]))))
answer = g('m-answer is-dark grain reveal', pc('eyebrow','John 14:6')+hc('display is-md','Jesus is<br><em>The Answer.</em>')+pc('lead','Putting your faith in Jesus Christ is the most important decision that you will ever make.')+bts(btn('Read The Answer'+ARROW,'/the-answer/','is-style-light'),btn('Armor Up: A Daily Prayer','/armor-up/','is-style-ghost')))
cta = g('m-band reveal', gw('band', hc('band__title','Bring the message to <em>your people.</em>')+gi('band__side', pc('','Camps, conferences, churches and student events. Ryan will do everything he can to work within your event’s budget.')+bts(btn('Book Your Next Event'+ARROW,'/booking/','is-style-light'),btn('Donate','/donate/','is-style-ghost'))),'flex'))
home = hero+statement+trio+ryan+collage+answer+cta
