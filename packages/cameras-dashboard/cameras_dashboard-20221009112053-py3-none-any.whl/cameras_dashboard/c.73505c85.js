import{_ as t,c as e,d as i,t as o,$ as r,z as s,r as n,n as a}from"./main-d07cb663.js";import{e as d}from"./c.fc0bbf07.js";import{U as c}from"./c.37525831.js";import"./c.a7a081d2.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";let l=t([a("hui-buttons-header-footer")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"method",static:!0,key:"getStubConfig",value:function(){return{entities:[]}}},{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"type",value:void 0},{kind:"field",decorators:[o()],key:"_configEntities",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(t){this._configEntities=c(t.entities).map((t=>{const e={tap_action:{action:"toggle"},hold_action:{action:"more-info"},...t};return"scene"===d(t.entity)&&(e.tap_action={action:"call-service",service:"scene.turn_on",target:{entity_id:e.entity}}),e}))}},{kind:"method",key:"render",value:function(){return r`
      ${"footer"===this.type?r`<li class="divider footer" role="separator"></li>`:""}
      <hui-buttons-base
        .hass=${this.hass}
        .configEntities=${this._configEntities}
        class=${s({footer:"footer"===this.type,header:"header"===this.type})}
      ></hui-buttons-base>
      ${"header"===this.type?r`<li class="divider header" role="separator"></li>`:""}
    `}},{kind:"field",static:!0,key:"styles",value:()=>n`
    .divider {
      height: 0;
      margin: 16px 0;
      list-style-type: none;
      border: none;
      border-bottom-width: 1px;
      border-bottom-style: solid;
      border-bottom-color: var(--divider-color);
    }
    .divider.header {
      margin-top: 0;
    }
    hui-buttons-base.footer {
      --padding-bottom: 16px;
    }
    hui-buttons-base.header {
      --padding-top: 16px;
    }
  `}]}}),e);export{l as HuiButtonsHeaderFooter};
