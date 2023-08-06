const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, z as o, r, n } from './main-dev.js';
import './statistics-chart-dev.js';
import { U as processConfigEntities, am as hasConfigOrEntitiesChanged, ae as fetchStatistics } from './ha-more-info-dialog-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiStatisticsGraphCard=_decorate([n("hui-statistics-graph-card")],function(_initialize,_LitElement){class HuiStatisticsGraphCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiStatisticsGraphCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-statistics-graph-card-editor-dev.js');return document.createElement("hui-statistics-graph-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {type:"statistics-graph",entities:[]};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_statistics",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",key:"_entities",value(){return [];}},{kind:"field",key:"_names",value(){return {};}},{kind:"field",key:"_fetching",value(){return false;}},{kind:"field",key:"_interval",value:void 0},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){_get(_getPrototypeOf(HuiStatisticsGraphCard.prototype),"disconnectedCallback",this).call(this);if(this._interval){clearInterval(this._interval);this._interval=undefined;}}},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiStatisticsGraphCard.prototype),"connectedCallback",this).call(this);if(!this.hasUpdated){return;}this._getStatistics();// statistics are created every hour
clearInterval(this._interval);this._interval=window.setInterval(()=>this._getStatistics(),1000*60*60);}},{kind:"method",key:"getCardSize",value:function getCardSize(){var _this$_config,_this$_entities;return (_this$_config=this._config)!==null&&_this$_config!==void 0&&_this$_config.title?2:0+2*(((_this$_entities=this._entities)===null||_this$_entities===void 0?void 0:_this$_entities.length)||1);}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entities||!Array.isArray(config.entities)){throw new Error("Entities need to be an array");}if(!config.entities.length){throw new Error("You must include at least one entity");}const configEntities=config.entities?processConfigEntities(config.entities,false):[];this._entities=[];configEntities.forEach(entity=>{this._entities.push(entity.entity);if(entity.name){this._names[entity.entity]=entity.name;}});if(typeof config.stat_types==="string"){this._config={...config,stat_types:[config.stat_types]};}else if(!config.stat_types){this._config={...config,stat_types:["sum","min","max","mean"]};}else {this._config=config;}}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("_statistics")){return true;}return hasConfigOrEntitiesChanged(this,changedProps);}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){_get(_getPrototypeOf(HuiStatisticsGraphCard.prototype),"willUpdate",this).call(this,changedProps);if(!this._config||!changedProps.has("_config")){return;}const oldConfig=changedProps.get("_config");if((oldConfig===null||oldConfig===void 0?void 0:oldConfig.entities)!==this._config.entities||(oldConfig===null||oldConfig===void 0?void 0:oldConfig.days_to_show)!==this._config.days_to_show||(oldConfig===null||oldConfig===void 0?void 0:oldConfig.period)!==this._config.period){this._getStatistics();// statistics are created every hour
clearInterval(this._interval);this._interval=window.setInterval(()=>this._getStatistics(),1000*60*60);}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-card .header=${this._config.title}>
        <div
          class="content ${o({"has-header":!!this._config.title})}"
        >
          <statistics-chart
            .hass=${this.hass}
            .isLoadingData=${!this._statistics}
            .statisticsData=${this._statistics}
            .chartType=${this._config.chart_type||"line"}
            .statTypes=${this._config.stat_types}
            .names=${this._names}
          ></statistics-chart>
        </div>
      </ha-card>
    `;}},{kind:"method",key:"_getStatistics",value:async function _getStatistics(){if(this._fetching){return;}const startDate=new Date();startDate.setTime(startDate.getTime()-1000*60*60*(24*(this._config.days_to_show||30)+1));this._fetching=true;try{this._statistics=await fetchStatistics(this.hass,startDate,undefined,this._entities,this._config.period);}finally{this._fetching=false;}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
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

export { HuiStatisticsGraphCard };
