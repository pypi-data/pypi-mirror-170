import{_ as t,c as i,d as e,t as s,$ as a,r as n,n as o}from"./main-d07cb663.js";import{s as h,a as r}from"./c.98305d6e.js";import{j as d,h as c,U as u}from"./c.fc0bbf07.js";import{X as l,Z as f}from"./c.37525831.js";import"./c.2ff699c8.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";import"./c.379373ef.js";t([o("hui-input-datetime-entity-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return l(this,t)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return a``;const t=this.hass.states[this._config.entity];if(!t)return a`
        <hui-warning>
          ${f(this.hass,this._config.entity)}
        </hui-warning>
      `;const i=this._config.name||d(t);return a`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        .hideName=${t.attributes.has_date&&t.attributes.has_time}
      >
        ${t.attributes.has_date?a`
              <ha-date-input
                .label=${t.attributes.has_time?i:void 0}
                .locale=${this.hass.locale}
                .disabled=${c.includes(t.state)}
                .value=${h(t)}
                @value-changed=${this._dateChanged}
              >
              </ha-date-input>
            `:""}
        ${t.attributes.has_time?a`
              <ha-time-input
                .value=${t.state===u?"":t.attributes.has_date?t.state.split(" ")[1]:t.state}
                .locale=${this.hass.locale}
                .disabled=${c.includes(t.state)}
                @value-changed=${this._timeChanged}
                @click=${this._stopEventPropagation}
              ></ha-time-input>
            `:""}
      </hui-generic-entity-row>
    `}},{kind:"method",key:"_stopEventPropagation",value:function(t){t.stopPropagation()}},{kind:"method",key:"_timeChanged",value:function(t){const i=this.hass.states[this._config.entity];r(this.hass,i.entity_id,t.detail.value,i.attributes.has_date?i.state.split(" ")[0]:void 0),t.target.blur()}},{kind:"method",key:"_dateChanged",value:function(t){const i=this.hass.states[this._config.entity];r(this.hass,i.entity_id,i.attributes.has_time?i.state.split(" ")[1]:void 0,t.detail.value),t.target.blur()}},{kind:"get",static:!0,key:"styles",value:function(){return n`
      ha-date-input + ha-time-input {
        margin-left: 4px;
      }
    `}}]}}),i);
