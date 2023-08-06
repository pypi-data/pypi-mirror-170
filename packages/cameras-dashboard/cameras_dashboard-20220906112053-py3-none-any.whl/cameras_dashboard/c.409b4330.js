import{_ as t,c as i,d as s,$ as e,n as o}from"./main-d07cb663.js";import{X as r,Z as n}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([o("hui-humidifier-entity-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[s()],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t||!t.entity)throw new Error("Entity must be specified");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return r(this,t)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return e``;const t=this.hass.states[this._config.entity];return t?e`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        .secondaryText=${t.attributes.humidity?`${this.hass.localize("ui.card.humidifier.humidity")}:\n            ${t.attributes.humidity} %${t.attributes.mode?` (${this.hass.localize(`state_attributes.humidifier.mode.${t.attributes.mode}`)||t.attributes.mode})`:""}`:""}
      >
        <ha-entity-toggle
          .hass=${this.hass}
          .stateObj=${t}
        ></ha-entity-toggle>
      </hui-generic-entity-row>
    `:e`
        <hui-warning>
          ${n(this.hass,this._config.entity)}
        </hui-warning>
      `}}]}}),i);
