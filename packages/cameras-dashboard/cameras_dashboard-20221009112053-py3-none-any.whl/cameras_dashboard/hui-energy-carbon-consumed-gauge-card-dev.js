const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, ez as mdiInformation, I as i, r, n } from './main-dev.js';
import { aQ as round } from './auth-dev.js';
import './ha-gauge-dev.js';
import { g as getEnergyDataCollection, e as energySourcesByType } from './energy-dev.js';
import { Z as createEntityNotFoundWarning, ac as calculateStatisticsSumGrowth } from './ha-more-info-dialog-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import { severityMap } from './hui-gauge-card-dev.js';
import './stop_propagation-dev.js';
import './subscribe-one-dev.js';
import './config_entries-dev.js';
import './index-dev3.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-energy-carbon-consumed-gauge-card")],function(_initialize,_SubscribeMixin){class HuiEnergyCarbonGaugeCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyCarbonGaugeCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 4;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>{this._data=data;})];}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}if(!this._data){return $`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;}if(!this._data.co2SignalEntity){return $``;}const co2State=this.hass.states[this._data.co2SignalEntity];if(!co2State){return $`<hui-warning>
        ${createEntityNotFoundWarning(this.hass,this._data.co2SignalEntity)}
      </hui-warning>`;}const prefs=this._data.prefs;const types=energySourcesByType(prefs);const totalGridConsumption=calculateStatisticsSumGrowth(this._data.stats,types.grid[0].flow_from.map(flow=>flow.stat_energy_from));let value;if(totalGridConsumption===0){value=100;}if(this._data.fossilEnergyConsumption&&totalGridConsumption){const highCarbonEnergy=this._data.fossilEnergyConsumption?Object.values(this._data.fossilEnergyConsumption).reduce((sum,a)=>sum+a,0):0;const totalSolarProduction=types.solar?calculateStatisticsSumGrowth(this._data.stats,types.solar.map(source=>source.stat_energy_from))||0:0;const totalGridReturned=calculateStatisticsSumGrowth(this._data.stats,types.grid[0].flow_to.map(flow=>flow.stat_energy_to))||0;const totalEnergyConsumed=totalGridConsumption+Math.max(0,totalSolarProduction-totalGridReturned);value=round((1-highCarbonEnergy/totalEnergyConsumed)*100);}return $`
      <ha-card>
        ${value!==undefined?$`
              <ha-svg-icon id="info" .path=${mdiInformation}></ha-svg-icon>
              <paper-tooltip animation-delay="0" for="info" position="left">
                <span>
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.carbon_consumed_gauge.card_indicates_energy_used")}
                </span>
              </paper-tooltip>
              <ha-gauge
                min="0"
                max="100"
                .value=${value}
                .locale=${this.hass.locale}
                label="%"
                style=${i({"--gauge-color":this._computeSeverity(value)})}
              ></ha-gauge>
              <div class="name">
                ${this.hass.localize("ui.panel.lovelace.cards.energy.carbon_consumed_gauge.non_fossil_energy_consumed")}
              </div>
            `:$`${this.hass.localize("ui.panel.lovelace.cards.energy.carbon_consumed_gauge.non_fossil_energy_not_calculated")}`}
      </ha-card>
    `;}},{kind:"method",key:"_computeSeverity",value:function _computeSeverity(numberValue){if(numberValue<10){return severityMap.red;}if(numberValue<30){return severityMap.yellow;}if(numberValue>75){return severityMap.green;}return severityMap.normal;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        height: 100%;
        overflow: hidden;
        padding: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        box-sizing: border-box;
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
        margin-top: 8px;
      }

      ha-svg-icon {
        position: absolute;
        right: 4px;
        top: 4px;
        color: var(--secondary-text-color);
      }
      paper-tooltip > span {
        font-size: 12px;
        line-height: 12px;
      }
      paper-tooltip {
        width: 80%;
        max-width: 250px;
        top: 8px !important;
      }
    `;}}]};},SubscribeMixin(s));
