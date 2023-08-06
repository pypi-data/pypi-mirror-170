const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, f as fireEvent, n } from './main-dev.js';
import { al as assign, am as object, an as optional, ao as string, aq as assert } from './auth-dev.js';
import './ha-entity-picker-dev.js';
import './hui-theme-select-editor-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './stop_propagation-dev.js';
import './ha-combo-box-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({entity:optional(string()),theme:optional(string())}));const includeDomains=["media_player"];let HuiMediaControlCardEditor=_decorate([n("hui-media-control-card-editor")],function(_initialize,_LitElement){class HuiMediaControlCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiMediaControlCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"get",key:"_entity",value:function _entity(){return this._config.entity||"";}},{kind:"get",key:"_theme",value:function _theme(){return this._config.theme||"";}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <div class="card-config">
        <ha-entity-picker
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})"
          .hass=${this.hass}
          .value=${this._entity}
          .configValue=${"entity"}
          .includeDomains=${includeDomains}
          @change=${this._valueChanged}
          allow-custom-entity
        ></ha-entity-picker>
        <!-- <hui-theme-select-editor
          .hass=${this.hass}
          .value=${this._theme}
          .configValue=${"theme"}
          @value-changed=${this._valueChanged}
        ></hui-theme-select-editor> -->
      </div>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){if(!this._config||!this.hass){return;}const target=ev.target;if(this[`_${target.configValue}`]===target.value){return;}if(target.configValue){if(target.value===""){this._config={...this._config};delete this._config[target.configValue];}else {this._config={...this._config,[target.configValue]:target.value};}}fireEvent(this,"config-changed",{config:this._config});}}]};},s);

export { HuiMediaControlCardEditor };
