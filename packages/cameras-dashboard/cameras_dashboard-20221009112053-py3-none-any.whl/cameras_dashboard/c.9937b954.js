import{_ as t,c as i,d as o,t as e,$ as s,n}from"./main-d07cb663.js";import{L as c,e as a}from"./c.fc0bbf07.js";import{U as r}from"./c.37525831.js";import"./c.a7a081d2.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";let f=t([n("hui-buttons-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"method",static:!0,key:"getStubConfig",value:function(){return{entities:[]}}},{kind:"field",decorators:[o({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function(t){this._configEntities=r(t.entities).map((t=>({tap_action:{action:t.entity&&c.has(a(t.entity))?"toggle":"more-info"},hold_action:{action:"more-info"},...t})))}},{kind:"method",key:"render",value:function(){return s`
      <hui-buttons-base
        .hass=${this.hass}
        .configEntities=${this._configEntities}
      ></hui-buttons-base>
    `}}]}}),i);export{f as HuiButtonsRow};
