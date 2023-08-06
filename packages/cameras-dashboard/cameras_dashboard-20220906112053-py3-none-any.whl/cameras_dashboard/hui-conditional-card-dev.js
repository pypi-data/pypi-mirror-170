const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, n } from './main-dev.js';
import { aa as computeCardSize, ab as createCardElement } from './ha-more-info-dialog-dev.js';
import { H as HuiConditionalBase } from './hui-conditional-base-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-conditional-card")],function(_initialize,_HuiConditionalBase){class HuiConditionalCard extends _HuiConditionalBase{constructor(...args){super(...args);_initialize(this);}}return {F:HuiConditionalCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-conditional-card-editor-dev.js');return document.createElement("hui-conditional-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {type:"conditional",conditions:[],// @ts-ignore
card:{}};}},{kind:"method",key:"setConfig",value:function setConfig(config){this.validateConfig(config);if(!config.card){throw new Error("No card configured");}this._element=this._createCardElement(config.card);}},{kind:"method",key:"getCardSize",value:function getCardSize(){return computeCardSize(this._element);}},{kind:"method",key:"_createCardElement",value:function _createCardElement(cardConfig){const element=createCardElement(cardConfig);if(this.hass){element.hass=this.hass;}element.addEventListener("ll-rebuild",ev=>{ev.stopPropagation();this._rebuildCard(cardConfig);},{once:true});return element;}},{kind:"method",key:"_rebuildCard",value:function _rebuildCard(config){this._element=this._createCardElement(config);if(this.lastChild){this.replaceChild(this._element,this.lastChild);}}}]};},HuiConditionalBase);
