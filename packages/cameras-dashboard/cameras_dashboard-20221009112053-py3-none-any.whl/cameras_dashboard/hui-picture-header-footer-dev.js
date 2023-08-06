const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, Q as l, z as o, r, n } from './main-dev.js';
import { Q as actionHandler, R as hasAction, T as handleAction } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiPictureHeaderFooter=_decorate([n("hui-picture-header-footer")],function(_initialize,_LitElement){class HuiPictureHeaderFooter extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureHeaderFooter,d:[{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {image:"https://www.home-assistant.io/images/lovelace/header-footer/balloons-header.png",tap_action:{action:"none"},hold_action:{action:"none"}};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"type",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.image){throw new Error("Image required");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.size===1&&changedProps.has("hass")){return !changedProps.get("hass");}return true;}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const clickable=Boolean(this._config.tap_action||this._config.hold_action);return $`
      <img
        @action=${this._handleAction}
        .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
        tabindex=${l(clickable?0:undefined)}
        class=${o({clickable})}
        src=${this.hass.hassUrl(this._config.image)}
      />
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      img.clickable {
        cursor: pointer;
      }

      img {
        display: block;
        width: 100%;
      }
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){handleAction(this,this.hass,this._config,ev.detail.action);}}]};},s);

export { HuiPictureHeaderFooter };
