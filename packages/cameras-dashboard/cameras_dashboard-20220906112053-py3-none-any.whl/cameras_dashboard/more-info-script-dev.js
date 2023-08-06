const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, n } from './main-dev.js';
import './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("more-info-script")],function(_initialize,_LitElement){class MoreInfoScript extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoScript,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}return $`
      <hr />
      <div class="flex">
        <div>
          ${this.hass.localize("ui.dialogs.more_info_control.script.last_triggered")}:
        </div>
        ${this.stateObj.attributes.last_triggered?$`
              <ha-relative-time
                .hass=${this.hass}
                .datetime=${this.stateObj.attributes.last_triggered}
                capitalize
              ></ha-relative-time>
            `:this.hass.localize("ui.components.relative_time.never")}
      </div>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .flex {
        display: flex;
        justify-content: space-between;
      }
      hr {
        border-color: var(--divider-color);
        border-bottom: none;
        margin: 16px 0;
      }
    `;}}]};},s);
