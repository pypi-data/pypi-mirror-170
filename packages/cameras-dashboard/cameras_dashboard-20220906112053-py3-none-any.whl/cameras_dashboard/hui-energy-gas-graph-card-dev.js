const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, z as o, b as memoizeOne, eE as labBrighten, eF as rgb2lab, ev as hex2rgb, eG as labDarken, eH as rgb2hex, eI as lab2rgb, r, n } from './main-dev.js';
import { s as startOfToday, a as endOfToday, g as getEnergyDataCollection, b as getEnergyGasUnit } from './energy-dev.js';
import { f as formatNumber, x as numberFormatToLocale, j as computeStateName } from './auth-dev.js';
import { w as formatTime } from './ha-more-info-dialog-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import { i as isToday } from './index-dev4.js';
import { d as differenceInDays, c as addHours } from './index-dev3.js';
import './subscribe-one-dev.js';
import './config_entries-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiEnergyGasGraphCard=_decorate([n("hui-energy-gas-graph-card")],function(_initialize,_SubscribeMixin){class HuiEnergyGasGraphCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyGasGraphCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_chartData",value(){return {datasets:[]};}},{kind:"field",decorators:[t()],key:"_start",value(){return startOfToday();}},{kind:"field",decorators:[t()],key:"_end",value(){return endOfToday();}},{kind:"field",decorators:[t()],key:"_unit",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>this._getStatistics(data))];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-card>
        ${this._config.title?$`<h1 class="card-header">${this._config.title}</h1>`:""}
        <div
          class="content ${o({"has-header":!!this._config.title})}"
        >
          <ha-chart-base
            .data=${this._chartData}
            .options=${this._createOptions(this._start,this._end,this.hass.locale,this._unit)}
            chart-type="bar"
          ></ha-chart-base>
          ${!this._chartData.datasets.length?$`<div class="no-data">
                ${isToday(this._start)?this.hass.localize("ui.panel.lovelace.cards.energy.no_data"):this.hass.localize("ui.panel.lovelace.cards.energy.no_data_period")}
              </div>`:""}
        </div>
      </ha-card>
    `;}},{kind:"field",key:"_createOptions",value(){return memoizeOne((start,end,locale,unit)=>{const dayDifference=differenceInDays(end,start);return {parsing:false,animation:false,scales:{x:{type:"time",suggestedMin:start.getTime(),suggestedMax:end.getTime(),adapters:{date:{locale:locale}},ticks:{maxRotation:0,sampleSize:5,autoSkipPadding:20,major:{enabled:true},font:context=>context.tick&&context.tick.major?{weight:"bold"}:{}},time:{tooltipFormat:dayDifference>35?"monthyear":dayDifference>7?"date":dayDifference>2?"weekday":dayDifference>0?"datetime":"hour",minUnit:dayDifference>35?"month":dayDifference>2?"day":"hour"},offset:true},y:{stacked:true,type:"linear",title:{display:true,text:unit},ticks:{beginAtZero:true}}},plugins:{tooltip:{mode:"nearest",callbacks:{title:datasets=>{if(dayDifference>0){return datasets[0].label;}const date=new Date(datasets[0].parsed.x);return `${formatTime(date,locale)} – ${formatTime(addHours(date,1),locale)}`;},label:context=>`${context.dataset.label}: ${formatNumber(context.parsed.y,locale)} ${unit}`}},filler:{propagate:false},legend:{display:false,labels:{usePointStyle:true}}},hover:{mode:"nearest"},elements:{bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:5}},// @ts-expect-error
locale:numberFormatToLocale(locale)};});}},{kind:"method",key:"_getStatistics",value:async function _getStatistics(energyData){const gasSources=energyData.prefs.energy_sources.filter(source=>source.type==="gas");this._unit=getEnergyGasUnit(this.hass,energyData.prefs)||"m³";const datasets=[];const computedStyles=getComputedStyle(this);const gasColor=computedStyles.getPropertyValue("--energy-gas-color").trim();gasSources.forEach((source,idx)=>{const data=[];const entity=this.hass.states[source.stat_energy_from];const modifiedColor=idx>0?this.hass.themes.darkMode?labBrighten(rgb2lab(hex2rgb(gasColor)),idx):labDarken(rgb2lab(hex2rgb(gasColor)),idx):undefined;const borderColor=modifiedColor?rgb2hex(lab2rgb(modifiedColor)):gasColor;let prevValue=null;let prevStart=null;const gasConsumptionData=[];// Process gas consumption data.
if(source.stat_energy_from in energyData.stats){const stats=energyData.stats[source.stat_energy_from];for(const point of stats){if(point.sum===null){continue;}if(prevValue===null){prevValue=point.sum;continue;}if(prevStart===point.start){continue;}const value=point.sum-prevValue;const date=new Date(point.start);gasConsumptionData.push({x:date.getTime(),y:value});prevStart=point.start;prevValue=point.sum;}}if(gasConsumptionData.length){data.push({label:entity?computeStateName(entity):source.stat_energy_from,borderColor,backgroundColor:borderColor+"7F",data:gasConsumptionData,stack:"gas"});}// Concat two arrays
Array.prototype.push.apply(datasets,data);});this._start=energyData.start;this._end=energyData.end||endOfToday();this._chartData={datasets};}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        height: 100%;
      }
      .card-header {
        padding-bottom: 0;
      }
      .content {
        padding: 16px;
      }
      .has-header {
        padding-top: 0;
      }
      .no-data {
        position: absolute;
        height: 100%;
        top: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20%;
        margin-left: 32px;
        box-sizing: border-box;
      }
    `;}}]};},SubscribeMixin(s));

export { HuiEnergyGasGraphCard };
