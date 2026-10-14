const {chromium}=require('playwright');(async()=>{const base=process.argv[2];const out=process.argv[3]||'/tmp/v';const b=await chromium.launch();
const errs=[];
for (const [u,n,w] of [['/','home',1440],['/','home-mobile',390],['/the-marathon/','inner',1440],['/booking/','booking',1440],['/about-ryan/','inner-mobile',390]]){
const p=await b.newPage({viewport:{width:w,height:900}});p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,150))});
await p.goto(base.includes('?')?base+'&url='+encodeURIComponent(u):base+u,{waitUntil:'networkidle',timeout:120000});
let f=p.mainFrame();for(let i=0;i<40;i++){const fr=p.frames().find(x=>/scope:|127\.0\.0\.1/.test(x.url()));if(fr&&await fr.$('.site-header').catch(()=>null)){f=fr;break}await p.waitForTimeout(3000)}
await f.evaluate(async()=>{document.getElementById('wpadminbar')?.remove();document.documentElement.style.setProperty('margin-top','0','important');document.querySelectorAll('img[loading]').forEach(i=>i.loading='eager');
 for(let y=0;y<document.body.scrollHeight;y+=300){scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'));document.body.classList.remove('admin-bar');await Promise.all([...document.images].map(i=>{i.decoding='sync';return (i.complete?Promise.resolve():new Promise(r=>{i.onload=i.onerror=r})).then(()=>i.decode().catch(()=>{}))}));scrollTo(0,0);await document.fonts.ready});
await p.waitForTimeout(1500);
if(f===p.mainFrame()) await p.screenshot({path:`${out}-${n}.png`,fullPage:true});
else { await f.evaluate((w)=>{document.querySelectorAll('.m-hero').forEach(e=>{e.style.setProperty('min-height',(w<600?792:828)+'px','important')})},w); const h=await f.evaluate(()=>document.documentElement.scrollHeight); await p.setViewportSize({width:w,height:Math.min(h+80,16000)}); await p.waitForTimeout(1500); await p.screenshot({path:`${out}-${n}.png`,fullPage:true}); }
await p.close();}
console.log('errors:',JSON.stringify(errs));await b.close();})();
