const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import { j as computeStateName, a as UNAVAILABLE, k as forwardHaptic } from './auth-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, a0 as setSelectOption } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-select-entity-row")],function(_initialize,_LitElement){class HuiSelectEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiSelectEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.entity){throw new Error("Entity must be specified");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        hideName
      >
        <ha-select
          .label=${this._config.name||computeStateName(stateObj)}
          .value=${stateObj.state}
          .disabled=${stateObj.state===UNAVAILABLE}
          naturalMenuWidth
          @selected=${this._selectedChanged}
          @click=${stopPropagation}
          @closed=${stopPropagation}
        >
          ${stateObj.attributes.options?stateObj.attributes.options.map(option=>$`
                    <mwc-list-item .value=${option}
                      >${stateObj.attributes.device_class&&this.hass.localize(`component.select.state.${stateObj.attributes.device_class}.${option}`)||this.hass.localize(`component.select.state._.${option}`)||option}
                    </mwc-list-item>
                  `):""}
        </ha-select>
      </hui-generic-entity-row>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      hui-generic-entity-row {
        display: flex;
        align-items: center;
      }
      ha-select {
        width: 100%;
      }
    `;}},{kind:"method",key:"_selectedChanged",value:function _selectedChanged(ev){const stateObj=this.hass.states[this._config.entity];const option=ev.target.value;if(option===stateObj.state){return;}forwardHaptic("light");setSelectOption(this.hass,stateObj.entity_id,option);}}]};},s);
