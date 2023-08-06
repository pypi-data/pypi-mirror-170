const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, X as mdiChevronLeft, Y as mdiChevronRight, r, n } from './main-dev.js';
import { d as formatDate, aM as formatDateMonthYear, aL as formatDateYear, aO as formatDateShort } from './auth-dev.js';
import { af as toggleAttribute } from './ha-more-info-dialog-dev.js';
import { g as getEnergyDataCollection, s as startOfToday, a as endOfToday } from './energy-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import { r as requiredArgs, b as toDate, s as startOfDay, e as endOfDay, d as differenceInDays } from './index-dev3.js';
import { g as startOfWeek, f as startOfMonth, s as startOfYear, d as addDays, c as addWeeks, a as addMonths, b as addYears, i as endOfWeek, e as endOfMonth, h as endOfYear } from './index-dev2.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './subscribe-one-dev.js';
import './config_entries-dev.js';

/**
 * @name isWithinInterval
 * @category Interval Helpers
 * @summary Is the given date within the interval?
 *
 * @description
 * Is the given date within the interval? (Including start and end.)
 *
 * @param {Date|Number} date - the date to check
 * @param {Interval} interval - the interval to check
 * @returns {Boolean} the date is within the interval
 * @throws {TypeError} 2 arguments required
 * @throws {RangeError} The start of an interval cannot be after its end
 * @throws {RangeError} Date in interval cannot be `Invalid Date`
 *
 * @example
 * // For the date within the interval:
 * isWithinInterval(new Date(2014, 0, 3), {
 *   start: new Date(2014, 0, 1),
 *   end: new Date(2014, 0, 7)
 * })
 * //=> true
 *
 * @example
 * // For the date outside of the interval:
 * isWithinInterval(new Date(2014, 0, 10), {
 *   start: new Date(2014, 0, 1),
 *   end: new Date(2014, 0, 7)
 * })
 * //=> false
 *
 * @example
 * // For date equal to interval start:
 * isWithinInterval(date, { start, end: date }) // => true
 *
 * @example
 * // For date equal to interval end:
 * isWithinInterval(date, { start: date, end }) // => true
 */function isWithinInterval(dirtyDate,interval){requiredArgs(2,arguments);var time=toDate(dirtyDate).getTime();var startTime=toDate(interval.start).getTime();var endTime=toDate(interval.end).getTime();// Throw an exception if start date is after end date or if any date is `Invalid Date`
if(!(startTime<=endTime)){throw new RangeError('Invalid interval');}return time>=startTime&&time<=endTime;}

_decorate([n("hui-energy-period-selector")],function(_initialize,_SubscribeMixin){class HuiEnergyPeriodSelector extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyPeriodSelector,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"collectionKey",value:void 0},{kind:"field",decorators:[t()],key:"_startDate",value:void 0},{kind:"field",decorators:[t()],key:"_endDate",value:void 0},{kind:"field",decorators:[t()],key:"_period",value:void 0},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiEnergyPeriodSelector.prototype),"connectedCallback",this).call(this);toggleAttribute(this,"narrow",this.offsetWidth<600);}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){return [getEnergyDataCollection(this.hass,{key:this.collectionKey}).subscribe(data=>this._updateDates(data))];}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._startDate){return $``;}const viewButtons=[{label:this.hass.localize("ui.panel.lovelace.components.energy_period_selector.day"),value:"day"},{label:this.hass.localize("ui.panel.lovelace.components.energy_period_selector.week"),value:"week"},{label:this.hass.localize("ui.panel.lovelace.components.energy_period_selector.month"),value:"month"},{label:this.hass.localize("ui.panel.lovelace.components.energy_period_selector.year"),value:"year"}];return $`
      <div class="row">
        <div class="label">
          ${this._period==="day"?formatDate(this._startDate,this.hass.locale):this._period==="month"?formatDateMonthYear(this._startDate,this.hass.locale):this._period==="year"?formatDateYear(this._startDate,this.hass.locale):`${formatDateShort(this._startDate,this.hass.locale)} – ${formatDateShort(this._endDate||new Date(),this.hass.locale)}`}
          <ha-icon-button
            .label=${this.hass.localize("ui.panel.lovelace.components.energy_period_selector.previous")}
            @click=${this._pickPrevious}
            .path=${mdiChevronLeft}
          ></ha-icon-button>
          <ha-icon-button
            .label=${this.hass.localize("ui.panel.lovelace.components.energy_period_selector.next")}
            @click=${this._pickNext}
            .path=${mdiChevronRight}
          ></ha-icon-button>
          <mwc-button dense outlined @click=${this._pickToday}>
            ${this.hass.localize("ui.panel.lovelace.components.energy_period_selector.today")}
          </mwc-button>
        </div>
        <div class="period">
          <ha-button-toggle-group
            .buttons=${viewButtons}
            .active=${this._period}
            dense
            @value-changed=${this._handleView}
          ></ha-button-toggle-group>
        </div>
      </div>
    `;}},{kind:"method",key:"_handleView",value:function _handleView(ev){this._period=ev.detail.value;const today=startOfToday();const start=!this._startDate||isWithinInterval(today,{start:this._startDate,end:this._endDate||endOfToday()})?today:this._startDate;this._setDate(this._period==="day"?startOfDay(start):this._period==="week"?startOfWeek(start,{weekStartsOn:1}):this._period==="month"?startOfMonth(start):startOfYear(start));}},{kind:"method",key:"_pickToday",value:function _pickToday(){this._setDate(this._period==="day"?startOfToday():this._period==="week"?startOfWeek(new Date(),{weekStartsOn:1}):this._period==="month"?startOfMonth(new Date()):startOfYear(new Date()));}},{kind:"method",key:"_pickPrevious",value:function _pickPrevious(){const newStart=this._period==="day"?addDays(this._startDate,-1):this._period==="week"?addWeeks(this._startDate,-1):this._period==="month"?addMonths(this._startDate,-1):addYears(this._startDate,-1);this._setDate(newStart);}},{kind:"method",key:"_pickNext",value:function _pickNext(){const newStart=this._period==="day"?addDays(this._startDate,1):this._period==="week"?addWeeks(this._startDate,1):this._period==="month"?addMonths(this._startDate,1):addYears(this._startDate,1);this._setDate(newStart);}},{kind:"method",key:"_setDate",value:function _setDate(startDate){const endDate=this._period==="day"?endOfDay(startDate):this._period==="week"?endOfWeek(startDate,{weekStartsOn:1}):this._period==="month"?endOfMonth(startDate):endOfYear(startDate);const energyCollection=getEnergyDataCollection(this.hass,{key:this.collectionKey});energyCollection.setPeriod(startDate,endDate);energyCollection.refresh();}},{kind:"method",key:"_updateDates",value:function _updateDates(energyData){this._startDate=energyData.start;this._endDate=energyData.end||endOfToday();const dayDifference=differenceInDays(this._endDate,this._startDate);this._period=dayDifference<1?"day":dayDifference===6?"week":dayDifference>26&&dayDifference<31// 28, 29, 30 or 31 days in a month
?"month":dayDifference===364||dayDifference===365// Leap year
?"year":undefined;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .row {
        display: flex;
        justify-content: flex-end;
      }
      :host([narrow]) .row {
        flex-direction: column-reverse;
      }
      :host([narrow]) .period {
        margin-bottom: 8px;
      }
      .label {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        font-size: 20px;
      }
      .period {
        display: flex;
        justify-content: flex-end;
      }
      :host {
        --mdc-button-outline-color: currentColor;
        --primary-color: currentColor;
        --mdc-theme-primary: currentColor;
        --mdc-button-disabled-outline-color: var(--disabled-text-color);
        --mdc-button-disabled-ink-color: var(--disabled-text-color);
        --mdc-icon-button-ripple-opacity: 0.2;
      }
      ha-icon-button {
        --mdc-icon-button-size: 28px;
      }
      ha-button-toggle-group {
        padding-left: 8px;
      }
      mwc-button {
        flex-shrink: 0;
      }
    `;}}]};},SubscribeMixin(s));

let HuiEnergyDateSelectionCard=_decorate([n("hui-energy-date-selection-card")],function(_initialize,_LitElement){class HuiEnergyDateSelectionCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEnergyDateSelectionCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 1;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <hui-energy-period-selector
        .hass=${this.hass}
        .collectionKey=${this._config.collection_key}
      ></hui-energy-period-selector>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r``;}}]};},s);

export { HuiEnergyDateSelectionCard };
