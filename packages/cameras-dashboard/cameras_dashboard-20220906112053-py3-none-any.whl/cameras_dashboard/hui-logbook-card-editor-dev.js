const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, as as array, ao as string, ax as number, aq as assert } from './auth-dev.js';
import './ha-entities-picker-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entities:optional(array(string())),title:optional(string()),hours_to_show:optional(number()),theme:optional(string())}));const SCHEMA=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"theme",selector:{theme:{}}},{name:"hours_to_show",selector:{number:{mode:"box",min:1}}}]}];let HuiLogbookCardEditor=_decorate([n("hui-logbook-card-editor")],function(_initialize,_LitElement){class HuiLogbookCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiLogbookCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"get",key:"_entities",value:function _entities(){return this._config.entities||[];}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <h3>
        ${`${this.hass.localize("ui.panel.lovelace.editor.card.generic.entities")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})`}
      </h3>
      <ha-entities-picker
        .hass=${this.hass}
        .value=${this._entities}
        @value-changed=${this._entitiesChanged}
      >
      </ha-entities-picker>
    `;}},{kind:"method",key:"_entitiesChanged",value:function _entitiesChanged(ev){this._config={...this._config,entities:ev.detail.value};fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.logbook.${schema.name}`);}}]};},s);

export { HuiLogbookCardEditor };
