import{_ as t,c as e,d as i,t as s,$ as a,r as n,n as r}from"./main-d07cb663.js";import{j as o,a as c,h}from"./c.fc0bbf07.js";import{s as d}from"./c.c1dd06c9.js";import{X as u,Z as l}from"./c.37525831.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([r("hui-input-text-entity-row")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return u(this,t)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return a``;const t=this.hass.states[this._config.entity];return t?a`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        hideName
      >
        <ha-textfield
          .label=${this._config.name||o(t)}
          .disabled=${t.state===c}
          .value=${t.state}
          .minlength=${t.attributes.min}
          .maxlength=${t.attributes.max}
          .autoValidate=${t.attributes.pattern}
          .pattern=${t.attributes.pattern}
          .type=${t.attributes.mode}
          @change=${this._selectedValueChanged}
          placeholder="(empty value)"
        ></ha-textfield>
      </hui-generic-entity-row>
    `:a`
        <hui-warning>
          ${l(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"method",key:"_selectedValueChanged",value:function(t){const e=this.hass.states[this._config.entity],i=t.target.value;i&&h.includes(i)?t.target.value=e.state:(i!==e.state&&d(this.hass,e.entity_id,i),t.target.blur())}},{kind:"field",static:!0,key:"styles",value:()=>n`
    hui-generic-entity-row {
      display: flex;
      align-items: center;
    }
    ha-textfield {
      width: 100%;
    }
  `}]}}),e);
