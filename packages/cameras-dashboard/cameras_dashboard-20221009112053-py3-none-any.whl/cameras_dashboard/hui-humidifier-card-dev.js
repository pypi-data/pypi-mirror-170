const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, af as y, ag as mdiDotsVertical, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, f as fireEvent, r, n } from './main-dev.js';
import { W as findEntities, Z as createEntityNotFoundWarning, X as hasConfigOrEntityChanged } from './ha-more-info-dialog-dev.js';
import { j as computeStateName, h as UNAVAILABLE_STATES } from './auth-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiHumidifierCard=_decorate([n("hui-humidifier-card")],function(_initialize,_LitElement){class HuiHumidifierCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiHumidifierCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-humidifier-card-editor-dev.js');return document.createElement("hui-humidifier-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const includeDomains=["humidifier"];const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains);return {type:"humidifier",entity:foundEntities[0]||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_setHum",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 6;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entity||config.entity.split(".")[0]!=="humidifier"){throw new Error("Missing humidifier entity");}this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const name=this._config.name||computeStateName(this.hass.states[this._config.entity]);const targetHumidity=stateObj.attributes.humidity!==null&&Number.isFinite(Number(stateObj.attributes.humidity))?stateObj.attributes.humidity:stateObj.attributes.min_humidity;const rtlDirection=computeRTLDirection(this.hass);const slider=UNAVAILABLE_STATES.includes(stateObj.state)?$` <round-slider disabled="true"></round-slider> `:$`
          <round-slider
            .value=${targetHumidity}
            .min=${stateObj.attributes.min_humidity}
            .max=${stateObj.attributes.max_humidity}
            .rtl=${rtlDirection==="rtl"}
            step="1"
            @value-changing=${this._dragEvent}
            @value-changed=${this._setHumidity}
          ></round-slider>
        `;const setValues=y`
      <svg viewBox="0 0 40 20">
        <text
          x="50%"
          dx="1"
          y="60%"
          text-anchor="middle"
          style="font-size: 13px;"
          class="set-value"
        >
          ${UNAVAILABLE_STATES.includes(stateObj.state)||this._setHum===undefined||this._setHum===null?"":y`
                    ${this._setHum.toFixed()}
                    <tspan dx="-3" dy="-6.5" style="font-size: 4px;">
                      %
                    </tspan>
                    `}
        </text>
      </svg>
      <svg id="set-values">
        <g>
          <text
            dy="22"
            text-anchor="middle"
            id="set-mode"
          >
            ${this.hass.localize(`state.default.${stateObj.state}`)}
            ${stateObj.attributes.mode&&!UNAVAILABLE_STATES.includes(stateObj.state)?$`
                    -
                    ${this.hass.localize(`state_attributes.humidifier.mode.${stateObj.attributes.mode}`)||stateObj.attributes.mode}
                  `:""}
          </text>
        </g>
      </svg>
    `;return $`
      <ha-card>
        <ha-icon-button
          .path=${mdiDotsVertical}
          class="more-info"
          @click=${this._handleMoreInfo}
          tabindex="0"
        ></ha-icon-button>

        <div class="content">
          <div id="controls">
            <div id="slider">
              ${slider}
              <div id="slider-center">
                <div id="humidity">${setValues}</div>
              </div>
            </div>
          </div>
          <div id="info" .title=${name}>${name}</div>
        </div>
      </ha-card>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiHumidifierCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass||!changedProps.has("hass")&&!changedProps.has("_config")){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return;}if(!oldHass||oldHass.states[this._config.entity]!==stateObj){this._rescale_svg();}}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){if(!this.hass||!this._config||!changedProps.has("hass")){return;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return;}const oldHass=changedProps.get("hass");if(!oldHass||oldHass.states[this._config.entity]!==stateObj){this._setHum=this._getSetHum(stateObj);}}},{kind:"method",key:"_rescale_svg",value:function _rescale_svg(){// Set the viewbox of the SVG containing the set humidity to perfectly
// fit the text
// That way it will auto-scale correctly
// This is not done to the SVG containing the current humidity, because
// it should not be centered on the text, but only on the value
if(this.shadowRoot&&this.shadowRoot.querySelector("ha-card")){this.shadowRoot.querySelector("ha-card").updateComplete.then(()=>{const svgRoot=this.shadowRoot.querySelector("#set-values");const box=svgRoot.querySelector("g").getBBox();svgRoot.setAttribute("viewBox",`${box.x} ${box.y} ${box.width} ${box.height}`);svgRoot.setAttribute("width",`${box.width}`);svgRoot.setAttribute("height",`${box.height}`);});}}},{kind:"method",key:"_getSetHum",value:function _getSetHum(stateObj){if(UNAVAILABLE_STATES.includes(stateObj.state)){return undefined;}return stateObj.attributes.humidity;}},{kind:"method",key:"_dragEvent",value:function _dragEvent(e){this._setHum=e.detail.value;}},{kind:"method",key:"_setHumidity",value:function _setHumidity(e){this.hass.callService("humidifier","set_humidity",{entity_id:this._config.entity,humidity:e.detail.value});}},{kind:"method",key:"_handleMoreInfo",value:function _handleMoreInfo(){fireEvent(this,"hass-more-info",{entityId:this._config.entity});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
      }

      ha-card {
        height: 100%;
        position: relative;
        overflow: hidden;
        --name-font-size: 1.2rem;
        --brightness-font-size: 1.2rem;
        --rail-border-color: transparent;
      }

      .more-info {
        position: absolute;
        cursor: pointer;
        top: 0;
        right: 0;
        border-radius: 100%;
        color: var(--secondary-text-color);
        z-index: 25;
      }

      .content {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
      }

      #controls {
        display: flex;
        justify-content: center;
        padding: 16px;
        position: relative;
      }

      #slider {
        height: 100%;
        width: 100%;
        position: relative;
        max-width: 250px;
        min-width: 100px;
      }

      round-slider {
        --round-slider-path-color: var(--slider-track-color);
        --round-slider-bar-color: var(--primary-color);
        padding-bottom: 10%;
      }

      #slider-center {
        position: absolute;
        width: calc(100% - 40px);
        height: calc(100% - 40px);
        box-sizing: border-box;
        border-radius: 100%;
        left: 20px;
        top: 20px;
        text-align: center;
        overflow-wrap: break-word;
        pointer-events: none;
      }

      #humidity {
        position: absolute;
        transform: translate(-50%, -50%);
        width: 100%;
        height: 50%;
        top: 45%;
        left: 50%;
      }

      #set-values {
        max-width: 80%;
        transform: translate(0, -50%);
        font-size: 20px;
      }

      #set-mode {
        fill: var(--secondary-text-color);
        font-size: 16px;
      }

      #info {
        display: flex-vertical;
        justify-content: center;
        text-align: center;
        padding: 16px;
        margin-top: -60px;
        font-size: var(--name-font-size);
      }

      text {
        fill: var(--primary-text-color);
      }
    `;}}]};},s);

export { HuiHumidifierCard };
