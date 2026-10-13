const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:900}});
const fails=[];p.on('requestfailed',r=>fails.push(r.url()));
await p.goto(process.argv[2],{waitUntil:'networkidle',timeout:120000});
let f=p.mainFrame();for(let i=0;i<40;i++){const fr=p.frames().find(x=>/scope:|127\.0\.0\.1/.test(x.url()));if(fr&&await fr.$('.site-header').catch(()=>null)){f=fr;break}await p.waitForTimeout(3000)}
await f.evaluate(()=>document.fonts.ready);
const r=await f.evaluate(()=>({h1:getComputedStyle(document.querySelector('h1')).fontFamily,body:getComputedStyle(document.body).fontFamily,nav:getComputedStyle(document.querySelector('.wp-block-navigation-item__content')).fontFamily,
 oswald:document.fonts.check('600 20px Oswald'),inter:document.fonts.check('400 16px Inter'),loaded:[...document.fonts].filter(x=>x.status=='loaded').map(x=>x.family+' '+x.weight+' '+x.style),
 google:[...document.querySelectorAll('link[href*="googleapis"]')].length, header:getComputedStyle(document.querySelector('.site-header')).backgroundColor}));
console.log(JSON.stringify(r));console.log('failed:',fails.filter(u=>/woff|font/.test(u)));
await f.evaluate(()=>{document.getElementById('wpadminbar')?.remove();scrollTo(0,0)});
await p.screenshot({path:process.argv[3]});
const s=await f.$('main h2');if(s){await s.scrollIntoViewIfNeeded();await p.waitForTimeout(500);await p.screenshot({path:process.argv[4]});}
await b.close();})();
