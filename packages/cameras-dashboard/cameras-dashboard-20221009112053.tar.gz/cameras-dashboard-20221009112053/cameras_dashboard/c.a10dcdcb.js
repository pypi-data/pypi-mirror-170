import{_ as i,c as e,d as a,t,b as o,$ as c,f as s,r as n,n as l}from"./main-d07cb663.js";import{al as r,am as d,an as h,ao as f,aq as m,C as u,e as g}from"./c.fc0bbf07.js";import"./c.ae68c3e2.js";import{c as p}from"./c.70b58286.js";import{b as _}from"./c.885af130.js";import"./c.95ef015c.js";import"./c.6c5cb033.js";import"./c.9c88d99b.js";import"./c.d294c310.js";import"./c.6dd7f489.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.c8cf0377.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";import"./c.5fe2e3ab.js";import"./c.2036cb65.js";import"./c.65b9d701.js";import"./c.c245ec1a.js";import"./c.c9178224.js";import"./c.bd9a7167.js";import"./c.1ded644c.js";import"./c.da136530.js";import"./c.fb31f48a.js";import"./c.2ff699c8.js";import"./c.650fd31d.js";import"./c.2465bf13.js";import"./c.3a0ccb1a.js";import"./c.f9f3b7e4.js";const b=r(_,d({name:h(f()),entity:h(f()),theme:h(f()),icon:h(f())}));let j=i([l("hui-light-card-editor")],(function(i,e){return{F:class extends e{constructor(...e){super(...e),i(this)}},d:[{kind:"field",decorators:[a({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(i){m(i,b),this._config=i}},{kind:"field",key:"_schema",value:()=>o(((i,e,a)=>[{name:"entity",required:!0,selector:{entity:{domain:"light"}}},{name:"",type:"grid",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{placeholder:e||(null==a?void 0:a.attributes.icon),fallbackPath:e||null!=a&&a.attributes.icon||!a||!i?void 0:u(g(i),a)}}}]}]))},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return c``;const i=["more-info","toggle","navigate","url","call-service","none"],e=this.hass.states[this._config.entity],a=this._schema(this._config.entity,this._config.icon,e);return c`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${a}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <!-- <div class="card-config">
        <hui-action-editor
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
          .hass=${this.hass}
          .config=${this._hold_action}
          .actions=${i}
          .configValue=${"hold_action"}
          @value-changed=${this._actionChanged}
        ></hui-action-editor>

        <hui-action-editor
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.double_tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
          .hass=${this.hass}
          .config=${this._double_tap_action}
          .actions=${i}
          .configValue=${"double_tap_action"}
          @value-changed=${this._actionChanged}
        ></hui-action-editor>
      </div> -->
    `}},{kind:"method",key:"_actionChanged",value:function(i){if(!this._config||!this.hass)return;const e=i.target,a=i.detail.value;this[`_${e.configValue}`]!==a&&(e.configValue&&(!1===a||a?this._config={...this._config,[e.configValue]:a}:(this._config={...this._config},delete this._config[e.configValue])),s(this,"config-changed",{config:this._config}))}},{kind:"method",key:"_valueChanged",value:function(i){s(this,"config-changed",{config:i.detail.value})}},{kind:"field",key:"_computeLabelCallback",value(){return i=>"entity"===i.name?this.hass.localize("ui.panel.lovelace.editor.card.generic.entity"):this.hass.localize(`ui.panel.lovelace.editor.card.generic.${i.name}`)}},{kind:"field",static:!0,key:"styles",value:()=>[p,n`
      /* ha-form,
      hui-action-editor {
        display: block;
        margin-bottom: 24px;
        overflow: auto;
      } */
    `]}]}}),e);export{j as HuiLightCardEditor};
