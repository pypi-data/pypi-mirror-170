import{_ as t,c as i,d as s,t as n,$ as e,r as o,n as r}from"./main-d07cb663.js";import{a as c}from"./c.fc0bbf07.js";import{X as a,Z as u}from"./c.37525831.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([r("hui-input-button-entity-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[s({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[n()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return a(this,t)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return e``;const t=this.hass.states[this._config.entity];return t?e`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        <mwc-button
          @click=${this._pressButton}
          .disabled=${t.state===c}
        >
          ${this.hass.localize("ui.card.button.press")}
        </mwc-button>
      </hui-generic-entity-row>
    `:e`
        <hui-warning>
          ${u(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"get",static:!0,key:"styles",value:function(){return o`
      mwc-button:last-child {
        margin-right: -0.57em;
      }
    `}},{kind:"method",key:"_pressButton",value:function(t){t.stopPropagation(),this.hass.callService("input_button","press",{entity_id:this._config.entity})}}]}}),i);
