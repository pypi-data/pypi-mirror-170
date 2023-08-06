import{_ as e,c as t,d as i,t as s,$ as a,f as o,n}from"./main-d07cb663.js";import"./c.c8cf0377.js";import{al as c,am as r,an as d,ar as h,ao as m,ax as l,ap as f,as as u,aq as _}from"./c.fc0bbf07.js";import"./c.25c3182d.js";import{p}from"./c.9bf416cd.js";import{e as g}from"./c.b0065faf.js";import{b}from"./c.885af130.js";import"./c.9c88d99b.js";import"./c.95ef015c.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";import"./c.f9f3b7e4.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.ebfe053a.js";const k=c(b,r({title:d(h([m(),l()])),theme:d(m()),columns:d(l()),show_name:d(f()),show_state:d(f()),show_icon:d(f()),state_color:d(f()),entities:u(g)})),j=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"columns",selector:{number:{min:1,mode:"box"}}},{name:"theme",selector:{theme:{}}}]},{name:"",type:"grid",column_min_width:"100px",schema:[{name:"show_name",selector:{boolean:{}}},{name:"show_icon",selector:{boolean:{}}},{name:"show_state",selector:{boolean:{}}}]},{name:"state_color",selector:{boolean:{}}}];let v=e([n("hui-glance-card-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"field",decorators:[s()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function(e){_(e,k),this._config=e,this._configEntities=p(e.entities)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return a``;const e={show_name:!0,show_icon:!0,show_state:!0,...this._config};return a`
      <ha-form
        .hass=${this.hass}
        .data=${e}
        .schema=${j}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <hui-entity-editor
        .hass=${this.hass}
        .entities=${this._configEntities}
        @entities-changed=${this._entitiesChanged}
      ></hui-entity-editor>
    `}},{kind:"method",key:"_valueChanged",value:function(e){const t=e.detail.value;o(this,"config-changed",{config:t})}},{kind:"method",key:"_entitiesChanged",value:function(e){let t=this._config;t={...t,entities:e.detail.entities},this._configEntities=p(this._config.entities),o(this,"config-changed",{config:t})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>this.hass.localize(`ui.panel.lovelace.editor.card.glance.${e.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}}]}}),t);export{v as HuiGlanceCardEditor};
