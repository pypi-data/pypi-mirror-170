import{_ as e,c as a,d as t,t as i,$ as s,f as c,n as o}from"./main-d07cb663.js";import"./c.c8cf0377.js";import{al as r,am as n,an as d,ao as l,aq as m}from"./c.fc0bbf07.js";import{b as u}from"./c.885af130.js";import"./c.9c88d99b.js";import"./c.95ef015c.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";const f=r(u,n({title:d(l()),url:d(l()),aspect_ratio:d(l())})),h=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"url",required:!0,selector:{text:{}}},{name:"aspect_ratio",selector:{text:{}}}]}];let p=e([o("hui-iframe-card-editor")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(e){m(e,f),this._config=e}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?s`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${h}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `:s``}},{kind:"method",key:"_valueChanged",value:function(e){c(this,"config-changed",{config:e.detail.value})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}}]}}),a);export{p as HuiIframeCardEditor};
