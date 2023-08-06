import{_ as t,c as i,d as s,t as e,$ as c,r as n,n as o}from"./main-d07cb663.js";import{h as a}from"./c.fc0bbf07.js";import{X as r,Z as h}from"./c.37525831.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([o("hui-lock-entity-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[s({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return r(this,t)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return c``;const t=this.hass.states[this._config.entity];return t?c`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        <mwc-button
          @click=${this._callService}
          .disabled=${a.includes(t.state)}
          class="text-content"
        >
          ${"locked"===t.state?this.hass.localize("ui.card.lock.unlock"):this.hass.localize("ui.card.lock.lock")}
        </mwc-button>
      </hui-generic-entity-row>
    `:c`
        <hui-warning>
          ${h(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"get",static:!0,key:"styles",value:function(){return n`
      mwc-button {
        margin-right: -0.57em;
      }
    `}},{kind:"method",key:"_callService",value:function(t){t.stopPropagation();const i=this.hass.states[this._config.entity];this.hass.callService("lock","locked"===i.state?"unlock":"lock",{entity_id:i.entity_id})}}]}}),i);
