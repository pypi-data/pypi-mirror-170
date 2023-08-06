const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, ez as mdiInformation, r, n } from './main-dev.js';
import { f as formatNumber } from './auth-dev.js';
import './ha-gauge-dev.js';
import { g as getEnergyDataCollection } from './energy-dev.js';
import { ac as calculateStatisticsSumGrowth } from './ha-more-info-dialog-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import './stop_propagation-dev.js';
import './subscribe-one-dev.js';
import './config_entries-dev.js';
import './index-dev3.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const LEVELS=[{level:-1,stroke:"var(--energy-grid-consumption-color)"},{level:0,stroke:"var(--energy-grid-return-color)"}];_decorate([n("hui-energy-grid-neutrality-gauge-card")],function(_initialize,_SubscribeMixin){class HuiEnergyGridGaugeCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyGridGaugeCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>{this._data=data;})];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 4;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}if(!this._data){return $`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;}const prefs=this._data.prefs;const gridSource=prefs.energy_sources.find(src=>src.type==="grid");let value;if(!gridSource){return $``;}const consumedFromGrid=calculateStatisticsSumGrowth(this._data.stats,gridSource.flow_from.map(flow=>flow.stat_energy_from));const returnedToGrid=calculateStatisticsSumGrowth(this._data.stats,gridSource.flow_to.map(flow=>flow.stat_energy_to));if(consumedFromGrid!==null&&returnedToGrid!==null){if(returnedToGrid>consumedFromGrid){value=1-consumedFromGrid/returnedToGrid;}else if(returnedToGrid<consumedFromGrid){value=(1-returnedToGrid/consumedFromGrid)*-1;}else {value=0;}}return $`
      <ha-card>
        ${value!==undefined?$`
              <ha-svg-icon id="info" .path=${mdiInformation}></ha-svg-icon>
              <paper-tooltip animation-delay="0" for="info" position="left">
                <span>
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.energy_dependency")}
                  <br /><br />
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.color_explain")}
                </span>
              </paper-tooltip>

              <ha-gauge
                min="-1"
                max="1"
                .value=${value}
                .valueText=${formatNumber(Math.abs(returnedToGrid-consumedFromGrid),this.hass.locale,{maximumFractionDigits:2})}
                .locale=${this.hass.locale}
                .levels=${LEVELS}
                label="kWh"
                needle
              ></ha-gauge>
              <div class="name">
                ${returnedToGrid>=consumedFromGrid?this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.net_returned_grid"):this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.net_consumed_grid")}
              </div>
            `:this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.grid_neutrality_not_calculated")}
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
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
