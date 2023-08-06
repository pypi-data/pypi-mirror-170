const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, r, n } from './main-dev.js';
import './ha-entities-picker-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ar as union, ao as string, ap as boolean, as as array, aq as assert } from './auth-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';
import './dynamic-element-directive-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({title:optional(union([string(),boolean()])),initial_view:optional(string()),theme:optional(string()),entities:array(string())}));const views=["dayGridMonth","dayGridDay","listWeek"];let HuiCalendarCardEditor=_decorate([n("hui-calendar-card-editor")],function(_initialize,_LitElement){class HuiCalendarCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCalendarCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne(localize=>[{name:"",type:"grid",schema:[{name:"title",required:false,selector:{text:{}}},{name:"initial_view",required:false,selector:{select:{options:views.map(view=>[view,localize(`ui.panel.lovelace.editor.card.calendar.views.${view}`)])}}}]},{name:"theme",required:false,selector:{theme:{}}}]);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const schema=this._schema(this.hass.localize);const data={initial_view:"dayGridMonth",...this._config};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <h3>
        ${this.hass.localize("ui.panel.lovelace.editor.card.calendar.calendar_entities")+" ("+this.hass.localize("ui.panel.lovelace.editor.card.config.required")+")"}
      </h3>
      <ha-entities-picker
        .hass=${this.hass}
        .value=${this._config.entities}
        .includeDomains=${["calendar"]}
        @value-changed=${this._entitiesChanged}
      >
      </ha-entities-picker>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;fireEvent(this,"config-changed",{config});}},{kind:"method",key:"_entitiesChanged",value:function _entitiesChanged(ev){const config={...this._config,entities:ev.detail.value};fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="title"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.title");}return this.hass.localize(`ui.panel.lovelace.editor.card.calendar.${schema.name}`);};}},{kind:"field",static:true,key:"styles",value(){return r`
    ha-form {
      display: block;
      overflow: auto;
    }
  `;}}]};},s);

export { HuiCalendarCardEditor };
