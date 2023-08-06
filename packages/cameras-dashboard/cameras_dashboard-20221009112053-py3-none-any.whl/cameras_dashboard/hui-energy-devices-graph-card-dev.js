const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, $, z as o, b as memoizeOne, f as fireEvent, r, n } from './main-dev.js';
import { aj as getRelativePosition } from './helpers.segment-dev.js';
import { ae as fetchStatistics, ag as calculateStatisticSumGrowth, ah as getColorByIndex } from './ha-more-info-dialog-dev.js';
import { j as computeStateName, f as formatNumber, x as numberFormatToLocale } from './auth-dev.js';
import { g as getEnergyDataCollection } from './energy-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import { d as differenceInDays, c as addHours } from './index-dev3.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './subscribe-one-dev.js';
import './config_entries-dev.js';

let HuiEnergyDevicesGraphCard=_decorate([n("hui-energy-devices-graph-card")],function(_initialize,_SubscribeMixin){class HuiEnergyDevicesGraphCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyDevicesGraphCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_data",value:void 0},{kind:"field",decorators:[t()],key:"_chartData",value(){return {datasets:[]};}},{kind:"field",decorators:[i("ha-chart-base")],key:"_chart",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>this._getStatistics(data))];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){var _this$_chartData,_this$_chartData$data;if(!this.hass||!this._config){return $``;}return $`
      <ha-card>
        ${this._config.title?$`<h1 class="card-header">${this._config.title}</h1>`:""}
        <div
          class="content ${o({"has-header":!!this._config.title})}"
        >
          <ha-chart-base
            .data=${this._chartData}
            .options=${this._createOptions(this.hass.locale)}
            .height=${(((_this$_chartData=this._chartData)===null||_this$_chartData===void 0?void 0:(_this$_chartData$data=_this$_chartData.datasets[0])===null||_this$_chartData$data===void 0?void 0:_this$_chartData$data.data.length)||0)*28+50}
            chart-type="bar"
          ></ha-chart-base>
        </div>
      </ha-card>
    `;}},{kind:"field",key:"_createOptions",value(){return memoizeOne(locale=>({parsing:false,animation:false,responsive:true,maintainAspectRatio:false,indexAxis:"y",scales:{y:{type:"category",ticks:{autoSkip:false,callback:index=>{const entityId=this._chartData.datasets[0].data[index].y;const entity=this.hass.states[entityId];return entity?computeStateName(entity):entityId;}}},x:{title:{display:true,text:"kWh"}}},elements:{bar:{borderWidth:1.5,borderRadius:4}},plugins:{tooltip:{mode:"nearest",callbacks:{title:item=>{const entity=this.hass.states[item[0].label];return entity?computeStateName(entity):item[0].label;},label:context=>`${context.dataset.label}: ${formatNumber(context.parsed.x,locale)} kWh`}}},// @ts-expect-error
locale:numberFormatToLocale(this.hass.locale),onClick:e=>{var _this$_chartData2,_this$_chartData2$dat,_this$_chartData2$dat2;const chart=e.chart;const canvasPosition=getRelativePosition(e,chart);const index=Math.abs(chart.scales.y.getValueForPixel(canvasPosition.y));fireEvent(this,"hass-more-info",{// @ts-ignore
entityId:(_this$_chartData2=this._chartData)===null||_this$_chartData2===void 0?void 0:(_this$_chartData2$dat=_this$_chartData2.datasets[0])===null||_this$_chartData2$dat===void 0?void 0:(_this$_chartData2$dat2=_this$_chartData2$dat.data[index])===null||_this$_chartData2$dat2===void 0?void 0:_this$_chartData2$dat2.y});}}));}},{kind:"method",key:"_getStatistics",value:async function _getStatistics(energyData){var _this$_chart;const dayDifference=differenceInDays(energyData.end||new Date(),energyData.start);this._data=await fetchStatistics(this.hass,addHours(energyData.start,-1),energyData.end,energyData.prefs.device_consumption.map(device=>device.stat_consumption),dayDifference>35?"month":dayDifference>2?"day":"hour");const startMinHour=addHours(energyData.start,-1);Object.values(this._data).forEach(stat=>{// if the start of the first value is after the requested period, we have the first data point, and should add a zero point
if(stat.length&&new Date(stat[0].start)>startMinHour){stat.unshift({...stat[0],start:startMinHour.toISOString(),end:startMinHour.toISOString(),sum:0,state:0});}});const data=[];const borderColor=[];const backgroundColor=[];const datasets=[{label:this.hass.localize("ui.panel.lovelace.cards.energy.energy_devices_graph.energy_usage"),borderColor,backgroundColor,data,barThickness:20}];energyData.prefs.device_consumption.forEach((device,idx)=>{const value=device.stat_consumption in this._data?calculateStatisticSumGrowth(this._data[device.stat_consumption])||0:0;data.push({// @ts-expect-error
y:device.stat_consumption,x:value,idx});});data.sort((a,b)=>b.x-a.x);data.forEach(d=>{const color=getColorByIndex(d.idx);borderColor.push(color);backgroundColor.push(color+"7F");});this._chartData={datasets};await this.updateComplete;(_this$_chart=this._chart)===null||_this$_chart===void 0?void 0:_this$_chart.updateChart("none");}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .card-header {
        padding-bottom: 0;
      }
      .content {
        padding: 16px;
      }
      .has-header {
        padding-top: 0;
      }
      ha-chart-base {
        --chart-max-height: none;
      }
    `;}}]};},SubscribeMixin(s));

export { HuiEnergyDevicesGraphCard };
