const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, z as o, Q as l, r, n } from './main-dev.js';
import { L as DOMAINS_TOGGLE, e as computeDomain, j as computeStateName } from './auth-dev.js';
import { W as findEntities, U as processConfigEntities, X as hasConfigOrEntityChanged, Q as actionHandler, R as hasAction, Z as createEntityNotFoundWarning, o as computeStateDisplay, T as handleAction } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const STATES_OFF=new Set(["closed","locked","not_home","off"]);_decorate([n("hui-picture-glance-card")],function(_initialize,_LitElement){class HuiPictureGlanceCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureGlanceCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-picture-glance-card-editor-dev.js');return document.createElement("hui-picture-glance-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const maxEntities=2;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,["sensor","binary_sensor"]);return {type:"picture-glance",title:"Kitchen",image:"https://demo.home-assistant.io/stub_config/kitchen.png",entities:foundEntities};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",key:"_entitiesDialog",value:void 0},{kind:"field",key:"_entitiesToggle",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.entities||!Array.isArray(config.entities)||!(config.image||config.camera_image||config.state_image)||config.state_image&&!config.entity){throw new Error("Invalid configuration");}const entities=processConfigEntities(config.entities);this._entitiesDialog=[];this._entitiesToggle=[];entities.forEach(item=>{if(config.force_dialog||!DOMAINS_TOGGLE.has(computeDomain(item.entity))){this._entitiesDialog.push(item);}else {this._entitiesToggle.push(item);}});this._config={hold_action:{action:"more-info"},...config};}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(hasConfigOrEntityChanged(this,changedProps)){return true;}const oldHass=changedProps.get("hass");if(!oldHass||oldHass.themes!==this.hass.themes||oldHass.locale!==this.hass.locale){return true;}if(this._entitiesDialog){for(const entity of this._entitiesDialog){if(oldHass.states[entity.entity]!==this.hass.states[entity.entity]){return true;}}}if(this._entitiesToggle){for(const entity of this._entitiesToggle){if(oldHass.states[entity.entity]!==this.hass.states[entity.entity]){return true;}}}return false;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiPictureGlanceCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}return $`
      <ha-card>
        <hui-image
          class=${o({clickable:Boolean(this._config.tap_action||this._config.hold_action||this._config.camera_image)})}
          @action=${this._handleAction}
          .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
          tabindex=${l(hasAction(this._config.tap_action)?"0":undefined)}
          .config=${this._config}
          .hass=${this.hass}
          .image=${this._config.image}
          .stateImage=${this._config.state_image}
          .stateFilter=${this._config.state_filter}
          .cameraImage=${this._config.camera_image}
          .cameraView=${this._config.camera_view}
          .entity=${this._config.entity}
          .aspectRatio=${this._config.aspect_ratio}
        ></hui-image>
        <div class="box">
          ${this._config.title?$` <div class="title">${this._config.title}</div> `:""}
          <div class="row">
            ${this._entitiesDialog.map(entityConf=>this.renderEntity(entityConf,true))}
          </div>
          <div class="row">
            ${this._entitiesToggle.map(entityConf=>this.renderEntity(entityConf,false))}
          </div>
        </div>
      </ha-card>
    `;}},{kind:"method",key:"renderEntity",value:function renderEntity(entityConf,dialog){const stateObj=this.hass.states[entityConf.entity];entityConf={tap_action:{action:dialog?"more-info":"toggle"},hold_action:{action:"more-info"},...entityConf};if(!stateObj){return $`
        <hui-warning-element
          .label=${createEntityNotFoundWarning(this.hass,entityConf.entity)}
        ></hui-warning-element>
      `;}return $`
      <div class="wrapper">
        <ha-icon-button
          @action=${this._handleAction}
          .actionHandler=${actionHandler({hasHold:hasAction(entityConf.hold_action),hasDoubleClick:hasAction(entityConf.double_tap_action)})}
          tabindex=${l(!hasAction(entityConf.tap_action)?"-1":undefined)}
          .disabled=${!hasAction(entityConf.tap_action)}
          .config=${entityConf}
          class=${o({"state-on":!STATES_OFF.has(stateObj.state)})}
          title=${`${computeStateName(stateObj)} : ${computeStateDisplay(this.hass.localize,stateObj,this.hass.locale)}`}
        >
          <ha-state-icon
            .icon=${entityConf.icon}
            .state=${stateObj}
          ></ha-state-icon>
        </ha-icon-button>

        ${this._config.show_state!==true&&entityConf.show_state!==true?$`<div class="state"></div>`:$`
              <div class="state">
                ${entityConf.attribute?$`
                      ${entityConf.prefix}${stateObj.attributes[entityConf.attribute]}${entityConf.suffix}
                    `:computeStateDisplay(this.hass.localize,stateObj,this.hass.locale)}
              </div>
            `}
      </div>
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){const config=ev.currentTarget.config;handleAction(this,this.hass,config,ev.detail.action);}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        position: relative;
        min-height: 48px;
        overflow: hidden;
        height: 100%;
        box-sizing: border-box;
        border-radius: 1.5rem;
      }

      hui-image.clickable {
        cursor: pointer;
      }

      .box {
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
        padding: 4px 8px;
        font-size: 16px;
        line-height: 40px;
        color: var(--ha-picture-card-text-color, white);
        display: flex;
        justify-content: space-between;
        flex-direction: row;
      }

      .box .title {
        font-weight: 500;
        margin-left: 8px;
      }

      ha-icon-button {
        --mdc-icon-button-size: 40px;
        --disabled-text-color: currentColor;
        color: var(--ha-picture-icon-button-color, #a9a9a9);
      }

      ha-icon-button.state-on {
        color: var(--ha-picture-icon-button-on-color, white);
      }
      hui-warning-element {
        padding: 0 8px;
      }
      .state {
        display: block;
        font-size: 12px;
        text-align: center;
        line-height: 12px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .row {
        display: flex;
        flex-direction: row;
      }
      .wrapper {
        display: flex;
        flex-direction: column;
        width: 40px;
      }
    `;}}]};},s);
