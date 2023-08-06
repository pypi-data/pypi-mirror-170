const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import { aq as assert } from './auth-dev.js';
import './ha-entity-picker-dev.js';
import './stop_propagation-dev.js';
import { g as graphHeaderFooterConfigStruct } from './structs-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './ha-combo-box-dev.js';
import './action-struct-dev.js';
import './entities-struct-dev.js';

const includeDomains=["sensor"];let HuiGraphFooterEditor=_decorate([n("hui-graph-footer-editor")],function(_initialize,_LitElement){class HuiGraphFooterEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGraphFooterEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,graphHeaderFooterConfigStruct);this._config=config;}},{kind:"get",key:"_entity",value:function _entity(){return this._config.entity||"";}},{kind:"get",key:"_detail",value:function _detail(){var _detail2;return (_detail2=this._config.detail)!==null&&_detail2!==void 0?_detail2:1;}},{kind:"get",key:"_hours_to_show",value:function _hours_to_show(){return this._config.hours_to_show||24;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <div class="card-config">
        <ha-entity-picker
          allow-custom-entity
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})"
          .hass=${this.hass}
          .value=${this._entity}
          .configValue=${"entity"}
          .includeDomains=${includeDomains}
          @change=${this._valueChanged}
        ></ha-entity-picker>
        <div class="side-by-side">
          <ha-formfield
            label=${this.hass.localize("ui.panel.lovelace.editor.card.sensor.show_more_detail")}
          >
            <ha-switch
              .checked=${this._detail===2}
              .configValue=${"detail"}
              @change=${this._change}
            ></ha-switch>
          </ha-formfield>
          <ha-textfield
            type="number"
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hours_to_show")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .value=${this._hours_to_show}
            min="1"
            .configValue=${"hours_to_show"}
            @input=${this._valueChanged}
          ></ha-textfield>
        </div>
      </div>
    `;}},{kind:"method",key:"_change",value:function _change(ev){if(!this._config||!this.hass){return;}const value=ev.target.checked?2:1;if(this._detail===value){return;}this._config={...this._config,detail:value};fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){if(!this._config||!this.hass){return;}const target=ev.target;if(this[`_${target.configValue}`]===target.value){return;}if(target.configValue){if(target.value===""||target.type==="number"&&isNaN(Number(target.value))){this._config={...this._config};delete this._config[target.configValue];}else {let value=target.value;if(target.type==="number"){value=Number(value);}this._config={...this._config,[target.configValue]:value};}}fireEvent(this,"config-changed",{config:this._config});}},{kind:"get",static:true,key:"styles",value:function styles(){return configElementStyle;}}]};},s);

export { HuiGraphFooterEditor };
