const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { s as stateToIsoDateString, a as setInputDateTimeValue } from './input_datetime-dev.js';
import { j as computeStateName, h as UNAVAILABLE_STATES, U as UNKNOWN } from './auth-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning } from './ha-more-info-dialog-dev.js';
import './ha-time-input-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './ha-base-time-input-dev.js';

_decorate([n("hui-input-datetime-entity-row")],function(_initialize,_LitElement){class HuiInputDatetimeEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiInputDatetimeEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const name=this._config.name||computeStateName(stateObj);return $`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        .hideName=${stateObj.attributes.has_date&&stateObj.attributes.has_time}
      >
        ${stateObj.attributes.has_date?$`
              <ha-date-input
                .label=${stateObj.attributes.has_time?name:undefined}
                .locale=${this.hass.locale}
                .disabled=${UNAVAILABLE_STATES.includes(stateObj.state)}
                .value=${stateToIsoDateString(stateObj)}
                @value-changed=${this._dateChanged}
              >
              </ha-date-input>
            `:``}
        ${stateObj.attributes.has_time?$`
              <ha-time-input
                .value=${stateObj.state===UNKNOWN?"":stateObj.attributes.has_date?stateObj.state.split(" ")[1]:stateObj.state}
                .locale=${this.hass.locale}
                .disabled=${UNAVAILABLE_STATES.includes(stateObj.state)}
                @value-changed=${this._timeChanged}
                @click=${this._stopEventPropagation}
              ></ha-time-input>
            `:``}
      </hui-generic-entity-row>
    `;}},{kind:"method",key:"_stopEventPropagation",value:function _stopEventPropagation(ev){ev.stopPropagation();}},{kind:"method",key:"_timeChanged",value:function _timeChanged(ev){const stateObj=this.hass.states[this._config.entity];setInputDateTimeValue(this.hass,stateObj.entity_id,ev.detail.value,stateObj.attributes.has_date?stateObj.state.split(" ")[0]:undefined);ev.target.blur();}},{kind:"method",key:"_dateChanged",value:function _dateChanged(ev){const stateObj=this.hass.states[this._config.entity];setInputDateTimeValue(this.hass,stateObj.entity_id,stateObj.attributes.has_time?stateObj.state.split(" ")[1]:undefined,ev.detail.value);ev.target.blur();}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-date-input + ha-time-input {
        margin-left: 4px;
      }
    `;}}]};},s);
