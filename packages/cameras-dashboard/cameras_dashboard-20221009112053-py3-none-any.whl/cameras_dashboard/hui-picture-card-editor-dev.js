const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, r, n } from './main-dev.js';
import { al as assign, am as object, an as optional, ao as string, aq as assert } from './auth-dev.js';
import './hui-action-editor-dev.js';
import './hui-theme-select-editor-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
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
import './ha-map-dev.js';
import './automation-dev.js';
import './guard-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({image:optional(string()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct)// theme: optional(string()),
}));let HuiPictureCardEditor=_decorate([n("hui-picture-card-editor")],function(_initialize,_LitElement){class HuiPictureCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"get",key:"_image",value:function _image(){return this._config.image||"";}},{kind:"get",key:"_tap_action",value:function _tap_action(){return this._config.tap_action||{action:"none"};}},{kind:"get",key:"_hold_action",value:function _hold_action(){return this._config.hold_action||{action:"none"};}// get _theme(): string {
//   return this._config!.theme || "";
// }
},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const actions=["navigate","url","call-service","none"];return $`
      <div class="card-config">
        <ha-textfield
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.image")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})"
          .value=${this._image}
          .configValue=${"image"}
          @input=${this._valueChanged}
        ></ha-textfield>
        <!-- <hui-theme-select-editor
          .hass=${this.hass}
          .value=${this._theme}
          .configValue=${"theme"}
          @value-changed=${this._valueChanged}
        ></hui-theme-select-editor> -->
        <!-- <div class="side-by-side">
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${actions}
            .configValue=${"tap_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${actions}
            .configValue=${"hold_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
        </div> -->
      </div>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){if(!this._config||!this.hass){return;}const target=ev.target;const value=ev.detail.value;if(this[`_${target.configValue}`]===target.value){return;}if(target.configValue){if(value!==false&&!value){this._config={...this._config};delete this._config[target.configValue];}else {this._config={...this._config,[target.configValue]:value};}}fireEvent(this,"config-changed",{config:this._config});}},{kind:"get",static:true,key:"styles",value:function styles(){return [configElementStyle,r`
        ha-textfield {
          display: block;
          margin-bottom: 8px;
        }
      `];}}]};},s);

export { HuiPictureCardEditor };
