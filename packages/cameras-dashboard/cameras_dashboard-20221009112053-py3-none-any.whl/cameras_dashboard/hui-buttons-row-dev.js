const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, n } from './main-dev.js';
import { L as DOMAINS_TOGGLE, e as computeDomain } from './auth-dev.js';
import { U as processConfigEntities } from './ha-more-info-dialog-dev.js';
import './hui-buttons-base-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiButtonsRow=_decorate([n("hui-buttons-row")],function(_initialize,_LitElement){class HuiButtonsRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiButtonsRow,d:[{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {entities:[]};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){this._configEntities=processConfigEntities(config.entities).map(entityConfig=>({tap_action:{action:entityConfig.entity&&DOMAINS_TOGGLE.has(computeDomain(entityConfig.entity))?"toggle":"more-info"},hold_action:{action:"more-info"},...entityConfig}));}},{kind:"method",key:"render",value:function render(){return $`
      <hui-buttons-base
        .hass=${this.hass}
        .configEntities=${this._configEntities}
      ></hui-buttons-base>
    `;}}]};},s);

export { HuiButtonsRow };
