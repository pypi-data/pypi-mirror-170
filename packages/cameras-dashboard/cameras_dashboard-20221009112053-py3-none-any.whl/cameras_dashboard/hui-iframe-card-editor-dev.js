const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, aq as assert } from './auth-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({title:optional(string()),url:optional(string()),aspect_ratio:optional(string())}));const SCHEMA=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"url",required:true,selector:{text:{}}},{name:"aspect_ratio",selector:{text:{}}}]}];let HuiIframeCardEditor=_decorate([n("hui-iframe-card-editor")],function(_initialize,_LitElement){class HuiIframeCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiIframeCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`);}}]};},s);

export { HuiIframeCardEditor };
