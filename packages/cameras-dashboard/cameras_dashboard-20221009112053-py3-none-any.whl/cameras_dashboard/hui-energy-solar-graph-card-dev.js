const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, z as o, b as memoizeOne, eE as labBrighten, eF as rgb2lab, ev as hex2rgb, eG as labDarken, eH as rgb2hex, eI as lab2rgb, r, n } from './main-dev.js';
import { w as formatTime } from './ha-more-info-dialog-dev.js';
import { f as formatNumber, x as numberFormatToLocale, j as computeStateName } from './auth-dev.js';
import { s as startOfToday, a as endOfToday, g as getEnergyDataCollection, c as getEnergySolarForecasts } from './energy-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import { i as isToday } from './index-dev4.js';
import { d as differenceInDays, c as addHours } from './index-dev3.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './subscribe-one-dev.js';
import './config_entries-dev.js';

let HuiEnergySolarGraphCard=_decorate([n("hui-energy-solar-graph-card")],function(_initialize,_SubscribeMixin){class HuiEnergySolarGraphCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergySolarGraphCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_chartData",value(){return {datasets:[]};}},{kind:"field",decorators:[t()],key:"_start",value(){return startOfToday();}},{kind:"field",decorators:[t()],key:"_end",value(){return endOfToday();}},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>this._getStatistics(data))];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-card>
        ${this._config.title?$`<h1 class="card-header">${this._config.title}</h1>`:""}
        <div
          class="content ${o({"has-header":!!this._config.title})}"
        >
          <ha-chart-base
            .data=${this._chartData}
            .options=${this._createOptions(this._start,this._end,this.hass.locale)}
            chart-type="bar"
          ></ha-chart-base>
          ${!this._chartData.datasets.length?$`<div class="no-data">
                ${isToday(this._start)?this.hass.localize("ui.panel.lovelace.cards.energy.no_data"):this.hass.localize("ui.panel.lovelace.cards.energy.no_data_period")}
              </div>`:""}
        </div>
      </ha-card>
    `;}},{kind:"field",key:"_createOptions",value(){return memoizeOne((start,end,locale)=>{const dayDifference=differenceInDays(end,start);return {parsing:false,animation:false,scales:{x:{type:"time",suggestedMin:start.getTime(),suggestedMax:end.getTime(),adapters:{date:{locale:locale}},ticks:{maxRotation:0,sampleSize:5,autoSkipPadding:20,major:{enabled:true},font:context=>context.tick&&context.tick.major?{weight:"bold"}:{}},time:{tooltipFormat:dayDifference>35?"monthyear":dayDifference>7?"date":dayDifference>2?"weekday":dayDifference>0?"datetime":"hour",minUnit:dayDifference>35?"month":dayDifference>2?"day":"hour"},offset:true},y:{stacked:true,type:"linear",title:{display:true,text:"kWh"},ticks:{beginAtZero:true}}},plugins:{tooltip:{mode:"nearest",callbacks:{title:datasets=>{if(dayDifference>0){return datasets[0].label;}const date=new Date(datasets[0].parsed.x);return `${formatTime(date,locale)} – ${formatTime(addHours(date,1),locale)}`;},label:context=>`${context.dataset.label}: ${formatNumber(context.parsed.y,locale)} kWh`}},filler:{propagate:false},legend:{display:false,labels:{usePointStyle:true}}},hover:{mode:"nearest"},elements:{line:{tension:0.3,borderWidth:1.5},bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:5}},// @ts-expect-error
locale:numberFormatToLocale(locale)};});}},{kind:"method",key:"_getStatistics",value:async function _getStatistics(energyData){const solarSources=energyData.prefs.energy_sources.filter(source=>source.type==="solar");let forecasts;if(solarSources.some(source=>{var _source$config_entry_;return (_source$config_entry_=source.config_entry_solar_forecast)===null||_source$config_entry_===void 0?void 0:_source$config_entry_.length;})){try{forecasts=await getEnergySolarForecasts(this.hass);}catch(_e){// ignore
}}const datasets=[];const computedStyles=getComputedStyle(this);const solarColor=computedStyles.getPropertyValue("--energy-solar-color").trim();const dayDifference=differenceInDays(energyData.end||new Date(),energyData.start);solarSources.forEach((source,idx)=>{const data=[];const entity=this.hass.states[source.stat_energy_from];const modifiedColor=idx>0?this.hass.themes.darkMode?labBrighten(rgb2lab(hex2rgb(solarColor)),idx):labDarken(rgb2lab(hex2rgb(solarColor)),idx):undefined;const borderColor=modifiedColor?rgb2hex(lab2rgb(modifiedColor)):solarColor;let prevValue=null;let prevStart=null;const solarProductionData=[];// Process solar production data.
if(source.stat_energy_from in energyData.stats){const stats=energyData.stats[source.stat_energy_from];for(const point of stats){if(point.sum===null){continue;}if(prevValue===null){prevValue=point.sum;continue;}if(prevStart===point.start){continue;}const value=point.sum-prevValue;const date=new Date(point.start);solarProductionData.push({x:date.getTime(),y:value});prevStart=point.start;prevValue=point.sum;}}if(solarProductionData.length){data.push({label:this.hass.localize("ui.panel.lovelace.cards.energy.energy_solar_graph.production",{name:entity?computeStateName(entity):source.stat_energy_from}),borderColor,backgroundColor:borderColor+"7F",data:solarProductionData,stack:"solar"});}// Process solar forecast data.
if(forecasts&&source.config_entry_solar_forecast){const forecastsData={};source.config_entry_solar_forecast.forEach(configEntryId=>{if(!forecasts[configEntryId]){return;}Object.entries(forecasts[configEntryId].wh_hours).forEach(([date,value])=>{const dateObj=new Date(date);if(dateObj<energyData.start||energyData.end&&dateObj>energyData.end){return;}if(dayDifference>35){dateObj.setDate(1);}if(dayDifference>2){dateObj.setHours(0,0,0,0);}else {dateObj.setMinutes(0,0,0);}const time=dateObj.getTime();if(time in forecastsData){forecastsData[time]+=value;}else {forecastsData[time]=value;}});});if(forecastsData){const solarForecastData=[];for(const[time,value]of Object.entries(forecastsData)){solarForecastData.push({x:Number(time),y:value/1000});}if(solarForecastData.length){data.push({type:"line",label:this.hass.localize("ui.panel.lovelace.cards.energy.energy_solar_graph.forecast",{name:entity?computeStateName(entity):source.stat_energy_from}),fill:false,stepped:false,borderColor:computedStyles.getPropertyValue("--primary-text-color"),borderDash:[7,5],pointRadius:0,data:solarForecastData});}}}// Concat two arrays
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

export { HuiEnergySolarGraphCard };
