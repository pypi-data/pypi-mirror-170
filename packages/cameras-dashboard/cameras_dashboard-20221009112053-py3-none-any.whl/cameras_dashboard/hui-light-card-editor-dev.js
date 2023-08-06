const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, r, n } from './main-dev.js';
import { al as assign, am as object, an as optional, ao as string, aq as assert, C as domainIcon, e as computeDomain } from './auth-dev.js';
import './hui-action-editor-dev.js';
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
import './hui-theme-select-editor-dev.js';
import './ha-map-dev.js';
import './automation-dev.js';
import './guard-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({name:optional(string()),entity:optional(string()),theme:optional(string()),icon:optional(string())// hold_action: optional(actionConfigStruct),
// double_tap_action: optional(actionConfigStruct),
}));let HuiLightCardEditor=_decorate([n("hui-light-card-editor")],function(_initialize,_LitElement){class HuiLightCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiLightCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne((entity,icon,entityState)=>[{name:"entity",required:true,selector:{entity:{domain:"light"}}},{name:"",type:"grid",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{placeholder:icon||(entityState===null||entityState===void 0?void 0:entityState.attributes.icon),fallbackPath:!icon&&!(entityState!==null&&entityState!==void 0&&entityState.attributes.icon)&&entityState&&entity?domainIcon(computeDomain(entity),entityState):undefined}}}]}// { name: "theme", selector: { theme: {} } },
]);}},{kind:"method",key:"render",value:// get _hold_action(): ActionConfig {
//   return this._config!.hold_action || { action: "more-info" };
// }
// get _double_tap_action(): ActionConfig | undefined {
//   return this._config!.double_tap_action;
// }
function render(){if(!this.hass||!this._config){return $``;}const actions=["more-info","toggle","navigate","url","call-service","none"];const entityState=this.hass.states[this._config.entity];const schema=this._schema(this._config.entity,this._config.icon,entityState);return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <!-- <div class="card-config">
        <hui-action-editor
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
          .hass=${this.hass}
          .config=${this._hold_action}
          .actions=${actions}
          .configValue=${"hold_action"}
          @value-changed=${this._actionChanged}
        ></hui-action-editor>

        <hui-action-editor
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.double_tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
          .hass=${this.hass}
          .config=${this._double_tap_action}
          .actions=${actions}
          .configValue=${"double_tap_action"}
          @value-changed=${this._actionChanged}
        ></hui-action-editor>
      </div> -->
    `;}},{kind:"method",key:"_actionChanged",value:function _actionChanged(ev){if(!this._config||!this.hass){return;}const target=ev.target;const value=ev.detail.value;if(this[`_${target.configValue}`]===value){return;}if(target.configValue){if(value!==false&&!value){this._config={...this._config};delete this._config[target.configValue];}else {this._config={...this._config,[target.configValue]:value};}}fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.entity");}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`);};}},{kind:"field",static:true,key:"styles",value(){return [configElementStyle,r`
      /* ha-form,
      hui-action-editor {
        display: block;
        margin-bottom: 24px;
        overflow: auto;
      } */
    `];}}]};},s);

export { HuiLightCardEditor };
