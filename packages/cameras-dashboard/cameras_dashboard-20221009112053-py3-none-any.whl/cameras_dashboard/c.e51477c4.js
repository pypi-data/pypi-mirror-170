import{_ as e,c as i,d as t,t as s,$ as a,f as o,r as n,n as c}from"./main-d07cb663.js";import"./c.c8cf0377.js";import{al as r,am as d,as as h,an as f,ao as m,ax as l,aq as u}from"./c.fc0bbf07.js";import"./c.25c3182d.js";import{p}from"./c.9bf416cd.js";import{e as g}from"./c.b0065faf.js";import{b as _}from"./c.885af130.js";import"./c.9c88d99b.js";import"./c.95ef015c.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";import"./c.f9f3b7e4.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.ebfe053a.js";const b=r(_,d({entities:h(g),title:f(m()),hours_to_show:f(l()),refresh_interval:f(l())})),k=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"hours_to_show",selector:{number:{min:1,mode:"box"}}},{name:"refresh_interval",selector:{number:{min:1,mode:"box"}}}]}];let v=e([c("hui-history-graph-card-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"field",decorators:[s()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function(e){u(e,b),this._config=e,this._configEntities=p(e.entities)}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?a`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${k}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <hui-entity-editor
        .hass=${this.hass}
        .entities=${this._configEntities}
        @entities-changed=${this._entitiesChanged}
      ></hui-entity-editor>
    `:a``}},{kind:"method",key:"_valueChanged",value:function(e){o(this,"config-changed",{config:e.detail.value})}},{kind:"method",key:"_entitiesChanged",value:function(e){let i=this._config;i={...i,entities:e.detail.entities},this._configEntities=p(i.entities),o(this,"config-changed",{config:i})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}},{kind:"field",static:!0,key:"styles",value:()=>n`
    ha-form {
      margin-bottom: 24px;
    }
  `}]}}),i);export{v as HuiHistoryGraphCardEditor};
