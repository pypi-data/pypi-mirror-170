const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, ax as number, ap as boolean, aq as assert } from './auth-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({name:optional(string()),entity:optional(string()),unit:optional(string()),min:optional(number()),max:optional(number()),severity:optional(object()),theme:optional(string()),needle:optional(boolean())}));let HuiGaugeCardEditor=_decorate([n("hui-gauge-card-editor")],function(_initialize,_LitElement){class HuiGaugeCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGaugeCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne(showSeverity=>{const schema=[{name:"entity",selector:{entity:{domain:["counter","input_number","number","sensor"]}}},{name:"",type:"grid",schema:[{name:"name",selector:{text:{}}},{name:"unit",selector:{text:{max:10}}}]},// { name: "theme", selector: { theme: {} } },
{name:"",type:"grid",schema:[{name:"min",selector:{number:{min:0,mode:"box"}}},{name:"max",selector:{number:{min:1,mode:"box"}}}]},{name:"",type:"grid",schema:[{name:"needle",selector:{boolean:{}}},{name:"show_severity",selector:{boolean:{}}}]}];if(showSeverity){schema.push({name:"",type:"grid",schema:[{name:"green",selector:{number:{min:0,mode:"box"}}},{name:"yellow",selector:{number:{min:0,mode:"box"}}},{name:"red",selector:{number:{min:0,mode:"box"}}}]});}return schema;});}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const schema=this._schema(this._config.severity!==undefined);const data={show_severity:this._config.severity!==undefined,...this._config};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){let config=ev.detail.value;if(config.show_severity){var _config$severity,_config$severity2,_config$severity3;config={...config,severity:{green:config.green||config.green===0?config.green:(_config$severity=config.severity)===null||_config$severity===void 0?void 0:_config$severity.green,yellow:config.yellow||config.yellow===0?config.yellow:(_config$severity2=config.severity)===null||_config$severity2===void 0?void 0:_config$severity2.yellow,red:config.red||config.red===0?config.red:(_config$severity3=config.severity)===null||_config$severity3===void 0?void 0:_config$severity3.red}};}else if(!config.show_severity&&config.severity){delete config.severity;}delete config.show_severity;delete config.green;delete config.yellow;delete config.red;fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{switch(schema.name){case"name":return this.hass.localize("ui.panel.lovelace.editor.card.generic.name");case"entity":return `${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})`;case"max":return this.hass.localize("ui.panel.lovelace.editor.card.generic.maximum");case"min":return this.hass.localize("ui.panel.lovelace.editor.card.generic.minimum");case"show_severity":return this.hass.localize("ui.panel.lovelace.editor.card.gauge.severity.define");case"needle":return this.hass.localize("ui.panel.lovelace.editor.card.gauge.needle_gauge");}return this.hass.localize(`ui.panel.lovelace.editor.card.gauge.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.gauge.severity.${schema.name}`);};}}]};},s);

export { HuiGaugeCardEditor };
