const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, aI as mdiCalendar, f as fireEvent, r, n } from './main-dev.js';
import { ae as formatDateNumeric } from './auth-dev.js';

const loadDatePickerDialog=()=>import('./ha-dialog-date-picker-dev.js');const showDatePickerDialog=(element,dialogParams)=>{fireEvent(element,"show-dialog",{dialogTag:"ha-dialog-date-picker",dialogImport:loadDatePickerDialog,dialogParams});};_decorate([n("ha-date-input")],function(_initialize,_LitElement){class HaDateInput extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaDateInput,d:[{kind:"field",decorators:[e({attribute:false})],key:"locale",value:void 0},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"method",key:"render",value:function render(){return $`<ha-textfield
      .label=${this.label}
      .disabled=${this.disabled}
      iconTrailing
      @click=${this._openDialog}
      .value=${this.value?formatDateNumeric(new Date(this.value),this.locale):""}
    >
      <ha-svg-icon slot="trailingIcon" .path=${mdiCalendar}></ha-svg-icon>
    </ha-textfield>`;}},{kind:"method",key:"_openDialog",value:function _openDialog(){if(this.disabled){return;}showDatePickerDialog(this,{min:"1970-01-01",value:this.value,onChange:value=>this._valueChanged(value),locale:this.locale.language});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(value){if(this.value!==value){this.value=value;fireEvent(this,"change");fireEvent(this,"value-changed",{value});}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-svg-icon {
        color: var(--secondary-text-color);
      }
    `;}}]};},s);

const stateToIsoDateString=entityState=>`${entityState.attributes.year||"1970"}-${String(entityState.attributes.month||"01").padStart(2,"0")}-${String(entityState.attributes.day||"01").padStart(2,"0")}T${String(entityState.attributes.hour||"00").padStart(2,"0")}:${String(entityState.attributes.minute||"00").padStart(2,"0")}:${String(entityState.attributes.second||"00").padStart(2,"0")}`;const setInputDateTimeValue=(hass,entityId,time=undefined,date=undefined)=>{const param={entity_id:entityId,time,date};hass.callService(entityId.split(".",1)[0],"set_datetime",param);};

export { setInputDateTimeValue as a, stateToIsoDateString as s };
