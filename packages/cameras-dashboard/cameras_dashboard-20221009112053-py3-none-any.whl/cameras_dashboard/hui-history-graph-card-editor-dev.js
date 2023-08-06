const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, r, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, as as array, an as optional, ao as string, ax as number, aq as assert } from './auth-dev.js';
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

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entities:array(entitiesConfigStruct),title:optional(string()),hours_to_show:optional(number()),refresh_interval:optional(number())}));const SCHEMA=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"hours_to_show",selector:{number:{min:1,mode:"box"}}},{name:"refresh_interval",selector:{number:{min:1,mode:"box"}}}]}];let HuiHistoryGraphCardEditor=_decorate([n("hui-history-graph-card-editor")],function(_initialize,_LitElement){class HuiHistoryGraphCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiHistoryGraphCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;this._configEntities=processEditorEntities(config.entities);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <hui-entity-editor
        .hass=${this.hass}
        .entities=${this._configEntities}
        @entities-changed=${this._entitiesChanged}
      ></hui-entity-editor>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"method",key:"_entitiesChanged",value:function _entitiesChanged(ev){let config=this._config;config={...config,entities:ev.detail.entities};this._configEntities=processEditorEntities(config.entities);fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`);}},{kind:"field",static:true,key:"styles",value(){return r`
    ha-form {
      margin-bottom: 24px;
    }
  `;}}]};},s);

export { HuiHistoryGraphCardEditor };
