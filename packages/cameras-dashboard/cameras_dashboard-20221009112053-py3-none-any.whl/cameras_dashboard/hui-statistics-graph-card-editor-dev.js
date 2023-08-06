const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, $, b as memoizeOne, f as fireEvent, n, r } from './main-dev.js';
import './ha-form-dev.js';
import { j as computeStateName, ar as union, at as literal, al as assign, am as object, as as array, an as optional, ao as string, ax as number, aq as assert } from './auth-dev.js';
import { s as stringCompare } from './compare-dev.js';
import { ai as getStatisticIds, U as processConfigEntities } from './ha-more-info-dialog-dev.js';
import { d as documentationUrl } from './documentation-url-dev.js';
import './ha-combo-box-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { e as entitiesConfigStruct } from './entities-struct-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './action-struct-dev.js';

_decorate([n("ha-statistic-picker")],function(_initialize,_LitElement){class HaStatisticPicker extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaStatisticPicker,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e({attribute:"statistic-types"})],key:"statisticTypes",value:void 0},{kind:"field",decorators:[e({type:Array})],key:"statisticIds",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-unit-of-measurement"})],key:"includeUnitOfMeasurement",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[e({type:Boolean,attribute:"entities-only"})],key:"entitiesOnly",value(){return false;}},{kind:"field",decorators:[t()],key:"_opened",value:void 0},{kind:"field",decorators:[i("ha-combo-box",true)],key:"comboBox",value:void 0},{kind:"field",key:"_init",value(){return false;}},{kind:"field",key:"_rowRenderer",value(){return item=>$`<mwc-list-item graphic="avatar" twoline>
    ${item.state?$`<state-badge slot="graphic" .stateObj=${item.state}></state-badge>`:""}
    <span>${item.name}</span>
    <span slot="secondary"
      >${item.id===""||item.id==="__missing"?$`<a
            target="_blank"
            rel="noopener noreferrer"
            href=${documentationUrl(this.hass)}
            >${this.hass.localize("ui.components.statistic-picker.learn_more")}</a
          >`:item.id}</span
    >
  </mwc-list-item>`;}},{kind:"field",key:"_getStatistics",value(){return memoizeOne((statisticIds,includeUnitOfMeasurement,includeDeviceClasses,entitiesOnly)=>{if(!statisticIds.length){return [{id:"",name:this.hass.localize("ui.components.statistic-picker.no_statistics")}];}if(includeUnitOfMeasurement){statisticIds=statisticIds.filter(meta=>includeUnitOfMeasurement.includes(meta.unit_of_measurement));}const output=[];statisticIds.forEach(meta=>{const entityState=this.hass.states[meta.statistic_id];if(!entityState){if(!entitiesOnly){output.push({id:meta.statistic_id,name:meta.name||meta.statistic_id});}return;}if(!includeDeviceClasses||includeDeviceClasses.includes(entityState.attributes.device_class||"")){output.push({id:meta.statistic_id,name:computeStateName(entityState),state:entityState});}});if(!output.length){return [{id:"",name:this.hass.localize("ui.components.statistic-picker.no_match")}];}if(output.length>1){output.sort((a,b)=>stringCompare(a.name||"",b.name||""));}output.push({id:"__missing",name:this.hass.localize("ui.components.statistic-picker.missing_entity")});return output;});}},{kind:"method",key:"open",value:/**
   * Show only statistics with these unit of measuments.
   * @type {Array}
   * @attr include-unit-of-measurement
   */ /**
   * Show only statistics with these device classes.
   * @type {Array}
   * @attr include-device-classes
   */ /**
   * Show only statistics on entities.
   * @type {Boolean}
   * @attr entities-only
   */function open(){var _this$comboBox;(_this$comboBox=this.comboBox)===null||_this$comboBox===void 0?void 0:_this$comboBox.open();}},{kind:"method",key:"focus",value:function focus(){var _this$comboBox2;(_this$comboBox2=this.comboBox)===null||_this$comboBox2===void 0?void 0:_this$comboBox2.focus();}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){if(!this.hasUpdated&&!this.statisticIds||changedProps.has("statisticTypes")){this._getStatisticIds();}if(!this._init&&this.statisticIds||changedProps.has("_opened")&&this._opened){this._init=true;if(this.hasUpdated){this.comboBox.items=this._getStatistics(this.statisticIds,this.includeUnitOfMeasurement,this.includeDeviceClasses,this.entitiesOnly);}else {this.updateComplete.then(()=>{this.comboBox.items=this._getStatistics(this.statisticIds,this.includeUnitOfMeasurement,this.includeDeviceClasses,this.entitiesOnly);});}}}},{kind:"method",key:"render",value:function render(){return $`
      <ha-combo-box
        .hass=${this.hass}
        .label=${this.label===undefined&&this.hass?this.hass.localize("ui.components.statistic-picker.statistic"):this.label}
        .value=${this._value}
        .renderer=${this._rowRenderer}
        .disabled=${this.disabled}
        item-value-path="id"
        item-id-path="id"
        item-label-path="name"
        @opened-changed=${this._openedChanged}
        @value-changed=${this._statisticChanged}
      ></ha-combo-box>
    `;}},{kind:"method",key:"_getStatisticIds",value:async function _getStatisticIds(){this.statisticIds=await getStatisticIds(this.hass,this.statisticTypes);}},{kind:"get",key:"_value",value:function _value(){return this.value||"";}},{kind:"method",key:"_statisticChanged",value:function _statisticChanged(ev){ev.stopPropagation();let newValue=ev.detail.value;if(newValue==="__missing"){newValue="";}if(newValue!==this._value){this._setValue(newValue);}}},{kind:"method",key:"_openedChanged",value:function _openedChanged(ev){this._opened=ev.detail.value;}},{kind:"method",key:"_setValue",value:function _setValue(value){this.value=value;setTimeout(()=>{fireEvent(this,"value-changed",{value});fireEvent(this,"change");},0);}}]};},s);

_decorate([n("ha-statistics-picker")],function(_initialize,_LitElement){class HaStatisticsPicker extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaStatisticsPicker,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({type:Array})],key:"value",value:void 0},{kind:"field",decorators:[e({type:Array})],key:"statisticIds",value:void 0},{kind:"field",decorators:[e({attribute:"statistic-types"})],key:"statisticTypes",value:void 0},{kind:"field",decorators:[e({attribute:"picked-statistic-label"})],key:"pickedStatisticLabel",value:void 0},{kind:"field",decorators:[e({attribute:"pick-statistic-label"})],key:"pickStatisticLabel",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass){return $``;}return $`
      ${this._currentStatistics.map(statisticId=>$`
          <div>
            <ha-statistic-picker
              .curValue=${statisticId}
              .hass=${this.hass}
              .value=${statisticId}
              .statisticTypes=${this.statisticTypes}
              .statisticIds=${this.statisticIds}
              .label=${this.pickedStatisticLabel}
              @value-changed=${this._statisticChanged}
            ></ha-statistic-picker>
          </div>
        `)}
      <div>
        <ha-statistic-picker
          .hass=${this.hass}
          .statisticTypes=${this.statisticTypes}
          .statisticIds=${this.statisticIds}
          .label=${this.pickStatisticLabel}
          @value-changed=${this._addStatistic}
        ></ha-statistic-picker>
      </div>
    `;}},{kind:"get",key:"_currentStatistics",value:function _currentStatistics(){return this.value||[];}},{kind:"method",key:"_updateStatistics",value:async function _updateStatistics(entities){this.value=entities;fireEvent(this,"value-changed",{value:entities});}},{kind:"method",key:"_statisticChanged",value:function _statisticChanged(event){event.stopPropagation();const oldValue=event.currentTarget.curValue;const newValue=event.detail.value;if(newValue===oldValue){return;}const currentStatistics=this._currentStatistics;if(!newValue||currentStatistics.includes(newValue)){this._updateStatistics(currentStatistics.filter(ent=>ent!==oldValue));return;}this._updateStatistics(currentStatistics.map(ent=>ent===oldValue?newValue:ent));}},{kind:"method",key:"_addStatistic",value:async function _addStatistic(event){event.stopPropagation();const toAdd=event.detail.value;if(!toAdd){return;}event.currentTarget.value="";if(!toAdd){return;}const currentEntities=this._currentStatistics;if(currentEntities.includes(toAdd)){return;}this._updateStatistics([...currentEntities,toAdd]);}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        width: 200px;
        display: block;
      }
      ha-statistic-picker {
        display: block;
        width: 100%;
        margin-top: 8px;
      }
    `;}}]};},s);

const statTypeStruct=union([literal("sum"),literal("min"),literal("max"),literal("mean")]);const cardConfigStruct=assign(baseLovelaceCardConfig,object({entities:array(entitiesConfigStruct),title:optional(string()),days_to_show:optional(number()),period:optional(union([literal("5minute"),literal("hour"),literal("day"),literal("month")])),chart_type:optional(union([literal("bar"),literal("line")])),stat_types:optional(union([array(statTypeStruct),statTypeStruct]))}));const periods=["5minute","hour","day","month"];let HuiStatisticsGraphCardEditor=_decorate([n("hui-statistics-graph-card-editor")],function(_initialize,_LitElement){class HuiStatisticsGraphCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiStatisticsGraphCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;this._configEntities=config.entities?processConfigEntities(config.entities,false).map(cfg=>cfg.entity):[];}},{kind:"field",key:"_schema",value(){return memoizeOne(localize=>[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"period",required:true,selector:{select:{options:periods.map(period=>({value:period,label:localize(`ui.panel.lovelace.editor.card.statistics-graph.periods.${period}`)}))}}},{name:"days_to_show",required:true,selector:{number:{min:1,mode:"box"}}},{name:"stat_types",required:true,type:"multi_select",options:[["mean","Mean"],["min","Min"],["max","Max"],["sum","Sum"]]},{name:"chart_type",required:true,type:"select",options:[["line","Line"],["bar","Bar"]]}]}]);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const schema=this._schema(this.hass.localize);const stat_types=this._config.stat_types?Array.isArray(this._config.stat_types)?this._config.stat_types:[this._config.stat_types]:["mean","min","max","sum"];const data={chart_type:"line",period:"hour",days_to_show:30,...this._config,stat_types};return $`
      <ha-form
        .hass=${this.hass}
        .data=${data}
        .schema=${schema}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
        <ha-statistics-picker
          .hass=${this.hass}
          .pickStatisticLabel=${`Add a statistic`}
          .pickedStatisticLabel=${`Statistic`}
          .value=${this._configEntities}
          .configValue=${"entities"}
          @value-changed=${this._entitiesChanged}
        ></ha-statistics-picker>
      </div>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"method",key:"_entitiesChanged",value:function _entitiesChanged(ev){fireEvent(this,"config-changed",{config:{...this._config,entities:ev.detail.value}});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.generic.${schema.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.statistics-graph.${schema.name}`);}},{kind:"field",static:true,key:"styles",value(){return r`
    ha-statistics-picker {
      width: 100%;
    }
  `;}}]};},s);

export { HuiStatisticsGraphCardEditor };
