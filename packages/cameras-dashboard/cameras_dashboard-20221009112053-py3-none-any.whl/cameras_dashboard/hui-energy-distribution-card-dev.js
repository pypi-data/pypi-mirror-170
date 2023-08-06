const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, eA as mdiLeaf, eB as mdiSolarPower, ak as mdiFire, af as y, eC as mdiTransmissionTower, eq as mdiArrowLeft, es as mdiArrowRight, z as o, bM as mdiHome, eD as mdiBatteryHigh, ca as mdiArrowDown, c8 as mdiArrowUp, r, n } from './main-dev.js';
import { f as formatNumber } from './auth-dev.js';
import { g as getEnergyDataCollection, e as energySourcesByType, b as getEnergyGasUnit } from './energy-dev.js';
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

const CIRCLE_CIRCUMFERENCE=238.76104;_decorate([n("hui-energy-distribution-card")],function(_initialize,_SubscribeMixin){class HuiEnergyDistrubutionCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyDistrubutionCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>{this._data=data;})];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"render",value:function render(){var _calculateStatisticsS,_homeHighCarbonCircum;if(!this._config){return $``;}if(!this._data){return $`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;}const prefs=this._data.prefs;const types=energySourcesByType(prefs);// The strategy only includes this card if we have a grid.
const hasSolarProduction=types.solar!==undefined;const hasBattery=types.battery!==undefined;const hasGas=types.gas!==undefined;const hasReturnToGrid=types.grid[0].flow_to.length>0;const totalFromGrid=(_calculateStatisticsS=calculateStatisticsSumGrowth(this._data.stats,types.grid[0].flow_from.map(flow=>flow.stat_energy_from)))!==null&&_calculateStatisticsS!==void 0?_calculateStatisticsS:0;let gasUsage=null;if(hasGas){var _calculateStatisticsS2;gasUsage=(_calculateStatisticsS2=calculateStatisticsSumGrowth(this._data.stats,types.gas.map(source=>source.stat_energy_from)))!==null&&_calculateStatisticsS2!==void 0?_calculateStatisticsS2:0;}let totalSolarProduction=null;if(hasSolarProduction){totalSolarProduction=calculateStatisticsSumGrowth(this._data.stats,types.solar.map(source=>source.stat_energy_from))||0;}let totalBatteryIn=null;let totalBatteryOut=null;if(hasBattery){totalBatteryIn=calculateStatisticsSumGrowth(this._data.stats,types.battery.map(source=>source.stat_energy_to))||0;totalBatteryOut=calculateStatisticsSumGrowth(this._data.stats,types.battery.map(source=>source.stat_energy_from))||0;}let returnedToGrid=null;if(hasReturnToGrid){returnedToGrid=calculateStatisticsSumGrowth(this._data.stats,types.grid[0].flow_to.map(flow=>flow.stat_energy_to))||0;}let solarConsumption=null;if(hasSolarProduction){solarConsumption=(totalSolarProduction||0)-(returnedToGrid||0)-(totalBatteryIn||0);}let batteryFromGrid=null;let batteryToGrid=null;if(solarConsumption!==null&&solarConsumption<0){// What we returned to the grid and what went in to the battery is more than produced,
// so we have used grid energy to fill the battery
// or returned battery energy to the grid
if(hasBattery){batteryFromGrid=solarConsumption*-1;if(batteryFromGrid>totalFromGrid){batteryToGrid=Math.min(0,batteryFromGrid-totalFromGrid);batteryFromGrid=totalFromGrid;}}solarConsumption=0;}let solarToBattery=null;if(hasSolarProduction&&hasBattery){if(!batteryToGrid){batteryToGrid=Math.max(0,(returnedToGrid||0)-(totalSolarProduction||0)-(totalBatteryIn||0)-(batteryFromGrid||0));}solarToBattery=totalBatteryIn-(batteryFromGrid||0);}else if(!hasSolarProduction&&hasBattery){batteryToGrid=returnedToGrid;}let batteryConsumption=null;if(hasBattery){batteryConsumption=(totalBatteryOut||0)-(batteryToGrid||0);}const gridConsumption=Math.max(0,totalFromGrid-(batteryFromGrid||0));const totalHomeConsumption=Math.max(0,gridConsumption+(solarConsumption||0)+(batteryConsumption||0));let homeSolarCircumference;if(hasSolarProduction){homeSolarCircumference=CIRCLE_CIRCUMFERENCE*(solarConsumption/totalHomeConsumption);}let homeBatteryCircumference;if(batteryConsumption){homeBatteryCircumference=CIRCLE_CIRCUMFERENCE*(batteryConsumption/totalHomeConsumption);}let lowCarbonEnergy;let homeLowCarbonCircumference;let homeHighCarbonCircumference;// This fallback is used in the demo
let electricityMapUrl="https://app.electricitymap.org";if(this._data.co2SignalEntity&&this._data.fossilEnergyConsumption){// Calculate high carbon consumption
const highCarbonEnergy=Object.values(this._data.fossilEnergyConsumption).reduce((sum,a)=>sum+a,0);const co2State=this.hass.states[this._data.co2SignalEntity];if(co2State!==null&&co2State!==void 0&&co2State.attributes.country_code){electricityMapUrl+=`/zone/${co2State.attributes.country_code}`;}if(highCarbonEnergy!==null){lowCarbonEnergy=totalFromGrid-highCarbonEnergy;let highCarbonConsumption;if(gridConsumption!==totalFromGrid){// Only get the part that was used for consumption and not the battery
highCarbonConsumption=highCarbonEnergy*(gridConsumption/totalFromGrid);}else {highCarbonConsumption=highCarbonEnergy;}homeHighCarbonCircumference=CIRCLE_CIRCUMFERENCE*(highCarbonConsumption/totalHomeConsumption);homeLowCarbonCircumference=CIRCLE_CIRCUMFERENCE-(homeSolarCircumference||0)-(homeBatteryCircumference||0)-homeHighCarbonCircumference;}}const totalLines=gridConsumption+(solarConsumption||0)+(returnedToGrid?returnedToGrid-(batteryToGrid||0):0)+(solarToBattery||0)+(batteryConsumption||0)+(batteryFromGrid||0)+(batteryToGrid||0);return $`
      <ha-card .header=${this._config.title}>
        <div class="card-content">
          ${lowCarbonEnergy!==undefined||hasSolarProduction||hasGas?$`<div class="row">
                ${lowCarbonEnergy===undefined?$`<div class="spacer"></div>`:$`<div class="circle-container low-carbon">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.non_fossil")}</span
                      >
                      <a
                        class="circle"
                        href=${electricityMapUrl}
                        target="_blank"
                        rel="noopener no referrer"
                      >
                        <ha-svg-icon .path=${mdiLeaf}></ha-svg-icon>
                        ${lowCarbonEnergy?formatNumber(lowCarbonEnergy,this.hass.locale,{maximumFractionDigits:1}):"—"}
                        kWh
                      </a>
                      <svg width="80" height="30">
                        <line x1="40" y1="0" x2="40" y2="30"></line>
                      </svg>
                    </div>`}
                ${hasSolarProduction?$`<div class="circle-container solar">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.solar")}</span
                      >
                      <div class="circle">
                        <ha-svg-icon .path=${mdiSolarPower}></ha-svg-icon>
                        ${formatNumber(totalSolarProduction||0,this.hass.locale,{maximumFractionDigits:1})}
                        kWh
                      </div>
                    </div>`:hasGas?$`<div class="spacer"></div>`:""}
                ${hasGas?$`<div class="circle-container gas">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.gas")}</span
                      >
                      <div class="circle">
                        <ha-svg-icon .path=${mdiFire}></ha-svg-icon>
                        ${formatNumber(gasUsage||0,this.hass.locale,{maximumFractionDigits:1})}
                        ${getEnergyGasUnit(this.hass,prefs)||"m³"}
                      </div>
                      <svg width="80" height="30">
                        <path d="M40 0 v30" id="gas" />
                        ${gasUsage?y`<circle
                    r="1"
                    class="gas"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="2s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#gas" />
                    </animateMotion>
                  </circle>`:""}
                      </svg>
                    </div>`:$`<div class="spacer"></div>`}
              </div>`:""}
          <div class="row">
            <div class="circle-container grid">
              <div class="circle">
                <ha-svg-icon .path=${mdiTransmissionTower}></ha-svg-icon>
                ${returnedToGrid!==null?$`<span class="return">
                      <ha-svg-icon
                        class="small"
                        .path=${mdiArrowLeft}
                      ></ha-svg-icon
                      >${formatNumber(returnedToGrid,this.hass.locale,{maximumFractionDigits:1})}
                      kWh
                    </span>`:""}
                <span class="consumption">
                  ${hasReturnToGrid?$`<ha-svg-icon
                        class="small"
                        .path=${mdiArrowRight}
                      ></ha-svg-icon>`:""}${formatNumber(totalFromGrid,this.hass.locale,{maximumFractionDigits:1})}
                  kWh
                </span>
              </div>
              <span class="label"
                >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.grid")}</span
              >
            </div>
            <div class="circle-container home">
              <div
                class="circle ${o({border:homeSolarCircumference===undefined&&homeLowCarbonCircumference===undefined})}"
              >
                <ha-svg-icon .path=${mdiHome}></ha-svg-icon>
                ${formatNumber(totalHomeConsumption,this.hass.locale,{maximumFractionDigits:1})}
                kWh
                ${homeSolarCircumference!==undefined||homeLowCarbonCircumference!==undefined?$`<svg>
                      ${homeSolarCircumference!==undefined?y`<circle
                            class="solar"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${homeSolarCircumference} ${CIRCLE_CIRCUMFERENCE-homeSolarCircumference}"
                            shape-rendering="geometricPrecision"
                            stroke-dashoffset="-${CIRCLE_CIRCUMFERENCE-homeSolarCircumference}"
                          />`:""}
                      ${homeBatteryCircumference?y`<circle
                            class="battery"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${homeBatteryCircumference} ${CIRCLE_CIRCUMFERENCE-homeBatteryCircumference}"
                            stroke-dashoffset="-${CIRCLE_CIRCUMFERENCE-homeBatteryCircumference-(homeSolarCircumference||0)}"
                            shape-rendering="geometricPrecision"
                          />`:""}
                      ${homeLowCarbonCircumference?y`<circle
                            class="low-carbon"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${homeLowCarbonCircumference} ${CIRCLE_CIRCUMFERENCE-homeLowCarbonCircumference}"
                            stroke-dashoffset="-${CIRCLE_CIRCUMFERENCE-homeLowCarbonCircumference-(homeBatteryCircumference||0)-(homeSolarCircumference||0)}"
                            shape-rendering="geometricPrecision"
                          />`:""}
                      <circle
                        class="grid"
                        cx="40"
                        cy="40"
                        r="38"
                        stroke-dasharray="${(_homeHighCarbonCircum=homeHighCarbonCircumference)!==null&&_homeHighCarbonCircum!==void 0?_homeHighCarbonCircum:CIRCLE_CIRCUMFERENCE-homeSolarCircumference-(homeBatteryCircumference||0)} ${homeHighCarbonCircumference!==undefined?CIRCLE_CIRCUMFERENCE-homeHighCarbonCircumference:homeSolarCircumference+(homeBatteryCircumference||0)}"
                        stroke-dashoffset="0"
                        shape-rendering="geometricPrecision"
                      />
                    </svg>`:""}
              </div>
              <span class="label"
                >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.home")}</span
              >
            </div>
          </div>
          ${hasBattery?$`<div class="row">
                <div class="spacer"></div>
                <div class="circle-container battery">
                  <div class="circle">
                    <ha-svg-icon .path=${mdiBatteryHigh}></ha-svg-icon>
                    <span class="battery-in">
                      <ha-svg-icon
                        class="small"
                        .path=${mdiArrowDown}
                      ></ha-svg-icon
                      >${formatNumber(totalBatteryIn||0,this.hass.locale,{maximumFractionDigits:1})}
                      kWh</span
                    >
                    <span class="battery-out">
                      <ha-svg-icon
                        class="small"
                        .path=${mdiArrowUp}
                      ></ha-svg-icon>
                      ${formatNumber(totalBatteryOut||0,this.hass.locale,{maximumFractionDigits:1})}
                      kWh</span
                    >
                  </div>
                  <span class="label"
                    >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.battery")}</span
                  >
                </div>
                <div class="spacer"></div>
              </div>`:""}
          <div class="lines ${o({battery:hasBattery})}">
            <svg
              viewBox="0 0 100 100"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
            >
              ${hasReturnToGrid&&hasSolarProduction?y`<path
                    id="return"
                    class="return"
                    d="M${hasBattery?45:47},0 v15 c0,${hasBattery?"35 -10,30 -30,30":"40 -10,35 -30,35"} h-20"
                    vector-effect="non-scaling-stroke"
                  ></path> `:""}
              ${hasSolarProduction?y`<path
                    id="solar"
                    class="solar"
                    d="M${hasBattery?55:53},0 v15 c0,${hasBattery?"35 10,30 30,30":"40 10,35 30,35"} h20"
                    vector-effect="non-scaling-stroke"
                  ></path>`:""}
              ${hasBattery?y`<path
                    id="battery-house"
                    class="battery-house"
                    d="M55,100 v-15 c0,-35 10,-30 30,-30 h20"
                    vector-effect="non-scaling-stroke"
                  ></path>
                  <path
                    id="battery-grid"
                    class=${o({"battery-from-grid":Boolean(batteryFromGrid),"battery-to-grid":Boolean(batteryToGrid)})}
                    d="M45,100 v-15 c0,-35 -10,-30 -30,-30 h-20"
                    vector-effect="non-scaling-stroke"
                  ></path>
                  `:""}
              ${hasBattery&&hasSolarProduction?y`<path
                    id="battery-solar"
                    class="battery-solar"
                    d="M50,0 V100"
                    vector-effect="non-scaling-stroke"
                  ></path>`:""}
              <path
                class="grid"
                id="grid"
                d="M0,${hasBattery?50:hasSolarProduction?56:53} H100"
                vector-effect="non-scaling-stroke"
              ></path>
              ${returnedToGrid&&hasSolarProduction?y`<circle
                    r="1"
                    class="return"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-(returnedToGrid-(batteryToGrid||0))/totalLines*6}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#return" />
                    </animateMotion>
                  </circle>`:""}
              ${solarConsumption?y`<circle
                    r="1"
                    class="solar"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-solarConsumption/totalLines*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#solar" />
                    </animateMotion>
                  </circle>`:""}
              ${gridConsumption?y`<circle
                    r="1"
                    class="grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-gridConsumption/totalLines*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#grid" />
                    </animateMotion>
                  </circle>`:""}
              ${solarToBattery?y`<circle
                    r="1"
                    class="battery-solar"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-solarToBattery/totalLines*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-solar" />
                    </animateMotion>
                  </circle>`:""}
              ${batteryConsumption?y`<circle
                    r="1"
                    class="battery-house"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-batteryConsumption/totalLines*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-house" />
                    </animateMotion>
                  </circle>`:""}
              ${batteryFromGrid?y`<circle
                    r="1"
                    class="battery-from-grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-batteryFromGrid/totalLines*5}s"
                      repeatCount="indefinite"
                      keyPoints="1;0" keyTimes="0;1"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-grid" />
                    </animateMotion>
                  </circle>`:""}
              ${batteryToGrid?y`<circle
                    r="1"
                    class="battery-to-grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-batteryToGrid/totalLines*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-grid" />
                    </animateMotion>
                  </circle>`:""}
            </svg>
          </div>
        </div>
        ${this._config.link_dashboard?$`
              <div class="card-actions">
                <a href="/energy"
                  ><mwc-button>
                    ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.go_to_energy_dashboard")}
                  </mwc-button></a
                >
              </div>
            `:""}
      </ha-card>
    `;}},{kind:"field",static:true,key:"styles",value(){return r`
    :host {
      --mdc-icon-size: 24px;
    }
    .card-content {
      position: relative;
    }
    .lines {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 146px;
      display: flex;
      justify-content: center;
      padding: 0 16px 16px;
      box-sizing: border-box;
    }
    .lines.battery {
      bottom: 100px;
      height: 156px;
    }
    .lines svg {
      width: calc(100% - 160px);
      height: 100%;
      max-width: 340px;
    }
    .row {
      display: flex;
      justify-content: space-between;
      max-width: 500px;
      margin: 0 auto;
    }
    .circle-container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .circle-container.low-carbon {
      margin-right: 4px;
    }
    .circle-container.solar {
      margin: 0 4px;
      height: 130px;
    }
    .circle-container.gas {
      margin-left: 4px;
      height: 130px;
    }
    .circle-container.battery {
      height: 110px;
      justify-content: flex-end;
    }
    .spacer {
      width: 84px;
    }
    .circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      box-sizing: border-box;
      border: 2px solid;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 12px;
      line-height: 12px;
      position: relative;
      text-decoration: none;
      color: var(--primary-text-color);
    }
    ha-svg-icon {
      padding-bottom: 2px;
    }
    ha-svg-icon.small {
      --mdc-icon-size: 12px;
    }
    .label {
      color: var(--secondary-text-color);
      font-size: 12px;
    }
    line,
    path {
      stroke: var(--primary-text-color);
      stroke-width: 1;
      fill: none;
    }
    .circle svg {
      position: absolute;
      fill: none;
      stroke-width: 4px;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
    }
    .gas path,
    .gas circle {
      stroke: var(--energy-gas-color);
    }
    circle.gas {
      stroke-width: 4;
      fill: var(--energy-gas-color);
    }
    .gas .circle {
      border-color: var(--energy-gas-color);
    }
    .low-carbon line {
      stroke: var(--energy-non-fossil-color);
    }
    .low-carbon .circle {
      border-color: var(--energy-non-fossil-color);
    }
    .low-carbon ha-svg-icon {
      color: var(--energy-non-fossil-color);
    }
    circle.low-carbon {
      stroke: var(--energy-non-fossil-color);
      fill: var(--energy-non-fossil-color);
    }
    .solar .circle {
      border-color: var(--energy-solar-color);
    }
    circle.solar,
    path.solar {
      stroke: var(--energy-solar-color);
    }
    circle.solar {
      stroke-width: 4;
      fill: var(--energy-solar-color);
    }
    .battery .circle {
      border-color: var(--energy-battery-in-color);
    }
    circle.battery,
    path.battery {
      stroke: var(--energy-battery-out-color);
    }
    path.battery-house,
    circle.battery-house {
      stroke: var(--energy-battery-out-color);
    }
    circle.battery-house {
      stroke-width: 4;
      fill: var(--energy-battery-out-color);
    }
    path.battery-solar,
    circle.battery-solar {
      stroke: var(--energy-battery-in-color);
    }
    circle.battery-solar {
      stroke-width: 4;
      fill: var(--energy-battery-in-color);
    }
    .battery-in {
      color: var(--energy-battery-in-color);
    }
    .battery-out {
      color: var(--energy-battery-out-color);
    }
    path.battery-from-grid {
      stroke: var(--energy-grid-consumption-color);
    }
    path.battery-to-grid {
      stroke: var(--energy-grid-return-color);
    }
    path.return,
    circle.return,
    circle.battery-to-grid {
      stroke: var(--energy-grid-return-color);
    }
    circle.return,
    circle.battery-to-grid {
      stroke-width: 4;
      fill: var(--energy-grid-return-color);
    }
    .return {
      color: var(--energy-grid-return-color);
    }
    .grid .circle {
      border-color: var(--energy-grid-consumption-color);
    }
    .consumption {
      color: var(--energy-grid-consumption-color);
    }
    circle.grid,
    circle.battery-from-grid,
    path.grid {
      stroke: var(--energy-grid-consumption-color);
    }
    circle.grid,
    circle.battery-from-grid {
      stroke-width: 4;
      fill: var(--energy-grid-consumption-color);
    }
    .home .circle {
      border-width: 0;
      border-color: var(--primary-color);
    }
    .home .circle.border {
      border-width: 2px;
    }
    .circle svg circle {
      animation: rotate-in 0.6s ease-in;
      transition: stroke-dashoffset 0.4s, stroke-dasharray 0.4s;
      fill: none;
    }
    @keyframes rotate-in {
      from {
        stroke-dashoffset: 238.76104;
        stroke-dasharray: 238.76104;
      }
    }
    .card-actions a {
      text-decoration: none;
    }
  `;}}]};},SubscribeMixin(s));
