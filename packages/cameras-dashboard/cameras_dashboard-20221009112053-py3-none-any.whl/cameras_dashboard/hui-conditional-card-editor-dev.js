const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, $, f as fireEvent, r, n } from './main-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-header-bar-dev.js';
import { am as object, ao as string, an as optional, al as assign, aw as any, as as array, aq as assert } from './auth-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import './ha-entity-picker-dev.js';
import './hui-card-picker-dev.js';
import './hui-element-editor-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './ha-combo-box-dev.js';
import './ha-more-info-dialog-dev.js';
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
import './entities-struct-dev.js';
import './action-struct-dev.js';

const conditionStruct=object({entity:string(),state:optional(string()),state_not:optional(string())});const cardConfigStruct=assign(baseLovelaceCardConfig,object({card:any(),conditions:optional(array(conditionStruct))}));let HuiConditionalCardEditor=_decorate([n("hui-conditional-card-editor")],function(_initialize,_LitElement){class HuiConditionalCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiConditionalCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"lovelace",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_GUImode",value(){return true;}},{kind:"field",decorators:[t()],key:"_guiModeAvailable",value(){return true;}},{kind:"field",decorators:[t()],key:"_cardTab",value(){return false;}},{kind:"field",decorators:[i("hui-card-element-editor")],key:"_cardEditorEl",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"method",key:"focusYamlEditor",value:function focusYamlEditor(){var _this$_cardEditorEl;(_this$_cardEditorEl=this._cardEditorEl)===null||_this$_cardEditorEl===void 0?void 0:_this$_cardEditorEl.focusYamlEditor();}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <mwc-tab-bar
        .activeIndex=${this._cardTab?1:0}
        @MDCTabBar:activated=${this._selectTab}
      >
        <mwc-tab
          .label=${this.hass.localize("ui.panel.lovelace.editor.card.conditional.conditions")}
        ></mwc-tab>
        <mwc-tab
          .label=${this.hass.localize("ui.panel.lovelace.editor.card.conditional.card")}
        ></mwc-tab>
      </mwc-tab-bar>
      ${this._cardTab?$`
            <div class="card">
              ${this._config.card.type!==undefined?$`
                    <div class="card-options">
                      <mwc-button
                        @click=${this._toggleMode}
                        .disabled=${!this._guiModeAvailable}
                        class="gui-mode-button"
                      >
                        ${this.hass.localize(!this._cardEditorEl||this._GUImode?"ui.panel.lovelace.editor.edit_card.show_code_editor":"ui.panel.lovelace.editor.edit_card.show_visual_editor")}
                      </mwc-button>
                      <mwc-button @click=${this._handleReplaceCard}
                        >${this.hass.localize("ui.panel.lovelace.editor.card.conditional.change_type")}</mwc-button
                      >
                    </div>
                    <hui-card-element-editor
                      .hass=${this.hass}
                      .value=${this._config.card}
                      .lovelace=${this.lovelace}
                      @config-changed=${this._handleCardChanged}
                      @GUImode-changed=${this._handleGUIModeChanged}
                    ></hui-card-element-editor>
                  `:$`
                    <hui-card-picker
                      .hass=${this.hass}
                      .lovelace=${this.lovelace}
                      @config-changed=${this._handleCardPicked}
                    ></hui-card-picker>
                  `}
            </div>
          `:$`
            <div class="conditions">
              ${this.hass.localize("ui.panel.lovelace.editor.card.conditional.condition_explanation")}
              ${this._config.conditions.map((cond,idx)=>{var _this$hass;return $`
                  <div class="condition">
                    <div class="entity">
                      <ha-entity-picker
                        .hass=${this.hass}
                        .value=${cond.entity}
                        .idx=${idx}
                        .configValue=${"entity"}
                        @change=${this._changeCondition}
                        allow-custom-entity
                      ></ha-entity-picker>
                    </div>
                    <div class="state">
                      <ha-select
                        .value=${cond.state_not!==undefined?"true":"false"}
                        .idx=${idx}
                        .configValue=${"invert"}
                        @selected=${this._changeCondition}
                        @closed=${stopPropagation}
                        naturalMenuWidth
                        fixedMenuPosition
                      >
                        <mwc-list-item value="false">
                          ${this.hass.localize("ui.panel.lovelace.editor.card.conditional.state_equal")}
                        </mwc-list-item>
                        <mwc-list-item value="true">
                          ${this.hass.localize("ui.panel.lovelace.editor.card.conditional.state_not_equal")}
                        </mwc-list-item>
                      </ha-select>
                      <ha-textfield
                        .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.state")} (${this.hass.localize("ui.panel.lovelace.editor.card.conditional.current_state")}: ${(_this$hass=this.hass)===null||_this$hass===void 0?void 0:_this$hass.states[cond.entity].state})"
                        .value=${cond.state_not!==undefined?cond.state_not:cond.state}
                        .idx=${idx}
                        .configValue=${"state"}
                        @input=${this._changeCondition}
                      ></ha-textfield>
                    </div>
                  </div>
                `;})}
              <div class="condition">
                <ha-entity-picker
                  .hass=${this.hass}
                  @change=${this._addCondition}
                ></ha-entity-picker>
              </div>
            </div>
          `}
    `;}},{kind:"method",key:"_selectTab",value:function _selectTab(ev){this._cardTab=ev.detail.index===1;}},{kind:"method",key:"_toggleMode",value:function _toggleMode(){var _this$_cardEditorEl2;(_this$_cardEditorEl2=this._cardEditorEl)===null||_this$_cardEditorEl2===void 0?void 0:_this$_cardEditorEl2.toggleMode();}},{kind:"method",key:"_setMode",value:function _setMode(value){this._GUImode=value;if(this._cardEditorEl){this._cardEditorEl.GUImode=value;}}},{kind:"method",key:"_handleGUIModeChanged",value:function _handleGUIModeChanged(ev){ev.stopPropagation();this._GUImode=ev.detail.guiMode;this._guiModeAvailable=ev.detail.guiModeAvailable;}},{kind:"method",key:"_handleCardPicked",value:function _handleCardPicked(ev){ev.stopPropagation();if(!this._config){return;}this._setMode(true);this._guiModeAvailable=true;this._config={...this._config,card:ev.detail.config};fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_handleCardChanged",value:function _handleCardChanged(ev){ev.stopPropagation();if(!this._config){return;}this._config={...this._config,card:ev.detail.config};this._guiModeAvailable=ev.detail.guiModeAvailable;fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_handleReplaceCard",value:function _handleReplaceCard(){if(!this._config){return;}// @ts-ignore
this._config={...this._config,card:{}};// @ts-ignore
fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_addCondition",value:function _addCondition(ev){const target=ev.target;if(target.value===""||!this._config){return;}const conditions=[...this._config.conditions];conditions.push({entity:target.value,state:""});this._config={...this._config,conditions};target.value="";fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_changeCondition",value:function _changeCondition(ev){const target=ev.target;if(!this._config||!target){return;}const conditions=[...this._config.conditions];if(target.configValue==="entity"&&target.value===""){conditions.splice(target.idx,1);}else {const condition={...conditions[target.idx]};if(target.configValue==="entity"){condition.entity=target.value;}else if(target.configValue==="state"){if(condition.state_not!==undefined){condition.state_not=target.value;}else {condition.state=target.value;}}else if(target.configValue==="invert"){if(target.value==="true"){if(condition.state){condition.state_not=condition.state;delete condition.state;}}else if(condition.state_not){condition.state=condition.state_not;delete condition.state_not;}}conditions[target.idx]=condition;}this._config={...this._config,conditions};fireEvent(this,"config-changed",{config:this._config});}},{kind:"get",static:true,key:"styles",value:function styles(){return [configElementStyle,r`
        mwc-tab-bar {
          border-bottom: 1px solid var(--divider-color);
        }
        .conditions {
          margin-top: 8px;
        }
        .condition {
          margin-top: 8px;
          border: 1px solid var(--divider-color);
          padding: 12px;
        }
        .condition .state {
          display: flex;
          align-items: flex-end;
        }
        .condition .state ha-select {
          margin-right: 16px;
        }
        .condition .state ha-textfield {
          flex-grow: 1;
        }

        .card {
          margin-top: 8px;
          border: 1px solid var(--divider-color);
          padding: 12px;
        }
        @media (max-width: 450px) {
          .card,
          .condition {
            margin: 8px -12px 0;
          }
        }
        .card .card-options {
          display: flex;
          justify-content: flex-end;
          width: 100%;
        }
        .gui-mode-button {
          margin-right: auto;
        }
      `];}}]};},s);

export { HuiConditionalCardEditor };
