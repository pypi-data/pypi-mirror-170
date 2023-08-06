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

_decorate([n("more-info-timer")],function(_initialize,_LitElement){class MoreInfoTimer extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoTimer,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}return $`
      <div class="actions">
        ${this.stateObj.state==="idle"||this.stateObj.state==="paused"?$`
              <mwc-button .action=${"start"} @click=${this._handleActionClick}>
                ${this.hass.localize("ui.card.timer.actions.start")}
              </mwc-button>
            `:""}
        ${this.stateObj.state==="active"?$`
              <mwc-button .action=${"pause"} @click=${this._handleActionClick}>
                ${this.hass.localize("ui.card.timer.actions.pause")}
              </mwc-button>
            `:""}
        ${this.stateObj.state==="active"||this.stateObj.state==="paused"?$`
              <mwc-button .action=${"cancel"} @click=${this._handleActionClick}>
                ${this.hass.localize("ui.card.timer.actions.cancel")}
              </mwc-button>
              <mwc-button .action=${"finish"} @click=${this._handleActionClick}>
                ${this.hass.localize("ui.card.timer.actions.finish")}
              </mwc-button>
            `:""}
      </div>
      <ha-attributes
        .hass=${this.hass}
        .stateObj=${this.stateObj}
        extra-filters="remaining"
      ></ha-attributes>
    `;}},{kind:"method",key:"_handleActionClick",value:function _handleActionClick(e){const action=e.currentTarget.action;this.hass.callService("timer",action,{entity_id:this.stateObj.entity_id});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .actions {
        margin: 8px 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
    `;}}]};},s);
