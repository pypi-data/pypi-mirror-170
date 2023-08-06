const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, z as o, b as memoizeOne, eE as labBrighten, eF as rgb2lab, ev as hex2rgb, eG as labDarken, eH as rgb2hex, eI as lab2rgb, r, n } from './main-dev.js';
import { w as formatTime } from './ha-more-info-dialog-dev.js';
import { f as formatNumber, x as numberFormatToLocale, j as computeStateName } from './auth-dev.js';
import { s as startOfToday, a as endOfToday, g as getEnergyDataCollection } from './energy-dev.js';
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

let HuiEnergyUsageGraphCard=_decorate([n("hui-energy-usage-graph-card")],function(_initialize,_SubscribeMixin){class HuiEnergyUsageGraphCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyUsageGraphCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_chartData",value(){return {datasets:[]};}},{kind:"field",decorators:[t()],key:"_start",value(){return startOfToday();}},{kind:"field",decorators:[t()],key:"_end",value(){return endOfToday();}},{kind:"field",key:"hassSubscribeRequiredHostProps",value(){return ["_config"];}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){var _this$_config;return [getEnergyDataCollection(this.hass,{key:(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.collection_key}).subscribe(data=>this._getStatistics(data))];}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
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
          ${!this._chartData.datasets.some(dataset=>dataset.data.length)?$`<div class="no-data">
                ${isToday(this._start)?this.hass.localize("ui.panel.lovelace.cards.energy.no_data"):this.hass.localize("ui.panel.lovelace.cards.energy.no_data_period")}
              </div>`:""}
        </div>
      </ha-card>
    `;}},{kind:"field",key:"_createOptions",value(){return memoizeOne((start,end,locale)=>{const dayDifference=differenceInDays(end,start);return {parsing:false,animation:false,scales:{x:{type:"time",suggestedMin:start.getTime(),suggestedMax:end.getTime(),adapters:{date:{locale:locale}},ticks:{maxRotation:0,sampleSize:5,autoSkipPadding:20,major:{enabled:true},font:context=>context.tick&&context.tick.major?{weight:"bold"}:{}},time:{tooltipFormat:dayDifference>35?"monthyear":dayDifference>7?"date":dayDifference>2?"weekday":dayDifference>0?"datetime":"hour",minUnit:dayDifference>35?"month":dayDifference>2?"day":"hour"},offset:true},y:{stacked:true,type:"linear",title:{display:true,text:"kWh"},ticks:{beginAtZero:true,callback:value=>formatNumber(Math.abs(value),locale)}}},plugins:{tooltip:{mode:"x",intersect:true,position:"nearest",filter:val=>val.formattedValue!=="0",callbacks:{title:datasets=>{if(dayDifference>0){return datasets[0].label;}const date=new Date(datasets[0].parsed.x);return `${formatTime(date,locale)} – ${formatTime(addHours(date,1),locale)}`;},label:context=>`${context.dataset.label}: ${formatNumber(Math.abs(context.parsed.y),locale)} kWh`,footer:contexts=>{let totalConsumed=0;let totalReturned=0;for(const context of contexts){const value=context.dataset.data[context.dataIndex].y;if(value>0){totalConsumed+=value;}else {totalReturned+=Math.abs(value);}}return [totalConsumed?this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.total_consumed",{num:formatNumber(totalConsumed,locale)}):"",totalReturned?this.hass.localize("ui.panel.lovelace.cards.energyenergy_usage_graph.total_returned",{num:formatNumber(totalReturned,locale)}):""].filter(Boolean);}}},filler:{propagate:false},legend:{display:false,labels:{usePointStyle:true}}},hover:{mode:"nearest"},elements:{bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:5}},// @ts-expect-error
locale:numberFormatToLocale(locale)};});}},{kind:"method",key:"_getStatistics",value:async function _getStatistics(energyData){const datasets=[];const statistics={};for(const source of energyData.prefs.energy_sources){if(source.type==="solar"){if(statistics.solar){statistics.solar.push(source.stat_energy_from);}else {statistics.solar=[source.stat_energy_from];}continue;}if(source.type==="battery"){if(statistics.to_battery){statistics.to_battery.push(source.stat_energy_to);statistics.from_battery.push(source.stat_energy_from);}else {statistics.to_battery=[source.stat_energy_to];statistics.from_battery=[source.stat_energy_from];}continue;}if(source.type!=="grid"){continue;}// grid source
for(const flowFrom of source.flow_from){if(statistics.from_grid){statistics.from_grid.push(flowFrom.stat_energy_from);}else {statistics.from_grid=[flowFrom.stat_energy_from];}}for(const flowTo of source.flow_to){if(statistics.to_grid){statistics.to_grid.push(flowTo.stat_energy_to);}else {statistics.to_grid=[flowTo.stat_energy_to];}}}this._start=energyData.start;this._end=energyData.end||endOfToday();const combinedData={};const summedData={};const computedStyles=getComputedStyle(this);const colors={to_grid:computedStyles.getPropertyValue("--energy-grid-return-color").trim(),to_battery:computedStyles.getPropertyValue("--energy-battery-in-color").trim(),from_grid:computedStyles.getPropertyValue("--energy-grid-consumption-color").trim(),used_grid:computedStyles.getPropertyValue("--energy-grid-consumption-color").trim(),used_solar:computedStyles.getPropertyValue("--energy-solar-color").trim(),used_battery:computedStyles.getPropertyValue("--energy-battery-out-color").trim()};const labels={used_grid:this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.combined_from_grid"),used_solar:this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.consumed_solar"),used_battery:this.hass.localize("ui.panel.lovelace.cards.energy.energy_usage_graph.consumed_battery")};Object.entries(statistics).forEach(([key,statIds])=>{const sum=["solar","to_grid","from_grid","to_battery","from_battery"].includes(key);const add=!["solar","from_battery"].includes(key);const totalStats={};const sets={};statIds.forEach(id=>{const stats=energyData.stats[id];if(!stats){return;}const set={};let prevValue;stats.forEach(stat=>{if(stat.sum===null){return;}if(prevValue===undefined){prevValue=stat.sum;return;}const val=stat.sum-prevValue;// Get total of solar and to grid to calculate the solar energy used
if(sum){totalStats[stat.start]=stat.start in totalStats?totalStats[stat.start]+val:val;}if(add&&!(stat.start in set)){set[stat.start]=val;}prevValue=stat.sum;});sets[id]=set;});if(sum){summedData[key]=totalStats;}if(add){combinedData[key]=sets;}});const grid_to_battery={};const battery_to_grid={};if((summedData.to_grid||summedData.to_battery)&&summedData.solar){const used_solar={};for(const start of Object.keys(summedData.solar)){var _summedData$to_grid,_summedData$to_batter;used_solar[start]=(summedData.solar[start]||0)-(((_summedData$to_grid=summedData.to_grid)===null||_summedData$to_grid===void 0?void 0:_summedData$to_grid[start])||0)-(((_summedData$to_batter=summedData.to_battery)===null||_summedData$to_batter===void 0?void 0:_summedData$to_batter[start])||0);if(used_solar[start]<0){if(summedData.to_battery){var _summedData$from_grid;grid_to_battery[start]=used_solar[start]*-1;if(grid_to_battery[start]>(((_summedData$from_grid=summedData.from_grid)===null||_summedData$from_grid===void 0?void 0:_summedData$from_grid[start])||0)){var _summedData$from_grid2,_summedData$from_grid3;battery_to_grid[start]=Math.min(0,grid_to_battery[start]-(((_summedData$from_grid2=summedData.from_grid)===null||_summedData$from_grid2===void 0?void 0:_summedData$from_grid2[start])||0));grid_to_battery[start]=(_summedData$from_grid3=summedData.from_grid)===null||_summedData$from_grid3===void 0?void 0:_summedData$from_grid3[start];}}used_solar[start]=0;}}combinedData.used_solar={used_solar};}if(summedData.from_battery){if(summedData.to_grid){const used_battery={};for(const start of Object.keys(summedData.from_battery)){used_battery[start]=(summedData.from_battery[start]||0)-(battery_to_grid[start]||0);}combinedData.used_battery={used_battery};}else {combinedData.used_battery={used_battery:summedData.from_battery};}}if(combinedData.from_grid&&summedData.to_battery){const used_grid={};for(const start of Object.keys(grid_to_battery)){let noOfSources=0;let source;for(const[key,stats]of Object.entries(combinedData.from_grid)){if(stats[start]){source=key;noOfSources++;}if(noOfSources>1){break;}}if(noOfSources===1){combinedData.from_grid[source][start]-=grid_to_battery[start]||0;}else {let total_from_grid=0;Object.values(combinedData.from_grid).forEach(stats=>{total_from_grid+=stats[start]||0;delete stats[start];});used_grid[start]=total_from_grid-(grid_to_battery[start]||0);}}combinedData.used_grid={used_grid};}let allKeys=[];Object.values(combinedData).forEach(sources=>{Object.values(sources).forEach(source=>{allKeys=allKeys.concat(Object.keys(source));});});const uniqueKeys=Array.from(new Set(allKeys));Object.entries(combinedData).forEach(([type,sources])=>{Object.entries(sources).forEach(([statId,source],idx)=>{const data=[];const entity=this.hass.states[statId];const modifiedColor=idx>0?this.hass.themes.darkMode?labBrighten(rgb2lab(hex2rgb(colors[type])),idx):labDarken(rgb2lab(hex2rgb(colors[type])),idx):undefined;const borderColor=modifiedColor?rgb2hex(lab2rgb(modifiedColor)):colors[type];data.push({label:type in labels?labels[type]:entity?computeStateName(entity):statId,order:type==="used_solar"?0:type==="to_battery"?Object.keys(combinedData).length:idx+1,borderColor,backgroundColor:borderColor+"7F",stack:"stack",data:[]});// Process chart data.
for(const key of uniqueKeys){const value=source[key]||0;const date=new Date(key);// @ts-expect-error
data[0].data.push({x:date.getTime(),y:value&&["to_grid","to_battery"].includes(type)?-1*value:value});}// Concat two arrays
Array.prototype.push.apply(datasets,data);});});this._chartData={datasets};}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
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

export { HuiEnergyUsageGraphCard };
