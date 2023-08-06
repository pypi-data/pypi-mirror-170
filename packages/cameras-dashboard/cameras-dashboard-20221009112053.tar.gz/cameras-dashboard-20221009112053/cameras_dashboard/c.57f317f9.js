import{_ as t,c as a,d as s,t as e,G as i,$ as o,z as r,b as n,f as c,r as d,n as h}from"./main-d07cb663.js";import{aj as l}from"./c.adc013f3.js";import{ae as u,ag as p,ah as f}from"./c.37525831.js";import{j as m,f as v,x as k}from"./c.fc0bbf07.js";import{g as b}from"./c.db8c8161.js";import{S as g}from"./c.65b9d701.js";import{d as _,c as y}from"./c.655d6539.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";import"./c.c13d4687.js";import"./c.da136530.js";let j=t([h("hui-energy-devices-graph-card")],(function(t,a){return{F:class extends a{constructor(...a){super(...a),t(this)}},d:[{kind:"field",decorators:[s({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"field",decorators:[e()],key:"_data",value:void 0},{kind:"field",decorators:[e()],key:"_chartData",value:()=>({datasets:[]})},{kind:"field",decorators:[i("ha-chart-base")],key:"_chart",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:()=>["_config"]},{kind:"method",key:"hassSubscribe",value:function(){var t;return[b(this.hass,{key:null===(t=this._config)||void 0===t?void 0:t.collection_key}).subscribe((t=>this._getStatistics(t)))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(t){this._config=t}},{kind:"method",key:"render",value:function(){var t,a;return this.hass&&this._config?o`
      <ha-card>
        ${this._config.title?o`<h1 class="card-header">${this._config.title}</h1>`:""}
        <div
          class="content ${r({"has-header":!!this._config.title})}"
        >
          <ha-chart-base
            .data=${this._chartData}
            .options=${this._createOptions(this.hass.locale)}
            .height=${28*((null===(t=this._chartData)||void 0===t||null===(a=t.datasets[0])||void 0===a?void 0:a.data.length)||0)+50}
            chart-type="bar"
          ></ha-chart-base>
        </div>
      </ha-card>
    `:o``}},{kind:"field",key:"_createOptions",value(){return n((t=>({parsing:!1,animation:!1,responsive:!0,maintainAspectRatio:!1,indexAxis:"y",scales:{y:{type:"category",ticks:{autoSkip:!1,callback:t=>{const a=this._chartData.datasets[0].data[t].y,s=this.hass.states[a];return s?m(s):a}}},x:{title:{display:!0,text:"kWh"}}},elements:{bar:{borderWidth:1.5,borderRadius:4}},plugins:{tooltip:{mode:"nearest",callbacks:{title:t=>{const a=this.hass.states[t[0].label];return a?m(a):t[0].label},label:a=>`${a.dataset.label}: ${v(a.parsed.x,t)} kWh`}}},locale:k(this.hass.locale),onClick:t=>{var a,s,e;const i=t.chart,o=l(t,i),r=Math.abs(i.scales.y.getValueForPixel(o.y));c(this,"hass-more-info",{entityId:null===(a=this._chartData)||void 0===a||null===(s=a.datasets[0])||void 0===s||null===(e=s.data[r])||void 0===e?void 0:e.y})}})))}},{kind:"method",key:"_getStatistics",value:async function(t){var a;const s=_(t.end||new Date,t.start);this._data=await u(this.hass,y(t.start,-1),t.end,t.prefs.device_consumption.map((t=>t.stat_consumption)),s>35?"month":s>2?"day":"hour");const e=y(t.start,-1);Object.values(this._data).forEach((t=>{t.length&&new Date(t[0].start)>e&&t.unshift({...t[0],start:e.toISOString(),end:e.toISOString(),sum:0,state:0})}));const i=[],o=[],r=[],n=[{label:this.hass.localize("ui.panel.lovelace.cards.energy.energy_devices_graph.energy_usage"),borderColor:o,backgroundColor:r,data:i,barThickness:20}];t.prefs.device_consumption.forEach(((t,a)=>{const s=t.stat_consumption in this._data&&p(this._data[t.stat_consumption])||0;i.push({y:t.stat_consumption,x:s,idx:a})})),i.sort(((t,a)=>a.x-t.x)),i.forEach((t=>{const a=f(t.idx);o.push(a),r.push(a+"7F")})),this._chartData={datasets:n},await this.updateComplete,null===(a=this._chart)||void 0===a||a.updateChart("none")}},{kind:"get",static:!0,key:"styles",value:function(){return d`
      .card-header {
        padding-bottom: 0;
      }
      .content {
        padding: 16px;
      }
      .has-header {
        padding-top: 0;
      }
      ha-chart-base {
        --chart-max-height: none;
      }
    `}}]}}),g(a));export{j as HuiEnergyDevicesGraphCard};
