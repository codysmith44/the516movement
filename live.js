const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:900}});
p.on('console',m=>{if(['error','warning'].includes(m.type()))console.log('CONSOLE',m.type(),m.text().slice(0,300))});p.on('pageerror',e=>console.log('PAGEERR',e.message.slice(0,300)));
await p.goto(process.argv[2]||'https://playground.wordpress.net/?blueprint-url=https://raw.githubusercontent.com/codysmith44/the516movement/main/blueprint.json');
let ok=false;for(let i=0;i<36;i++){await p.waitForTimeout(5000);for(const f of p.frames()){try{const t=await f.title();if(/516/.test(t)){ok=t;}}catch(e){}} if(ok)break;
const txt=await p.evaluate(()=>document.body.innerText.slice(0,200));if(/Could not load|failed/i.test(txt)){console.log('FAILTEXT',txt);break;}}
console.log('RESULT',ok);await p.waitForTimeout(4000);await p.screenshot({path:'screenshots/playground-live.png'});await b.close();})();
