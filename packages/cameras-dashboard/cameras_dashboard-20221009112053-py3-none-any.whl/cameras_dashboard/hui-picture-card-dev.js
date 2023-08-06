const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, Q as l, z as o, r, n } from './main-dev.js';
import { Q as actionHandler, R as hasAction, T as handleAction } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiPictureCard=_decorate([n("hui-picture-card")],function(_initialize,_LitElement){class HuiPictureCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-picture-card-editor-dev.js');return document.createElement("hui-picture-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {type:"picture",image:"/local/logoauto_og.png",tap_action:{action:"none"},hold_action:{action:"none"}};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 5;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.image){throw new Error("Image required");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.size===1&&changedProps.has("hass")){return !changedProps.get("hass");}return true;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiPictureCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}return $`
      <ha-card
        @action=${this._handleAction}
        .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
        tabindex=${l(hasAction(this._config.tap_action)?"0":undefined)}
        class=${o({clickable:Boolean(this._config.tap_action||this._config.hold_action||this._config.double_tap_action)})}
      >
        <img src=${this.hass.hassUrl(this._config.image)} />
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        overflow: hidden;
        height: 100%;
        border-radius: 1.5rem;
        display: flex;
        align-items: center;
      }

      ha-card.clickable {
        cursor: pointer;
      }

      img {
        display: block;
        width: 100%;
      }
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){handleAction(this,this.hass,this._config,ev.detail.action);}}]};},s);

export { HuiPictureCard };
