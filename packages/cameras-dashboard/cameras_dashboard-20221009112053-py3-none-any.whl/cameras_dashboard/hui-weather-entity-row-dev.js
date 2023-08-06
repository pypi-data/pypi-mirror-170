const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, z as o, Q as l, r, n } from './main-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, a6 as getWeatherStateIcon, Q as actionHandler, R as hasAction, o as computeStateDisplay, z as getWeatherUnit, a7 as getSecondaryWeatherAttribute, T as handleAction, a8 as weatherSVGStyles } from './ha-more-info-dialog-dev.js';
import { j as computeStateName, h as UNAVAILABLE_STATES, f as formatNumber } from './auth-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-weather-entity-row")],function(_initialize,_LitElement){class HuiWeatherEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiWeatherEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!(config!==null&&config!==void 0&&config.entity)){throw new Error("Entity must be specified");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const pointer=!(this._config.tap_action&&this._config.tap_action.action!=="none");const weatherStateIcon=getWeatherStateIcon(stateObj.state,this);return $`
      <div
        class="icon-image ${o({pointer})}"
        @action=${this._handleAction}
        .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
        tabindex=${l(pointer?"0":undefined)}
      >
        ${weatherStateIcon||$`
          <ha-state-icon
            class="weather-icon"
            .state=${stateObj}
          ></ha-state-icon>
        `}
      </div>
      <div
        class="info ${o({pointer})}"
        @action=${this._handleAction}
        .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
      >
        ${this._config.name||computeStateName(stateObj)}
      </div>
      <div
        class="attributes ${o({pointer})}"
        @action=${this._handleAction}
        .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
      >
        <div>
          ${UNAVAILABLE_STATES.includes(stateObj.state)?computeStateDisplay(this.hass.localize,stateObj,this.hass.locale):$`
                ${formatNumber(stateObj.attributes.temperature,this.hass.locale)}
                ${getWeatherUnit(this.hass,"temperature")}
              `}
        </div>
        <div class="secondary">
          ${getSecondaryWeatherAttribute(this.hass,stateObj)}
        </div>
      </div>
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){handleAction(this,this.hass,this._config,ev.detail.action);}},{kind:"get",static:true,key:"styles",value:function styles(){return [weatherSVGStyles,r`
        :host {
          display: flex;
          align-items: center;
          flex-direction: row;
        }

        .info {
          margin-left: 16px;
          flex: 1 0 60px;
        }

        .info,
        .info > * {
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .icon-image {
          display: flex;
          align-items: center;
          min-width: 40px;
        }

        .icon-image > * {
          flex: 0 0 40px;
          height: 40px;
        }

        .icon-image:focus {
          outline: none;
          background-color: var(--divider-color);
          border-radius: 50%;
        }

        .weather-icon {
          --mdc-icon-size: 40px;
        }

        :host([rtl]) .flex {
          margin-left: 0;
          margin-right: 16px;
        }

        .pointer {
          cursor: pointer;
        }

        .attributes {
          display: flex;
          flex-direction: column;
          justify-content: center;
          text-align: right;
          margin-left: 8px;
        }

        .secondary {
          color: var(--secondary-text-color);
        }
      `];}}]};},s);
