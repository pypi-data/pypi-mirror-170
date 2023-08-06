const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, Q as l, r, n } from './main-dev.js';
import { e as computeDomain, j as computeStateName } from './auth-dev.js';
import { W as findEntities, X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, o as computeStateDisplay, Q as actionHandler, R as hasAction, T as handleAction } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-picture-entity-card")],function(_initialize,_LitElement){class HuiPictureEntityCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureEntityCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-picture-entity-card-editor-dev.js');return document.createElement("hui-picture-entity-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,["light","switch"]);return {type:"picture-entity",entity:foundEntities[0]||"",image:"https://demo.home-assistant.io/stub_config/bedroom.png"};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.entity){throw new Error("Entity must be specified");}if(computeDomain(config.entity)!=="camera"&&!config.image&&!config.state_image&&!config.camera_image){throw new Error("No image source configured");}this._config={show_name:true,show_state:true,...config};}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiPictureEntityCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const name=this._config.name||computeStateName(stateObj);const entityState=computeStateDisplay(this.hass.localize,stateObj,this.hass.locale);let footer="";if(this._config.show_name&&this._config.show_state){footer=$`
        <div class="footer both">
          <div>${name}</div>
          <!-- <div>${entityState}</div> -->
        </div>
      `;}else if(this._config.show_name){footer=$`<div class="footer single">${name}</div>`;}else if(this._config.show_state){footer=$`<div class="footer single">${entityState}</div>`;}return $`
      <ha-card>
        <hui-image
          .hass=${this.hass}
          .image=${this._config.image}
          .stateImage=${this._config.state_image}
          .stateFilter=${this._config.state_filter}
          .cameraImage=${computeDomain(this._config.entity)==="camera"?this._config.entity:this._config.camera_image}
          .cameraView=${this._config.camera_view}
          .entity=${this._config.entity}
          .aspectRatio=${this._config.aspect_ratio}
          @action=${this._handleAction}
          .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
          tabindex=${l(hasAction(this._config.tap_action)||this._config.entity?"0":undefined)}
        ></hui-image>
        ${footer}
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        cursor: pointer;
        min-height: 75px;
        overflow: hidden;
        position: relative;
        height: 100%;
        box-sizing: border-box;
        border-radius: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      hui-image {
        width: 100%;
        cursor: pointer;
      }

      .footer {
        /* start paper-font-common-nowrap style */
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        /* end paper-font-common-nowrap style */

        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: var(
          --ha-picture-card-background-color,
          rgba(0, 0, 0, 0.3)
        );
        padding: 16px;
        font-size: 16px;
        line-height: 16px;
        color: var(--ha-picture-card-text-color, white);
        pointer-events: none;
      }

      .both {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }

      .single {
        text-align: center;
      }
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){handleAction(this,this.hass,this._config,ev.detail.action);}}]};},s);
