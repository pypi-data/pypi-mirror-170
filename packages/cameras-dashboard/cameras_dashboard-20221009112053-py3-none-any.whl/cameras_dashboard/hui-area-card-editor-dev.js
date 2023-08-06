const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import { al as assign, am as object, an as optional, ao as string, ap as boolean, aq as assert } from './auth-dev.js';
import './ha-form-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './stop_propagation-dev.js';
import './dynamic-element-directive-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({area:optional(string()),navigation_path:optional(string()),theme:optional(string()),show_camera:optional(boolean())}));const SCHEMA=[{name:"area",selector:{area:{}}},{name:"show_camera",required:false,selector:{boolean:{}}},{name:"",type:"grid",schema:[{name:"navigation_path",required:false,selector:{text:{}}},{name:"theme",required:false,selector:{theme:{}}}]}];let HuiAreaCardEditor=_decorate([n("hui-area-card-editor")],function(_initialize,_LitElement){class HuiAreaCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiAreaCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{switch(schema.name){case"area":return this.hass.localize("ui.panel.lovelace.editor.card.area.name");case"navigation_path":return this.hass.localize("ui.panel.lovelace.editor.action-editor.navigation_path");}return this.hass.localize(`ui.panel.lovelace.editor.card.area.${schema.name}`);};}}]};},s);

export { HuiAreaCardEditor };
