# ---- v4: system ----
fd=T/'assets/fonts'
for f in fd.iterdir(): f.unlink()
for fam,files in [('newsreader',['newsreader-latin-opsz-normal.woff2','newsreader-latin-opsz-italic.woff2']),('source-sans-3',['source-sans-3-latin-wght-normal.woff2','source-sans-3-latin-wght-italic.woff2'])]:
  for f in files: shutil.copy(f'node_modules/@fontsource-variable/{fam}/files/{f}', fd/f)
  shutil.copy(f'node_modules/@fontsource-variable/{fam}/LICENSE', fd/f'{fam.upper()}-OFL.txt')
NR="Newsreader, Georgia, 'Times New Roman', serif"
theme['settings']['typography']['fontFamilies']=[
 {"slug":"heading","name":"Newsreader","fontFamily":NR,"fontFace":[
   {"fontFamily":"Newsreader","fontWeight":"200 800","fontStyle":"normal","fontDisplay":"swap","src":["file:./assets/fonts/newsreader-latin-opsz-normal.woff2"]},
   {"fontFamily":"Newsreader","fontWeight":"200 800","fontStyle":"italic","fontDisplay":"swap","src":["file:./assets/fonts/newsreader-latin-opsz-italic.woff2"]}]},
 {"slug":"body","name":"Source Sans 3","fontFamily":"'Source Sans 3', 'Segoe UI', Arial, sans-serif","fontFace":[
   {"fontFamily":"Source Sans 3","fontWeight":"200 900","fontStyle":"normal","fontDisplay":"swap","src":["file:./assets/fonts/source-sans-3-latin-wght-normal.woff2"]},
   {"fontFamily":"Source Sans 3","fontWeight":"200 900","fontStyle":"italic","fontDisplay":"swap","src":["file:./assets/fonts/source-sans-3-latin-wght-italic.woff2"]}]},
 {"slug":"accent","name":"Newsreader Italic","fontFamily":NR}]
st=theme['styles']
st['elements']['heading']['typography'].pop('textTransform',None)
st['elements']['heading']['typography'].update({"fontWeight":"600","letterSpacing":"-0.015em","lineHeight":"1.05"})
st['elements']['button']['typography'].update({"textTransform":"none","letterSpacing":"0","fontFamily":"var(--wp--preset--font-family--body)","fontWeight":"600","fontSize":"1.0625rem"})
st['blocks']['core/navigation']={"typography":{"fontFamily":"var(--wp--preset--font-family--body)","fontSize":"1.0625rem","fontWeight":"500"}}
w('theme.json', json.dumps(theme, indent=2))
w('templates/page.html', (T/'templates/page.html').read_text().replace('<!-- wp:paragraph {"className":"eyebrow"} --><p class="eyebrow">The 516 Movement</p><!-- /wp:paragraph -->',''))
import re as _re
css=open('v2.css').read()
css=_re.sub(r'text-transform:uppercase;?','',css)
css=_re.sub(r'letter-spacing:\.(0[4-9]|[1-9])\d*em;?','',css)
w('style.css', (T/'style.css').read_text().split('*/')[0]+'*/\n'+css+open('v4.css').read())
_lab={'Book Your Next Event':'Book your next event','Learn More About M516':'Learn more about M516','Our Values':'Our values','Read The Answer':'Read The Answer','Armor Up: A Daily Prayer':'Armor Up: a daily prayer','Learn About The Marathon':'Learn about The Marathon','Join The Marathon':'Join The Marathon','Contact Us':'Contact us','Tell Us':'Tell us'}
def _fix(s):
  for a,b in _lab.items(): s=s.replace('>'+a+' <span','>'+b+' <span').replace('>'+a+'</a>','>'+b+'</a>')
  return s
pages={k:(v[0],_fix(v[1])) for k,v in pages.items()}
for f in ['home','hero','cta-booking','numbered-trio']:
  pf=T/f'patterns/{f}.php'
  if pf.exists(): pf.write_text(_fix(pf.read_text()))
