const {chromium}=require('playwright');(async()=>{const base=process.argv[2],out=process.argv[3];const b=await chromium.launch();
for (const w of [390,768]){const p=await b.newPage({viewport:{width:w,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,150))});
await p.goto(base,{waitUntil:'networkidle',timeout:120000});
let f=p.mainFrame();for(let i=0;i<40;i++){const fr=p.frames().find(x=>/scope:|127\.0\.0\.1/.test(x.url()));if(fr&&await fr.$('.site-header').catch(()=>null)){f=fr;break}await p.waitForTimeout(3000)}
await f.evaluate(()=>scrollTo(0,600));await p.waitForTimeout(400);
if(!await f.isVisible('.wp-block-navigation__responsive-container-open')){console.log(w,'hamburger hidden (desktop nav); nav fits:',await f.evaluate(()=>{const n=document.querySelector('.site-header__inner');return n.scrollWidth<=n.clientWidth+1}));await p.screenshot({path:`${out}-${w}.png`});await p.close();continue;}
await f.click('.wp-block-navigation__responsive-container-open');await p.waitForTimeout(800);
const info=await f.evaluate(()=>{const c=document.querySelector('.wp-block-navigation__responsive-container');const r=c.getBoundingClientRect();const h=document.querySelector('.site-header');const cs=getComputedStyle(c);
 const close=document.querySelector('.wp-block-navigation__responsive-container-close');const cr=close?.getBoundingClientRect();
 const a=[...c.querySelectorAll('a')].slice(0,3).map(x=>[x.textContent.trim(),getComputedStyle(x).color]);
 return {open:c.classList.contains('is-menu-open'),rect:[r.top,r.left,r.width,r.height].map(Math.round),vh:innerHeight,pos:cs.position,z:cs.zIndex,bg:cs.backgroundColor,headerFilter:getComputedStyle(h).backdropFilter,close:cr&&[cr.top,cr.left,cr.width].map(Math.round),bodyOverflow:getComputedStyle(document.documentElement).overflow,links:a}});
await f.click('.wp-block-navigation-submenu__toggle >> nth=0').catch(()=>{});await p.waitForTimeout(300);info.scrollable=await f.evaluate(()=>{const c=document.querySelector('.wp-block-navigation__responsive-container');return [c.scrollHeight,c.clientHeight]});
console.log(w,JSON.stringify(info),'errs',JSON.stringify(errs));
await p.screenshot({path:`${out}-${w}.png`});
// close
await f.click('.wp-block-navigation__responsive-container-close').catch(e=>console.log('close fail',e.message.slice(0,80)));await p.waitForTimeout(500);
console.log(' closed:',await f.evaluate(()=>!document.querySelector('.wp-block-navigation__responsive-container').classList.contains('is-menu-open')));
// navigate
await f.click('.wp-block-navigation__responsive-container-open');await p.waitForTimeout(600);
await Promise.all([f.waitForNavigation({timeout:20000}).catch(()=>null),f.click('.wp-block-navigation__responsive-container a[href*="booking"] >> nth=0').catch(e=>console.log('nav click fail',e.message.slice(0,120)))]);
await p.waitForTimeout(1500);const fr2=p.frames().find(x=>/booking/.test(x.url()));console.log(' navigated:',!!fr2||/booking/.test(f.url()));
await p.close();}
await b.close();})();
