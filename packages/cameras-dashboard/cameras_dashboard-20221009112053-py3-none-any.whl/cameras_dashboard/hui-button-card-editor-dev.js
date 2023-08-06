const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, n } from './main-dev.js';
import { al as assign, am as object, an as optional, ao as string, ap as boolean, aq as assert, C as domainIcon, e as computeDomain } from './auth-dev.js';
import './hui-action-editor-dev.js';
import './ha-form-dev.js';
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

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),name:optional(string()),show_name:optional(boolean()),icon:optional(string()),show_icon:optional(boolean()),icon_height:optional(string()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),theme:optional(string()),show_state:optional(boolean())}));const actions=["more-info","toggle","navigate","url","call-service","none"];let HuiButtonCardEditor=_decorate([n("hui-button-card-editor")],function(_initialize,_LitElement){class HuiButtonCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiButtonCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne((entity,icon,entityState)=>[{name:"entity",selector:{entity:{domain:["light","switch","cover","automation","fan"]}}},{name:"",type:"grid",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{placeholder:icon||(entityState===null||entityState===void 0?void 0:entityState.attributes.icon),fallbackPath:!icon&&!(entityState!==null&&entityState!==void 0&&entityState.attributes.icon)&&entityState&&entity?domainIcon(computeDomain(entity),entityState):undefined}}}]},{name:"",type:"grid",column_min_width:"100px",schema:[// { name: "show_name", selector: { boolean: {} } },
// { name: "show_state", selector: { boolean: {} } },
// { name: "show_icon", selector: { boolean: {} } },
]},{name:"",type:"grid",schema:[// { name: "icon_height", selector: { text: { suffix: "px" } } },
// { name: "theme", selector: { theme: {} } },
]}]);}},{kind:"get",key:"_tap_action",value:function _tap_action(){return this._config.tap_action;}},{kind:"get",key:"_hold_action",value:function _hold_action(){return this._config.hold_action||{action:"more-info"};}},{kind:"method",key:"render",value:function render(){var _data$icon_height;if(!this.hass||!this._config){return $``;}const entityState=this._config.entity?this.hass.states[this._config.entity]:undefined;const schema=this._schema(this._config.entity,this._config.icon,entityState);const data={show_name:true,show_icon:true,...this._config};if((_data$icon_height=data.icon_height)!==null&&_data$icon_height!==void 0&&_data$icon_height.includes("px")){data.icon_height=String(parseFloat(data.icon_height));}return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <!-- <div class="card-config">
        <div class="side-by-side">
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${actions}
            .configValue=${"tap_action"}
            .tooltipText=${this.hass.localize("ui.panel.lovelace.editor.card.button.default_action_help")}
            @value-changed=${this._actionChanged}
          ></hui-action-editor>
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${actions}
            .configValue=${"hold_action"}
            .tooltipText=${this.hass.localize("ui.panel.lovelace.editor.card.button.default_action_help")}
            @value-changed=${this._actionChanged}
          ></hui-action-editor>
        </div>
      </div> -->
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;if(config.icon_height&&!config.icon_height.endsWith("px")){config.icon_height+="px";}fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return `${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")}`;}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`);};}},{kind:"method",key:"_actionChanged",value:function _actionChanged(ev){if(!this._config||!this.hass){return;}const target=ev.target;const value=ev.detail.value;if(this[`_${target.configValue}`]===value){return;}let newConfig;if(target.configValue){if(value!==false&&!value){newConfig={...this._config};delete newConfig[target.configValue];}else {newConfig={...this._config,[target.configValue]:value};}}fireEvent(this,"config-changed",{config:newConfig});}},{kind:"get",static:true,key:"styles",value:function styles(){return configElementStyle;}}]};},s);

export { HuiButtonCardEditor };
