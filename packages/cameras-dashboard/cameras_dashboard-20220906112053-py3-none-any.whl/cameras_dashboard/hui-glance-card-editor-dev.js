const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ar as union, ao as string, ax as number, ap as boolean, as as array, aq as assert } from './auth-dev.js';
import './hui-entity-editor-dev.js';
import { p as processEditorEntities } from './process-editor-entities-dev.js';
import { e as entitiesConfigStruct } from './entities-struct-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './guard-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';
import './action-struct-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({title:optional(union([string(),number()])),theme:optional(string()),columns:optional(number()),show_name:optional(boolean()),show_state:optional(boolean()),show_icon:optional(boolean()),state_color:optional(boolean()),entities:array(entitiesConfigStruct)}));const SCHEMA=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"columns",selector:{number:{min:1,mode:"box"}}},{name:"theme",selector:{theme:{}}}]},{name:"",type:"grid",column_min_width:"100px",schema:[{name:"show_name",selector:{boolean:{}}},{name:"show_icon",selector:{boolean:{}}},{name:"show_state",selector:{boolean:{}}}]},{name:"state_color",selector:{boolean:{}}}];let HuiGlanceCardEditor=_decorate([n("hui-glance-card-editor")],function(_initialize,_LitElement){class HuiGlanceCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGlanceCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;this._configEntities=processEditorEntities(config.entities);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const data={show_name:true,show_icon:true,show_state:true,...this._config};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <hui-entity-editor
        .hass=${this.hass}
        .entities=${this._configEntities}
        @entities-changed=${this._entitiesChanged}
      ></hui-entity-editor>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;fireEvent(this,"config-changed",{config});}},{kind:"method",key:"_entitiesChanged",value:function _entitiesChanged(ev){let config=this._config;config={...config,entities:ev.detail.entities};this._configEntities=processEditorEntities(this._config.entities);fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.glance.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`);}}]};},s);

export { HuiGlanceCardEditor };
