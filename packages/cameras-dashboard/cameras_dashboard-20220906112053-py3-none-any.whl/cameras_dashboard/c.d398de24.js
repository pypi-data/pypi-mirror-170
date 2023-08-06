import{_ as t,c as e,d as i,$ as s,r,n as a}from"./main-d07cb663.js";import"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([a("more-info-script")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function(){return this.hass&&this.stateObj?s`
      <hr />
      <div class="flex">
        <div>
          ${this.hass.localize("ui.dialogs.more_info_control.script.last_triggered")}:
        </div>
        ${this.stateObj.attributes.last_triggered?s`
              <ha-relative-time
                .hass=${this.hass}
                .datetime=${this.stateObj.attributes.last_triggered}
                capitalize
              ></ha-relative-time>
            `:this.hass.localize("ui.components.relative_time.never")}
      </div>
    `:s``}},{kind:"get",static:!0,key:"styles",value:function(){return r`
      .flex {
        display: flex;
        justify-content: space-between;
      }
      hr {
        border-color: var(--divider-color);
        border-bottom: none;
        margin: 16px 0;
      }
    `}}]}}),e);
