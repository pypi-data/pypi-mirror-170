const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, I as i, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, f as fireEvent, r, n } from './main-dev.js';
import { a as UNAVAILABLE, j as computeStateName } from './auth-dev.js';
import { W as findEntities, D as isValidEntityId, Z as createEntityNotFoundWarning, X as hasConfigOrEntityChanged } from './ha-more-info-dialog-dev.js';
import './ha-gauge-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const severityMap={red:"var(--error-color)",green:"var(--success-color)",yellow:"var(--warning-color)",normal:"var(--accent-color)"};_decorate([n("hui-gauge-card")],function(_initialize,_LitElement){class HuiGaugeCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGaugeCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-gauge-card-editor-dev.js');return document.createElement("hui-gauge-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const includeDomains=["counter","input_number","number","sensor"];const maxEntities=1;const entityFilter=stateObj=>!isNaN(Number(stateObj.state));const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains,entityFilter);return {type:"gauge",entity:foundEntities[0]||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 4;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entity){throw new Error("Entity must be specified");}if(!isValidEntityId(config.entity)){throw new Error("Invalid entity");}this._config={min:0,max:100,...config};}},{kind:"method",key:"render",value:function render(){var _this$_config$name,_this$hass;if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const entityState=Number(stateObj.state);if(stateObj.state===UNAVAILABLE){return $`
        <hui-warning
          >${this.hass.localize("ui.panel.lovelace.warning.entity_unavailable","entity",this._config.entity)}</hui-warning
        >
      `;}if(isNaN(entityState)){return $`
        <hui-warning
          >${this.hass.localize("ui.panel.lovelace.warning.entity_non_numeric","entity",this._config.entity)}</hui-warning
        >
      `;}const name=(_this$_config$name=this._config.name)!==null&&_this$_config$name!==void 0?_this$_config$name:computeStateName(stateObj);// Use `stateObj.state` as value to keep formatting (e.g trailing zeros)
// for consistent value display across gauge, entity, entity-row, etc.
return $`
      <ha-card @click=${this._handleClick} tabindex="0">
        <ha-gauge
          .min=${this._config.min}
          .max=${this._config.max}
          .value=${stateObj.state}
          .locale=${this.hass.locale}
          .label=${this._config.unit||((_this$hass=this.hass)===null||_this$hass===void 0?void 0:_this$hass.states[this._config.entity].attributes.unit_of_measurement)||""}
          style=${i({"--gauge-color":this._computeSeverity(entityState)})}
          .needle=${this._config.needle}
          .levels=${this._config.needle?this._severityLevels():undefined}
        ></ha-gauge>
        <div class="name" .title=${name}>${name}</div>
      </ha-card>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiGaugeCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"_computeSeverity",value:function _computeSeverity(numberValue){if(this._config.needle){return undefined;}const sections=this._config.severity;if(!sections){return severityMap.normal;}const sectionsArray=Object.keys(sections);const sortable=sectionsArray.map(severity=>[severity,sections[severity]]);for(const severity of sortable){if(severityMap[severity[0]]==null||isNaN(severity[1])){return severityMap.normal;}}sortable.sort((a,b)=>a[1]-b[1]);if(numberValue>=sortable[0][1]&&numberValue<sortable[1][1]){return severityMap[sortable[0][0]];}if(numberValue>=sortable[1][1]&&numberValue<sortable[2][1]){return severityMap[sortable[1][0]];}if(numberValue>=sortable[2][1]){return severityMap[sortable[2][0]];}return severityMap.normal;}},{kind:"method",key:"_severityLevels",value:function _severityLevels(){const sections=this._config.severity;if(!sections){return [{level:0,stroke:severityMap.normal}];}const sectionsArray=Object.keys(sections);return sectionsArray.map(severity=>({level:sections[severity],stroke:severityMap[severity]}));}},{kind:"method",key:"_handleClick",value:function _handleClick(){fireEvent(this,"hass-more-info",{entityId:this._config.entity});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        cursor: pointer;
        height: 100%;
        overflow: hidden;
        padding: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        box-sizing: border-box;
        border-radius: 1.5rem;
      }

      ha-card:focus {
        outline: none;
        background: var(--divider-color);
      }

      ha-gauge {
        width: 100%;
        max-width: 250px;
      }

      .name {
        text-align: center;
        line-height: initial;
        color: var(--primary-text-color);
        width: 100%;
        font-size: 15px;
        font-weight: 450;
        margin-top: 10%;
        white-space: nowrap;
        display: inline-block;
        overflow: hidden;
        max-width: 200px;
        float: left;
        text-overflow: ellipsis;
      }
    `;}}]};},s);

export { severityMap };
