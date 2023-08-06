const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, $, eJ as mdiImageFilterCenterFocus, j as _get, k as _getPrototypeOf, b as memoizeOne, r, n } from './main-dev.js';
import { e as computeDomain } from './auth-dev.js';
import { U as processConfigEntities, ap as parseAspectRatio, W as findEntities, ah as getColorByIndex, Y as fetchRecent } from './ha-more-info-dialog-dev.js';
import './ha-map-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const MINUTE=60000;_decorate([n("hui-map-card")],function(_initialize,_LitElement){class HuiMapCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiMapCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({type:Boolean,reflect:true})],key:"isPanel",value(){return false;}},{kind:"field",decorators:[t()],key:"_history",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[i("ha-map")],key:"_map",value:void 0},{kind:"field",key:"_date",value:void 0},{kind:"field",key:"_configEntities",value:void 0},{kind:"field",key:"_colorDict",value(){return {};}},{kind:"field",key:"_colorIndex",value(){return 0;}},{kind:"method",key:"setConfig",value:function setConfig(config){var _config$entities;if(!config){throw new Error("Error in card configuration.");}if(!((_config$entities=config.entities)!==null&&_config$entities!==void 0&&_config$entities.length)&&!config.geo_location_sources){throw new Error("Either entities or geo_location_sources must be specified");}if(config.entities&&!Array.isArray(config.entities)){throw new Error("Entities need to be an array");}if(config.geo_location_sources&&!Array.isArray(config.geo_location_sources)){throw new Error("Geo_location_sources needs to be an array");}this._config=config;this._configEntities=(config.entities?processConfigEntities(config.entities):[]).map(entity=>entity.entity);this._cleanupHistory();}},{kind:"method",key:"getCardSize",value:function getCardSize(){var _this$_config;if(!((_this$_config=this._config)!==null&&_this$_config!==void 0&&_this$_config.aspect_ratio)){return 7;}const ratio=parseAspectRatio(this._config.aspect_ratio);const ar=ratio&&ratio.w>0&&ratio.h>0?`${(100*ratio.h/ratio.w).toFixed(2)}`:"100";return 1+Math.floor(Number(ar)/25)||3;}},{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-map-card-editor-dev.js');return document.createElement("hui-map-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const includeDomains=["device_tracker"];const maxEntities=2;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains);return {type:"map",entities:foundEntities};}},{kind:"method",key:"render",value:function render(){var _this$_config$default;if(!this._config){return $``;}return $`
      <ha-card id="card" .header=${this._config.title}>
        <div id="root">
          <ha-map
            .hass=${this.hass}
            .entities=${this._getEntities(this.hass.states,this._config,this._configEntities)}
            .zoom=${(_this$_config$default=this._config.default_zoom)!==null&&_this$_config$default!==void 0?_this$_config$default:14}
            .paths=${this._getHistoryPaths(this._config,this._history)}
            .darkMode=${this._config.dark_mode}
          ></ha-map>
          <ha-icon-button
            .label=${this.hass.localize("ui.panel.lovelace.cards.map.reset_focus")}
            .path=${mdiImageFilterCenterFocus}
            @click=${this._fitMap}
            tabindex="0"
          ></ha-icon-button>
        </div>
      </ha-card>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(!changedProps.has("hass")||changedProps.size>1){return true;}const oldHass=changedProps.get("hass");if(!oldHass||!this._configEntities){return true;}if(oldHass.themes.darkMode!==this.hass.themes.darkMode){return true;}// Check if any state has changed
for(const entity of this._configEntities){if(oldHass.states[entity]!==this.hass.states[entity]){return true;}}return false;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(changedProps){_get(_getPrototypeOf(HuiMapCard.prototype),"firstUpdated",this).call(this,changedProps);const root=this.shadowRoot.getElementById("root");if(!this._config||this.isPanel||!root){return;}if(!this._config.aspect_ratio){root.style.paddingBottom="100%";return;}const ratio=parseAspectRatio(this._config.aspect_ratio);root.style.paddingBottom=ratio&&ratio.w>0&&ratio.h>0?`${(100*ratio.h/ratio.w).toFixed(2)}%`:root.style.paddingBottom="100%";}},{kind:"method",key:"updated",value:function updated(changedProps){var _this$_config2,_this$_configEntities;if((_this$_config2=this._config)!==null&&_this$_config2!==void 0&&_this$_config2.hours_to_show&&(_this$_configEntities=this._configEntities)!==null&&_this$_configEntities!==void 0&&_this$_configEntities.length){if(changedProps.has("_config")){this._getHistory();}else if(Date.now()-this._date.getTime()>=MINUTE){this._getHistory();}}}},{kind:"method",key:"_fitMap",value:function _fitMap(){var _this$_map;(_this$_map=this._map)===null||_this$_map===void 0?void 0:_this$_map.fitMap();}},{kind:"method",key:"_getColor",value:function _getColor(entityId){let color=this._colorDict[entityId];if(color){return color;}color=getColorByIndex(this._colorIndex);this._colorIndex++;this._colorDict[entityId]=color;return color;}},{kind:"field",key:"_getEntities",value(){return memoizeOne((states,config,configEntities)=>{if(!states||!config){return undefined;}let entities=configEntities||[];if(config.geo_location_sources){const geoEntities=[];// Calculate visible geo location sources
const includesAll=config.geo_location_sources.includes("all");for(const stateObj of Object.values(states)){if(computeDomain(stateObj.entity_id)==="geo_location"&&(includesAll||config.geo_location_sources.includes(stateObj.attributes.source))){geoEntities.push(stateObj.entity_id);}}entities=[...entities,...geoEntities];}return entities.map(entity=>({entity_id:entity,color:this._getColor(entity)}));});}},{kind:"field",key:"_getHistoryPaths",value(){return memoizeOne((config,history)=>{if(!config.hours_to_show||!history){return undefined;}const paths=[];for(const entityStates of history){if((entityStates===null||entityStates===void 0?void 0:entityStates.length)<=1){continue;}// filter location data from states and remove all invalid locations
const points=entityStates.reduce((accumulator,entityState)=>{const latitude=entityState.attributes.latitude;const longitude=entityState.attributes.longitude;if(latitude&&longitude){accumulator.push([latitude,longitude]);}return accumulator;},[]);paths.push({points,color:this._getColor(entityStates[0].entity_id),gradualOpacity:0.8});}return paths;});}},{kind:"method",key:"_getHistory",value:async function _getHistory(){this._date=new Date();if(!this._configEntities){return;}const entityIds=this._configEntities.join(",");const endTime=new Date();const startTime=new Date();startTime.setHours(endTime.getHours()-this._config.hours_to_show);const skipInitialState=false;const significantChangesOnly=false;const minimalResponse=false;const stateHistory=await fetchRecent(this.hass,entityIds,startTime,endTime,skipInitialState,significantChangesOnly,minimalResponse);if(stateHistory.length<1){return;}this._history=stateHistory;}},{kind:"method",key:"_cleanupHistory",value:function _cleanupHistory(){if(!this._history){return;}if(this._config.hours_to_show<=0){this._history=undefined;}else {// remove unused entities
this._history=this._history.reduce((accumulator,entityStates)=>{var _this$_configEntities2;const entityId=entityStates[0].entity_id;if((_this$_configEntities2=this._configEntities)!==null&&_this$_configEntities2!==void 0&&_this$_configEntities2.includes(entityId)){accumulator.push(entityStates);}return accumulator;},[]);}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        overflow: hidden;
        width: 100%;
        height: 100%;
      }

      ha-map {
        z-index: 0;
        border: none;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: inherit;
      }

      ha-icon-button {
        position: absolute;
        top: 75px;
        left: 3px;
        outline: none;
      }

      #root {
        position: relative;
      }

      :host([ispanel]) #root {
        height: 100%;
      }
    `;}}]};},s);
