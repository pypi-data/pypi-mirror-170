const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, z as o, r, n } from './main-dev.js';
import { z as isComponentLoaded, F as fetchUsers, c as computeStateDomain } from './auth-dev.js';
import { W as findEntities, al as throttle, U as processConfigEntities, aq as getLogbookData } from './ha-more-info-dialog-dev.js';
import './ha-circular-progress-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './repeat-dev.js';

let HuiLogbookCard=_decorate([n("hui-logbook-card")],function(_initialize,_LitElement){class HuiLogbookCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiLogbookCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-logbook-card-editor-dev.js');return document.createElement("hui-logbook-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFill){const includeDomains=["light","switch"];const maxEntities=3;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFill,includeDomains);return {entities:foundEntities};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_logbookEntries",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"field",decorators:[t()],key:"_userIdToName",value(){return {};}},{kind:"field",key:"_lastLogbookDate",value:void 0},{kind:"field",key:"_fetchUserPromise",value:void 0},{kind:"field",key:"_error",value:void 0},{kind:"field",key:"_throttleGetLogbookEntries",value(){return throttle(()=>{this._getLogBookData();},10000);}},{kind:"method",key:"getCardSize",value:function getCardSize(){var _this$_config;return 9+((_this$_config=this._config)!==null&&_this$_config!==void 0&&_this$_config.title?1:0);}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entities.length){throw new Error("Entities must be specified");}this._configEntities=processConfigEntities(config.entities);this._config={hours_to_show:24,...config};}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("_config")||changedProps.has("_persons")||changedProps.has("_logbookEntries")){return true;}const oldHass=changedProps.get("hass");if(!this._configEntities||!oldHass||oldHass.themes!==this.hass.themes||oldHass.locale!==this.hass.locale){return true;}for(const entity of this._configEntities){if(oldHass.states[entity.entity]!==this.hass.states[entity.entity]){return true;}}return false;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){this._fetchUserPromise=this._fetchUserNames();}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(HuiLogbookCard.prototype),"updated",this).call(this,changedProperties);if(!this._config||!this.hass){return;}const configChanged=changedProperties.has("_config");const hassChanged=changedProperties.has("hass");const oldHass=changedProperties.get("hass");const oldConfig=changedProperties.get("_config");if(hassChanged&&(oldHass===null||oldHass===void 0?void 0:oldHass.themes)!==this.hass.themes||configChanged&&(oldConfig===null||oldConfig===void 0?void 0:oldConfig.theme)!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}if(configChanged&&((oldConfig===null||oldConfig===void 0?void 0:oldConfig.entities)!==this._config.entities||(oldConfig===null||oldConfig===void 0?void 0:oldConfig.hours_to_show)!==this._config.hours_to_show)){this._logbookEntries=undefined;this._lastLogbookDate=undefined;if(!this._configEntities){return;}this._throttleGetLogbookEntries();return;}if(oldHass&&this._configEntities.some(entity=>oldHass.states[entity.entity]!==this.hass.states[entity.entity])){// wait for commit of data (we only account for the default setting of 1 sec)
setTimeout(this._throttleGetLogbookEntries,1000);}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}if(!isComponentLoaded(this.hass,"logbook")){return $`
        <hui-warning>
          ${this.hass.localize("ui.components.logbook.component_not_loaded")}</hui-warning
        >
      `;}return $`
      <ha-card
        .header=${this._config.title}
        class=${o({"no-header":!this._config.title})}
      >
        <div class="content">
          ${this._error?$`
                <div class="no-entries">
                  ${`${this.hass.localize("ui.components.logbook.retrieval_error")}: ${this._error}`}
                </div>
              `:!this._logbookEntries?$`
                <ha-circular-progress
                  active
                  alt=${this.hass.localize("ui.common.loading")}
                ></ha-circular-progress>
              `:this._logbookEntries.length?$`
                <ha-logbook
                  narrow
                  relative-time
                  virtualize
                  .hass=${this.hass}
                  .entries=${this._logbookEntries}
                  .userIdToName=${this._userIdToName}
                ></ha-logbook>
              `:$`
                <div class="no-entries">
                  ${this.hass.localize("ui.components.logbook.entries_not_found")}
                </div>
              `}
        </div>
      </ha-card>
    `;}},{kind:"method",key:"_getLogBookData",value:async function _getLogBookData(){if(!this.hass||!this._config||!isComponentLoaded(this.hass,"logbook")){return;}const hoursToShowDate=new Date(new Date().getTime()-this._config.hours_to_show*60*60*1000);const lastDate=this._lastLogbookDate||hoursToShowDate;const now=new Date();let newEntries;try{[newEntries]=await Promise.all([getLogbookData(this.hass,lastDate.toISOString(),now.toISOString(),this._configEntities.map(entity=>entity.entity).toString(),true),this._fetchUserPromise]);}catch(err){this._error=err.message;return;}const logbookEntries=this._logbookEntries?[...newEntries,...this._logbookEntries]:newEntries;this._logbookEntries=logbookEntries.filter(logEntry=>new Date(logEntry.when)>hoursToShowDate);this._lastLogbookDate=now;}},{kind:"method",key:"_fetchUserNames",value:async function _fetchUserNames(){var _this$hass$user;const userIdToName={};// Start loading users
const userProm=((_this$hass$user=this.hass.user)===null||_this$hass$user===void 0?void 0:_this$hass$user.is_admin)&&fetchUsers(this.hass);// Process persons
Object.values(this.hass.states).forEach(entity=>{if(entity.attributes.user_id&&computeStateDomain(entity)==="person"){this._userIdToName[entity.attributes.user_id]=entity.attributes.friendly_name;}});// Process users
if(userProm){const users=await userProm;for(const user of users){if(!(user.id in userIdToName)){userIdToName[user.id]=user.name;}}}this._userIdToName=userIdToName;}},{kind:"get",static:true,key:"styles",value:function styles(){return [r`
        ha-card {
          height: 100%;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
        }

        .content {
          padding: 0 16px 16px;
        }

        .no-header .content {
          padding-top: 16px;
        }

        .no-entries {
          text-align: center;
          padding: 16px;
          color: var(--secondary-text-color);
        }

        ha-logbook {
          height: 385px;
          display: block;
        }

        ha-circular-progress {
          display: flex;
          justify-content: center;
        }
      `];}}]};},s);

export { HuiLogbookCard };
