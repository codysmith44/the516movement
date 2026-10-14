const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('http://127.0.0.1:9400/booking/',{waitUntil:'networkidle'});
console.log(JSON.stringify(await p.evaluate(()=>{const r=s=>{const e=document.querySelector(s);const c=getComputedStyle(e);return [s,e.className.slice(0,90),Math.round(e.getBoundingClientRect().left),c.paddingLeft,c.maxWidth,c.marginLeft]};return [r('.m516-logo'),r('.site-header'),r('.page-hero'),r('.page-hero__title'),r('.site-main')]}),null,1));await b.close();})();
