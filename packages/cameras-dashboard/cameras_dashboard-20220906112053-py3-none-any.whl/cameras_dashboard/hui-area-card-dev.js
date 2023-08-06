const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { ew as mdiLightbulbMultiple, ex as mdiLightbulbMultipleOff, cR as mdiToggleSwitch, cS as mdiToggleSwitchOff, an as mdiWaterPercent, ey as mdiRun, _ as _decorate, c as s, d as e, t, b as memoizeOne, $, z as o, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, r, n } from './main-dev.js';
import { C as domainIcon, e as computeDomain, h as UNAVAILABLE_STATES, S as STATES_OFF, f as formatNumber, ac as subscribeEntityRegistry, k as forwardHaptic } from './auth-dev.js';
import { v as navigate } from './ha-more-info-dialog-dev.js';
import { s as subscribeOne } from './subscribe-one-dev.js';
import { a as subscribeAreaRegistry, s as subscribeDeviceRegistry } from './device_registry-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './compare-dev.js';

const SENSOR_DOMAINS=["sensor"];const ALERT_DOMAINS=["binary_sensor"];const TOGGLE_DOMAINS=["light","switch","fan"];const OTHER_DOMAINS=["camera"];const DEVICE_CLASSES={sensor:["temperature"],binary_sensor:["motion"]};const DOMAIN_ICONS={light:{on:mdiLightbulbMultiple,off:mdiLightbulbMultipleOff},switch:{on:mdiToggleSwitch,off:mdiToggleSwitchOff},fan:{on:domainIcon("fan"),off:domainIcon("fan")},sensor:{humidity:mdiWaterPercent},binary_sensor:{motion:mdiRun}};let HuiAreaCard=_decorate([n("hui-area-card")],function(_initialize,_SubscribeMixin){class HuiAreaCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiAreaCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-area-card-editor-dev.js');return document.createElement("hui-area-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:async function getStubConfig(hass){var _areas$;const areas=await subscribeOne(hass.connection,subscribeAreaRegistry);return {type:"area",area:((_areas$=areas[0])===null||_areas$===void 0?void 0:_areas$.area_id)||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_entities",value:void 0},{kind:"field",decorators:[t()],key:"_devices",value:void 0},{kind:"field",decorators:[t()],key:"_areas",value:void 0},{kind:"field",key:"_entitiesByDomain",value(){return memoizeOne((areaId,devicesInArea,registryEntities,states)=>{const entitiesInArea=registryEntities.filter(entry=>!entry.entity_category&&(entry.area_id?entry.area_id===areaId:entry.device_id&&devicesInArea.has(entry.device_id))).map(entry=>entry.entity_id);const entitiesByDomain={};for(const entity of entitiesInArea){const domain=computeDomain(entity);if(!TOGGLE_DOMAINS.includes(domain)&&!SENSOR_DOMAINS.includes(domain)&&!ALERT_DOMAINS.includes(domain)&&!OTHER_DOMAINS.includes(domain)){continue;}const stateObj=states[entity];if(!stateObj){continue;}if((SENSOR_DOMAINS.includes(domain)||ALERT_DOMAINS.includes(domain))&&!DEVICE_CLASSES[domain].includes(stateObj.attributes.device_class||"")){continue;}if(!(domain in entitiesByDomain)){entitiesByDomain[domain]=[];}entitiesByDomain[domain].push(stateObj);}return entitiesByDomain;});}},{kind:"method",key:"_isOn",value:function _isOn(domain,deviceClass){const entities=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states)[domain];if(!entities){return undefined;}return (deviceClass?entities.filter(entity=>entity.attributes.device_class===deviceClass):entities).some(entity=>!UNAVAILABLE_STATES.includes(entity.state)&&!STATES_OFF.includes(entity.state));}},{kind:"method",key:"_average",value:function _average(domain,deviceClass){const entities=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states)[domain].filter(entity=>deviceClass?entity.attributes.device_class===deviceClass:true);if(!entities){return undefined;}let uom;const values=entities.filter(entity=>{if(!entity.attributes.unit_of_measurement||isNaN(Number(entity.state))){return false;}if(!uom){uom=entity.attributes.unit_of_measurement;return true;}return entity.attributes.unit_of_measurement===uom;});if(!values.length){return undefined;}const sum=values.reduce((total,entity)=>total+Number(entity.state),0);return `${formatNumber(sum/values.length,this.hass.locale,{maximumFractionDigits:1})} ${uom}`;}},{kind:"field",key:"_area",value(){return memoizeOne((areaId,areas)=>areas.find(area=>area.area_id===areaId)||null);}},{kind:"field",key:"_devicesInArea",value(){return memoizeOne((areaId,devices)=>new Set(areaId?devices.filter(device=>device.area_id===areaId).map(device=>device.id):[]));}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){return [subscribeAreaRegistry(this.hass.connection,areas=>{this._areas=areas;}),subscribeDeviceRegistry(this.hass.connection,devices=>{this._devices=devices;}),subscribeEntityRegistry(this.hass.connection,entries=>{this._entities=entries;})];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.area){throw new Error("Area Required");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("_config")||!this._config){return true;}if(changedProps.has("_devicesInArea")||changedProps.has("_areas")||changedProps.has("_entities")){return true;}if(!changedProps.has("hass")){return false;}const oldHass=changedProps.get("hass");if(!oldHass||oldHass.themes!==this.hass.themes||oldHass.locale!==this.hass.locale){return true;}if(!this._devices||!this._devicesInArea(this._config.area,this._devices)||!this._entities){return false;}const entities=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states);for(const domainEntities of Object.values(entities)){for(const stateObj of domainEntities){if(oldHass.states[stateObj.entity_id]!==stateObj){return true;}}}return false;}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass||!this._areas||!this._devices||!this._entities){return $``;}const entitiesByDomain=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states);const area=this._area(this._config.area,this._areas);if(area===null){return $`
        <hui-warning>
          ${this.hass.localize("ui.card.area.area_not_found")}
        </hui-warning>
      `;}const sensors=[];SENSOR_DOMAINS.forEach(domain=>{if(!(domain in entitiesByDomain)){return;}DEVICE_CLASSES[domain].forEach(deviceClass=>{if(entitiesByDomain[domain].some(entity=>entity.attributes.device_class===deviceClass)){sensors.push($`
            ${DOMAIN_ICONS[domain][deviceClass]?$`<ha-svg-icon
                  .path=${DOMAIN_ICONS[domain][deviceClass]}
                ></ha-svg-icon>`:""}
            ${this._average(domain,deviceClass)}
          `);}});});let cameraEntityId;if(this._config.show_camera&&"camera"in entitiesByDomain){cameraEntityId=entitiesByDomain.camera[0].entity_id;}return $`
      <ha-card class=${area.picture||cameraEntityId?"image":""}>
        ${area.picture||cameraEntityId?$`<hui-image
              .config=${this._config}
              .hass=${this.hass}
              .image=${area.picture?area.picture:undefined}
              .cameraImage=${cameraEntityId}
              aspectRatio="16:9"
            ></hui-image>`:""}

        <div
          class="container ${o({navigate:this._config.navigation_path!==undefined})}"
          @click=${this._handleNavigation}
        >
          <div class="alerts">
            ${ALERT_DOMAINS.map(domain=>{if(!(domain in entitiesByDomain)){return "";}return DEVICE_CLASSES[domain].map(deviceClass=>this._isOn(domain,deviceClass)?$`
                      ${DOMAIN_ICONS[domain][deviceClass]?$`<ha-svg-icon
                            .path=${DOMAIN_ICONS[domain][deviceClass]}
                          ></ha-svg-icon>`:""}
                    `:"");})}
          </div>
          <div class="bottom">
            <div>
              <div class="name">${area.name}</div>
              ${sensors.length?$`<div class="sensors">${sensors}</div>`:""}
            </div>
            <div class="buttons">
              ${TOGGLE_DOMAINS.map(domain=>{if(!(domain in entitiesByDomain)){return "";}const on=this._isOn(domain);return TOGGLE_DOMAINS.includes(domain)?$`
                      <ha-icon-button
                        class=${on?"on":"off"}
                        .path=${DOMAIN_ICONS[domain][on?"on":"off"]}
                        .domain=${domain}
                        @click=${this._toggle}
                      >
                      </ha-icon-button>
                    `:"";})}
            </div>
          </div>
        </div>
      </ha-card>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiAreaCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(changedProps.has("hass")&&(!oldHass||oldHass.themes!==this.hass.themes)||changedProps.has("_config")&&(!oldConfig||oldConfig.theme!==this._config.theme)){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"_handleNavigation",value:function _handleNavigation(){if(this._config.navigation_path){navigate(this._config.navigation_path);}}},{kind:"method",key:"_toggle",value:function _toggle(ev){ev.stopPropagation();const domain=ev.currentTarget.domain;if(TOGGLE_DOMAINS.includes(domain)){this.hass.callService(domain,this._isOn(domain)?"turn_off":"turn_on",undefined,{area_id:this._config.area});}forwardHaptic("light");}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        overflow: hidden;
        position: relative;
        padding-bottom: 56.25%;
        background-size: cover;
      }

      ha-card.image {
        padding-bottom: 0;
      }

      .container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          0,
          rgba(33, 33, 33, 0.9) 0%,
          rgba(33, 33, 33, 0) 45%
        );
      }

      ha-card:not(.image) .container::before {
        position: absolute;
        content: "";
        width: 100%;
        height: 100%;
        background-color: var(--sidebar-selected-icon-color);
        opacity: 0.12;
      }

      .sensors {
        color: #e3e3e3;
        font-size: 16px;
        --mdc-icon-size: 24px;
        opacity: 0.6;
        margin-top: 8px;
      }

      .alerts {
        padding: 16px;
      }

      .alerts ha-svg-icon {
        background: var(--accent-color);
        color: var(--text-accent-color, var(--text-primary-color));
        padding: 8px;
        border-radius: 50%;
      }

      .name {
        color: white;
        font-size: 24px;
      }

      .bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px;
      }

      .navigate {
        cursor: pointer;
      }

      ha-icon-button {
        color: white;
        background-color: var(--area-button-color, #727272b2);
        border-radius: 50%;
        margin-left: 8px;
        --mdc-icon-button-size: 44px;
      }
      .on {
        color: var(--paper-item-icon-active-color, #fdd835);
      }
    `;}}]};},SubscribeMixin(s));

export { HuiAreaCard };
