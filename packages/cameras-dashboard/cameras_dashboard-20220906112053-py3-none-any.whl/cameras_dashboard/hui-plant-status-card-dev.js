const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, r, f as fireEvent, n, an as mdiWaterPercent, bb as mdiThermometer, b7 as mdiWhiteBalanceSunny, eL as mdiSprout } from './main-dev.js';
import { j as computeStateName, aU as batteryIcon } from './auth-dev.js';
import { W as findEntities, X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, Q as actionHandler } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const SENSOR_ICONS={moisture:mdiWaterPercent,temperature:mdiThermometer,brightness:mdiWhiteBalanceSunny,conductivity:mdiSprout,battery:undefined};_decorate([n("hui-plant-status-card")],function(_initialize,_LitElement){class HuiPlantStatusCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPlantStatusCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-plant-status-card-editor-dev.js');return document.createElement("hui-plant-status-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const includeDomains=["plant"];const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains);return {type:"plant-status",entity:foundEntities[0]||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entity||config.entity.split(".")[0]!=="plant"){throw new Error("Missing plant entity");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiPlantStatusCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <ha-card
        class=${stateObj.attributes.entity_picture?"has-plant-image":""}
      >
        <div
          class="banner"
          style="background-image:url(${stateObj.attributes.entity_picture})"
        >
          <div class="header">
            ${this._config.name||computeStateName(stateObj)}
          </div>
        </div>
        <div class="content">
          ${this.computeAttributes(stateObj).map(item=>$`
              <div
                class="attributes"
                @action=${this._handleMoreInfo}
                .actionHandler=${actionHandler()}
                tabindex="0"
                .value=${item}
              >
                <div>
                  <ha-svg-icon
                    .path=${this.computeIcon(item,stateObj.attributes.battery)}
                  ></ha-svg-icon>
                </div>
                <div
                  class=${stateObj.attributes.problem.indexOf(item)===-1?"":"problem"}
                >
                  ${stateObj.attributes[item]}
                </div>
                <div class="uom">
                  ${stateObj.attributes.unit_of_measurement_dict[item]||""}
                </div>
              </div>
            `)}
        </div>
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        height: 100%;
        box-sizing: border-box;
      }
      .banner {
        display: flex;
        align-items: flex-end;
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        padding-top: 12px;
      }

      .has-plant-image .banner {
        padding-top: 30%;
      }

      .header {
        /* start paper-font-headline style */
        font-family: "Roboto", "Noto", sans-serif;
        -webkit-font-smoothing: antialiased; /* OS X subpixel AA bleed bug */
        text-rendering: optimizeLegibility;
        font-size: 24px;
        font-weight: 400;
        letter-spacing: -0.012em;
        /* end paper-font-headline style */

        line-height: 40px;
        padding: 8px 16px;
      }

      .has-plant-image .header {
        font-size: 16px;
        font-weight: 500;
        line-height: 16px;
        padding: 16px;
        color: white;
        width: 100%;
        background: rgba(0, 0, 0, var(--dark-secondary-opacity));
      }

      .content {
        display: flex;
        justify-content: space-between;
        padding: 16px 32px 24px 32px;
      }

      .has-plant-image .content {
        padding-bottom: 16px;
      }

      ha-svg-icon {
        color: var(--paper-item-icon-color);
        margin-bottom: 8px;
      }

      .attributes {
        cursor: pointer;
      }

      .attributes:focus {
        outline: none;
        background: var(--divider-color);
        border-radius: 100%;
      }

      .attributes div {
        text-align: center;
      }

      .problem {
        color: var(--error-color);
        font-weight: bold;
      }

      .uom {
        color: var(--secondary-text-color);
      }
    `;}},{kind:"method",key:"computeAttributes",value:function computeAttributes(stateObj){return Object.keys(SENSOR_ICONS).filter(key=>key in stateObj.attributes);}},{kind:"method",key:"computeIcon",value:function computeIcon(attr,batLvl){if(attr==="battery"){return batteryIcon(batLvl);}return SENSOR_ICONS[attr];}},{kind:"method",key:"_handleMoreInfo",value:function _handleMoreInfo(ev){const target=ev.currentTarget;const stateObj=this.hass.states[this._config.entity];if(target.value){fireEvent(this,"hass-more-info",{entityId:stateObj.attributes.sensors[target.value]});}}}]};},s);
