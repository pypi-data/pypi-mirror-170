import{_ as a,c as e,d as t,t as i,$ as o,f as s,n as r}from"./main-d07cb663.js";import{al as c,am as n,an as l,ao as d,ap as h,aq as m}from"./c.fc0bbf07.js";import"./c.c8cf0377.js";import{b as u}from"./c.885af130.js";import"./c.95ef015c.js";import"./c.9c88d99b.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";const f=c(u,n({area:l(d()),navigation_path:l(d()),theme:l(d()),show_camera:l(h())})),p=[{name:"area",selector:{area:{}}},{name:"show_camera",required:!1,selector:{boolean:{}}},{name:"",type:"grid",schema:[{name:"navigation_path",required:!1,selector:{text:{}}},{name:"theme",required:!1,selector:{theme:{}}}]}];let v=a([r("hui-area-card-editor")],(function(a,e){return{F:class extends e{constructor(...e){super(...e),a(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(a){m(a,f),this._config=a}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?o`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${p}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `:o``}},{kind:"method",key:"_valueChanged",value:function(a){const e=a.detail.value;s(this,"config-changed",{config:e})}},{kind:"field",key:"_computeLabelCallback",value(){return a=>{switch(a.name){case"area":return this.hass.localize("ui.panel.lovelace.editor.card.area.name");case"navigation_path":return this.hass.localize("ui.panel.lovelace.editor.action-editor.navigation_path")}return this.hass.localize(`ui.panel.lovelace.editor.card.area.${a.name}`)}}}]}}),e);export{v as HuiAreaCardEditor};
