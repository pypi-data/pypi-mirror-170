const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { ai as getStatisticIds, aj as getGraphColorByIndex, ak as statisticsHaveType } from './ha-more-info-dialog-dev.js';
import { z as isComponentLoaded, f as formatNumber, x as numberFormatToLocale, j as computeStateName } from './auth-dev.js';

_decorate([n("statistics-chart")],function(_initialize,_LitElement){class StatisticsChart extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:StatisticsChart,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"statisticsData",value:void 0},{kind:"field",decorators:[e({type:Array})],key:"statisticIds",value:void 0},{kind:"field",decorators:[e()],key:"names",value(){return false;}},{kind:"field",decorators:[e()],key:"unit",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"endTime",value:void 0},{kind:"field",decorators:[e({type:Array})],key:"statTypes",value(){return ["sum","min","mean","max"];}},{kind:"field",decorators:[e()],key:"chartType",value(){return "line";}},{kind:"field",decorators:[e({type:Boolean})],key:"isLoadingData",value(){return false;}},{kind:"field",decorators:[t()],key:"_chartData",value(){return {datasets:[]};}},{kind:"field",decorators:[t()],key:"_chartOptions",value:void 0},{kind:"field",key:"_computedStyle",value:void 0},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return changedProps.size>1||!changedProps.has("hass");}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){if(!this.hasUpdated){this._createOptions();}if(changedProps.has("statisticsData")||changedProps.has("statTypes")){this._generateData();}}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){this._computedStyle=getComputedStyle(this);}},{kind:"method",key:"render",value:function render(){if(!isComponentLoaded(this.hass,"history")){return $`<div class="info">
        ${this.hass.localize("ui.components.history_charts.history_disabled")}
      </div>`;}if(this.isLoadingData&&!this.statisticsData){return $`<div class="info">
        ${this.hass.localize("ui.components.statistics_charts.loading_statistics")}
      </div>`;}if(!this.statisticsData||!Object.keys(this.statisticsData).length){return $`<div class="info">
        ${this.hass.localize("ui.components.statistics_charts.no_statistics_found")}
      </div>`;}return $`
      <ha-chart-base
        .data=${this._chartData}
        .options=${this._chartOptions}
        .chartType=${this.chartType}
      ></ha-chart-base>
    `;}},{kind:"method",key:"_createOptions",value:function _createOptions(){this._chartOptions={parsing:false,animation:false,scales:{x:{type:"time",adapters:{date:{locale:this.hass.locale}},ticks:{maxRotation:0,sampleSize:5,autoSkipPadding:20,major:{enabled:true},font:context=>context.tick&&context.tick.major?{weight:"bold"}:{}},time:{tooltipFormat:"datetime"}},y:{beginAtZero:false,ticks:{maxTicksLimit:7},title:{display:this.unit,text:this.unit}}},plugins:{tooltip:{mode:"nearest",callbacks:{label:context=>`${context.dataset.label}: ${formatNumber(context.parsed.y,this.hass.locale)} ${// @ts-ignore
context.dataset.unit||""}`}},filler:{propagate:true},legend:{display:true,labels:{usePointStyle:true}}},hover:{mode:"nearest"},elements:{line:{tension:0.4,borderWidth:1.5},bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:5}},// @ts-expect-error
locale:numberFormatToLocale(this.hass.locale)};}},{kind:"method",key:"_getStatisticIds",value:async function _getStatisticIds(){this.statisticIds=await getStatisticIds(this.hass);}},{kind:"method",key:"_generateData",value:async function _generateData(){if(!this.statisticsData){return;}if(!this.statisticIds){await this._getStatisticIds();}let colorIndex=0;const statisticsData=Object.values(this.statisticsData);const totalDataSets=[];let endTime;if(statisticsData.length===0){return;}endTime=this.endTime||// Get the highest date from the last date of each statistic
new Date(Math.max(...statisticsData.map(stats=>new Date(stats[stats.length-1].start).getTime())));if(endTime>new Date()){endTime=new Date();}let unit;const names=this.names||{};statisticsData.forEach(stats=>{const firstStat=stats[0];let name=names[firstStat.statistic_id];if(!name){const entityState=this.hass.states[firstStat.statistic_id];if(entityState){name=computeStateName(entityState);}else {name=firstStat.statistic_id;}}const meta=this.statisticIds.find(stat=>stat.statistic_id===firstStat.statistic_id);if(!this.unit){if(unit===undefined){unit=meta===null||meta===void 0?void 0:meta.unit_of_measurement;}else if(unit!==(meta===null||meta===void 0?void 0:meta.unit_of_measurement)){unit=null;}}// array containing [value1, value2, etc]
let prevValues=null;// The datasets for the current statistic
const statDataSets=[];const pushData=(timestamp,dataValues)=>{if(!dataValues)return;if(timestamp>endTime){// Drop data points that are after the requested endTime. This could happen if
// endTime is "now" and client time is not in sync with server time.
return;}statDataSets.forEach((d,i)=>{if(dataValues[i]===null&&prevValues&&prevValues[i]!==null){// null data values show up as gaps in the chart.
// If the current value for the dataset is null and the previous
// value of the data set is not null, then add an 'end' point
// to the chart for the previous value. Otherwise the gap will
// be too big. It will go from the start of the previous data
// value until the start of the next data value.
d.data.push({x:timestamp.getTime(),y:prevValues[i]});}d.data.push({x:timestamp.getTime(),y:dataValues[i]});});prevValues=dataValues;};const color=getGraphColorByIndex(colorIndex,this._computedStyle);colorIndex++;const statTypes=[];const drawBands=this.statTypes.includes("mean")&&statisticsHaveType(stats,"mean");const sortedTypes=drawBands?[...this.statTypes].sort((a,b)=>{if(a==="min"||b==="max"){return -1;}if(a==="max"||b==="min"){return +1;}return 0;}):this.statTypes;sortedTypes.forEach(type=>{if(statisticsHaveType(stats,type)){const band=drawBands&&(type==="min"||type==="max");statTypes.push(type);statDataSets.push({label:`${name} (${this.hass.localize(`ui.components.statistics_charts.statistic_types.${type}`)})
            `,fill:drawBands?type==="min"?"+1":type==="max"?"-1":false:false,borderColor:band?color+"7F":color,backgroundColor:band?color+"3F":color+"7F",pointRadius:0,data:[],// @ts-ignore
unit:meta===null||meta===void 0?void 0:meta.unit_of_measurement,band});}});let prevDate=null;// Process chart data.
let initVal=null;let prevSum=null;stats.forEach(stat=>{const date=new Date(stat.start);if(prevDate===date){return;}prevDate=date;const dataValues=[];statTypes.forEach(type=>{let val;if(type==="sum"){if(!initVal){initVal=val=stat.state;prevSum=stat.sum;}else {val=initVal+((stat.sum||0)-prevSum);}}else {val=stat[type];}dataValues.push(val!==null?Math.round(val*100)/100:null);});pushData(date,dataValues);});// Add an entry for final values
pushData(endTime,prevValues);// Concat two arrays
Array.prototype.push.apply(totalDataSets,statDataSets);});if(unit!==null){this._chartOptions={...this._chartOptions,scales:{...this._chartOptions.scales,y:{...this._chartOptions.scales.y,title:{display:unit,text:unit}}}};}this._chartData={datasets:totalDataSets};}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
        min-height: 60px;
      }
      .info {
        text-align: center;
        line-height: 60px;
        color: var(--secondary-text-color);
      }
    `;}}]};},s);
