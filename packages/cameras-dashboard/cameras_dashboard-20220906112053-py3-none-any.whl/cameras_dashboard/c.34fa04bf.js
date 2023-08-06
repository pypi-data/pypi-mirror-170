import{_ as e,c as a,d as t,t as i,$ as s,f as o,n as c}from"./main-d07cb663.js";import"./c.c8cf0377.js";import{al as n,am as r,an as d,ao as l,aq as m}from"./c.fc0bbf07.js";import{b as h}from"./c.885af130.js";import"./c.9c88d99b.js";import"./c.95ef015c.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";const u=n(h,r({entity:d(l()),name:d(l()),theme:d(l())})),f=[{name:"entity",required:!0,selector:{entity:{domain:"plant"}}},{name:"name",selector:{text:{}}},{name:"theme",selector:{theme:{}}}];let p=e([c("hui-plant-status-card-editor")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(e){m(e,u),this._config=e}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?s`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${f}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `:s``}},{kind:"method",key:"_valueChanged",value:function(e){o(this,"config-changed",{config:e.detail.value})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>"entity"===e.name?this.hass.localize("ui.panel.lovelace.editor.card.generic.entity"):this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}}]}}),a);export{p as HuiPlantStatusCardEditor};
