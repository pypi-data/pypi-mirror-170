const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, as as array, aq as assert } from './auth-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),name:optional(string()),states:optional(array())// theme: optional(string()),
}));const states=["arm_home","arm_away","arm_night","arm_vacation","arm_custom_bypass"];let HuiAlarmPanelCardEditor=_decorate([n("hui-alarm-panel-card-editor")],function(_initialize,_LitElement){class HuiAlarmPanelCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiAlarmPanelCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne(localize=>[{name:"entity",required:true,selector:{entity:{domain:"alarm_control_panel"}}},// {
// type: "grid",
// name: "",
// schema: [
{name:"name",selector:{text:{}}},// { name: "theme", selector: { theme: {} } },
// ],
// },
{type:"multi_select",name:"states",options:states.map(s=>[s,localize(`ui.card.alarm_control_panel.${s}`)])}]);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${this._schema(this.hass.localize)}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.entity");}if(schema.name==="name"){return this.hass.localize(`ui.panel.lovelace.editor.card.generic.name`);}return this.hass.localize(`ui.panel.lovelace.editor.card.alarm-panel.${schema.name==="states"?"available_states":schema.name}`);};}}]};},s);

export { HuiAlarmPanelCardEditor };
