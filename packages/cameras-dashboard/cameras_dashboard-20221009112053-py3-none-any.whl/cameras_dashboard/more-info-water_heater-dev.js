const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { P as PolymerElement, q as html, e4 as Debouncer, e5 as timeOut } from './main-dev.js';
import { E as EventsMixin, x as LocalizeMixin } from './ha-more-info-dialog-dev.js';
import { s as supportsFeature } from './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const featureClassNames=(stateObj,classNames)=>{if(!stateObj||!stateObj.attributes.supported_features){return "";}return Object.keys(classNames).map(feature=>supportsFeature(stateObj,Number(feature))?classNames[feature]:"").filter(attr=>attr!=="").join(" ");};

/*
 * @appliesMixin EventsMixin
 */class HaWaterHeaterControl extends EventsMixin(PolymerElement){static get template(){return html`
      <style include="iron-flex iron-flex-alignment"></style>
      <style>
        /* local DOM styles go here */
        :host {
          @apply --layout-flex;
          @apply --layout-horizontal;
          @apply --layout-justified;
        }
        .in-flux#target_temperature {
          color: var(--error-color);
        }
        #target_temperature {
          @apply --layout-self-center;
          font-size: 200%;
        }
        .control-buttons {
          font-size: 200%;
          text-align: right;
        }
        ha-icon-button {
          height: 48px;
          width: 48px;
        }
      </style>

      <!-- local DOM goes here -->
      <div id="target_temperature">[[value]] [[units]]</div>
      <div class="control-buttons">
        <div>
          <ha-icon-button on-click="incrementValue">
            <ha-icon icon="hass:chevron-up"></ha-icon>
          </ha-icon-button>
        </div>
        <div>
          <ha-icon-button on-click="decrementValue">
            <ha-icon icon="hass:chevron-down"></ha-icon>
          </ha-icon-button>
        </div>
      </div>
    `;}static get properties(){return {value:{type:Number,observer:"valueChanged"},units:{type:String},min:{type:Number},max:{type:Number},step:{type:Number,value:1}};}temperatureStateInFlux(inFlux){this.$.target_temperature.classList.toggle("in-flux",inFlux);}incrementValue(){const newval=this.value+this.step;if(this.value<this.max){this.last_changed=Date.now();this.temperatureStateInFlux(true);}if(newval<=this.max){// If no initial target_temp
// this forces control to start
// from the min configured instead of 0
if(newval<=this.min){this.value=this.min;}else {this.value=newval;}}else {this.value=this.max;}}decrementValue(){const newval=this.value-this.step;if(this.value>this.min){this.last_changed=Date.now();this.temperatureStateInFlux(true);}if(newval>=this.min){this.value=newval;}else {this.value=this.min;}}valueChanged(){// when the last_changed timestamp is changed,
// trigger a potential event fire in
// the future, as long as last changed is far enough in the
// past.
if(this.last_changed){window.setTimeout(()=>{const now=Date.now();if(now-this.last_changed>=2000){this.fire("change");this.temperatureStateInFlux(false);this.last_changed=null;}},2010);}}}customElements.define("ha-water_heater-control",HaWaterHeaterControl);

/*
 * @appliesMixin EventsMixin
 * @appliesMixin LocalizeMixin
 */class MoreInfoWaterHeater extends LocalizeMixin(EventsMixin(PolymerElement)){static get template(){return html`
      <style include="iron-flex"></style>
      <style>
        :host {
          color: var(--primary-text-color);
        }

        ha-select {
          width: 100%;
        }

        ha-water_heater-control.range-control-left,
        ha-water_heater-control.range-control-right {
          float: left;
          width: 46%;
        }
        ha-water_heater-control.range-control-left {
          margin-right: 4%;
        }
        ha-water_heater-control.range-control-right {
          margin-left: 4%;
        }

        .single-row {
          padding: 8px 0;
        }
      </style>

      <div class$="[[computeClassNames(stateObj)]]">
        <div class="container-temperature">
          <div class$="[[stateObj.attributes.operation_mode]]">
            <div hidden$="[[!supportsTemperatureControls(stateObj)]]">
              [[localize('ui.card.water_heater.target_temperature')]]
            </div>
            <template is="dom-if" if="[[supportsTemperature(stateObj)]]">
              <ha-water_heater-control
                value="[[stateObj.attributes.temperature]]"
                units="[[hass.config.unit_system.temperature]]"
                step="[[computeTemperatureStepSize(hass, stateObj)]]"
                min="[[stateObj.attributes.min_temp]]"
                max="[[stateObj.attributes.max_temp]]"
                on-change="targetTemperatureChanged"
              >
              </ha-water_heater-control>
            </template>
          </div>
        </div>

        <template is="dom-if" if="[[supportsOperationMode(stateObj)]]">
          <div class="container-operation_list">
            <div class="controls">
              <ha-select
                label="[[localize('ui.card.water_heater.operation')]]"
                value="[[stateObj.attributes.operation_mode]]"
                on-selected="handleOperationmodeChanged"
                fixedMenuPosition
                naturalMenuWidth
                on-closed="stopPropagation"
              >
                <template
                  is="dom-repeat"
                  items="[[stateObj.attributes.operation_list]]"
                >
                  <mwc-list-item value="[[item]]">
                    [[_localizeOperationMode(localize, item)]]
                  </mwc-list-item>
                </template>
              </ha-select>
            </div>
          </div>
        </template>

        <template is="dom-if" if="[[supportsAwayMode(stateObj)]]">
          <div class="container-away_mode">
            <div class="center horizontal layout single-row">
              <div class="flex">
                [[localize('ui.card.water_heater.away_mode')]]
              </div>
              <ha-switch
                checked="[[awayToggleChecked]]"
                on-change="awayToggleChanged"
              >
              </ha-switch>
            </div>
          </div>
        </template>
      </div>
    `;}static get properties(){return {hass:{type:Object},stateObj:{type:Object,observer:"stateObjChanged"},awayToggleChecked:Boolean};}stateObjChanged(newVal,oldVal){if(newVal){this.setProperties({awayToggleChecked:newVal.attributes.away_mode==="on"});}if(oldVal){this._debouncer=Debouncer.debounce(this._debouncer,timeOut.after(500),()=>{this.fire("iron-resize");});}}computeTemperatureStepSize(hass,stateObj){if(stateObj.attributes.target_temp_step){return stateObj.attributes.target_temp_step;}if(hass.config.unit_system.temperature.indexOf("F")!==-1){return 1;}return 0.5;}supportsTemperatureControls(stateObj){return this.supportsTemperature(stateObj);}supportsTemperature(stateObj){return supportsFeature(stateObj,1)&&typeof stateObj.attributes.temperature==="number";}supportsOperationMode(stateObj){return supportsFeature(stateObj,2);}supportsAwayMode(stateObj){return supportsFeature(stateObj,4);}computeClassNames(stateObj){const _featureClassNames={1:"has-target_temperature",2:"has-operation_mode",4:"has-away_mode"};const classes=[featureClassNames(stateObj,_featureClassNames)];classes.push("more-info-water_heater");return classes.join(" ");}targetTemperatureChanged(ev){const temperature=ev.target.value;if(temperature===this.stateObj.attributes.temperature)return;this.callServiceHelper("set_temperature",{temperature:temperature});}awayToggleChanged(ev){const oldVal=this.stateObj.attributes.away_mode==="on";const newVal=ev.target.checked;if(oldVal===newVal)return;this.callServiceHelper("set_away_mode",{away_mode:newVal});}handleOperationmodeChanged(ev){const oldVal=this.stateObj.attributes.operation_mode;const newVal=ev.target.value;if(!newVal||oldVal===newVal)return;this.callServiceHelper("set_operation_mode",{operation_mode:newVal});}stopPropagation(ev){ev.stopPropagation();}callServiceHelper(service,data){// We call stateChanged after a successful call to re-sync the inputs
// with the state. It will be out of sync if our service call did not
// result in the entity to be turned on. Since the state is not changing,
// the resync is not called automatic.
/* eslint-disable no-param-reassign */data.entity_id=this.stateObj.entity_id;/* eslint-enable no-param-reassign */this.hass.callService("water_heater",service,data).then(()=>{this.stateObjChanged(this.stateObj);});}_localizeOperationMode(localize,mode){return localize(`component.water_heater.state._.${mode}`)||mode;}}customElements.define("more-info-water_heater",MoreInfoWaterHeater);
