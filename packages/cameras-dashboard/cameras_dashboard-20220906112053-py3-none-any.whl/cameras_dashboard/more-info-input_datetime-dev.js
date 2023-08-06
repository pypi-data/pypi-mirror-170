const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, n } from './main-dev.js';
import { s as stateToIsoDateString, a as setInputDateTimeValue } from './input_datetime-dev.js';
import './ha-time-input-dev.js';
import { h as UNAVAILABLE_STATES, U as UNKNOWN } from './auth-dev.js';
import './ha-base-time-input-dev.js';
import './stop_propagation-dev.js';

_decorate([n("more-info-input_datetime")],function(_initialize,_LitElement){class MoreInfoInputDatetime extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoInputDatetime,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.stateObj){return $``;}return $`
        ${this.stateObj.attributes.has_date?$`
                <ha-date-input
                  .locale=${this.hass.locale}
                  .value=${stateToIsoDateString(this.stateObj)}
                  .disabled=${UNAVAILABLE_STATES.includes(this.stateObj.state)}
                  @value-changed=${this._dateChanged}
                >
                </ha-date-input>
              `:``}
        ${this.stateObj.attributes.has_time?$`
                <ha-time-input
                  .value=${this.stateObj.state===UNKNOWN?"":this.stateObj.attributes.has_date?this.stateObj.state.split(" ")[1]:this.stateObj.state}
                  .locale=${this.hass.locale}
                  .disabled=${UNAVAILABLE_STATES.includes(this.stateObj.state)}
                  @value-changed=${this._timeChanged}
                  @click=${this._stopEventPropagation}
                ></ha-time-input>
              `:``}
      </hui-generic-entity-row>
    `;}},{kind:"method",key:"_stopEventPropagation",value:function _stopEventPropagation(ev){ev.stopPropagation();}},{kind:"method",key:"_timeChanged",value:function _timeChanged(ev){setInputDateTimeValue(this.hass,this.stateObj.entity_id,ev.detail.value,this.stateObj.attributes.has_date?this.stateObj.state.split(" ")[0]:undefined);ev.target.blur();}},{kind:"method",key:"_dateChanged",value:function _dateChanged(ev){setInputDateTimeValue(this.hass,this.stateObj.entity_id,this.stateObj.attributes.has_time?this.stateObj.state.split(" ")[1]:undefined,ev.detail.value);ev.target.blur();}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: flex;
        align-items: center;
        justify-content: flex-end;
      }
      ha-date-input + ha-time-input {
        margin-left: 4px;
      }
    `;}}]};},s);
