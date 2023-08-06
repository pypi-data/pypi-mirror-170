const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, ar as union, at as literal, ax as number, aq as assert, C as domainIcon, e as computeDomain } from './auth-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),name:optional(string()),icon:optional(string()),graph:optional(union([literal("line"),literal("none")])),unit:optional(string()),detail:optional(number()),// theme: optional(string()),
hours_to_show:optional(number())}));let HuiSensorCardEditor=_decorate([n("hui-sensor-card-editor")],function(_initialize,_LitElement){class HuiSensorCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiSensorCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne((entity,icon,entityState)=>[{name:"entity",selector:{entity:{domain:["counter","input_number","number","sensor"]}}},{name:"name",selector:{text:{}}},{type:"grid",name:"",schema:[{name:"icon",selector:{icon:{placeholder:icon||(entityState===null||entityState===void 0?void 0:entityState.attributes.icon),fallbackPath:!icon&&!(entityState!==null&&entityState!==void 0&&entityState.attributes.icon)&&entityState?domainIcon(computeDomain(entity),entityState):undefined}}},{name:"graph",selector:{select:{options:[{value:"none",label:"None"},{value:"line",label:"Line"}]}}},{name:"unit",selector:{text:{}}},{name:"detail",selector:{boolean:{}}},// { name: "theme", selector: { theme: {} } },
{name:"hours_to_show",selector:{number:{min:1,mode:"box"}}}]}]);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const entityState=this.hass.states[this._config.entity];const schema=this._schema(this._config.entity,this._config.icon,entityState);const data={hours_to_show:24,graph:"none",...this._config,detail:this._config.detail===2};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;config.detail=config.detail?2:1;fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.entity");}if(schema.name==="detail"){return this.hass.localize("ui.panel.lovelace.editor.card.sensor.show_more_detail");}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.sensor.${schema.name}`);};}},{kind:"get",static:true,key:"styles",value:function styles(){return configElementStyle;}}]};},s);

export { HuiSensorCardEditor };
