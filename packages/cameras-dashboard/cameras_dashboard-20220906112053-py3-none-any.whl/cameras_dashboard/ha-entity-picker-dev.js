const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, b as memoizeOne, $, f as fireEvent, n } from './main-dev.js';
import { j as computeStateName, e as computeDomain } from './auth-dev.js';
import './ha-combo-box-dev.js';

const rowRenderer=item=>$`<mwc-list-item graphic="avatar" .twoline=${!!item.entity_id}>
      ${item.state?$`<state-badge slot="graphic" .stateObj=${item}></state-badge>`:""}
      <span>${item.friendly_name}</span>
      <span slot="secondary">${item.entity_id}</span>
    </mwc-list-item>`;_decorate([n("ha-entity-picker")],function(_initialize,_LitElement){class HaEntityPicker extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaEntityPicker,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"autofocus",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value:void 0},{kind:"field",decorators:[e({type:Boolean,attribute:"allow-custom-entity"})],key:"allowCustomEntity",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-unit-of-measurement"})],key:"includeUnitOfMeasurement",value:void 0},{kind:"field",decorators:[e()],key:"entityFilter",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"hideClearIcon",value(){return false;}},{kind:"field",decorators:[t()],key:"_opened",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"filterBrowserModEntities",value(){return true;}},{kind:"field",decorators:[i("ha-combo-box",true)],key:"comboBox",value:void 0},{kind:"method",key:"open",value:/**
   * Show entities from specific domains.
   * @type {Array}
   * @attr include-domains
   */ /**
   * Show no entities of these domains.
   * @type {Array}
   * @attr exclude-domains
   */ /**
   * Show only entities of these device classes.
   * @type {Array}
   * @attr include-device-classes
   */ /**
   * Show only entities with these unit of measuments.
   * @type {Array}
   * @attr include-unit-of-measurement
   */function open(){this.updateComplete.then(()=>{var _this$comboBox;(_this$comboBox=this.comboBox)===null||_this$comboBox===void 0?void 0:_this$comboBox.open();});}},{kind:"method",key:"focus",value:function focus(){this.updateComplete.then(()=>{var _this$comboBox2;(_this$comboBox2=this.comboBox)===null||_this$comboBox2===void 0?void 0:_this$comboBox2.focus();});}},{kind:"field",key:"_initedStates",value(){return false;}},{kind:"field",key:"_states",value(){return [];}},{kind:"field",key:"_getStates",value(){return memoizeOne((_opened,hass,includeDomains,excludeDomains,entityFilter,includeDeviceClasses,includeUnitOfMeasurement,filterBrowserMod)=>{let states=[];if(!hass){return [];}let entityIds=Object.keys(hass.states);if(!entityIds.length){return [{entity_id:"",state:"",last_changed:"",last_updated:"",context:{id:"",user_id:null},friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_entities"),attributes:{friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_entities"),icon:"mdi:magnify"}}];}if(includeDomains){entityIds=entityIds.filter(eid=>includeDomains.includes(computeDomain(eid)));}if(excludeDomains){entityIds=entityIds.filter(eid=>!excludeDomains.includes(computeDomain(eid)));}states=entityIds.sort().map(key=>({...hass.states[key],friendly_name:computeStateName(hass.states[key])||key}));if(includeDeviceClasses){states=states.filter(stateObj=>// We always want to include the entity of the current value
stateObj.entity_id===this.value||stateObj.attributes.device_class&&includeDeviceClasses.includes(stateObj.attributes.device_class));}if(includeUnitOfMeasurement){states=states.filter(stateObj=>// We always want to include the entity of the current value
stateObj.entity_id===this.value||stateObj.attributes.unit_of_measurement&&includeUnitOfMeasurement.includes(stateObj.attributes.unit_of_measurement));}if(entityFilter){states=states.filter(stateObj=>// We always want to include the entity of the current value
stateObj.entity_id===this.value||entityFilter(stateObj));}// @zroger499 adds a filter to remove browser mod Entities from the cards entity pickers
if(filterBrowserMod){const browserModRegex=/browser_.{8}_.{8}/;states=states.filter(stateObj=>browserModRegex.exec(stateObj.entity_id)===null);}// @zroger499 Filter the automations used in the backend
const backgroundAutomations=["automation.avaiable_wallpaper_update","automation.avaiable_wallpaper_update_on_ha_start","automation.create_dashboard","automation.delete_dashboard","automation.import_a_lovelace_dashboard_to_homekit_infused","automation.populate_view_input_select_after_picking_a_dashboard","automation.run_deepstack_face_identification_time_based","automation.run_deepstack_face_identification_time_based_2","automation.run_deepstack_face_identification_time_based_3","automation.themes","automation.update_dropdown_menu_in_for_dashboards_when_a_dashboard_file_is_created","automation.update_dropdown_menu_in_for_dashboards_when_a_dashboard_file_is_deleted","automation.update_dropdown_menu_in_for_dashboards_when_a_dashboard_file_is_moved","automation.update_dropdown_menu_in_import_dashboard_when_ha_starts","automation.wallpaper_selector"];states=states.filter(stateObj=>!backgroundAutomations.includes(stateObj.entity_id));if(!states.length){return [{entity_id:"",state:"",last_changed:"",last_updated:"",context:{id:"",user_id:null},friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_match"),attributes:{friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_match"),icon:"mdi:magnify"}}];}return states;});}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("value")||changedProps.has("label")||changedProps.has("disabled")){return true;}return !(!changedProps.has("_opened")&&this._opened);}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){if(!this._initedStates||changedProps.has("_opened")&&this._opened){this._states=this._getStates(this._opened,this.hass,this.includeDomains,this.excludeDomains,this.entityFilter,this.includeDeviceClasses,this.includeUnitOfMeasurement,this.filterBrowserModEntities);if(this._initedStates){this.comboBox.filteredItems=this._states;}this._initedStates=true;}}},{kind:"method",key:"render",value:function render(){return $`
      <ha-combo-box
        item-value-path="entity_id"
        item-label-path="friendly_name"
        .hass=${this.hass}
        .value=${this._value}
        .label=${this.label===undefined?this.hass.localize("ui.components.entity.entity-picker.entity"):this.label}
        .allowCustomValue=${this.allowCustomEntity}
        .filteredItems=${this._states}
        .renderer=${rowRenderer}
        @opened-changed=${this._openedChanged}
        @value-changed=${this._valueChanged}
        @filter-changed=${this._filterChanged}
      >
      </ha-combo-box>
    `;}},{kind:"get",key:"_value",value:function _value(){return this.value||"";}},{kind:"method",key:"_openedChanged",value:function _openedChanged(ev){this._opened=ev.detail.value;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){ev.stopPropagation();const newValue=ev.detail.value;if(newValue!==this._value){this._setValue(newValue);}}},{kind:"method",key:"_filterChanged",value:function _filterChanged(ev){const filterString=ev.detail.value.toLowerCase();this.comboBox.filteredItems=this._states.filter(entityState=>entityState.entity_id.toLowerCase().includes(filterString)||computeStateName(entityState).toLowerCase().includes(filterString));if(this.comboBox.filteredItems.length===0){this.comboBox.filteredItems.push({entity_id:"",state:"",last_changed:"",last_updated:"",context:{id:"",user_id:null},friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_match"),attributes:{friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_match"),icon:"mdi:magnify"}});}}},{kind:"method",key:"_setValue",value:function _setValue(value){this.value=value;setTimeout(()=>{fireEvent(this,"value-changed",{value});fireEvent(this,"change");},0);}}]};},s);
