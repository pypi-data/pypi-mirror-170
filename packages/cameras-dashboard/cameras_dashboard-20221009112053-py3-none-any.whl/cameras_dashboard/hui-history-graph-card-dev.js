const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, z as o, r, n } from './main-dev.js';
import { U as processConfigEntities, al as throttle, am as hasConfigOrEntitiesChanged, an as getRecentWithCache } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiHistoryGraphCard=_decorate([n("hui-history-graph-card")],function(_initialize,_LitElement){class HuiHistoryGraphCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiHistoryGraphCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-history-graph-card-editor-dev.js');return document.createElement("hui-history-graph-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){// Hard coded to sun.sun to prevent high server load when it would pick an entity with a lot of state changes
return {type:"history-graph",entities:["sun.sun"]};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_stateHistory",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",key:"_configEntities",value:void 0},{kind:"field",key:"_names",value(){return {};}},{kind:"field",key:"_cacheConfig",value:void 0},{kind:"field",key:"_fetching",value(){return false;}},{kind:"field",key:"_throttleGetStateHistory",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){var _this$_config,_this$_configEntities;return (_this$_config=this._config)!==null&&_this$_config!==void 0&&_this$_config.title?2:0+2*(((_this$_configEntities=this._configEntities)===null||_this$_configEntities===void 0?void 0:_this$_configEntities.length)||1);}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entities||!Array.isArray(config.entities)){throw new Error("Entities need to be an array");}if(!config.entities.length){throw new Error("You must include at least one entity");}this._configEntities=config.entities?processConfigEntities(config.entities):[];const _entities=[];this._configEntities.forEach(entity=>{_entities.push(entity.entity);if(entity.name){this._names[entity.entity]=entity.name;}});this._throttleGetStateHistory=throttle(()=>{this._getStateHistory();},config.refresh_interval||10*1000);this._cacheConfig={cacheKey:_entities.join(),hoursToShow:config.hours_to_show||24};this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("_stateHistory")){return true;}return hasConfigOrEntitiesChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiHistoryGraphCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass||!this._throttleGetStateHistory||!this._cacheConfig){return;}if(!changedProps.has("_config")&&!changedProps.has("hass")){return;}const oldConfig=changedProps.get("_config");if(changedProps.has("_config")&&((oldConfig===null||oldConfig===void 0?void 0:oldConfig.entities)!==this._config.entities||(oldConfig===null||oldConfig===void 0?void 0:oldConfig.hours_to_show)!==this._config.hours_to_show)){this._throttleGetStateHistory();}else if(changedProps.has("hass")){// wait for commit of data (we only account for the default setting of 1 sec)
setTimeout(this._throttleGetStateHistory,1000);}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-card .header=${this._config.title}>
        <div
          class="content ${o({"has-header":!!this._config.title})}"
        >
          <state-history-charts
            .hass=${this.hass}
            .isLoadingData=${!this._stateHistory}
            .historyData=${this._stateHistory}
            .names=${this._names}
            up-to-now
            no-single
          ></state-history-charts>
        </div>
      </ha-card>
    `;}},{kind:"method",key:"_getStateHistory",value:async function _getStateHistory(){if(this._fetching){return;}this._fetching=true;try{this._stateHistory={...(await getRecentWithCache(this.hass,this._cacheConfig.cacheKey,this._cacheConfig,this.hass.localize,this.hass.language))};}finally{this._fetching=false;}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        height: 100%;
      }
      .content {
        padding: 16px;
      }
      .has-header {
        padding-top: 0;
      }
    `;}}]};},s);

export { HuiHistoryGraphCard };
