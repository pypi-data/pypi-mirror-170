import{_ as t,c as i,d as e,$ as s,r as a,n as r}from"./main-d07cb663.js";import"./c.37525831.js";import{t as o}from"./c.3a0ccb1a.js";import{h as c}from"./c.fc0bbf07.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([r("more-info-automation")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:!1})],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function(){return this.hass&&this.stateObj?s`
      <hr />
      <div class="flex">
        <div>${this.hass.localize("ui.card.automation.last_triggered")}:</div>
        <ha-relative-time
          .hass=${this.hass}
          .datetime=${this.stateObj.attributes.last_triggered}
          capitalize
        ></ha-relative-time>
      </div>

      <div class="actions">
        <mwc-button
          @click=${this._runActions}
          .disabled=${c.includes(this.stateObj.state)}
        >
          ${this.hass.localize("ui.card.automation.trigger")}
        </mwc-button>
      </div>
    `:s``}},{kind:"method",key:"_runActions",value:function(){o(this.hass,this.stateObj.entity_id)}},{kind:"get",static:!0,key:"styles",value:function(){return a`
      .flex {
        display: flex;
        justify-content: space-between;
      }
      .actions {
        margin: 8px 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
      hr {
        border-color: var(--divider-color);
        border-bottom: none;
        margin: 16px 0;
      }
    `}}]}}),i);
