const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, n } from './main-dev.js';
import { Z as createEntityNotFoundWarning, a1 as computeDisplayTimer, X as hasConfigOrEntityChanged, a2 as timerTimeRemaining } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-timer-entity-row")],function(_initialize,_LitElement){class HuiTimerEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiTimerEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_timeRemaining",value:void 0},{kind:"field",key:"_interval",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;if(!this.hass){return;}const stateObj=this.hass.states[this._config.entity];if(stateObj){this._startInterval(stateObj);}else {this._clearInterval();}}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){_get(_getPrototypeOf(HuiTimerEntityRow.prototype),"disconnectedCallback",this).call(this);this._clearInterval();}},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiTimerEntityRow.prototype),"connectedCallback",this).call(this);if(this._config&&this._config.entity){var _this$hass;const stateObj=(_this$hass=this.hass)===null||_this$hass===void 0?void 0:_this$hass.states[this._config.entity];if(stateObj){this._startInterval(stateObj);}}}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        <div class="text-content">
          ${computeDisplayTimer(this.hass,stateObj,this._timeRemaining)}
        </div>
      </hui-generic-entity-row>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("_timeRemaining")){return true;}return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiTimerEntityRow.prototype),"updated",this).call(this,changedProps);if(!this._config||!changedProps.has("hass")){return;}const stateObj=this.hass.states[this._config.entity];const oldHass=changedProps.get("hass");const oldStateObj=oldHass?oldHass.states[this._config.entity]:undefined;if(oldStateObj!==stateObj){this._startInterval(stateObj);}else if(!stateObj){this._clearInterval();}}},{kind:"method",key:"_clearInterval",value:function _clearInterval(){if(this._interval){window.clearInterval(this._interval);this._interval=undefined;}}},{kind:"method",key:"_startInterval",value:function _startInterval(stateObj){this._clearInterval();this._calculateRemaining(stateObj);if(stateObj.state==="active"){this._interval=window.setInterval(()=>this._calculateRemaining(stateObj),1000);}}},{kind:"method",key:"_calculateRemaining",value:function _calculateRemaining(stateObj){this._timeRemaining=timerTimeRemaining(stateObj);}}]};},s);
