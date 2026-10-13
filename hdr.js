const {chromium}=require('playwright');(async()=>{const base=process.argv[2];const b=await chromium.launch();
const shot=async(w,name,open)=>{const p=await b.newPage({viewport:{width:w,height:800}});await p.goto(base,{waitUntil:'networkidle',timeout:90000});
let f=p.mainFrame();for(let i=0;i<40;i++){const fr=p.frames().find(x=>x.url().includes('/scope:')||x.url().includes('127.0.0.1'));if(fr&&await fr.$('.site-header').catch(()=>null)){f=fr;break}await p.waitForTimeout(3000)}
await f.evaluate(()=>document.getElementById('wpadminbar')?.remove());
if(open){await f.click('.wp-block-navigation__responsive-container-open');await p.waitForTimeout(800);}
else{await f.hover('.wp-block-navigation-submenu >> nth=0').catch(()=>{});await p.waitForTimeout(600);}
await p.screenshot({path:name});await p.close();};
await shot(1366,process.argv[3],false);await shot(390,process.argv[4],true);await b.close();})();
