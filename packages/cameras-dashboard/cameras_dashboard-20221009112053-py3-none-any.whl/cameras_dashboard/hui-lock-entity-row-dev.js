const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { h as UNAVAILABLE_STATES } from './auth-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-lock-entity-row")],function(_initialize,_LitElement){class HuiLockEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiLockEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        <mwc-button
          @click=${this._callService}
          .disabled=${UNAVAILABLE_STATES.includes(stateObj.state)}
          class="text-content"
        >
          ${stateObj.state==="locked"?this.hass.localize("ui.card.lock.unlock"):this.hass.localize("ui.card.lock.lock")}
        </mwc-button>
      </hui-generic-entity-row>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      mwc-button {
        margin-right: -0.57em;
      }
    `;}},{kind:"method",key:"_callService",value:function _callService(ev){ev.stopPropagation();const stateObj=this.hass.states[this._config.entity];this.hass.callService("lock",stateObj.state==="locked"?"unlock":"lock",{entity_id:stateObj.entity_id});}}]};},s);
