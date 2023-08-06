const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, z as o, r, n } from './main-dev.js';
import { e as computeDomain } from './auth-dev.js';
import { U as processConfigEntities } from './ha-more-info-dialog-dev.js';
import './hui-buttons-base-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiButtonsHeaderFooter=_decorate([n("hui-buttons-header-footer")],function(_initialize,_LitElement){class HuiButtonsHeaderFooter extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiButtonsHeaderFooter,d:[{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {entities:[]};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"type",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._configEntities=processConfigEntities(config.entities).map(entityConfig=>{const conf={tap_action:{action:"toggle"},hold_action:{action:"more-info"},...entityConfig};if(computeDomain(entityConfig.entity)==="scene"){conf.tap_action={action:"call-service",service:"scene.turn_on",target:{entity_id:conf.entity}};}return conf;});}},{kind:"method",key:"render",value:function render(){return $`
      ${this.type==="footer"?$`<li class="divider footer" role="separator"></li>`:""}
      <hui-buttons-base
        .hass=${this.hass}
        .configEntities=${this._configEntities}
        class=${o({footer:this.type==="footer",header:this.type==="header"})}
      ></hui-buttons-base>
      ${this.type==="header"?$`<li class="divider header" role="separator"></li>`:""}
    `;}},{kind:"field",static:true,key:"styles",value(){return r`
    .divider {
      height: 0;
      margin: 16px 0;
      list-style-type: none;
      border: none;
      border-bottom-width: 1px;
      border-bottom-style: solid;
      border-bottom-color: var(--divider-color);
    }
    .divider.header {
      margin-top: 0;
    }
    hui-buttons-base.footer {
      --padding-bottom: 16px;
    }
    hui-buttons-base.header {
      --padding-top: 16px;
    }
  `;}}]};},s);

export { HuiButtonsHeaderFooter };
