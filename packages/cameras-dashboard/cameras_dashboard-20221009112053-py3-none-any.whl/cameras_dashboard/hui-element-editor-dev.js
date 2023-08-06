const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, b as memoizeOne, $, f as fireEvent, n, N as _defineProperty, G as i, j as _get, k as _getPrototypeOf, r } from './main-dev.js';
import { d as dump, l as load } from './js-yaml-dev.js';
import { h as handleStructError } from './ha-code-editor-dev.js';
import { H as deepEqual } from './ha-more-info-dialog-dev.js';
import './ha-circular-progress-dev.js';
import './stop_propagation-dev.js';
import './ha-form-dev.js';
import { aq as assert, e as computeDomain, C as domainIcon } from './auth-dev.js';
import { e as entitiesConfigStruct } from './entities-struct-dev.js';

const SecondaryInfoValues={"entity-id":{},"last-changed":{},"last-updated":{},"last-triggered":{domains:["automation","script"]},position:{domains:["cover"]},"tilt-position":{domains:["cover"]},brightness:{domains:["light"]}};_decorate([n("hui-generic-entity-row-editor")],function(_initialize,_LitElement){class HuiGenericEntityRowEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGenericEntityRowEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,entitiesConfigStruct);this._config=config;}},{kind:"field",key:"_schema",value(){return memoizeOne((entity,icon,entityState,localize)=>{const domain=computeDomain(entity);return [{name:"entity",required:true,selector:{entity:{}}},{type:"grid",name:"",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{placeholder:icon||(entityState===null||entityState===void 0?void 0:entityState.attributes.icon),fallbackPath:!icon&&!(entityState!==null&&entityState!==void 0&&entityState.attributes.icon)&&entityState?domainIcon(domain,entityState):undefined}}}]},{name:"secondary_info",selector:{select:{options:Object.keys(SecondaryInfoValues).filter(info=>!("domains"in SecondaryInfoValues[info])||"domains"in SecondaryInfoValues[info]&&SecondaryInfoValues[info].domains.includes(domain)).map(info=>({value:info,label:localize(`ui.panel.lovelace.editor.card.entities.secondary_info_values.${info}`)}))}}}];});}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const entityState=this.hass.states[this._config.entity];const schema=this._schema(this._config.entity,this._config.icon,entityState,this.hass.localize);return $`
      <ha-form
        .hass=${this.hass}
        .data=${this._config}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{if(schema.name==="entity"){return this.hass.localize("ui.panel.lovelace.editor.card.generic.entity");}return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.entity-row.${schema.name}`);};}}]};},s);

class GUISupportError extends Error{constructor(message,warnings,errors){super(message);_defineProperty(this,"warnings",void 0);_defineProperty(this,"errors",void 0);this.name="GUISupportError";this.warnings=warnings;this.errors=errors;}}

let HuiElementEditor=_decorate(null,function(_initialize,_LitElement){class HuiElementEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiElementEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"lovelace",value:void 0},{kind:"field",decorators:[t()],key:"_yaml",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configElement",value:void 0},{kind:"field",decorators:[t()],key:"_configElementType",value:void 0},{kind:"field",decorators:[t()],key:"_guiMode",value(){return true;}},{kind:"field",decorators:[t()],key:"_errors",value:void 0},{kind:"field",decorators:[t()],key:"_warnings",value:void 0},{kind:"field",decorators:[t()],key:"_guiSupported",value:void 0},{kind:"field",decorators:[t()],key:"_loading",value(){return false;}},{kind:"field",decorators:[i("ha-code-editor")],key:"_yamlEditor",value:void 0},{kind:"get",key:"yaml",value:// Error: Configuration broken - do not save
// Warning: GUI editor can't handle configuration - ok to save
function yaml(){if(!this._yaml){this._yaml=dump(this._config);}return this._yaml||"";}},{kind:"set",key:"yaml",value:function yaml(_yaml){this._yaml=_yaml;try{this._config=load(this.yaml);this._errors=undefined;}catch(err){this._errors=[err.message];}this._setConfig();}},{kind:"get",key:"value",value:function value(){return this._config;}},{kind:"set",key:"value",value:function value(config){if(this._config&&deepEqual(config,this._config)){return;}this._config=config;this._yaml=undefined;this._errors=undefined;this._setConfig();}},{kind:"method",key:"_setConfig",value:function _setConfig(){var _this$_errors;if(!this._errors){try{this._updateConfigElement();}catch(err){this._errors=[err.message];}}fireEvent(this,"config-changed",{config:this.value,error:(_this$_errors=this._errors)===null||_this$_errors===void 0?void 0:_this$_errors.join(", "),guiModeAvailable:!(this.hasWarning||this.hasError||this._guiSupported===false)});}},{kind:"get",key:"hasWarning",value:function hasWarning(){return this._warnings!==undefined&&this._warnings.length>0;}},{kind:"get",key:"hasError",value:function hasError(){return this._errors!==undefined&&this._errors.length>0;}},{kind:"get",key:"GUImode",value:function GUImode(){return this._guiMode;}},{kind:"set",key:"GUImode",value:function GUImode(guiMode){this._guiMode=guiMode;fireEvent(this,"GUImode-changed",{guiMode,guiModeAvailable:!(this.hasWarning||this.hasError||this._guiSupported===false)});}},{kind:"method",key:"toggleMode",value:function toggleMode(){this.GUImode=!this.GUImode;}},{kind:"method",key:"focusYamlEditor",value:function focusYamlEditor(){var _this$_configElement,_this$_yamlEditor;if((_this$_configElement=this._configElement)!==null&&_this$_configElement!==void 0&&_this$_configElement.focusYamlEditor){this._configElement.focusYamlEditor();}if(!((_this$_yamlEditor=this._yamlEditor)!==null&&_this$_yamlEditor!==void 0&&_this$_yamlEditor.codemirror)){return;}this._yamlEditor.codemirror.focus();}},{kind:"method",key:"getConfigElement",value:async function getConfigElement(){return undefined;}},{kind:"get",key:"configElementType",value:function configElementType(){return this.value?this.value.type:undefined;}},{kind:"method",key:"render",value:function render(){return $`
      <div class="wrapper">
        ${this.GUImode?$`
              <div class="gui-editor">
                ${this._loading?$`
                      <ha-circular-progress
                        active
                        alt="Loading"
                        class="center margin-bot"
                      ></ha-circular-progress>
                    `:this._configElement}
              </div>
            `:$`
              <div class="yaml-editor">
                <!-- <ha-code-editor
                  mode="yaml"
                  autofocus
                  autocomplete-entities
                  .hass=${this.hass}
                  .value=${this.yaml}
                  .error=${Boolean(this._errors)}
                  @value-changed=${this._handleYAMLChanged}
                  @keydown=${this._ignoreKeydown}
                  dir="ltr"
                ></ha-code-editor> -->
              </div>
            `}
        ${this._guiSupported===false&&this.configElementType?$`
              <div class="info">
                ${this.hass.localize("ui.errors.config.editor_not_available","type",this.configElementType)}
              </div>
            `:""}
        ${this.hasError?$`
              <div class="error">
                ${this.hass.localize("ui.errors.config.error_detected")}:
                <br />
                <ul>
                  ${this._errors.map(error=>$`<li>${error}</li>`)}
                </ul>
              </div>
            `:""}
        ${this.hasWarning?$`
              <ha-alert
                alert-type="warning"
                .title="${this.hass.localize("ui.errors.config.editor_not_supported")}:"
              >
                ${this._warnings.length>0&&this._warnings[0]!==undefined?$` <ul>
                      ${this._warnings.map(warning=>$`<li>${warning}</li>`)}
                    </ul>`:""}
                ${this.hass.localize("ui.errors.config.edit_in_yaml_supported")}
              </ha-alert>
            `:""}
      </div>
    `;}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(HuiElementEditor.prototype),"updated",this).call(this,changedProperties);if(this._configElement&&changedProperties.has("hass")){this._configElement.hass=this.hass;}if(this._configElement&&"lovelace"in this._configElement&&changedProperties.has("lovelace")){this._configElement.lovelace=this.lovelace;}}},{kind:"method",key:"_handleUIConfigChanged",value:function _handleUIConfigChanged(ev){ev.stopPropagation();const config=ev.detail.config;this.value=config;}},{kind:"method",key:"_handleYAMLChanged",value:function _handleYAMLChanged(ev){ev.stopPropagation();const newYaml=ev.detail.value;if(newYaml!==this.yaml){this.yaml=newYaml;}}},{kind:"method",key:"_updateConfigElement",value:async function _updateConfigElement(){if(!this.value){return;}let configElement;try{this._errors=undefined;this._warnings=undefined;if(this._configElementType!==this.configElementType){// If the type has changed, we need to load a new GUI editor
this._guiSupported=undefined;this._configElement=undefined;if(!this.configElementType){throw new Error(this.hass.localize("ui.errors.config.no_type_provided"));}this._configElementType=this.configElementType;this._loading=true;configElement=await this.getConfigElement();if(configElement){configElement.hass=this.hass;if("lovelace"in configElement){configElement.lovelace=this.lovelace;}configElement.addEventListener("config-changed",ev=>this._handleUIConfigChanged(ev));this._configElement=configElement;this._guiSupported=true;}}if(this._configElement){// Setup GUI editor and check that it can handle the current config
try{this._configElement.setConfig(this.value);}catch(err){const msgs=handleStructError(this.hass,err);throw new GUISupportError("Config is not supported",msgs.warnings,msgs.errors);}}else {this._guiSupported=false;this.GUImode=false;}}catch(err){if(err instanceof GUISupportError){var _err$warnings;this._warnings=(_err$warnings=err.warnings)!==null&&_err$warnings!==void 0?_err$warnings:[err.message];this._errors=err.errors||undefined;}else {this._errors=[err.message];}this.GUImode=false;}finally{this._loading=false;}}},{kind:"method",key:"_ignoreKeydown",value:function _ignoreKeydown(ev){ev.stopPropagation();}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: flex;
      }
      .wrapper {
        width: 100%;
      }
      .gui-editor,
      .yaml-editor {
        padding: 8px 0px;
      }
      ha-code-editor {
        --code-mirror-max-height: calc(100vh - 245px);
      }
      .error,
      .warning,
      .info {
        word-break: break-word;
        margin-top: 8px;
      }
      .error {
        color: var(--error-color);
      }
      .warning {
        color: var(--warning-color);
      }
      .warning ul,
      .error ul {
        margin: 4px 0;
      }
      .warning li,
      .error li {
        white-space: pre-wrap;
      }
      ha-circular-progress {
        display: block;
        margin: auto;
      }
    `;}}]};},s);

export { HuiElementEditor as H };
