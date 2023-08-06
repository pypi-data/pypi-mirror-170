const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import { al as assign, am as object, an as optional, ao as string, ap as boolean, aq as assert } from './auth-dev.js';
import './hui-action-editor-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './stop_propagation-dev.js';
import './ha-selector-dev.js';
import './dynamic-element-directive-dev.js';
import './compare-dev.js';
import './ha-code-editor-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';
import './ha-form-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './js-yaml-dev.js';
import './device_registry-dev.js';
import './subscribe-mixin-dev.js';
import './brands-url-dev.js';
import './show-media-browser-dialog-dev.js';
import './is-entity-id-dev.js';
import './documentation-url-dev.js';
import './config_entries-dev.js';
import './ha-area-picker-dev.js';
import './ha-time-input-dev.js';
import './hui-theme-select-editor-dev.js';
import './ha-map-dev.js';
import './automation-dev.js';
import './guard-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),image:optional(string()),name:optional(string()),camera_image:optional(string()),camera_view:optional(string()),aspect_ratio:optional(string()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),show_name:optional(boolean()),show_state:optional(boolean()),theme:optional(string())}));const SCHEMA=[{name:"entity",required:true,selector:{entity:{domain:["light","switch","cover","automation","fan"]}}},{name:"name",selector:{text:{}}},{name:"image",selector:{text:{}}}];let HuiPictureEntityCardEditor=_decorate([n("hui-picture-entity-card-editor")],function(_initialize,_LitElement){class HuiPictureEntityCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureEntityCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"get",key:"_tap_action",value:function _tap_action(){return this._config.tap_action||{action:"more-info"};}},{kind:"get",key:"_hold_action",value:function _hold_action(){return this._config.hold_action;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const data={show_state:true,show_name:true,camera_view:"auto",...this._config};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"method",key:"_changed",value:function _changed(ev){if(!this._config||!this.hass){return;}const target=ev.target;const value=ev.detail.value;if(this[`_${target.configValue}`]===value){return;}if(value!==false&&!value){this._config={...this._config};delete this._config[target.configValue];}else {this._config={...this._config,[target.configValue]:value};}fireEvent(this,"config-changed",{config:this._config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.entity");}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.picture-entity.${schema.name}`);};}},{kind:"field",static:true,key:"styles",value(){return configElementStyle;}}]};},s);

export { HuiPictureEntityCardEditor };
