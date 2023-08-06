const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import './hui-action-editor-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, as as array, aq as assert } from './auth-dev.js';
import './hui-entity-editor-dev.js';
import { p as processEditorEntities } from './process-editor-entities-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { e as entitiesConfigStruct } from './entities-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './stop_propagation-dev.js';
import './ha-selector-dev.js';
import './dynamic-element-directive-dev.js';
import './compare-dev.js';
import './ha-code-editor-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';
import './js-yaml-dev.js';
import './device_registry-dev.js';
import './subscribe-mixin-dev.js';
import './brands-url-dev.js';
import './show-media-browser-dialog-dev.js';
import './is-entity-id-dev.js';
import './documentation-url-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './config_entries-dev.js';
import './ha-area-picker-dev.js';
import './ha-time-input-dev.js';
import './ha-base-time-input-dev.js';
import './hui-theme-select-editor-dev.js';
import './ha-map-dev.js';
import './automation-dev.js';
import './guard-dev.js';
import './ha-check-list-item-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({title:optional(string()),entity:optional(string()),image:optional(string()),camera_image:optional(string()),camera_view:optional(string()),aspect_ratio:optional(string()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),entities:array(entitiesConfigStruct),theme:optional(string())}));const actions=["more-info","toggle","navigate","call-service","none"];const SCHEMA=[{name:"title",selector:{text:{}}},{name:"image",selector:{text:{}}},{name:"camera_image",selector:{entity:{domain:"camera"}}},{name:"",type:"grid",schema:[{name:"camera_view",selector:{select:{options:["auto","live"]}}},{name:"aspect_ratio",selector:{text:{}}}]},{name:"entity",selector:{entity:{}}}// { name: "theme", selector: { theme: {} } },
];let HuiPictureGlanceCardEditor=_decorate([n("hui-picture-glance-card-editor")],function(_initialize,_LitElement){class HuiPictureGlanceCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureGlanceCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;this._configEntities=processEditorEntities(config.entities);}},{kind:"get",key:"_tap_action",value:function _tap_action(){return this._config.tap_action||{action:"toggle"};}},{kind:"get",key:"_hold_action",value:function _hold_action(){return this._config.hold_action||{action:"more-info"};}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const data={camera_view:"auto",...this._config};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <div class="card-config">
        <div class="side-by-side">
          <hui-action-editor
            .label=${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")}
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${actions}
            .configValue=${"tap_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
          <hui-action-editor
            .label=${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")}
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${actions}
            .configValue=${"hold_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
        </div>
        <hui-entity-editor
          .hass=${this.hass}
          .entities=${this._configEntities}
          @entities-changed=${this._changed}
        ></hui-entity-editor>
      </div>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"method",key:"_changed",value:function _changed(ev){if(!this._config||!this.hass){return;}const target=ev.target;const value=ev.detail.value;if(ev.detail&&ev.detail.entities){this._config={...this._config,entities:ev.detail.entities};this._configEntities=processEditorEntities(this._config.entities);}else if(target.configValue){if(this[`_${target.configValue}`]===value){return;}if(value!==false&&!value){this._config={...this._config};delete this._config[target.configValue];}else {this._config={...this._config,[target.configValue]:value};}}fireEvent(this,"config-changed",{config:this._config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.picture-glance.state_entity");}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.picture-glance.${schema.name}`);};}},{kind:"field",static:true,key:"styles",value(){return configElementStyle;}}]};},s);

export { HuiPictureGlanceCardEditor };
