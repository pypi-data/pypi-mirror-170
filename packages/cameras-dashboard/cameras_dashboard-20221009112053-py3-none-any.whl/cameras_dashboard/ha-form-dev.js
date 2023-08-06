const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { ah as __decorate, n, _ as _decorate, c as s, d as e, G as i, $, f as fireEvent, r, j as _get, k as _getPrototypeOf, t, dN as mdiMenuUp, dO as mdiMenuDown, U as __extends, V as __assign, ay as MDCFoundation, aB as observer, R as e$1, bq as ariaProperty, K as e$2, dq as FormElement, T as RippleHandlers, aA as addHasRemoveClass, z as o, Q as l, dP as mdiEyeOff, b5 as mdiEye } from './main-dev.js';
import { d as dynamicElement } from './dynamic-element-directive-dev.js';
import { a as styles$1, F as FormfieldBase, s as stopPropagation } from './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

let Formfield=class Formfield extends FormfieldBase{};Formfield.styles=[styles$1];Formfield=__decorate([n('mwc-formfield')],Formfield);

_decorate([n("ha-form-boolean")],function(_initialize,_LitElement){class HaFormBoolean extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormBoolean,d:[{kind:"field",decorators:[e()],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[i("ha-checkbox",true)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){return $`
      <mwc-formfield .label=${this.label}>
        <ha-checkbox
          .checked=${this.data}
          .disabled=${this.disabled}
          @change=${this._valueChanged}
        ></ha-checkbox>
      </mwc-formfield>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"value-changed",{value:ev.target.checked});}}]};},s);

_decorate([n("ha-form-constant")],function(_initialize,_LitElement){class HaFormConstant extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormConstant,d:[{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"method",key:"render",value:function render(){return $`<span class="label">${this.label}</span>${this.schema.value?`: ${this.schema.value}`:""}`;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
      }
      .label {
        font-weight: 500;
      }
    `;}}]};},s);

_decorate([n("ha-form-grid")],function(_initialize,_LitElement){class HaFormGrid extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormGrid,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"data",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[e()],key:"computeLabel",value:void 0},{kind:"field",decorators:[e()],key:"computeHelper",value:void 0},{kind:"method",key:"firstUpdated",value:function firstUpdated(changedProps){_get(_getPrototypeOf(HaFormGrid.prototype),"firstUpdated",this).call(this,changedProps);this.setAttribute("own-margin","");}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HaFormGrid.prototype),"updated",this).call(this,changedProps);if(changedProps.has("schema")){if(this.schema.column_min_width){this.style.setProperty("--form-grid-min-width",this.schema.column_min_width);}else {this.style.setProperty("--form-grid-min-width","");}}}},{kind:"method",key:"render",value:function render(){return $`
      ${this.schema.schema.map(item=>$`
            <ha-form
              .hass=${this.hass}
              .data=${this.data}
              .schema=${[item]}
              .disabled=${this.disabled}
              .computeLabel=${this.computeLabel}
              .computeHelper=${this.computeHelper}
            ></ha-form>
          `)}
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: grid !important;
        grid-template-columns: repeat(
          var(--form-grid-column-count, auto-fit),
          minmax(var(--form-grid-min-width, 180px), 1fr)
        );
        grid-gap: 1vw;
      }
      :host > ha-form {
        display: block;
        margin-bottom: 24px;
      }
    `;}}]};},s);

_decorate([n("ha-form-float")],function(_initialize,_LitElement){class HaFormFloat extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormFloat,d:[{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[i("ha-textfield")],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){var _this$schema$descript;return $`
      <ha-textfield
        inputMode="decimal"
        .label=${this.label}
        .value=${this.data!==undefined?this.data:""}
        .disabled=${this.disabled}
        .required=${this.schema.required}
        .autoValidate=${this.schema.required}
        .suffix=${(_this$schema$descript=this.schema.description)===null||_this$schema$descript===void 0?void 0:_this$schema$descript.suffix}
        .validationMessage=${this.schema.required?"Required":undefined}
        @input=${this._valueChanged}
      ></ha-textfield>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){if(changedProps.has("schema")){this.toggleAttribute("own-margin",!!this.schema.required);}}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const source=ev.target;const rawValue=source.value.replace(",",".");let value;if(rawValue.endsWith(".")){return;}if(rawValue!==""){value=parseFloat(rawValue);if(isNaN(value)){value=undefined;}}// Detect anything changed
if(this.data===value){// parseFloat will drop invalid text at the end, in that case update textfield
const newRawValue=value===undefined?"":String(value);if(source.value!==newRawValue){source.value=newRawValue;}return;}fireEvent(this,"value-changed",{value});}},{kind:"field",static:true,key:"styles",value(){return r`
    :host([own-margin]) {
      margin-bottom: 5px;
    }
    ha-textfield {
      display: block;
    }
  `;}}]};},s);

_decorate([n("ha-form-integer")],function(_initialize,_LitElement){class HaFormInteger extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormInteger,d:[{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[i("ha-textfield ha-slider")],key:"_input",value:void 0},{kind:"field",key:"_lastValue",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){var _this$schema$descript;if(this.schema.valueMin!==undefined&&this.schema.valueMax!==undefined&&this.schema.valueMax-this.schema.valueMin<256){return $`
        <div>
          ${this.label}
          <div class="flex">
            ${!this.schema.required?$`
                  <ha-checkbox
                    @change=${this._handleCheckboxChange}
                    .checked=${this.data!==undefined}
                    .disabled=${this.disabled}
                  ></ha-checkbox>
                `:""}
            <ha-slider
              pin
              ignore-bar-touch
              .value=${this._value}
              .min=${this.schema.valueMin}
              .max=${this.schema.valueMax}
              .disabled=${this.disabled||this.data===undefined&&!this.schema.required}
              @change=${this._valueChanged}
            ></ha-slider>
          </div>
        </div>
      `;}return $`
      <ha-textfield
        type="number"
        inputMode="numeric"
        .label=${this.label}
        .value=${this.data!==undefined?this.data:""}
        .disabled=${this.disabled}
        .required=${this.schema.required}
        .autoValidate=${this.schema.required}
        .suffix=${(_this$schema$descript=this.schema.description)===null||_this$schema$descript===void 0?void 0:_this$schema$descript.suffix}
        .validationMessage=${this.schema.required?"Required":undefined}
        @input=${this._valueChanged}
      ></ha-textfield>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){if(changedProps.has("schema")){this.toggleAttribute("own-margin",!("valueMin"in this.schema&&"valueMax"in this.schema)&&!!this.schema.required);}}},{kind:"get",key:"_value",value:function _value(){var _this$schema$descript2;if(this.data!==undefined){return this.data;}if(!this.schema.required){return this.schema.valueMin||0;}return ((_this$schema$descript2=this.schema.description)===null||_this$schema$descript2===void 0?void 0:_this$schema$descript2.suggested_value)||this.schema.default||this.schema.valueMin||0;}},{kind:"method",key:"_handleCheckboxChange",value:function _handleCheckboxChange(ev){const checked=ev.target.checked;let value;if(checked){for(const candidate of [this._lastValue,(_this$schema$descript3=this.schema.description)===null||_this$schema$descript3===void 0?void 0:_this$schema$descript3.suggested_value,this.schema.default,0]){var _this$schema$descript3;if(candidate!==undefined){value=candidate;break;}}}else {// We track last value so user can disable and enable a field without losing
// their value.
this._lastValue=this.data;}fireEvent(this,"value-changed",{value});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const source=ev.target;const rawValue=source.value;let value;if(rawValue!==""){value=parseInt(String(rawValue));}if(this.data===value){// parseInt will drop invalid text at the end, in that case update textfield
const newRawValue=value===undefined?"":String(value);if(source.value!==newRawValue){source.value=newRawValue;}return;}fireEvent(this,"value-changed",{value});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host([own-margin]) {
        margin-bottom: 5px;
      }
      .flex {
        display: flex;
      }
      ha-slider {
        flex: 1;
      }
      ha-textfield {
        display: block;
      }
    `;}}]};},s);

function optionValue(item){return Array.isArray(item)?item[0]:item;}function optionLabel(item){return Array.isArray(item)?item[1]||item[0]:item;}const SHOW_ALL_ENTRIES_LIMIT=6;_decorate([n("ha-form-multi_select")],function(_initialize,_LitElement){class HaFormMultiSelect extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormMultiSelect,d:[{kind:"field",decorators:[e()],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[t()],key:"_opened",value(){return false;}},{kind:"field",decorators:[i("ha-button-menu")],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){const options=Array.isArray(this.schema.options)?this.schema.options:Object.entries(this.schema.options);const data=this.data||[];// We will just render all checkboxes.
if(options.length<SHOW_ALL_ENTRIES_LIMIT){return $`<div>
        ${this.label}${options.map(item=>{const value=optionValue(item);return $`
            <ha-formfield .label=${optionLabel(item)}>
              <ha-checkbox
                .checked=${data.includes(value)}
                .value=${value}
                .disabled=${this.disabled}
                @change=${this._valueChanged}
              ></ha-checkbox>
            </ha-formfield>
          `;})}
      </div> `;}return $`
      <ha-button-menu
        .disabled=${this.disabled}
        fixed
        corner="BOTTOM_START"
        @opened=${this._handleOpen}
        @closed=${this._handleClose}
        multi
        activatable
      >
        <ha-textfield
          slot="trigger"
          .label=${this.label}
          .value=${data.map(value=>this.schema.options[value]||value).join(", ")}
          .disabled=${this.disabled}
          tabindex="-1"
        ></ha-textfield>
        <ha-svg-icon
          slot="trigger"
          .path=${this._opened?mdiMenuUp:mdiMenuDown}
        ></ha-svg-icon>
        ${options.map(item=>{const value=optionValue(item);const selected=data.includes(value);return $`<ha-check-list-item
            left
            .selected=${selected}
            .activated=${selected}
            @request-selected=${this._selectedChanged}
            .value=${value}
            .disabled=${this.disabled}
          >
            ${optionLabel(item)}
          </ha-check-list-item>`;})}
      </ha-button-menu>
    `;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){this.updateComplete.then(()=>{var _this$shadowRoot;const{formElement,mdcRoot}=((_this$shadowRoot=this.shadowRoot)===null||_this$shadowRoot===void 0?void 0:_this$shadowRoot.querySelector("ha-textfield"))||{};if(formElement){formElement.style.textOverflow="ellipsis";}if(mdcRoot){mdcRoot.style.cursor="pointer";}});}},{kind:"method",key:"updated",value:function updated(changedProps){if(changedProps.has("schema")){this.toggleAttribute("own-margin",Object.keys(this.schema.options).length>=SHOW_ALL_ENTRIES_LIMIT&&!!this.schema.required);}}},{kind:"method",key:"_selectedChanged",value:function _selectedChanged(ev){ev.stopPropagation();if(ev.detail.source==="property"){return;}this._handleValueChanged(ev.target.value,ev.detail.selected);}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const{value,checked}=ev.target;this._handleValueChanged(value,checked);}},{kind:"method",key:"_handleValueChanged",value:function _handleValueChanged(value,checked){let newValue;if(checked){if(!this.data){newValue=[value];}else if(this.data.includes(value)){return;}else {newValue=[...this.data,value];}}else {if(!this.data.includes(value)){return;}newValue=this.data.filter(v=>v!==value);}fireEvent(this,"value-changed",{value:newValue});}},{kind:"method",key:"_handleOpen",value:function _handleOpen(ev){ev.stopPropagation();this._opened=true;this.toggleAttribute("opened",true);}},{kind:"method",key:"_handleClose",value:function _handleClose(ev){ev.stopPropagation();this._opened=false;this.toggleAttribute("opened",false);}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host([own-margin]) {
        margin-bottom: 5px;
      }
      ha-button-menu {
        display: block;
        cursor: pointer;
      }
      ha-formfield {
        display: block;
        padding-right: 16px;
      }
      ha-textfield {
        display: block;
        pointer-events: none;
      }
      ha-svg-icon {
        color: var(--input-dropdown-icon-color);
        position: absolute;
        right: 1em;
        top: 1em;
        cursor: pointer;
      }
      :host([opened]) ha-svg-icon {
        color: var(--primary-color);
      }
      :host([opened]) ha-button-menu {
        --mdc-text-field-idle-line-color: var(--input-hover-line-color);
        --mdc-text-field-label-ink-color: var(--primary-color);
      }
    `;}}]};},s);

_decorate([n("ha-duration-input")],function(_initialize,_LitElement){class HaDurationInput extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaDurationInput,d:[{kind:"field",decorators:[e({attribute:false})],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"required",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"enableMillisecond",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[i("paper-time-input",true)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){return $`
      <ha-base-time-input
        .label=${this.label}
        .required=${this.required}
        .autoValidate=${this.required}
        .disabled=${this.disabled}
        errorMessage="Required"
        enableSecond
        .enableMillisecond=${this.enableMillisecond}
        format="24"
        .hours=${this._hours}
        .minutes=${this._minutes}
        .seconds=${this._seconds}
        .milliseconds=${this._milliseconds}
        @value-changed=${this._durationChanged}
        noHoursLimit
        hourLabel="hh"
        minLabel="mm"
        secLabel="ss"
        millisecLabel="ms"
      ></ha-base-time-input>
    `;}},{kind:"get",key:"_hours",value:function _hours(){var _this$data;return (_this$data=this.data)!==null&&_this$data!==void 0&&_this$data.hours?Number(this.data.hours):0;}},{kind:"get",key:"_minutes",value:function _minutes(){var _this$data2;return (_this$data2=this.data)!==null&&_this$data2!==void 0&&_this$data2.minutes?Number(this.data.minutes):0;}},{kind:"get",key:"_seconds",value:function _seconds(){var _this$data3;return (_this$data3=this.data)!==null&&_this$data3!==void 0&&_this$data3.seconds?Number(this.data.seconds):0;}},{kind:"get",key:"_milliseconds",value:function _milliseconds(){var _this$data4;return (_this$data4=this.data)!==null&&_this$data4!==void 0&&_this$data4.milliseconds?Number(this.data.milliseconds):0;}},{kind:"method",key:"_durationChanged",value:function _durationChanged(ev){ev.stopPropagation();const value={...ev.detail.value};if(!this.enableMillisecond&&!value.milliseconds){// @ts-ignore
delete value.milliseconds;}else if(value.milliseconds>999){value.seconds+=Math.floor(value.milliseconds/1000);value.milliseconds%=1000;}if(value.seconds>59){value.minutes+=Math.floor(value.seconds/60);value.seconds%=60;}if(value.minutes>59){value.hours+=Math.floor(value.minutes/60);value.minutes%=60;}fireEvent(this,"value-changed",{value});}}]};},s);

_decorate([n("ha-form-positive_time_period_dict")],function(_initialize,_LitElement){class HaFormTimePeriod extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormTimePeriod,d:[{kind:"field",decorators:[e()],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[i("ha-time-input",true)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){return $`
      <ha-duration-input
        .label=${this.label}
        .required=${this.schema.required}
        .data=${this.data}
        .disabled=${this.disabled}
      ></ha-duration-input>
    `;}}]};},s);

/**
 * @license
 * Copyright 2020 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */ // Style preference for leading underscores.
// tslint:disable:strip-private-property-underscore
/**
 * Unique symbol for marking roots
 */const selectionController=Symbol('selection controller');/**
 * Set of checkable elements with added metadata
 */class SingleSelectionSet{constructor(){this.selected=null;this.ordered=null;this.set=new Set();}}/**
 * Controller that provides behavior similar to a native `<input type="radio">`
 * group.
 *
 * Behaviors:
 *
 * - Selection via key navigation (currently LTR is supported)
 * - Deselection of other grouped, checkable controls upon selection
 * - Grouping of checkable elements by name
 *   - Defaults grouping scope to host shadow root
 *   - Document-wide scoping enabled
 * - Land focus only on checked element. Focuses leading element when none
 *   checked.
 *
 * Intended Usage:
 *
 * ```ts
 * class MyElement extends HTMLElement {
 *   private selectionController: SingleSelectionController | null = null;
 *   name = "";
 *   global = false;
 *
 *   private _checked = false;
 *   set checked(checked: boolean) {
 *     const oldVal = this._checked;
 *     if (checked === oldVal) return;
 *
 *     this._checked = checked;
 *
 *     if (this.selectionController) {
 *       this.selectionController.update(this)
 *     }
 *   }
 *
 *   get checked() {
 *     return this._checked;
 *   }
 *
 *   connectedCallback() {
 *     this.selectionController = SelectionController.getController(this);
 *     this.selectionController.register(this);
 *     this.selectionController.update(this);
 *   }
 *
 *   disconnectedCallback() {
 *     this.selectionController!.unregister(this);
 *     this.selectionController = null;
 *   }
 * }
 * ```
 */class SingleSelectionController{constructor(element){this.sets={};this.focusedSet=null;this.mouseIsDown=false;this.updating=false;element.addEventListener('keydown',e=>{this.keyDownHandler(e);});element.addEventListener('mousedown',()=>{this.mousedownHandler();});element.addEventListener('mouseup',()=>{this.mouseupHandler();});}/**
     * Get a controller for the given element. If no controller exists, one will
     * be created. Defaults to getting the controller scoped to the element's root
     * node shadow root unless `element.global` is true. Then, it will get a
     * `window.document`-scoped controller.
     *
     * @param element Element from which to get / create a SelectionController. If
     *     `element.global` is true, it gets a selection controller scoped to
     *     `window.document`.
     */static getController(element){const useGlobal=!('global'in element)||'global'in element&&element.global;const root=useGlobal?document:element.getRootNode();let controller=root[selectionController];if(controller===undefined){controller=new SingleSelectionController(root);root[selectionController]=controller;}return controller;}keyDownHandler(e){const element=e.target;if(!('checked'in element)){return;}if(!this.has(element)){return;}if(e.key=='ArrowRight'||e.key=='ArrowDown'){this.selectNext(element);}else if(e.key=='ArrowLeft'||e.key=='ArrowUp'){this.selectPrevious(element);}}mousedownHandler(){this.mouseIsDown=true;}mouseupHandler(){this.mouseIsDown=false;}/**
     * Whether or not the controller controls  the given element.
     *
     * @param element element to check
     */has(element){const set=this.getSet(element.name);return set.set.has(element);}/**
     * Selects and returns the controlled element previous to the given element in
     * document position order. See
     * [Node.compareDocumentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Node/compareDocumentPosition).
     *
     * @param element element relative from which preceding element is fetched
     */selectPrevious(element){const order=this.getOrdered(element);const i=order.indexOf(element);const previous=order[i-1]||order[order.length-1];this.select(previous);return previous;}/**
     * Selects and returns the controlled element next to the given element in
     * document position order. See
     * [Node.compareDocumentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Node/compareDocumentPosition).
     *
     * @param element element relative from which following element is fetched
     */selectNext(element){const order=this.getOrdered(element);const i=order.indexOf(element);const next=order[i+1]||order[0];this.select(next);return next;}select(element){element.click();}/**
     * Focuses the selected element in the given element's selection set. User's
     * mouse selection will override this focus.
     *
     * @param element Element from which selection set is derived and subsequently
     *     focused.
     * @deprecated update() method now handles focus management by setting
     *     appropriate tabindex to form element.
     */focus(element){// Only manage focus state when using keyboard
if(this.mouseIsDown){return;}const set=this.getSet(element.name);const currentFocusedSet=this.focusedSet;this.focusedSet=set;if(currentFocusedSet!=set&&set.selected&&set.selected!=element){set.selected.focus();}}/**
     * @return Returns true if atleast one radio is selected in the radio group.
     */isAnySelected(element){const set=this.getSet(element.name);for(const e of set.set){if(e.checked){return true;}}return false;}/**
     * Returns the elements in the given element's selection set in document
     * position order.
     * [Node.compareDocumentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Node/compareDocumentPosition).
     *
     * @param element Element from which selection set is derived and subsequently
     *     ordered.
     */getOrdered(element){const set=this.getSet(element.name);if(!set.ordered){set.ordered=Array.from(set.set);set.ordered.sort((a,b)=>a.compareDocumentPosition(b)==Node.DOCUMENT_POSITION_PRECEDING?1:0);}return set.ordered;}/**
     * Gets the selection set of the given name and creates one if it does not yet
     * exist.
     *
     * @param name Name of set
     */getSet(name){if(!this.sets[name]){this.sets[name]=new SingleSelectionSet();}return this.sets[name];}/**
     * Register the element in the selection controller.
     *
     * @param element Element to register. Registers in set of `element.name`.
     */register(element){// TODO(b/168546148): Remove accessing 'name' via getAttribute() when new
// base class is created without single selection controller. Component
// maybe booted up after it is connected to DOM in which case properties
// (including `name`) are not updated yet.
const name=element.name||element.getAttribute('name')||'';const set=this.getSet(name);set.set.add(element);set.ordered=null;}/**
     * Unregister the element from selection controller.
     *
     * @param element Element to register. Registers in set of `element.name`.
     */unregister(element){const set=this.getSet(element.name);set.set.delete(element);set.ordered=null;if(set.selected==element){set.selected=null;}}/**
     * Unselects other elements in element's set if element is checked. Noop
     * otherwise.
     *
     * @param element Element from which to calculate selection controller update.
     */update(element){if(this.updating){return;}this.updating=true;const set=this.getSet(element.name);if(element.checked){for(const e of set.set){if(e==element){continue;}e.checked=false;}set.selected=element;}// When tabbing through land focus on the checked radio in the group.
if(this.isAnySelected(element)){for(const e of set.set){if(e.formElementTabIndex===undefined){break;}e.formElementTabIndex=e.checked?0:-1;}}this.updating=false;}}

/**
 * @license
 * Copyright 2016 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */var strings={NATIVE_CONTROL_SELECTOR:'.mdc-radio__native-control'};var cssClasses={DISABLED:'mdc-radio--disabled',ROOT:'mdc-radio'};

var MDCRadioFoundation=/** @class */function(_super){__extends(MDCRadioFoundation,_super);function MDCRadioFoundation(adapter){return _super.call(this,__assign(__assign({},MDCRadioFoundation.defaultAdapter),adapter))||this;}Object.defineProperty(MDCRadioFoundation,"cssClasses",{get:function(){return cssClasses;},enumerable:false,configurable:true});Object.defineProperty(MDCRadioFoundation,"strings",{get:function(){return strings;},enumerable:false,configurable:true});Object.defineProperty(MDCRadioFoundation,"defaultAdapter",{get:function(){return {addClass:function(){return undefined;},removeClass:function(){return undefined;},setNativeControlDisabled:function(){return undefined;}};},enumerable:false,configurable:true});MDCRadioFoundation.prototype.setDisabled=function(disabled){var DISABLED=MDCRadioFoundation.cssClasses.DISABLED;this.adapter.setNativeControlDisabled(disabled);if(disabled){this.adapter.addClass(DISABLED);}else {this.adapter.removeClass(DISABLED);}};return MDCRadioFoundation;}(MDCFoundation);var MDCRadioFoundation$1 = MDCRadioFoundation;

/**
 * @fires checked
 * @soyCompatible
 */class RadioBase extends FormElement{constructor(){super(...arguments);this._checked=false;this.useStateLayerCustomProperties=false;this.global=false;this.disabled=false;this.value='on';this.name='';/**
         * Touch target extends beyond visual boundary of a component by default.
         * Set to `true` to remove touch target added to the component.
         * @see https://material.io/design/usability/accessibility.html
         */this.reducedTouchTarget=false;this.mdcFoundationClass=MDCRadioFoundation$1;/**
         * input's tabindex is updated based on checked status.
         * Tab navigation will be removed from unchecked radios.
         */this.formElementTabIndex=0;this.focused=false;this.shouldRenderRipple=false;this.rippleElement=null;this.rippleHandlers=new RippleHandlers(()=>{this.shouldRenderRipple=true;this.ripple.then(v=>{this.rippleElement=v;});return this.ripple;});}get checked(){return this._checked;}/**
     * We define our own getter/setter for `checked` because we need to track
     * changes to it synchronously.
     *
     * The order in which the `checked` property is set across radio buttons
     * within the same group is very important. However, we can't rely on
     * UpdatingElement's `updated` callback to observe these changes (which is
     * also what the `@observer` decorator uses), because it batches changes to
     * all properties.
     *
     * Consider:
     *
     *   radio1.disabled = true;
     *   radio2.checked = true;
     *   radio1.checked = true;
     *
     * In this case we'd first see all changes for radio1, and then for radio2,
     * and we couldn't tell that radio1 was the most recently checked.
     */set checked(isChecked){var _a,_b;const oldValue=this._checked;if(isChecked===oldValue){return;}this._checked=isChecked;if(this.formElement){this.formElement.checked=isChecked;}(_a=this._selectionController)===null||_a===void 0?void 0:_a.update(this);if(isChecked===false){// Remove focus ring when unchecked on other radio programmatically.
// Blur on input since this determines the focus style.
(_b=this.formElement)===null||_b===void 0?void 0:_b.blur();}this.requestUpdate('checked',oldValue);// useful when unchecks self and wrapping element needs to synchronize
// TODO(b/168543810): Remove triggering event on programmatic API call.
this.dispatchEvent(new Event('checked',{bubbles:true,composed:true}));}_handleUpdatedValue(newValue){// the observer function can't access protected fields (according to
// closure compiler) because it's not a method on the class, so we need this
// wrapper.
this.formElement.value=newValue;}/** @soyTemplate */renderRipple(){return this.shouldRenderRipple?$`<mwc-ripple unbounded accent
        .internalUseStateLayerCustomProperties="${this.useStateLayerCustomProperties}"
        .disabled="${this.disabled}"></mwc-ripple>`:'';}get isRippleActive(){var _a;return ((_a=this.rippleElement)===null||_a===void 0?void 0:_a.isActive)||false;}connectedCallback(){super.connectedCallback();// Note that we must defer creating the selection controller until the
// element has connected, because selection controllers are keyed by the
// radio's shadow root. For example, if we're stamping in a lit map
// or repeat, then we'll be constructed before we're added to a root node.
//
// Also note if we aren't using native shadow DOM, we still need a
// SelectionController, because we should update checked status of other
// radios in the group when selection changes. It also simplifies
// implementation and testing to use one in all cases.
//
// eslint-disable-next-line @typescript-eslint/no-use-before-define
this._selectionController=SingleSelectionController.getController(this);this._selectionController.register(this);// Radios maybe checked before connected, update selection as soon it is
// connected to DOM. Last checked radio button in the DOM will be selected.
//
// NOTE: If we update selection only after firstUpdate() we might mistakenly
// update checked status before other radios are rendered.
this._selectionController.update(this);}disconnectedCallback(){// The controller is initialized in connectedCallback, so if we are in
// disconnectedCallback then it must be initialized.
// eslint-disable-next-line @typescript-eslint/no-non-null-assertion
this._selectionController.unregister(this);this._selectionController=undefined;}focus(){this.formElement.focus();}createAdapter(){return Object.assign(Object.assign({},addHasRemoveClass(this.mdcRoot)),{setNativeControlDisabled:disabled=>{this.formElement.disabled=disabled;}});}handleFocus(){this.focused=true;this.handleRippleFocus();}handleClick(){// Firefox has weird behavior with radios if they are not focused
this.formElement.focus();}handleBlur(){this.focused=false;this.formElement.blur();this.rippleHandlers.endFocus();}setFormData(formData){if(this.name&&this.checked){formData.append(this.name,this.value);}}/**
     * @soyTemplate
     * @soyAttributes radioAttributes: input
     * @soyClasses radioClasses: .mdc-radio
     */render(){/** @classMap */const classes={'mdc-radio--touch':!this.reducedTouchTarget,'mdc-ripple-upgraded--background-focused':this.focused,'mdc-radio--disabled':this.disabled};return $`
      <div class="mdc-radio ${o(classes)}">
        <input
          tabindex="${this.formElementTabIndex}"
          class="mdc-radio__native-control"
          type="radio"
          name="${this.name}"
          aria-label="${l(this.ariaLabel)}"
          aria-labelledby="${l(this.ariaLabelledBy)}"
          .checked="${this.checked}"
          .value="${this.value}"
          ?disabled="${this.disabled}"
          @change="${this.changeHandler}"
          @focus="${this.handleFocus}"
          @click="${this.handleClick}"
          @blur="${this.handleBlur}"
          @mousedown="${this.handleRippleMouseDown}"
          @mouseenter="${this.handleRippleMouseEnter}"
          @mouseleave="${this.handleRippleMouseLeave}"
          @touchstart="${this.handleRippleTouchStart}"
          @touchend="${this.handleRippleDeactivate}"
          @touchcancel="${this.handleRippleDeactivate}">
        <div class="mdc-radio__background">
          <div class="mdc-radio__outer-circle"></div>
          <div class="mdc-radio__inner-circle"></div>
        </div>
        ${this.renderRipple()}
      </div>`;}handleRippleMouseDown(event){const onUp=()=>{window.removeEventListener('mouseup',onUp);this.handleRippleDeactivate();};window.addEventListener('mouseup',onUp);this.rippleHandlers.startPress(event);}handleRippleTouchStart(event){this.rippleHandlers.startPress(event);}handleRippleDeactivate(){this.rippleHandlers.endPress();}handleRippleMouseEnter(){this.rippleHandlers.startHover();}handleRippleMouseLeave(){this.rippleHandlers.endHover();}handleRippleFocus(){this.rippleHandlers.startFocus();}changeHandler(){this.checked=this.formElement.checked;}}__decorate([i('.mdc-radio')],RadioBase.prototype,"mdcRoot",void 0);__decorate([i('input')],RadioBase.prototype,"formElement",void 0);__decorate([t()],RadioBase.prototype,"useStateLayerCustomProperties",void 0);__decorate([e({type:Boolean})],RadioBase.prototype,"global",void 0);__decorate([e({type:Boolean,reflect:true})],RadioBase.prototype,"checked",null);__decorate([e({type:Boolean}),observer(function(disabled){this.mdcFoundation.setDisabled(disabled);})],RadioBase.prototype,"disabled",void 0);__decorate([e({type:String}),observer(function(value){this._handleUpdatedValue(value);})],RadioBase.prototype,"value",void 0);__decorate([e({type:String})],RadioBase.prototype,"name",void 0);__decorate([e({type:Boolean})],RadioBase.prototype,"reducedTouchTarget",void 0);__decorate([e({type:Number})],RadioBase.prototype,"formElementTabIndex",void 0);__decorate([t()],RadioBase.prototype,"focused",void 0);__decorate([t()],RadioBase.prototype,"shouldRenderRipple",void 0);__decorate([e$1('mwc-ripple')],RadioBase.prototype,"ripple",void 0);__decorate([ariaProperty,e({attribute:'aria-label'})],RadioBase.prototype,"ariaLabel",void 0);__decorate([ariaProperty,e({attribute:'aria-labelledby'})],RadioBase.prototype,"ariaLabelledBy",void 0);__decorate([e$2({passive:true})],RadioBase.prototype,"handleRippleTouchStart",null);

const styles=r`.mdc-touch-target-wrapper{display:inline}.mdc-radio{padding:calc((40px - 20px) / 2)}.mdc-radio .mdc-radio__native-control:enabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.54)}.mdc-radio .mdc-radio__native-control:enabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-radio .mdc-radio__native-control:enabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio .mdc-radio__background::before{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786)}.mdc-radio .mdc-radio__background::before{top:calc(-1 * (40px - 20px) / 2);left:calc(-1 * (40px - 20px) / 2);width:40px;height:40px}.mdc-radio .mdc-radio__native-control{top:calc((40px - 40px) / 2);right:calc((40px - 40px) / 2);left:calc((40px - 40px) / 2);width:40px;height:40px}@media screen and (forced-colors: active),(-ms-high-contrast: active){.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:GrayText}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:GrayText}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:GrayText}}.mdc-radio{display:inline-block;position:relative;flex:0 0 auto;box-sizing:content-box;width:20px;height:20px;cursor:pointer;will-change:opacity,transform,border-color,color}.mdc-radio__background{display:inline-block;position:relative;box-sizing:border-box;width:20px;height:20px}.mdc-radio__background::before{position:absolute;transform:scale(0, 0);border-radius:50%;opacity:0;pointer-events:none;content:"";transition:opacity 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1),transform 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__outer-circle{position:absolute;top:0;left:0;box-sizing:border-box;width:100%;height:100%;border-width:2px;border-style:solid;border-radius:50%;transition:border-color 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__inner-circle{position:absolute;top:0;left:0;box-sizing:border-box;width:100%;height:100%;transform:scale(0, 0);border-width:10px;border-style:solid;border-radius:50%;transition:transform 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1),border-color 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__native-control{position:absolute;margin:0;padding:0;opacity:0;cursor:inherit;z-index:1}.mdc-radio--touch{margin-top:4px;margin-bottom:4px;margin-right:4px;margin-left:4px}.mdc-radio--touch .mdc-radio__native-control{top:calc((40px - 48px) / 2);right:calc((40px - 48px) / 2);left:calc((40px - 48px) / 2);width:48px;height:48px}.mdc-radio__native-control:checked+.mdc-radio__background,.mdc-radio__native-control:disabled+.mdc-radio__background{transition:opacity 120ms 0ms cubic-bezier(0, 0, 0.2, 1),transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__outer-circle{transition:border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{transition:transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1),border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio--disabled{cursor:default;pointer-events:none}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__inner-circle{transform:scale(0.5);transition:transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1),border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:disabled+.mdc-radio__background,[aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background{cursor:default}.mdc-radio__native-control:focus+.mdc-radio__background::before{transform:scale(1);opacity:.12;transition:opacity 120ms 0ms cubic-bezier(0, 0, 0.2, 1),transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}:host{display:inline-block;outline:none}.mdc-radio{vertical-align:bottom}.mdc-radio .mdc-radio__native-control:enabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-unchecked-color, rgba(0, 0, 0, 0.54))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}`;

_decorate([n("ha-radio")],function(_initialize,_RadioBase){class HaRadio extends _RadioBase{constructor(...args){super(...args);_initialize(this);}}return {F:HaRadio,d:[{kind:"field",static:true,key:"styles",value(){return [styles,r`
      :host {
        --mdc-radio-unchecked-color: var(--primary-text-color);
        --mdc-theme-secondary: var(--primary-text-color);
      }
    `];}}]};},RadioBase);

_decorate([n("ha-form-select")],function(_initialize,_LitElement){class HaFormSelect extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormSelect,d:[{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[i("ha-select",true)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){if(this.schema.required&&this.schema.options.length<6){return $`
        <div>
          ${this.label}
          ${this.schema.options.map(([value,label])=>$`
              <mwc-formfield .label=${label}>
                <ha-radio
                  .checked=${value===this.data}
                  .value=${value}
                  .disabled=${this.disabled}
                  @change=${this._valueChanged}
                ></ha-radio>
              </mwc-formfield>
            `)}
        </div>
      `;}return $`
      <ha-select
        fixedMenuPosition
        naturalMenuWidth
        .label=${this.label}
        .value=${this.data}
        .disabled=${this.disabled}
        @closed=${stopPropagation}
        @selected=${this._valueChanged}
      >
        ${!this.schema.required?$`<mwc-list-item value=""></mwc-list-item>`:""}
        ${this.schema.options.map(([value,label])=>$`
            <mwc-list-item .value=${value}>${label}</mwc-list-item>
          `)}
      </ha-select>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){ev.stopPropagation();let value=ev.target.value;if(value===this.data){return;}if(value===""){value=undefined;}fireEvent(this,"value-changed",{value});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-select,
      mwc-formfield {
        display: block;
      }
    `;}}]};},s);

const MASKED_FIELDS=["password","secret","token"];_decorate([n("ha-form-string")],function(_initialize,_LitElement){class HaFormString extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaFormString,d:[{kind:"field",decorators:[e()],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"data",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[t()],key:"_unmaskedPassword",value(){return false;}},{kind:"field",decorators:[i("ha-textfield")],key:"_input",value:void 0},{kind:"method",key:"focus",value:function focus(){if(this._input){this._input.focus();}}},{kind:"method",key:"render",value:function render(){var _this$schema$descript;const isPassword=MASKED_FIELDS.some(field=>this.schema.name.includes(field));return $`
      <ha-textfield
        .type=${!isPassword?this._stringType:this._unmaskedPassword?"text":"password"}
        .label=${this.label}
        .value=${this.data||""}
        .disabled=${this.disabled}
        .required=${this.schema.required}
        .autoValidate=${this.schema.required}
        .suffix=${isPassword?// reserve some space for the icon.
$`<div style="width: 24px"></div>`:(_this$schema$descript=this.schema.description)===null||_this$schema$descript===void 0?void 0:_this$schema$descript.suffix}
        .validationMessage=${this.schema.required?"Required":undefined}
        @input=${this._valueChanged}
      ></ha-textfield>
      ${isPassword?$`<ha-icon-button
            toggles
            .label=${`${this._unmaskedPassword?"Hide":"Show"} password`}
            @click=${this._toggleUnmaskedPassword}
            .path=${this._unmaskedPassword?mdiEyeOff:mdiEye}
          ></ha-icon-button>`:""}
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){if(changedProps.has("schema")){this.toggleAttribute("own-margin",!!this.schema.required);}}},{kind:"method",key:"_toggleUnmaskedPassword",value:function _toggleUnmaskedPassword(){this._unmaskedPassword=!this._unmaskedPassword;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){let value=ev.target.value;if(this.data===value){return;}if(value===""&&!this.schema.required){value=undefined;}fireEvent(this,"value-changed",{value});}},{kind:"get",key:"_stringType",value:function _stringType(){if(this.schema.format){if(["email","url"].includes(this.schema.format)){return this.schema.format;}if(this.schema.format==="fqdnurl"){return "url";}}return "text";}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
        position: relative;
      }
      :host([own-margin]) {
        margin-bottom: 5px;
      }
      ha-textfield {
        display: block;
      }
      ha-icon-button {
        position: absolute;
        top: 1em;
        right: 12px;
        --mdc-icon-button-size: 24px;
        color: var(--secondary-text-color);
      }
    `;}}]};},s);

const getValue=(obj,item)=>obj?!item.name?obj:obj[item.name]:null;const getError=(obj,item)=>obj&&item.name?obj[item.name]:null;let selectorImported=false;_decorate([n("ha-form")],function(_initialize,_LitElement){class HaForm extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaForm,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"data",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e()],key:"error",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[e()],key:"computeError",value:void 0},{kind:"field",decorators:[e()],key:"computeLabel",value:void 0},{kind:"field",decorators:[e()],key:"computeHelper",value:void 0},{kind:"method",key:"focus",value:function focus(){var _this$shadowRoot;const root=(_this$shadowRoot=this.shadowRoot)===null||_this$shadowRoot===void 0?void 0:_this$shadowRoot.querySelector(".root");if(!root){return;}for(const child of root.children){if(child.tagName!=="HA-ALERT"){child.focus();break;}}}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProperties){var _this$schema;_get(_getPrototypeOf(HaForm.prototype),"willUpdate",this).call(this,changedProperties);if(!selectorImported&&changedProperties.has("schema")&&(_this$schema=this.schema)!==null&&_this$schema!==void 0&&_this$schema.some(item=>"selector"in item)){selectorImported=true;import('./ha-selector-dev.js');}}},{kind:"method",key:"render",value:function render(){return $`
      <div class="root">
        ${this.error&&this.error.base?$`
              <ha-alert alert-type="error">
                ${this._computeError(this.error.base,this.schema)}
              </ha-alert>
            `:""}
        ${this.schema.map(item=>{const error=getError(this.error,item);return $`
            ${error?$`
                  <ha-alert own-margin alert-type="error">
                    ${this._computeError(error,item)}
                  </ha-alert>
                `:""}
            ${"selector"in item?$`<ha-selector
                  .schema=${item}
                  .hass=${this.hass}
                  .selector=${item.selector}
                  .value=${getValue(this.data,item)}
                  .label=${this._computeLabel(item,this.data)}
                  .disabled=${this.disabled}
                  .helper=${this._computeHelper(item)}
                  .required=${item.required||false}
                ></ha-selector>`:dynamicElement(`ha-form-${item.type}`,{schema:item,data:getValue(this.data,item),label:this._computeLabel(item,this.data),disabled:this.disabled,hass:this.hass,computeLabel:this.computeLabel,computeHelper:this.computeHelper})}
          `;})}
      </div>
    `;}},{kind:"method",key:"createRenderRoot",value:function createRenderRoot(){const root=_get(_getPrototypeOf(HaForm.prototype),"createRenderRoot",this).call(this);// attach it as soon as possible to make sure we fetch all events.
root.addEventListener("value-changed",ev=>{ev.stopPropagation();const schema=ev.target.schema;const newValue=!schema.name?ev.detail.value:{[schema.name]:ev.detail.value};// console.log("new-value", newValue);
fireEvent(this,"value-changed",{value:{...this.data,...newValue}});});return root;}},{kind:"method",key:"_computeLabel",value:function _computeLabel(schema,data){// console.log("compute SCHEMA", schema);
// console.log("compute data", data);
// console.log("compute data.name", schema.name);
return this.computeLabel?this.computeLabel(schema,data):schema?schema.name:"";}},{kind:"method",key:"_computeHelper",value:function _computeHelper(schema){return this.computeHelper?this.computeHelper(schema):"";}},{kind:"method",key:"_computeError",value:function _computeError(error,schema){return this.computeError?this.computeError(error,schema):error;}},{kind:"get",static:true,key:"styles",value:function styles(){// .root has overflow: auto to avoid margin collapse
return r`
      .root {
        margin-bottom: -24px;
        overflow: clip visible;
        /* border-radius: 1.5rem; */
      }
      .root > * {
        display: block;
      }
      .root > *:not([own-margin]) {
        margin-bottom: 15px;
      }
      ha-alert[own-margin] {
        margin-bottom: 10px;
      }
    `;}}]};},s);
