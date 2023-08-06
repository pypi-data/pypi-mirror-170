import{_ as t,c as i,d as s,t as o,$ as e,r as n,n as r}from"./main-d07cb663.js";import{X as c,Z as a,_ as h}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([r("hui-cover-entity-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[s({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[o()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return c(this,t)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return e``;const t=this.hass.states[this._config.entity];return t?e`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        ${"medium"!==this._config.layout?h(t)?e`
                <ha-cover-tilt-controls
                  .hass=${this.hass}
                  .stateObj=${t}
                ></ha-cover-tilt-controls>
              `:e`
                <ha-cover-controls
                  .hass=${this.hass}
                  .stateObj=${t}
                ></ha-cover-controls>
              `:e``}
      </hui-generic-entity-row>
    `:e`
        <hui-warning>
          ${a(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"get",static:!0,key:"styles",value:function(){return n`
      ha-cover-controls,
      ha-cover-tilt-controls {
        margin-right: -0.57em;
      }
    `}}]}}),i);
