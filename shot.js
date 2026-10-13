const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const [u,n,w] of [['/','home',1366],['/about-ryan/','about-ryan',1366],['/the-marathon/','the-marathon',1366],['/','home-mobile',390]]){
const p=await b.newPage({viewport:{width:w,height:900}});await p.goto('http://127.0.0.1:9400'+u,{waitUntil:'networkidle',timeout:60000});
await p.evaluate(async()=>{document.getElementById('wpadminbar')?.remove();document.querySelectorAll('img[loading]').forEach(i=>i.loading='eager');for(let y=0;y<document.body.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,100))}scrollTo(0,0)});await p.waitForLoadState('networkidle');
await p.screenshot({path:`screenshots/${n}.png`,fullPage:true});await p.close();}
await b.close();})();
