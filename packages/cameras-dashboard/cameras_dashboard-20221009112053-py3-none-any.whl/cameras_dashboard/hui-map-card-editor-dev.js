const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, at as mdiClose, f as fireEvent, r, n, t } from './main-dev.js';
import './ha-form-dev.js';
import { al as assign, am as object, an as optional, ao as string, ax as number, ap as boolean, as as array, aq as assert } from './auth-dev.js';
import './stop_propagation-dev.js';
import './hui-entity-editor-dev.js';
import { p as processEditorEntities } from './process-editor-entities-dev.js';
import { e as entitiesConfigStruct } from './entities-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './guard-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';
import './action-struct-dev.js';

_decorate([n("hui-input-list-editor")],function(_initialize,_LitElement){class HuiInputListEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiInputListEditor,d:[{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e()],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"inputLabel",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.value){return $``;}return $`
      ${this.value.map((listEntry,index)=>$`
          <ha-textfield
            .label=${this.inputLabel}
            .value=${listEntry}
            .configValue=${"entry"}
            .index=${index}
            @input=${this._valueChanged}
            @blur=${this._consolidateEntries}
            @keydown=${this._handleKeyDown}
            iconTrailing
            ><ha-icon-button
              slot="trailingIcon"
              class="clear-button"
              .path=${mdiClose}
              no-ripple
              @click=${this._removeEntry}
              .label=${this.hass.localize("ui.common.clear")}
            >
            </ha-icon-button>
          </ha-textfield>
        `)}
      <ha-textfield
        .label=${this.inputLabel}
        @change=${this._addEntry}
      ></ha-textfield>
    `;}},{kind:"method",key:"_addEntry",value:function _addEntry(ev){const target=ev.target;if(target.value===""){return;}const newEntries=this.value.concat(target.value);target.value="";fireEvent(this,"value-changed",{value:newEntries});ev.target.blur();}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){ev.stopPropagation();const target=ev.target;const newEntries=this.value.concat();newEntries[target.index]=target.value;fireEvent(this,"value-changed",{value:newEntries});}},{kind:"method",key:"_handleKeyDown",value:function _handleKeyDown(ev){if(ev.key==="Enter"){ev.stopPropagation();this._consolidateEntries(ev);}}},{kind:"method",key:"_consolidateEntries",value:function _consolidateEntries(ev){const target=ev.target;if(target.value===""){const newEntries=this.value.concat();newEntries.splice(target.index,1);fireEvent(this,"value-changed",{value:newEntries});}}},{kind:"method",key:"_removeEntry",value:function _removeEntry(ev){const parent=ev.currentTarget.parentElement;const newEntries=this.value.concat();newEntries.splice(parent.index,1);fireEvent(this,"value-changed",{value:newEntries});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-icon-button {
        margin-right: -24px;
        color: var(--secondary-text-color);
      }
      ha-textfield {
        display: block;
      }
    `;}}]};},s);

const cardConfigStruct=assign(baseLovelaceCardConfig,object({title:optional(string()),aspect_ratio:optional(string()),default_zoom:optional(number()),dark_mode:optional(boolean()),entities:array(entitiesConfigStruct),hours_to_show:optional(number()),geo_location_sources:optional(array(string()))}));const SCHEMA=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"aspect_ratio",selector:{text:{}}},{name:"default_zoom",selector:{number:{mode:"box",min:0}}},{name:"dark_mode",selector:{boolean:{}}},{name:"hours_to_show",selector:{number:{mode:"box",min:1}}}]}];let HuiMapCardEditor=_decorate([n("hui-map-card-editor")],function(_initialize,_LitElement){class HuiMapCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiMapCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;this._configEntities=config.entities?processEditorEntities(config.entities):[];}},{kind:"get",key:"_geo_location_sources",value:function _geo_location_sources(){return this._config.geo_location_sources||[];}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${SCHEMA}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <div class="card-config">
        <hui-entity-editor
          .hass=${this.hass}
          .entities=${this._configEntities}
          @entities-changed=${this._entitiesValueChanged}
        ></hui-entity-editor>
        <h3>
          ${this.hass.localize("ui.panel.lovelace.editor.card.map.geo_location_sources")}
        </h3>
        <div class="geo_location_sources">
          <hui-input-list-editor
            .inputLabel=${this.hass.localize("ui.panel.lovelace.editor.card.map.source")}
            .hass=${this.hass}
            .value=${this._geo_location_sources}
            @value-changed=${this._geoSourcesChanged}
          ></hui-input-list-editor>
        </div>
      </div>
    `;}},{kind:"method",key:"_entitiesValueChanged",value:function _entitiesValueChanged(ev){if(ev.detail&&ev.detail.entities){this._config={...this._config,entities:ev.detail.entities};this._configEntities=processEditorEntities(this._config.entities);fireEvent(this,"config-changed",{config:this._config});}}},{kind:"method",key:"_geoSourcesChanged",value:function _geoSourcesChanged(ev){if(!this._config||!this.hass){return;}const value=ev.detail.value;if(this._geo_location_sources===value){return;}if(value===""){this._config={...this._config};delete this._config.geo_location_sources;}else {this._config={...this._config,geo_location_sources:value};}fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.map.${schema.name}`);}},{kind:"get",static:true,key:"styles",value:function styles(){return [configElementStyle,r`
        .geo_location_sources {
          padding-left: 20px;
        }
      `];}}]};},s);

export { HuiMapCardEditor };
