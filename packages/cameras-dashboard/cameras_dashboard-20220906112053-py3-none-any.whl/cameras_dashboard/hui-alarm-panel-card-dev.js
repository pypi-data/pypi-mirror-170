const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, R as e$1, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, z as o, T as RippleHandlers, K as e$2, f as fireEvent, r, n } from './main-dev.js';
import { aP as alarmPanelIcon, a as UNAVAILABLE } from './auth-dev.js';
import { F as FORMAT_NUMBER, c as callAlarmAction } from './alarm_control_panel-dev.js';
import { W as findEntities, Z as createEntityNotFoundWarning } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const BUTTONS=["1","2","3","4","5","6","7","8","9","","0","clear"];_decorate([n("hui-alarm-panel-card")],function(_initialize,_LitElement){class HuiAlarmPanelCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiAlarmPanelCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-alarm-panel-card-editor-dev.js');return document.createElement("hui-alarm-panel-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const includeDomains=["alarm_control_panel"];const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains);return {type:"alarm-panel",states:["arm_home","arm_away"],entity:foundEntities[0]||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[i("#alarmCode")],key:"_input",value:void 0},{kind:"field",decorators:[e({type:String})],key:"layout",value(){return "big";}},{kind:"field",decorators:[t()],key:"_shouldRenderRipple",value(){return false;}},{kind:"field",decorators:[t()],key:"_show_lock",value(){return false;}},{kind:"field",decorators:[e$1("mwc-ripple")],key:"_ripple",value:void 0},{kind:"method",key:"getCardSize",value:async function getCardSize(){if(!this._config||!this.hass){return 9;}const stateObj=this.hass.states[this._config.entity];return !stateObj||stateObj.attributes.code_format!==FORMAT_NUMBER?4:9;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.entity||config.entity.split(".")[0]!=="alarm_control_panel"){throw new Error("Invalid configuration");}const defaults={states:["arm_away","arm_home"]};this._config={...defaults,...config};}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiAlarmPanelCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}if(oldHass&&(oldHass.states[this._config.entity].state==="disarmed"||oldHass.states[this._config.entity].state==="arming")&&this.hass.states[this._config.entity].state!=="disarmed"&&this.hass.states[this._config.entity].state!=="arming"){this._show_lock=true;setTimeout(()=>{this._show_lock=false;},1500);}}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("_config")){return true;}const oldHass=changedProps.get("hass");if(!oldHass||oldHass.themes!==this.hass.themes||oldHass.locale!==this.hass.locale){return true;}return oldHass.states[this._config.entity]!==this.hass.states[this._config.entity];}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning> ${createEntityNotFoundWarning(this.hass)} </hui-warning>
      `;}const stateLabel=this._stateDisplay(stateObj.state);console.log("armed",stateObj.state);return $`
      ${this.layout==="big"?$`
            <ha-card>
              <div
                class=${o({blur_this_b:this._show_lock===true,content_main:this._show_lock===false})}
              >
                <h1 class="card-header">
                  ${this._config.name||stateObj.attributes.friendly_name||stateLabel}
                  <ha-chip
                    hasIcon
                    class=${o({[stateObj.state]:true})}
                    @click=${this._handleMoreInfo}
                  >
                    <ha-svg-icon
                      slot="icon"
                      .path=${alarmPanelIcon(stateObj.state)}
                    >
                    </ha-svg-icon>
                    ${stateLabel}
                  </ha-chip>
                </h1>
                <div id="armActions" class="actions">
                  ${(stateObj.state==="disarmed"?this._config.states:["disarm"]).map(stateAction=>$`
                      <mwc-button
                        .action=${stateAction}
                        @click=${this._handleActionClick}
                        outlined
                      >
                        ${this._actionDisplay(stateAction)}
                      </mwc-button>
                    `)}
                </div>
                ${!stateObj.attributes.code_format?$``:$`
                      <ha-textfield
                        id="alarmCode"
                        .label=${this.hass.localize("ui.card.alarm_control_panel.code")}
                        type="password"
                        .inputmode=${stateObj.attributes.code_format===FORMAT_NUMBER?"numeric":"text"}
                      ></ha-textfield>
                    `}
                ${stateObj.attributes.code_format!==FORMAT_NUMBER?$``:$`
                      <div id="keypad">
                        ${BUTTONS.map(value=>value===""?$` <mwc-button disabled></mwc-button> `:$`
                                <mwc-button
                                  .value=${value}
                                  @click=${this._handlePadClick}
                                  outlined
                                  class=${o({numberkey:value!=="clear"})}
                                >
                                  ${value==="clear"?this.hass.localize(`ui.card.alarm_control_panel.clear_code`):value}
                                </mwc-button>
                              `)}
                      </div>
                    `}
              </div>
              ${this._show_lock?$`
                    <svg
                      viewBox="-10 -8 70 70"
                      height="100%"
                      width="100%"
                      class="svg-icon"
                    >
                      <path
                        id="svg-lock"
                        d="M 25 3 C 18.3633 3 13 8.3633 13 15 L 13 20 L 37 20 L 37 15 C 37 8.3633 31.6367 3 25 3 Z M 25 5 C 30.5664 5 35 9.4336 35 15 L 35 20 L 15 20 L 15 15 C 15 9.4336 19.4336 5 25 5 Z M 25 3"
                      />
                      <path
                        id="svg-base"
                        d="M 35 20 L 37 20 L 9 20 C 7.3008 20 6 21.3008 6 23 L 6 47 C 6 48.6992 7.3008 50 9 50 L 41 50 C 42.6992 50 44 48.6992 44 47 L 44 23 C 44 21.3008 42.6992 20 41 20 L 35 20 M 35 20 V 20 H 37 M 37 20 M 35 20 L 35 15 L 37 15 L 37 20 Z Z Z Z M 25 30 C 26.6992 30 28 31.3008 28 33 C 28 33.8984 27.6016 34.6875 27 35.1875 L 27 38 C 27 39.1016 26.1016 40 25 40 C 23.8984 40 23 39.1016 23 38 L 23 35.1875 C 22.3984 34.6875 22 33.8984 22 33 C 22 31.3008 23.3008 30 25 30 Z"
                      />
                    </svg>
                  `:$``}
            </ha-card>
          `:$`
            <ha-card
              @click=${this._handleMoreInfo}
              @focus=${this.handleRippleFocus}
              @blur=${this.handleRippleBlur}
              @mousedown=${this.handleRippleActivate}
              @mouseup=${this.handleRippleDeactivate}
              @touchstart=${this.handleRippleActivate}
              @touchend=${this.handleRippleDeactivate}
              @touchcancel=${this.handleRippleDeactivate}
              class=${o({"small-card":this.layout==="small","medium-card":this.layout==="medium",unavailable:stateObj.state===UNAVAILABLE})}
            >
              <ha-state-icon
                class="ha-status-icon-small"
                .icon=${"shield-home"}
              >
              </ha-state-icon>
              ${this._shouldRenderRipple?$`<mwc-ripple></mwc-ripple>`:""}
              ${stateObj.state===UNAVAILABLE?$` <unavailable-icon></unavailable-icon>`:$``}</ha-card
            >
          `}
    `;}},{kind:"field",key:"_rippleHandlers",value(){return new RippleHandlers(()=>{this._shouldRenderRipple=true;return this._ripple;});}},{kind:"method",decorators:[e$2({passive:true})],key:"handleRippleActivate",value:function handleRippleActivate(evt){this._rippleHandlers.startPress(evt);}},{kind:"method",key:"handleRippleDeactivate",value:function handleRippleDeactivate(){this._rippleHandlers.endPress();}},{kind:"method",key:"handleRippleFocus",value:function handleRippleFocus(){this._rippleHandlers.startFocus();}},{kind:"method",key:"handleRippleBlur",value:function handleRippleBlur(){this._rippleHandlers.endFocus();}},{kind:"method",key:"_actionDisplay",value:function _actionDisplay(entityState){return this.hass.localize(`ui.card.alarm_control_panel.${entityState}`);}},{kind:"method",key:"_stateDisplay",value:function _stateDisplay(entityState){return entityState===UNAVAILABLE?this.hass.localize("state.default.unavailable"):this.hass.localize(`component.alarm_control_panel.state._.${entityState}`)||entityState;}},{kind:"method",key:"_handlePadClick",value:function _handlePadClick(e){const val=e.currentTarget.value;this._input.value=val==="clear"?"":this._input.value+val;}},{kind:"method",key:"_handleActionClick",value:function _handleActionClick(e){const input=this._input;callAlarmAction(this.hass,this._config.entity,e.currentTarget.action,(input===null||input===void 0?void 0:input.value)||undefined);if(input){input.value="";}}},{kind:"method",key:"_handleMoreInfo",value:function _handleMoreInfo(){fireEvent(this,"hass-more-info",{entityId:this._config.entity});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .unavailable {
        pointer-events: none;
      }
      unavailable-icon {
        position: absolute;
        top: 11px;
        right: 10%;
      }

      ha-card:focus {
        outline: none;
      }

      .ha-status-icon-small {
        width: 63%;
        /* margin-left: 5%; */
        height: auto;
        color: var(--paper-item-icon-color, #7b7b7b);
        --mdc-icon-size: 100%;
      }
      .svg-icon {
        fill: var(--paper-item-icon-color, #44739e);
      }

      ha-state-icon,
      span {
        outline: none;
      }
      unavailable-icon {
        position: absolute;
        top: 11px;
        right: 10%;
      }
      .state {
        font-size: 0.9rem;
        color: var(--secondary-text-color);
      }

      ha-card {
        padding-bottom: 16px;
        position: relative;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-sizing: border-box;
        --alarm-color-disarmed: var(--label-badge-green);
        --alarm-color-pending: var(--label-badge-yellow);
        --alarm-color-triggered: var(--label-badge-red);
        --alarm-color-armed: var(--label-badge-red);
        --alarm-color-autoarm: rgba(0, 153, 255, 0.1);
        --alarm-state-color: var(--alarm-color-armed);
      }
      .small-card {
        cursor: pointer;
        display: flex;
        flex-direction: column;
        padding: 4% 0;
        font-size: 1.2rem;
        height: 100%;
        box-sizing: border-box;
        justify-content: center;
        overflow: hidden;
        border-radius: 1.5rem;
        font-weight: 450;
        /* aspect-ratio: 1; */
      }
      .medium-card {
        cursor: pointer;
        display: flex;
        flex-direction: column;
        padding: 4% 0;
        font-size: 1.8rem;
        height: 100%;
        box-sizing: border-box;
        justify-content: center;
        overflow: hidden;
        border-radius: 1.5rem;
        font-weight: 450;
        /* aspect-ratio: 1; */
      }

      ha-chip {
        --ha-chip-background-color: var(--alarm-state-color);
        --primary-text-color: var(--text-primary-color);
        line-height: initial;
      }

      .card-header {
        display: flex;
        padding: 0 6%;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        font-size: 1.5rem;
        font-weight: 400;
        box-sizing: border-box;
      }

      ha-chip {
        animation: none;
      }
      .unavailable {
        --alarm-state-color: var(--state-unavailable-color);
      }

      .disarmed {
        --alarm-state-color: var(--alarm-color-disarmed);
        animation: none;
      }

      .triggered {
        --alarm-state-color: var(--alarm-color-triggered);
        animation: pulse 1s infinite;
      }

      .arming {
        --alarm-state-color: var(--alarm-color-pending);
        animation: pulse 1s infinite;
      }

      .pending {
        --alarm-state-color: var(--alarm-color-pending);
        animation: pulse 1s infinite;
      }

      @keyframes pulse {
        0% {
          opacity: 1;
        }
        50% {
          opacity: 0;
        }
        100% {
          opacity: 1;
        }
      }

      @keyframes lock {
        0% {
          transform: matrix(1, 0, 0, 1, 0, -4.7);
          fill: var(--paper-item-icon-color, #44739e);
        }
        100% {
          transform: matrix(1, 0, 0, 1, 0, 0);
          fill: var(--accent-color);
        }
      }
      @keyframes lock-color {
        0% {
          fill: var(--paper-item-icon-color, #44739e);
        }
        100% {
          fill: var(--accent-color);
        }
      }

      ha-textfield {
        display: block;
        margin: 8px;
        max-width: 150px;
        text-align: center;
      }

      .state {
        margin-left: 16px;
        position: relative;
        bottom: 16px;
        color: var(--alarm-state-color);
        animation: none;
      }

      #keypad {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin: auto;
        width: 100%;
        max-width: 300px;
      }

      #keypad mwc-button {
        padding: 8px;
        width: 30%;
        box-sizing: border-box;
      }

      .actions {
        margin: 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }

      .actions mwc-button {
        margin: 0 4px 4px;
      }

      mwc-button#disarm {
        color: var(--error-color);
      }

      mwc-button.numberkey {
        --mdc-typography-button-font-size: var(--keypad-font-size, 0.875rem);
      }

      .blur_this_b {
        transition: 0.8s ease-out;
        filter: blur(1.5rem);
      }
      .content_main {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-sizing: border-box;
        transition: 0.6s ease-out;
      }
      .svg-icon {
        position: absolute;
        width: 60%;
      }
      #svg-lock {
        animation: lock 1.5s ease-out;
      }
      #svg-base {
        animation: lock-color 1.5s ease-out;
      }
    `;}}]};},s);
