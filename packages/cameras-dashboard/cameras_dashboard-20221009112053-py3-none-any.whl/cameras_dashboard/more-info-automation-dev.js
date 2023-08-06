const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, n } from './main-dev.js';
import './ha-more-info-dialog-dev.js';
import { t as triggerAutomationActions } from './automation-dev.js';
import { h as UNAVAILABLE_STATES } from './auth-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("more-info-automation")],function(_initialize,_LitElement){class MoreInfoAutomation extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoAutomation,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}return $`
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
          .disabled=${UNAVAILABLE_STATES.includes(this.stateObj.state)}
        >
          ${this.hass.localize("ui.card.automation.trigger")}
        </mwc-button>
      </div>
    `;}},{kind:"method",key:"_runActions",value:function _runActions(){triggerAutomationActions(this.hass,this.stateObj.entity_id);}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
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
    `;}}]};},s);
