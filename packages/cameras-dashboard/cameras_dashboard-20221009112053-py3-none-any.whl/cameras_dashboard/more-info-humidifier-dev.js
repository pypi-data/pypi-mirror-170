const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, z as o, j as _get, k as _getPrototypeOf, f as fireEvent, r } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import { s as supportsFeature } from './auth-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';

const HUMIDIFIER_SUPPORT_MODES=1;

let MoreInfoHumidifier=_decorate(null,function(_initialize,_LitElement){class MoreInfoHumidifier extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoHumidifier,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"field",key:"_resizeDebounce",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.stateObj){return $``;}const hass=this.hass;const stateObj=this.stateObj;const supportModes=supportsFeature(stateObj,HUMIDIFIER_SUPPORT_MODES);const rtlDirection=computeRTLDirection(hass);return $`
      <div
        class=${o({"has-modes":supportModes})}
      >
        <div class="container-humidity">
          <div>${hass.localize("ui.card.humidifier.humidity")}</div>
          <div class="single-row">
            <div class="target-humidity">${stateObj.attributes.humidity} %</div>
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

        ${supportModes?$`
              <ha-select
                .label=${hass.localize("ui.card.humidifier.mode")}
                .value=${stateObj.attributes.mode}
                fixedMenuPosition
                naturalMenuWidth
                @selected=${this._handleModeChanged}
                @closed=${stopPropagation}
              >
                ${stateObj.attributes.available_modes.map(mode=>$`
                    <mwc-list-item .value=${mode}>
                      ${hass.localize(`state_attributes.humidifier.mode.${mode}`)||mode}
                    </mwc-list-item>
                  `)}
              </ha-select>
            `:""}
      </div>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(MoreInfoHumidifier.prototype),"updated",this).call(this,changedProps);if(!changedProps.has("stateObj")||!this.stateObj){return;}if(this._resizeDebounce){clearTimeout(this._resizeDebounce);}this._resizeDebounce=window.setTimeout(()=>{fireEvent(this,"iron-resize");this._resizeDebounce=undefined;},500);}},{kind:"method",key:"_targetHumiditySliderChanged",value:function _targetHumiditySliderChanged(ev){const newVal=ev.target.value;this._callServiceHelper(this.stateObj.attributes.humidity,newVal,"set_humidity",{humidity:newVal});}},{kind:"method",key:"_handleModeChanged",value:function _handleModeChanged(ev){const newVal=ev.target.value||null;this._callServiceHelper(this.stateObj.attributes.mode,newVal,"set_mode",{mode:newVal});}},{kind:"method",key:"_callServiceHelper",value:async function _callServiceHelper(oldVal,newVal,service,data){if(oldVal===newVal){return;}data.entity_id=this.stateObj.entity_id;const curState=this.stateObj;await this.hass.callService("humidifier",service,data);// We reset stateObj to re-sync the inputs with the state. It will be out
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

      .single-row {
        padding: 8px 0;
      }
    `;}}]};},s);customElements.define("more-info-humidifier",MoreInfoHumidifier);
