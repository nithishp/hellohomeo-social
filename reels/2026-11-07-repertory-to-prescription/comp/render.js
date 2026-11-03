const { chromium } = require('playwright') ;
const fs=require('fs');
(async()=>{ const [,,mode,out,a,b,fps]=process.argv; fs.mkdirSync(out,{recursive:true});
 const br=await chromium.launch({args:['--no-sandbox','--font-render-hinting=none']});
 const p=await br.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 await p.goto('http://localhost:8765/index.html'); await p.evaluate(()=>window.ready);
 const fam=await p.evaluate(()=>[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight).join(','));
 console.log('fonts',fam);
 let times=[]; if(mode==='times') times=a.split(',').map(Number); else { const F=+fps||30; for(let f=Math.round(+a*F); f<Math.round(+b*F); f++) times.push(f/F); }
 for(const t of times){ await p.evaluate(t=>window.seek(t),t);
   const name= mode==='times'? `t${t.toFixed(2)}.png` : `f${String(Math.round(t*(+fps||30))).padStart(4,'0')}.png`;
   await p.screenshot({path:`${out}/${name}`,omitBackground:true}); }
 await br.close(); })();
