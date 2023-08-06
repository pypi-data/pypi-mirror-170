const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { j as computeStateName, a as UNAVAILABLE, h as UNAVAILABLE_STATES } from './auth-dev.js';
import { s as setValue } from './input_text-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-input-text-entity-row")],function(_initialize,_LitElement){class HuiInputTextEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiInputTextEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        hideName
      >
        <ha-textfield
          .label=${this._config.name||computeStateName(stateObj)}
          .disabled=${stateObj.state===UNAVAILABLE}
          .value=${stateObj.state}
          .minlength=${stateObj.attributes.min}
          .maxlength=${stateObj.attributes.max}
          .autoValidate=${stateObj.attributes.pattern}
          .pattern=${stateObj.attributes.pattern}
          .type=${stateObj.attributes.mode}
          @change=${this._selectedValueChanged}
          placeholder="(empty value)"
        ></ha-textfield>
      </hui-generic-entity-row>
    `;}},{kind:"method",key:"_selectedValueChanged",value:function _selectedValueChanged(ev){const stateObj=this.hass.states[this._config.entity];const newValue=ev.target.value;// Filter out invalid text states
if(newValue&&UNAVAILABLE_STATES.includes(newValue)){ev.target.value=stateObj.state;return;}if(newValue!==stateObj.state){setValue(this.hass,stateObj.entity_id,newValue);}ev.target.blur();}},{kind:"field",static:true,key:"styles",value(){return r`
    hui-generic-entity-row {
      display: flex;
      align-items: center;
    }
    ha-textfield {
      width: 100%;
    }
  `;}}]};},s);
