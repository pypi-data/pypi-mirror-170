const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, f as fireEvent, $, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, ap as boolean, aq as assert, a as UNAVAILABLE } from './auth-dev.js';
import { P as memoize } from './ha-more-info-dialog-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),name:optional(string()),theme:optional(string()),show_current:optional(boolean()),show_forecast:optional(boolean()),secondary_info_attribute:optional(string()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),double_tap_action:optional(actionConfigStruct)}));let HuiWeatherForecastCardEditor=_decorate([n("hui-weather-forecast-card-editor")],function(_initialize,_LitElement){class HuiWeatherForecastCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiWeatherForecastCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;if(/* cannot show forecast in case it is unavailable on the entity */config.show_forecast===true&&this._has_forecast===false||/* cannot hide both weather and forecast, need one of them */config.show_current===false&&config.show_forecast===false){/* reset to sane default, show weather, but hide forecast */fireEvent(this,"config-changed",{config:{...config,show_current:true,show_forecast:false}});}}},{kind:"get",key:"_has_forecast",value:function _has_forecast(){if(this.hass&&this._config){const stateObj=this.hass.states[this._config.entity];if(stateObj&&stateObj.state!==UNAVAILABLE){var _stateObj$attributes$;return !!((_stateObj$attributes$=stateObj.attributes.forecast)!==null&&_stateObj$attributes$!==void 0&&_stateObj$attributes$.length);}}return undefined;}},{kind:"field",key:"_schema",value(){return memoize(()=>{const schema=[{name:"entity",required:true,selector:{entity:{domain:"weather"}}},{name:"name",selector:{text:{}}},{name:"",type:"grid",schema:[// {
//   name: "secondary_info_attribute",
//   selector: { attribute: { entity_id: entity } },
// },
// { name: "theme", selector: { theme: {} } },
]}];// if (hasForecast) {
//   schema.push({
//     name: "forecast",
//     selector: {
//       select: {
//         options: [
//           {
//             value: "show_both",
//             label: localize(
//               "ui.panel.lovelace.editor.card.weather-forecast.show_both"
//             ),
//           },
//           {
//             value: "show_current",
//             label: localize(
//               "ui.panel.lovelace.editor.card.weather-forecast.show_only_current"
//             ),
//           },
//           {
//             value: "show_forecast",
//             label: localize(
//               "ui.panel.lovelace.editor.card.weather-forecast.show_only_forecast"
//             ),
//           },
//         ],
//       },
//     },
//   });
// }
return schema;});}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const schema=this._schema(this._config.entity,this.hass.localize,this._has_forecast);const data={show_current:true,show_forecast:this._has_forecast,...this._config};data.forecast=data.show_current&&data.show_forecast?"show_both":data.show_current?"show_current":"show_forecast";return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;if(config.forecast==="show_both"){config.show_current=true;config.show_forecast=true;}else if(config.forecast==="show_current"){config.show_current=true;config.show_forecast=false;}else {config.show_current=false;config.show_forecast=true;}delete config.forecast;fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return `${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})`;}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.weather_forecast.${schema.name}`);};}}]};},s);

export { HuiWeatherForecastCardEditor };
