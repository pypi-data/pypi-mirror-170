import{_ as e,c as i,d as a,t,b as s,$ as c,f as o,r as n,n as l}from"./main-d07cb663.js";import"./c.e60a95ea.js";import"./c.c8cf0377.js";import{al as r,am as d,an as h,ar as m,ao as u,ap as f,as as p,aq as v}from"./c.fc0bbf07.js";import{b as k}from"./c.885af130.js";import"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.9c88d99b.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";const g=r(k,d({title:h(m([u(),f()])),initial_view:h(u()),theme:h(u()),entities:p(u())})),_=["dayGridMonth","dayGridDay","listWeek"];let j=e([l("hui-calendar-card-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[a({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(e){v(e,g),this._config=e}},{kind:"field",key:"_schema",value:()=>s((e=>[{name:"",type:"grid",schema:[{name:"title",required:!1,selector:{text:{}}},{name:"initial_view",required:!1,selector:{select:{options:_.map((i=>[i,e(`ui.panel.lovelace.editor.card.calendar.views.${i}`)]))}}}]},{name:"theme",required:!1,selector:{theme:{}}}]))},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return c``;const e=this._schema(this.hass.localize),i={initial_view:"dayGridMonth",...this._config};return c`
      <ha-form
        .hass=${this.hass}
        .data=${i}
        .schema=${e}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <h3>
        ${this.hass.localize("ui.panel.lovelace.editor.card.calendar.calendar_entities")+" ("+this.hass.localize("ui.panel.lovelace.editor.card.config.required")+")"}
      </h3>
      <ha-entities-picker
        .hass=${this.hass}
        .value=${this._config.entities}
        .includeDomains=${["calendar"]}
        @value-changed=${this._entitiesChanged}
      >
      </ha-entities-picker>
    `}},{kind:"method",key:"_valueChanged",value:function(e){const i=e.detail.value;o(this,"config-changed",{config:i})}},{kind:"method",key:"_entitiesChanged",value:function(e){const i={...this._config,entities:e.detail.value};o(this,"config-changed",{config:i})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>"title"===e.name?this.hass.localize("ui.panel.lovelace.editor.card.generic.title"):this.hass.localize(`ui.panel.lovelace.editor.card.calendar.${e.name}`)}},{kind:"field",static:!0,key:"styles",value:()=>n`
    ha-form {
      display: block;
      overflow: auto;
    }
  `}]}}),i);export{j as HuiCalendarCardEditor};
