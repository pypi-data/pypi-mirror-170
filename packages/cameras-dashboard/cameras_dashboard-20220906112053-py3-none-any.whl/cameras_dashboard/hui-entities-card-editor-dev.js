const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { f as fireEvent, _ as _decorate, c as s, d as e, $, dF as mdiPlus, at as mdiClose, av as mdiPencil, r, n, t, j as _get, k as _getPrototypeOf, ep as mdiDrag, G as i$1, eq as mdiArrowLeft } from './main-dev.js';
import { aE as refine, ao as string, am as object, at as literal, an as optional, ar as union, ax as number, ap as boolean, aw as any, as as array, av as enums, au as type, aF as dynamic, al as assign, aq as assert } from './auth-dev.js';
import { a as entityId } from './is-entity-id-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';
import './stop_propagation-dev.js';
import './hui-theme-select-editor-dev.js';
import { T as TIMESTAMP_RENDERING_FORMATS, e as entitiesConfigStruct } from './entities-struct-dev.js';
import { h as headerFooterConfigStructs } from './structs-dev.js';
import { i } from './guard-dev.js';
import './ha-entity-picker-dev.js';
import { s as sortableStyles, p as processEditorEntities } from './process-editor-entities-dev.js';
import { F as getRowElementClass, G as getHeaderFooterElementClass } from './ha-more-info-dialog-dev.js';
import { H as HuiElementEditor } from './hui-element-editor-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './ha-combo-box-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './js-yaml-dev.js';
import './ha-code-editor-dev.js';
import './ha-form-dev.js';
import './dynamic-element-directive-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

const isCustomType=value=>value.startsWith("custom:");const customType=()=>refine(string(),"custom element type",isCustomType);

const importCreateHeaderFooterDialog=()=>import('./hui-dialog-create-headerfooter-dev.js');const showCreateHeaderFooterDialog=(element,createHeaderFooterDialogParams)=>{fireEvent(element,"show-dialog",{dialogTag:"hui-dialog-create-headerfooter",dialogImport:importCreateHeaderFooterDialog,dialogParams:createHeaderFooterDialogParams});};

_decorate([n("hui-header-footer-editor")],function(_initialize,_LitElement){class HuiHeaderFooterEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiHeaderFooterEditor,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",key:"lovelaceConfig",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"config",value:void 0},{kind:"field",decorators:[e()],key:"configValue",value:void 0},{kind:"method",key:"render",value:function render(){var _this$config,_this$config2,_this$config3;return $`
      <div>
        <span>
          ${this.hass.localize(`ui.panel.lovelace.editor.header-footer.${this.configValue}`)}:
          ${!((_this$config=this.config)!==null&&_this$config!==void 0&&_this$config.type)?this.hass.localize("ui.panel.lovelace.editor.common.none"):this.hass.localize(`ui.panel.lovelace.editor.header-footer.types.${(_this$config2=this.config)===null||_this$config2===void 0?void 0:_this$config2.type}.name`)}
        </span>
      </div>
      <div>
        ${!((_this$config3=this.config)!==null&&_this$config3!==void 0&&_this$config3.type)?$`
              <ha-icon-button
                .label=${this.hass.localize("ui.panel.lovelace.editor.common.add")}
                .path=${mdiPlus}
                class="add-icon"
                @click=${this._add}
              ></ha-icon-button>
            `:$`
              <ha-icon-button
                .label=${this.hass.localize("ui.panel.lovelace.editor.common.clear")}
                .path=${mdiClose}
                class="remove-icon"
                @click=${this._delete}
              ></ha-icon-button>
              <ha-icon-button
                .label=${this.hass.localize("ui.panel.lovelace.editor.common.edit")}
                .path=${mdiPencil}
                class="edit-icon"
                @click=${this._edit}
              ></ha-icon-button>
            `}
      </div>
    `;}},{kind:"method",key:"_edit",value:function _edit(){fireEvent(this,"edit-detail-element",{subElementConfig:{elementConfig:this.config,type:this.configValue}});}},{kind:"method",key:"_add",value:function _add(){showCreateHeaderFooterDialog(this,{pickHeaderFooter:config=>this._elementPicked(config),type:this.configValue});}},{kind:"method",key:"_elementPicked",value:function _elementPicked(config){fireEvent(this,"value-changed",{value:config});fireEvent(this,"edit-detail-element",{subElementConfig:{elementConfig:config,type:this.configValue}});}},{kind:"method",key:"_delete",value:function _delete(){fireEvent(this,"value-changed",{value:""});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        font-size: 16px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 12px;
      }

      :host > div {
        display: flex;
        align-items: center;
      }

      ha-icon-button,
      .header-footer-icon {
        --mdc-icon-button-size: 36px;
        color: var(--secondary-text-color);
      }

      .header-footer-icon {
        padding-right: 8px;
      }
    `;}}]};},s);

let Sortable;_decorate([n("hui-entities-card-row-editor")],function(_initialize,_LitElement){class HuiEntitiesCardRowEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEntitiesCardRowEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"entities",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[t()],key:"_attached",value(){return false;}},{kind:"field",decorators:[t()],key:"_renderEmptySortable",value(){return false;}},{kind:"field",key:"_sortable",value:void 0},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiEntitiesCardRowEditor.prototype),"connectedCallback",this).call(this);this._attached=true;}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){_get(_getPrototypeOf(HuiEntitiesCardRowEditor.prototype),"disconnectedCallback",this).call(this);this._attached=false;}},{kind:"method",key:"render",value:function render(){if(!this.entities||!this.hass){return $``;}return $`
      <h3>
        ${this.label||`${this.hass.localize("ui.panel.lovelace.editor.card.generic.entities")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})`}
      </h3>
      <div class="entities">
        ${i([this.entities,this._renderEmptySortable],()=>this._renderEmptySortable?"":this.entities.map((entityConf,index)=>$`
                  <div class="entity">
                    <ha-svg-icon class="handle" .path=${mdiDrag}></ha-svg-icon>
                    ${entityConf.type?$`
                          <div class="special-row">
                            <div>
                              <span>
                                ${this.hass.localize(`ui.panel.lovelace.editor.card.entities.entity_row.${entityConf.type}`)}
                              </span>
                              <span class="secondary"
                                >${this.hass.localize("ui.panel.lovelace.editor.card.entities.edit_special_row")}</span
                              >
                            </div>
                          </div>
                        `:$`
                          <ha-entity-picker
                            allow-custom-entity
                            hideClearIcon
                            .hass=${this.hass}
                            .value=${entityConf.entity}
                            .index=${index}
                            @value-changed=${this._valueChanged}
                          ></ha-entity-picker>
                        `}
                    <ha-icon-button
                      .label=${this.hass.localize("ui.components.entity.entity-picker.clear")}
                      .path=${mdiClose}
                      class="remove-icon"
                      .index=${index}
                      @click=${this._removeRow}
                    ></ha-icon-button>
                    <ha-icon-button
                      .label=${this.hass.localize("ui.components.entity.entity-picker.edit")}
                      .path=${mdiPencil}
                      class="edit-icon"
                      .index=${index}
                      @click=${this._editRow}
                    ></ha-icon-button>
                  </div>
                `))}
      </div>
      <ha-entity-picker
        class="add-entity"
        .hass=${this.hass}
        @value-changed=${this._addEntity}
      ></ha-entity-picker>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiEntitiesCardRowEditor.prototype),"updated",this).call(this,changedProps);const attachedChanged=changedProps.has("_attached");const entitiesChanged=changedProps.has("entities");if(!entitiesChanged&&!attachedChanged){return;}if(attachedChanged&&!this._attached){var _this$_sortable;// Tear down sortable, if available
(_this$_sortable=this._sortable)===null||_this$_sortable===void 0?void 0:_this$_sortable.destroy();this._sortable=undefined;return;}if(!this._sortable&&this.entities){this._createSortable();return;}if(entitiesChanged){this._handleEntitiesChanged();}}},{kind:"method",key:"_handleEntitiesChanged",value:async function _handleEntitiesChanged(){this._renderEmptySortable=true;await this.updateComplete;const container=this.shadowRoot.querySelector(".entities");while(container.lastElementChild){container.removeChild(container.lastElementChild);}this._renderEmptySortable=false;}},{kind:"method",key:"_createSortable",value:async function _createSortable(){if(!Sortable){const sortableImport=await import('./sortable.core.esm-dev.js');Sortable=sortableImport.Sortable;Sortable.mount(sortableImport.OnSpill);Sortable.mount(sortableImport.AutoScroll());}this._sortable=new Sortable(this.shadowRoot.querySelector(".entities"),{animation:150,fallbackClass:"sortable-fallback",handle:".handle",onEnd:async evt=>this._rowMoved(evt)});}},{kind:"method",key:"_addEntity",value:async function _addEntity(ev){const value=ev.detail.value;if(value===""){return;}const newConfigEntities=this.entities.concat({entity:value});ev.target.value="";fireEvent(this,"entities-changed",{entities:newConfigEntities});}},{kind:"method",key:"_rowMoved",value:function _rowMoved(ev){if(ev.oldIndex===ev.newIndex){return;}const newEntities=this.entities.concat();newEntities.splice(ev.newIndex,0,newEntities.splice(ev.oldIndex,1)[0]);fireEvent(this,"entities-changed",{entities:newEntities});}},{kind:"method",key:"_removeRow",value:function _removeRow(ev){const index=ev.currentTarget.index;const newConfigEntities=this.entities.concat();newConfigEntities.splice(index,1);fireEvent(this,"entities-changed",{entities:newConfigEntities});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const value=ev.detail.value;const index=ev.target.index;const newConfigEntities=this.entities.concat();if(value===""||value===undefined){newConfigEntities.splice(index,1);}else {newConfigEntities[index]={...newConfigEntities[index],entity:value};}fireEvent(this,"entities-changed",{entities:newConfigEntities});}},{kind:"method",key:"_editRow",value:function _editRow(ev){const index=ev.currentTarget.index;fireEvent(this,"edit-detail-element",{subElementConfig:{index,type:"row",elementConfig:this.entities[index]}});}},{kind:"get",static:true,key:"styles",value:function styles(){return [sortableStyles,r`
        ha-entity-picker {
          margin-top: 8px;
        }
        .add-entity {
          display: block;
          margin-left: 31px;
          margin-right: 71px;
        }
        .entity {
          display: flex;
          align-items: center;
        }

        .entity .handle {
          padding-right: 8px;
          cursor: move;
        }

        .entity ha-entity-picker {
          flex-grow: 1;
        }

        .special-row {
          height: 60px;
          font-size: 16px;
          display: flex;
          align-items: center;
          justify-content: space-between;
          flex-grow: 1;
        }

        .special-row div {
          display: flex;
          flex-direction: column;
        }

        .remove-icon,
        .edit-icon {
          --mdc-icon-button-size: 36px;
          color: var(--secondary-text-color);
        }

        .secondary {
          font-size: 12px;
          color: var(--secondary-text-color);
        }
      `];}}]};},s);

const GENERIC_ROW_TYPE="generic-row";_decorate([n("hui-row-element-editor")],function(_initialize,_HuiElementEditor){class HuiRowElementEditor extends _HuiElementEditor{constructor(...args){super(...args);_initialize(this);}}return {F:HuiRowElementEditor,d:[{kind:"get",key:"configElementType",value:function configElementType(){var _this$value,_this$value2;if(!((_this$value=this.value)!==null&&_this$value!==void 0&&_this$value.type)&&"entity"in this.value){return GENERIC_ROW_TYPE;}return (_this$value2=this.value)===null||_this$value2===void 0?void 0:_this$value2.type;}},{kind:"method",key:"getConfigElement",value:async function getConfigElement(){if(this.configElementType===GENERIC_ROW_TYPE){return document.createElement("hui-generic-entity-row-editor");}const elClass=await getRowElementClass(this.configElementType);// Check if a GUI editor exists
if(elClass&&elClass.getConfigElement){return elClass.getConfigElement();}return undefined;}}]};},HuiElementEditor);

_decorate([n("hui-headerfooter-element-editor")],function(_initialize,_HuiElementEditor){class HuiHeaderFooterElementEditor extends _HuiElementEditor{constructor(...args){super(...args);_initialize(this);}}return {F:HuiHeaderFooterElementEditor,d:[{kind:"method",key:"getConfigElement",value:async function getConfigElement(){const elClass=await getHeaderFooterElementClass(this.configElementType);// Check if a GUI editor exists
if(elClass&&elClass.getConfigElement){return elClass.getConfigElement();}return undefined;}}]};},HuiElementEditor);

_decorate([n("hui-sub-element-editor")],function(_initialize,_LitElement){class HuiSubElementEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiSubElementEditor,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"config",value:void 0},{kind:"field",decorators:[t()],key:"_guiModeAvailable",value(){return true;}},{kind:"field",decorators:[t()],key:"_guiMode",value(){return true;}},{kind:"field",decorators:[i$1(".editor")],key:"_editorElement",value:void 0},{kind:"method",key:"render",value:function render(){var _this$config;return $`
      <div class="header">
        <div class="back-title">
          <ha-icon-button
            .label=${this.hass.localize("ui.common.back")}
            .path=${mdiArrowLeft}
            @click=${this._goBack}
          ></ha-icon-button>
          <span slot="title"
            >${this.hass.localize(`ui.panel.lovelace.editor.sub-element-editor.types.${(_this$config=this.config)===null||_this$config===void 0?void 0:_this$config.type}`)}</span
          >
        </div>
        <mwc-button
          slot="secondaryAction"
          .disabled=${!this._guiModeAvailable}
          @click=${this._toggleMode}
        >
          ${this.hass.localize(this._guiMode?"ui.panel.lovelace.editor.edit_card.show_code_editor":"ui.panel.lovelace.editor.edit_card.show_visual_editor")}
        </mwc-button>
      </div>
      ${this.config.type==="row"?$`
            <hui-row-element-editor
              class="editor"
              .hass=${this.hass}
              .value=${this.config.elementConfig}
              @config-changed=${this._handleConfigChanged}
              @GUImode-changed=${this._handleGUIModeChanged}
            ></hui-row-element-editor>
          `:this.config.type==="header"||this.config.type==="footer"?$`
            <hui-headerfooter-element-editor
              class="editor"
              .hass=${this.hass}
              .value=${this.config.elementConfig}
              @config-changed=${this._handleConfigChanged}
              @GUImode-changed=${this._handleGUIModeChanged}
            ></hui-headerfooter-element-editor>
          `:""}
    `;}},{kind:"method",key:"_goBack",value:function _goBack(){fireEvent(this,"go-back");}},{kind:"method",key:"_toggleMode",value:function _toggleMode(){var _this$_editorElement;(_this$_editorElement=this._editorElement)===null||_this$_editorElement===void 0?void 0:_this$_editorElement.toggleMode();}},{kind:"method",key:"_handleGUIModeChanged",value:function _handleGUIModeChanged(ev){ev.stopPropagation();this._guiMode=ev.detail.guiMode;this._guiModeAvailable=ev.detail.guiModeAvailable;}},{kind:"method",key:"_handleConfigChanged",value:function _handleConfigChanged(ev){this._guiModeAvailable=ev.detail.guiModeAvailable;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .back-title {
        display: flex;
        align-items: center;
        font-size: 18px;
      }
    `;}}]};},s);

const buttonEntitiesRowConfigStruct=object({type:literal("button"),entity:optional(string()),name:optional(string()),icon:optional(string()),action_name:optional(string()),tap_action:actionConfigStruct,hold_action:optional(actionConfigStruct),double_tap_action:optional(actionConfigStruct)});const castEntitiesRowConfigStruct=object({type:literal("cast"),view:union([string(),number()]),dashboard:optional(string()),name:optional(string()),icon:optional(string()),hide_if_unavailable:optional(boolean())});const callServiceEntitiesRowConfigStruct=object({type:literal("call-service"),name:string(),service:string(),icon:optional(string()),action_name:optional(string()),service_data:optional(any())});const conditionalEntitiesRowConfigStruct=object({type:literal("conditional"),row:any(),conditions:array(object({entity:string(),state:optional(string()),state_not:optional(string())}))});const dividerEntitiesRowConfigStruct=object({type:literal("divider"),style:optional(any())});const sectionEntitiesRowConfigStruct=object({type:literal("section"),label:optional(string())});const webLinkEntitiesRowConfigStruct=object({type:literal("weblink"),url:string(),name:optional(string()),icon:optional(string())});const buttonsEntitiesRowConfigStruct=object({type:literal("buttons"),entities:array(union([object({entity:string(),name:optional(string()),icon:optional(string()),image:optional(string()),show_name:optional(boolean()),show_icon:optional(boolean()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),double_tap_action:optional(actionConfigStruct)}),string()]))});const attributeEntitiesRowConfigStruct=object({type:literal("attribute"),entity:string(),attribute:string(),prefix:optional(string()),suffix:optional(string()),name:optional(string()),icon:optional(string()),format:optional(enums(TIMESTAMP_RENDERING_FORMATS))});const textEntitiesRowConfigStruct=object({type:literal("text"),name:string(),text:string(),icon:optional(string())});const customEntitiesRowConfigStruct=type({type:customType()});const entitiesRowConfigStruct=dynamic(value=>{if(value&&typeof value==="object"&&"type"in value){if(isCustomType(value.type)){return customEntitiesRowConfigStruct;}switch(value.type){case"attribute":{return attributeEntitiesRowConfigStruct;}case"button":{return buttonEntitiesRowConfigStruct;}case"buttons":{return buttonsEntitiesRowConfigStruct;}case"call-service":{return callServiceEntitiesRowConfigStruct;}case"cast":{return castEntitiesRowConfigStruct;}case"conditional":{return conditionalEntitiesRowConfigStruct;}case"divider":{return dividerEntitiesRowConfigStruct;}case"section":{return sectionEntitiesRowConfigStruct;}case"text":{return textEntitiesRowConfigStruct;}case"weblink":{return webLinkEntitiesRowConfigStruct;}}}// No "type" property => has to be the default entity row config struct
return entitiesConfigStruct;});const cardConfigStruct=assign(baseLovelaceCardConfig,object({title:optional(union([string(),boolean()])),entity:optional(entityId()),theme:optional(string()),icon:optional(string()),show_header_toggle:optional(boolean()),state_color:optional(boolean()),entities:array(entitiesRowConfigStruct),header:optional(headerFooterConfigStructs),footer:optional(headerFooterConfigStructs)}));let HuiEntitiesCardEditor=_decorate([n("hui-entities-card-editor")],function(_initialize,_LitElement){class HuiEntitiesCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEntitiesCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"field",decorators:[t()],key:"_subElementEditorConfig",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;this._configEntities=processEditorEntities(config.entities);}},{kind:"get",key:"_title",value:function _title(){return this._config.title||"";}},{kind:"get",key:"_theme",value:function _theme(){return this._config.theme||"";}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}if(this._subElementEditorConfig){return $`
        <hui-sub-element-editor
          .hass=${this.hass}
          .config=${this._subElementEditorConfig}
          @go-back=${this._goBack}
          @config-changed=${this._handleSubElementChanged}
        >
        </hui-sub-element-editor>
      `;}return $`
      <div class="card-config">
        <ha-textfield
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.title")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
          .value=${this._title}
          .configValue=${"title"}
          @input=${this._valueChanged}
        ></ha-textfield>
        <!-- <hui-theme-select-editor
          .hass=${this.hass}
          .value=${this._theme}
          .configValue=${"theme"}
          @value-changed=${this._valueChanged}
        ></hui-theme-select-editor> -->
        <div class="side-by-side">
          <ha-formfield
            .label=${""+this.hass.localize("ui.panel.lovelace.editor.card.entities.show_header_toggle")}
            .dir=${computeRTLDirection(this.hass)}
          >
            <ha-switch
              .checked=${this._config.show_header_toggle}
              .configValue=${"show_header_toggle"}
              @change=${this._valueChanged}
            ></ha-switch>
          </ha-formfield>
          <!-- <ha-formfield
            .label=${this.hass.localize("ui.panel.lovelace.editor.card.generic.state_color")}
            .dir=${computeRTLDirection(this.hass)}
          >
            <ha-switch
              .checked=${this._config.state_color}
              .configValue=${"state_color"}
              @change=${this._valueChanged}
            ></ha-switch>
          </ha-formfield> -->
        </div>
        <!-- <hui-header-footer-editor
          .hass=${this.hass}
          .configValue=${"header"}
          .config=${this._config.header}
          @value-changed=${this._valueChanged}
          @edit-detail-element=${this._editDetailElement}
        ></hui-header-footer-editor>
        <hui-header-footer-editor
          .hass=${this.hass}
          .configValue=${"footer"}
          .config=${this._config.footer}
          @value-changed=${this._valueChanged}
          @edit-detail-element=${this._editDetailElement}
        ></hui-header-footer-editor> -->
      </div>
      <hui-entities-card-row-editor
        .hass=${this.hass}
        .entities=${this._configEntities}
        @entities-changed=${this._valueChanged}
        @edit-detail-element=${this._editDetailElement}
      ></hui-entities-card-row-editor>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){var _this$_subElementEdit;ev.stopPropagation();if(!this._config||!this.hass){return;}const target=ev.target;const configValue=target.configValue||((_this$_subElementEdit=this._subElementEditorConfig)===null||_this$_subElementEdit===void 0?void 0:_this$_subElementEdit.type);const value=target.checked!==undefined?target.checked:target.value||ev.detail.config||ev.detail.value;if(configValue==="title"&&target.value===this._title||configValue==="theme"&&target.value===this._theme){return;}if(configValue==="row"||ev.detail&&ev.detail.entities){const newConfigEntities=ev.detail.entities||this._configEntities.concat();if(configValue==="row"){if(!value){newConfigEntities.splice(this._subElementEditorConfig.index,1);this._goBack();}else {newConfigEntities[this._subElementEditorConfig.index]=value;}this._subElementEditorConfig.elementConfig=value;}this._config={...this._config,entities:newConfigEntities};this._configEntities=processEditorEntities(this._config.entities);}else if(configValue){if(value===""){this._config={...this._config};delete this._config[configValue];}else {this._config={...this._config,[configValue]:value};}}fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_handleSubElementChanged",value:function _handleSubElementChanged(ev){var _this$_subElementEdit2;ev.stopPropagation();if(!this._config||!this.hass){return;}const configValue=(_this$_subElementEdit2=this._subElementEditorConfig)===null||_this$_subElementEdit2===void 0?void 0:_this$_subElementEdit2.type;const value=ev.detail.config;if(configValue==="row"){const newConfigEntities=this._configEntities.concat();if(!value){newConfigEntities.splice(this._subElementEditorConfig.index,1);this._goBack();}else {newConfigEntities[this._subElementEditorConfig.index]=value;}this._config={...this._config,entities:newConfigEntities};this._configEntities=processEditorEntities(this._config.entities);}else if(configValue){if(value===""){this._config={...this._config};delete this._config[configValue];}else {this._config={...this._config,[configValue]:value};}}this._subElementEditorConfig={...this._subElementEditorConfig,elementConfig:value};fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_editDetailElement",value:function _editDetailElement(ev){this._subElementEditorConfig=ev.detail.subElementConfig;}},{kind:"method",key:"_goBack",value:function _goBack(){this._subElementEditorConfig=undefined;}},{kind:"get",static:true,key:"styles",value:function styles(){return [configElementStyle,r`
        .edit-entity-row-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-size: 18px;
        }

        hui-header-footer-editor {
          padding-top: 4px;
        }

        ha-textfield {
          display: block;
          margin-bottom: 16px;
        }

        /* ha-formfield {
          margin-left: 5%;
          margin-top: 3%;
          margin-bottom: 3%;
          /* min-height: 36px; */
          /* display: flex;
          justify-content: center;
          align-items: flex-end;
          width: 100%;
          flex-direction: row;
        } */

        ha-switch2 {
          padding-right: 20px;
        } */
      `];}}]};},s);

export { HuiEntitiesCardEditor };
