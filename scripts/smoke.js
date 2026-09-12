const {JSDOM}=require('jsdom'); const fs=require('fs');
const html=fs.readFileSync(require('path').join(__dirname,'..','index.html'),'utf8').replace(/<script src=[^>]*><\/script>/,'');
const dom=new JSDOM(html,{runScripts:'outside-only'}); const w=dom.window;
w.fetch=()=>Promise.reject(new Error('no net')); w.AbortSignal={timeout:()=>null}; w.requestAnimationFrame=()=>0;
let mapInst; let ZOOM=1.4;
w.maplibregl={Map:class{constructor(){this.h={};mapInst=this;} on(e,l,f){(this.h[e]=this.h[e]||[]).push(f||l);} once(){} setProjection(){} addControl(){} getCenter(){return{lng:0,lat:0}} setCenter(){} getZoom(){return ZOOM} getBounds(){return{contains(p){return p[0]>100&&p[0]<150&&p[1]>20&&p[1]<50},toArray(){return[[100,20],[150,50]]}}} addImage(){} hasImage(){return true} addSource(){} addLayer(){} getLayer(){return true} getSource(){return{setData(){},_data:{features:[]}}} setFilter(){} setPaintProperty(){} queryRenderedFeatures(){return[]} getCanvas(){return{style:{}}} fitBounds(){} flyTo(){} fire(e){(this.h[e]||[]).forEach(f=>f())}},NavigationControl:class{},Marker:class{setLngLat(){return this} addTo(){return this} remove(){}},LngLatBounds:class{extend(){return this}}};
w.HTMLCanvasElement.prototype.getContext=()=>({beginPath(){},arc(){},fill(){},stroke(){},moveTo(){},lineTo(){},closePath(){},fillRect(){},quadraticCurveTo(){},save(){},restore(){},translate(){},rotate(){},arcTo(){},getImageData(){return{}}});
const s=html.match(/<script>([\s\S]*)<\/script>/)[1];
const extra=`
;map.fire("load");(function(){ const q=s=>document.querySelectorAll(s).length, T=s=>document.querySelector(s).textContent;
 console.log('world view (featured tab) -> cards:',q('.card'),'| title:',T('#side-title')); document.querySelector('.tab[data-tab=destinations]').click(); console.log('destinations tab ->',q('.dest'),'dests | title:',T('#side-title')); document.querySelector('.tab[data-tab=featured]').click();
 window.__setZoom(3.2); apply(); console.log('zoomed into Japan box -> cards:',q('.card'),'| title:',T('#side-title'));
 openTour(TOURS[0]); console.log('open tour -> days:',q('.day'),'| current:',current.name);
 document.querySelector('#fly').click(); console.log('fly:',T('#fly')); closeTour(); console.log('closed -> fly:',T('#fly'),'| cards:',q('.card'));
 window.__setZoom(1.4); apply(); console.log('zoomed out -> destinations:',q('.dest'));
 cityFilter='Japan'; apply(); console.log('country filter Japan -> cards:',q('.card'),'| title:',T('#side-title')); cityFilter=null; apply();
 document.querySelector('#f-type').value='Rail'; apply(); console.log('Rail filter -> destinations:',q('.dest'),'| count:',T('#n'));
})();`;
w.__setZoom=z=>{ZOOM=z};
try{ w.eval(s+extra.replace('window.__setZoom(3.2); apply();','window.__setZoom(3.2); apply();')); }catch(e){ console.log('RUNTIME ERR', e.stack.split('\n').slice(0,3).join(' | ')); }
