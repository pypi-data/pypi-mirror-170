const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, G as i, $, dY as mdiChevronUp, H as mdiChevronDown, f as fireEvent, r, n, z as o, j as _get, k as _getPrototypeOf } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import { s as supportsFeature } from './auth-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';
import { c as conditionalClamp, a as CLIMATE_SUPPORT_TARGET_TEMPERATURE, b as CLIMATE_SUPPORT_TARGET_TEMPERATURE_RANGE, e as CLIMATE_SUPPORT_TARGET_HUMIDITY, g as CLIMATE_SUPPORT_FAN_MODE, h as CLIMATE_SUPPORT_PRESET_MODE, i as CLIMATE_SUPPORT_SWING_MODE, j as CLIMATE_SUPPORT_AUX_HEAT, k as compareClimateHvacModes } from './ha-more-info-dialog-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("ha-climate-control")],function(_initialize,_LitElement){class HaClimateControl extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaClimateControl,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e()],key:"unit",value(){return "";}},{kind:"field",decorators:[e()],key:"min",value:void 0},{kind:"field",decorators:[e()],key:"max",value:void 0},{kind:"field",decorators:[e()],key:"step",value(){return 1;}},{kind:"field",key:"_lastChanged",value:void 0},{kind:"field",decorators:[i("#target_temperature")],key:"_targetTemperature",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      <div id="target_temperature">${this.value} ${this.unit}</div>
      <div class="control-buttons">
        <div>
          <ha-icon-button
            .path=${mdiChevronUp}
            .label=${this.hass.localize("ui.components.climate-control.temperature_up")}
            @click=${this._incrementValue}
          >
          </ha-icon-button>
        </div>
        <div>
          <ha-icon-button
            .path=${mdiChevronDown}
            .label=${this.hass.localize("ui.components.climate-control.temperature_down")}
            @click=${this._decrementValue}
          >
          </ha-icon-button>
        </div>
      </div>
    `;}},{kind:"method",key:"updated",value:function updated(changedProperties){if(changedProperties.has("value")){this._valueChanged();}}},{kind:"method",key:"_temperatureStateInFlux",value:function _temperatureStateInFlux(inFlux){this._targetTemperature.classList.toggle("in-flux",inFlux);}},{kind:"method",key:"_round",value:function _round(value){// Round value to precision derived from step.
// Inspired by https://github.com/soundar24/roundSlider/blob/master/src/roundslider.js
const s=this.step.toString().split(".");return s[1]?parseFloat(value.toFixed(s[1].length)):Math.round(value);}},{kind:"method",key:"_incrementValue",value:function _incrementValue(){const newValue=this._round(this.value+this.step);this._processNewValue(newValue);}},{kind:"method",key:"_decrementValue",value:function _decrementValue(){const newValue=this._round(this.value-this.step);this._processNewValue(newValue);}},{kind:"method",key:"_processNewValue",value:function _processNewValue(value){const newValue=conditionalClamp(value,this.min,this.max);if(this.value!==newValue){this.value=newValue;this._lastChanged=Date.now();this._temperatureStateInFlux(true);}}},{kind:"method",key:"_valueChanged",value:function _valueChanged(){// When the last_changed timestamp is changed,
// trigger a potential event fire in the future,
// as long as last_changed is far enough in the past.
if(this._lastChanged){window.setTimeout(()=>{const now=Date.now();if(now-this._lastChanged>=2000){fireEvent(this,"change");this._temperatureStateInFlux(false);this._lastChanged=undefined;}},2010);}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: flex;
        justify-content: space-between;
      }
      .in-flux {
        color: var(--error-color);
      }
      #target_temperature {
        align-self: center;
        font-size: 28px;
        direction: ltr;
      }
      .control-buttons {
        font-size: 24px;
        text-align: right;
      }
      ha-icon-button {
        --mdc-icon-size: 32px;
      }
    `;}}]};},s);

let MoreInfoClimate=_decorate(null,function(_initialize,_LitElement){class MoreInfoClimate extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoClimate,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"field",key:"_resizeDebounce",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.stateObj){return $``;}const hass=this.hass;const stateObj=this.stateObj;const supportTargetTemperature=supportsFeature(stateObj,CLIMATE_SUPPORT_TARGET_TEMPERATURE);const supportTargetTemperatureRange=supportsFeature(stateObj,CLIMATE_SUPPORT_TARGET_TEMPERATURE_RANGE);const supportTargetHumidity=supportsFeature(stateObj,CLIMATE_SUPPORT_TARGET_HUMIDITY);const supportFanMode=supportsFeature(stateObj,CLIMATE_SUPPORT_FAN_MODE);const supportPresetMode=supportsFeature(stateObj,CLIMATE_SUPPORT_PRESET_MODE);const supportSwingMode=supportsFeature(stateObj,CLIMATE_SUPPORT_SWING_MODE);const supportAuxHeat=supportsFeature(stateObj,CLIMATE_SUPPORT_AUX_HEAT);const temperatureStepSize=stateObj.attributes.target_temp_step||(hass.config.unit_system.temperature.indexOf("F")===-1?0.5:1);const rtlDirection=computeRTLDirection(hass);return $`
      <div
        class=${o({"has-current_temperature":"current_temperature"in stateObj.attributes,"has-current_humidity":"current_humidity"in stateObj.attributes,"has-target_temperature":supportTargetTemperature,"has-target_temperature_range":supportTargetTemperatureRange,"has-target_humidity":supportTargetHumidity,"has-fan_mode":supportFanMode,"has-swing_mode":supportSwingMode,"has-aux_heat":supportAuxHeat,"has-preset_mode":supportPresetMode})}
      >
        <div class="container-temperature">
          <div class=${stateObj.state}>
            ${supportTargetTemperature||supportTargetTemperatureRange?$`
                  <div>
                    ${hass.localize("ui.card.climate.target_temperature")}
                  </div>
                `:""}
            ${stateObj.attributes.temperature!==undefined&&stateObj.attributes.temperature!==null?$`
                  <ha-climate-control
                    .hass=${this.hass}
                    .value=${stateObj.attributes.temperature}
                    .unit=${hass.config.unit_system.temperature}
                    .step=${temperatureStepSize}
                    .min=${stateObj.attributes.min_temp}
                    .max=${stateObj.attributes.max_temp}
                    @change=${this._targetTemperatureChanged}
                  ></ha-climate-control>
                `:""}
            ${stateObj.attributes.target_temp_low!==undefined&&stateObj.attributes.target_temp_low!==null||stateObj.attributes.target_temp_high!==undefined&&stateObj.attributes.target_temp_high!==null?$`
                  <ha-climate-control
                    .hass=${this.hass}
                    .value=${stateObj.attributes.target_temp_low}
                    .unit=${hass.config.unit_system.temperature}
                    .step=${temperatureStepSize}
                    .min=${stateObj.attributes.min_temp}
                    .max=${stateObj.attributes.target_temp_high}
                    class="range-control-left"
                    @change=${this._targetTemperatureLowChanged}
                  ></ha-climate-control>
                  <ha-climate-control
                    .hass=${this.hass}
                    .value=${stateObj.attributes.target_temp_high}
                    .unit=${hass.config.unit_system.temperature}
                    .step=${temperatureStepSize}
                    .min=${stateObj.attributes.target_temp_low}
                    .max=${stateObj.attributes.max_temp}
                    class="range-control-right"
                    @change=${this._targetTemperatureHighChanged}
                  ></ha-climate-control>
                `:""}
          </div>
        </div>

        ${supportTargetHumidity?$`
              <div class="container-humidity">
                <div>${hass.localize("ui.card.climate.target_humidity")}</div>
                <div class="single-row">
                  <div class="target-humidity">
                    ${stateObj.attributes.humidity} %
                  </div>
                  <ha-slider
                    step="1"
                    pin
                    ignore-bar-touch
                    dir=${rtlDirection}
                    .min=${stateObj.attributes.min_humidity}
                    .max=${stateObj.attributes.max_humidity}
                    .value=${stateObj.attributes.humidity}
                    @change=${this._targetHumiditySliderChanged}
                  >
                  </ha-slider>
                </div>
              </div>
            `:""}

        <div class="container-hvac_modes">
          <div class="controls">
            <ha-select
              .label=${hass.localize("ui.card.climate.operation")}
              .value=${stateObj.state}
              fixedMenuPosition
              naturalMenuWidth
              @selected=${this._handleOperationmodeChanged}
              @closed=${stopPropagation}
            >
              ${stateObj.attributes.hvac_modes.concat().sort(compareClimateHvacModes).map(mode=>$`
                    <mwc-list-item .value=${mode}>
                      ${hass.localize(`component.climate.state._.${mode}`)}
                    </mwc-list-item>
                  `)}
            </ha-select>
          </div>
        </div>

        ${supportPresetMode&&stateObj.attributes.preset_modes?$`
              <div class="container-preset_modes">
                <ha-select
                  .label=${hass.localize("ui.card.climate.preset_mode")}
                  .value=${stateObj.attributes.preset_mode}
                  fixedMenuPosition
                  naturalMenuWidth
                  @selected=${this._handlePresetmodeChanged}
                  @closed=${stopPropagation}
                >
                  ${stateObj.attributes.preset_modes.map(mode=>$`
                      <mwc-list-item .value=${mode}>
                        ${hass.localize(`state_attributes.climate.preset_mode.${mode}`)||mode}
                      </mwc-list-item>
                    `)}
                </ha-select>
              </div>
            `:""}
        ${supportFanMode&&stateObj.attributes.fan_modes?$`
              <div class="container-fan_list">
                <ha-select
                  .label=${hass.localize("ui.card.climate.fan_mode")}
                  .value=${stateObj.attributes.fan_mode}
                  fixedMenuPosition
                  naturalMenuWidth
                  @selected=${this._handleFanmodeChanged}
                  @closed=${stopPropagation}
                >
                  ${stateObj.attributes.fan_modes.map(mode=>$`
                      <mwc-list-item .value=${mode}>
                        ${hass.localize(`state_attributes.climate.fan_mode.${mode}`)||mode}
                      </mwc-list-item>
                    `)}
                </ha-select>
              </div>
            `:""}
        ${supportSwingMode&&stateObj.attributes.swing_modes?$`
              <div class="container-swing_list">
                <ha-select
                  .label=${hass.localize("ui.card.climate.swing_mode")}
                  .value=${stateObj.attributes.swing_mode}
                  fixedMenuPosition
                  naturalMenuWidth
                  @selected=${this._handleSwingmodeChanged}
                  @closed=${stopPropagation}
                >
                  ${stateObj.attributes.swing_modes.map(mode=>$`
                      <mwc-list-item .value=${mode}>${mode}</mwc-list-item>
                    `)}
                </ha-select>
              </div>
            `:""}
        ${supportAuxHeat?$`
              <div class="container-aux_heat">
                <div class="center horizontal layout single-row">
                  <div class="flex">
                    ${hass.localize("ui.card.climate.aux_heat")}
                  </div>
                  <ha-switch
                    .checked=${stateObj.attributes.aux_heat==="on"}
                    @change=${this._auxToggleChanged}
                  ></ha-switch>
                </div>
              </div>
            `:""}
      </div>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(MoreInfoClimate.prototype),"updated",this).call(this,changedProps);if(!changedProps.has("stateObj")||!this.stateObj){return;}if(this._resizeDebounce){clearTimeout(this._resizeDebounce);}this._resizeDebounce=window.setTimeout(()=>{fireEvent(this,"iron-resize");this._resizeDebounce=undefined;},500);}},{kind:"method",key:"_targetTemperatureChanged",value:function _targetTemperatureChanged(ev){const newVal=ev.target.value;this._callServiceHelper(this.stateObj.attributes.temperature,newVal,"set_temperature",{temperature:newVal});}},{kind:"method",key:"_targetTemperatureLowChanged",value:function _targetTemperatureLowChanged(ev){const newVal=ev.currentTarget.value;this._callServiceHelper(this.stateObj.attributes.target_temp_low,newVal,"set_temperature",{target_temp_low:newVal,target_temp_high:this.stateObj.attributes.target_temp_high});}},{kind:"method",key:"_targetTemperatureHighChanged",value:function _targetTemperatureHighChanged(ev){const newVal=ev.currentTarget.value;this._callServiceHelper(this.stateObj.attributes.target_temp_high,newVal,"set_temperature",{target_temp_low:this.stateObj.attributes.target_temp_low,target_temp_high:newVal});}},{kind:"method",key:"_targetHumiditySliderChanged",value:function _targetHumiditySliderChanged(ev){const newVal=ev.target.value;this._callServiceHelper(this.stateObj.attributes.humidity,newVal,"set_humidity",{humidity:newVal});}},{kind:"method",key:"_auxToggleChanged",value:function _auxToggleChanged(ev){const newVal=ev.target.checked;this._callServiceHelper(this.stateObj.attributes.aux_heat==="on",newVal,"set_aux_heat",{aux_heat:newVal});}},{kind:"method",key:"_handleFanmodeChanged",value:function _handleFanmodeChanged(ev){const newVal=ev.target.value;this._callServiceHelper(this.stateObj.attributes.fan_mode,newVal,"set_fan_mode",{fan_mode:newVal});}},{kind:"method",key:"_handleOperationmodeChanged",value:function _handleOperationmodeChanged(ev){const newVal=ev.target.value;this._callServiceHelper(this.stateObj.state,newVal,"set_hvac_mode",{hvac_mode:newVal});}},{kind:"method",key:"_handleSwingmodeChanged",value:function _handleSwingmodeChanged(ev){const newVal=ev.target.value;this._callServiceHelper(this.stateObj.attributes.swing_mode,newVal,"set_swing_mode",{swing_mode:newVal});}},{kind:"method",key:"_handlePresetmodeChanged",value:function _handlePresetmodeChanged(ev){const newVal=ev.target.value||null;this._callServiceHelper(this.stateObj.attributes.preset_mode,newVal,"set_preset_mode",{preset_mode:newVal});}},{kind:"method",key:"_callServiceHelper",value:async function _callServiceHelper(oldVal,newVal,service,data){if(oldVal===newVal){return;}data.entity_id=this.stateObj.entity_id;const curState=this.stateObj;await this.hass.callService("climate",service,data);// We reset stateObj to re-sync the inputs with the state. It will be out
// of sync if our service call did not result in the entity to be turned
// on. Since the state is not changing, the resync is not called automatic.
await new Promise(resolve=>setTimeout(resolve,2000));// No need to resync if we received a new state.
if(this.stateObj!==curState){return;}this.stateObj=undefined;await this.updateComplete;// Only restore if not set yet by a state change
if(this.stateObj===undefined){this.stateObj=curState;}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        color: var(--primary-text-color);
      }

      ha-select {
        width: 100%;
        margin-top: 8px;
      }

      ha-slider {
        width: 100%;
      }

      .container-humidity .single-row {
        display: flex;
        height: 50px;
      }

      .target-humidity {
        width: 90px;
        font-size: 200%;
        margin: auto;
        direction: ltr;
      }

      ha-climate-control.range-control-left,
      ha-climate-control.range-control-right {
        float: left;
        width: 46%;
      }
      ha-climate-control.range-control-left {
        margin-right: 4%;
      }
      ha-climate-control.range-control-right {
        margin-left: 4%;
      }

      .single-row {
        padding: 8px 0;
      }
    `;}}]};},s);customElements.define("more-info-climate",MoreInfoClimate);
