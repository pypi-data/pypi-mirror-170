const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, n } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, ap as boolean, aq as assert, C as domainIcon, e as computeDomain } from './auth-dev.js';
import { h as headerFooterConfigStructs } from './structs-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './action-struct-dev.js';
import './entities-struct-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),name:optional(string()),icon:optional(string()),attribute:optional(string()),unit:optional(string()),theme:optional(string()),state_color:optional(boolean()),footer:optional(headerFooterConfigStructs)}));let HuiEntityCardEditor=_decorate([n("hui-entity-card-editor")],function(_initialize,_LitElement){class HuiEntityCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEntityCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne((entity,icon,entityState)=>[{name:"entity",required:true,selector:{entity:{}}},{type:"grid",name:"",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{placeholder:icon||(entityState===null||entityState===void 0?void 0:entityState.attributes.icon),fallbackPath:!icon&&!(entityState!==null&&entityState!==void 0&&entityState.attributes.icon)&&entityState?domainIcon(computeDomain(entity),entityState):undefined}}},{name:"attribute",selector:{attribute:{entity_id:entity}}},{name:"unit",selector:{text:{}}},{name:"theme",selector:{theme:{}}},{name:"state_color",selector:{boolean:{}}}]}]);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const entityState=this.hass.states[this._config.entity];const schema=this._schema(this._config.entity,this._config.icon,entityState);return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;Object.keys(config).forEach(k=>config[k]===""&&delete config[k]);fireEvent(this,"config-changed",{config});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.entity");}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`);};}}]};},s);

export { HuiEntityCardEditor };
