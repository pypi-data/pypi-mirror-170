import{_ as t,c as e,d as r,t as a,$ as s,z as o,b as i,eE as n,eF as d,ev as l,eG as c,eH as u,eI as f,r as _,n as g}from"./main-d07cb663.js";import{w as h}from"./c.37525831.js";import{f as y,x as m,j as p}from"./c.fc0bbf07.js";import{s as b,a as k,g as v}from"./c.db8c8161.js";import{S as j}from"./c.65b9d701.js";import{i as x}from"./c.144e89ef.js";import{d as O,c as z}from"./c.655d6539.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";import"./c.c13d4687.js";import"./c.da136530.js";let S=t([g("hui-energy-usage-graph-card")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[r({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"field",decorators:[a()],key:"_chartData",value:()=>({datasets:[]})},{kind:"field",decorators:[a()],key:"_start",value:()=>b()},{kind:"field",decorators:[a()],key:"_end",value:()=>k()},{kind:"field",key:"hassSubscribeRequiredHostProps",value:()=>["_config"]},{kind:"method",key:"hassSubscribe",value:function(){var t;return[v(this.hass,{key:null===(t=this._config)||void 0===t?void 0:t.collection_key}).subscribe((t=>this._getStatistics(t)))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(t){this._config=t}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?s`
      <ha-card>
        ${this._config.title?s`<h1 class="card-header">${this._config.title}</h1>`:""}
        <div
          class="content ${o({"has-header":!!this._config.title})}"
        >
          <ha-chart-base
            .data=${this._chartData}
            .options=${this._createOptions(this._start,this._end,this.hass.locale)}
            chart-type="bar"
          ></ha-chart-base>
          ${this._chartData.datasets.some((t=>t.data.length))?"":s`<div class="no-data">
                ${x(this._start)?this.hass.localize("ui.panel.lovelace.cards.energy.no_data"):this.hass.localize("ui.panel.lovelace.cards.energy.no_data_period")}
              </div>`}
        </div>
      </ha-card>
    `:s``}},{kind:"field",key:"_createOptions",value(){return i(((t,e,r)=>{const a=O(e,t);return{parsing:!1,animation:!1,scales:{x:{type:"time",suggestedMin:t.getTime(),suggestedMax:e.getTime(),adapters:{date:{locale:r}},ticks:{maxRotation:0,sampleSize:5,autoSkipPadding:20,major:{enabled:!0},font:t=>t.tick&&t.tick.major?{weight:"bold"}:{}},time:{tooltipFormat:a>35?"monthyear":a>7?"date":a>2?"weekday":a>0?"datetime":"hour",minUnit:a>35?"month":a>2?"day":"hour"},offset:!0},y:{stacked:!0,type:"linear",title:{display:!0,text:"kWh"},ticks:{beginAtZero:!0,callback:t=>y(Math.abs(t),r)}}},plugins:{tooltip:{mode:"x",intersect:!0,position:"nearest",filter:t=>"0"!==t.formattedValue,callbacks:{title:t=>{if(a>0)return t[0].label;const e=new Date(t[0].parsed.x);return`${h(e,r)} – ${h(z(e,1),r)}`},label:t=>`${t.dataset.label}: ${y(Math.abs(t.parsed.y),r)} kWh`,footer:t=>{let e=0,a=0;for(const r of t){const t=r.dataset.data[r.dataIndex].y;t>0?e+=t:a+=Math.abs(t)}return[e?this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.total_consumed",{num:y(e,r)}):"",a?this.hass.localize("ui.panel.lovelace.cards.energyenergy_usage_graph.total_returned",{num:y(a,r)}):""].filter(Boolean)}}},filler:{propagate:!1},legend:{display:!1,labels:{usePointStyle:!0}}},hover:{mode:"nearest"},elements:{bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:5}},locale:m(r)}}))}},{kind:"method",key:"_getStatistics",value:async function(t){const e=[],r={};for(const e of t.prefs.energy_sources)if("solar"!==e.type)if("battery"!==e.type){if("grid"===e.type){for(const t of e.flow_from)r.from_grid?r.from_grid.push(t.stat_energy_from):r.from_grid=[t.stat_energy_from];for(const t of e.flow_to)r.to_grid?r.to_grid.push(t.stat_energy_to):r.to_grid=[t.stat_energy_to]}}else r.to_battery?(r.to_battery.push(e.stat_energy_to),r.from_battery.push(e.stat_energy_from)):(r.to_battery=[e.stat_energy_to],r.from_battery=[e.stat_energy_from]);else r.solar?r.solar.push(e.stat_energy_from):r.solar=[e.stat_energy_from];this._start=t.start,this._end=t.end||k();const a={},s={},o=getComputedStyle(this),i={to_grid:o.getPropertyValue("--energy-grid-return-color").trim(),to_battery:o.getPropertyValue("--energy-battery-in-color").trim(),from_grid:o.getPropertyValue("--energy-grid-consumption-color").trim(),used_grid:o.getPropertyValue("--energy-grid-consumption-color").trim(),used_solar:o.getPropertyValue("--energy-solar-color").trim(),used_battery:o.getPropertyValue("--energy-battery-out-color").trim()},_={used_grid:this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.combined_from_grid"),used_solar:this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.consumed_solar"),used_battery:this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.consumed_battery")};Object.entries(r).forEach((([e,r])=>{const o=["solar","to_grid","from_grid","to_battery","from_battery"].includes(e),i=!["solar","from_battery"].includes(e),n={},d={};r.forEach((e=>{const r=t.stats[e];if(!r)return;const a={};let s;r.forEach((t=>{if(null===t.sum)return;if(void 0===s)return void(s=t.sum);const e=t.sum-s;o&&(n[t.start]=t.start in n?n[t.start]+e:e),i&&!(t.start in a)&&(a[t.start]=e),s=t.sum})),d[e]=a})),o&&(s[e]=n),i&&(a[e]=d)}));const g={},h={};if((s.to_grid||s.to_battery)&&s.solar){const t={};for(const e of Object.keys(s.solar)){var y,m;if(t[e]=(s.solar[e]||0)-((null===(y=s.to_grid)||void 0===y?void 0:y[e])||0)-((null===(m=s.to_battery)||void 0===m?void 0:m[e])||0),t[e]<0){var b,v,j;if(s.to_battery)if(g[e]=-1*t[e],g[e]>((null===(b=s.from_grid)||void 0===b?void 0:b[e])||0))h[e]=Math.min(0,g[e]-((null===(v=s.from_grid)||void 0===v?void 0:v[e])||0)),g[e]=null===(j=s.from_grid)||void 0===j?void 0:j[e];t[e]=0}}a.used_solar={used_solar:t}}if(s.from_battery)if(s.to_grid){const t={};for(const e of Object.keys(s.from_battery))t[e]=(s.from_battery[e]||0)-(h[e]||0);a.used_battery={used_battery:t}}else a.used_battery={used_battery:s.from_battery};if(a.from_grid&&s.to_battery){const t={};for(const e of Object.keys(g)){let r,s=0;for(const[t,o]of Object.entries(a.from_grid))if(o[e]&&(r=t,s++),s>1)break;if(1===s)a.from_grid[r][e]-=g[e]||0;else{let r=0;Object.values(a.from_grid).forEach((t=>{r+=t[e]||0,delete t[e]})),t[e]=r-(g[e]||0)}}a.used_grid={used_grid:t}}let x=[];Object.values(a).forEach((t=>{Object.values(t).forEach((t=>{x=x.concat(Object.keys(t))}))}));const O=Array.from(new Set(x));Object.entries(a).forEach((([t,r])=>{Object.entries(r).forEach((([r,s],o)=>{const g=[],h=this.hass.states[r],y=o>0?this.hass.themes.darkMode?n(d(l(i[t])),o):c(d(l(i[t])),o):void 0,m=y?u(f(y)):i[t];g.push({label:t in _?_[t]:h?p(h):r,order:"used_solar"===t?0:"to_battery"===t?Object.keys(a).length:o+1,borderColor:m,backgroundColor:m+"7F",stack:"stack",data:[]});for(const e of O){const r=s[e]||0,a=new Date(e);g[0].data.push({x:a.getTime(),y:r&&["to_grid","to_battery"].includes(t)?-1*r:r})}Array.prototype.push.apply(e,g)}))})),this._chartData={datasets:e}}},{kind:"get",static:!0,key:"styles",value:function(){return _`
      ha-card {
        height: 100%;
      }
      .card-header {
        padding-bottom: 0;
      }
      .content {
        padding: 16px;
      }
      .has-header {
        padding-top: 0;
      }
      .no-data {
        position: absolute;
        height: 100%;
        top: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20%;
        margin-left: 32px;
        box-sizing: border-box;
      }
    `}}]}}),j(e));export{S as HuiEnergyUsageGraphCard};
