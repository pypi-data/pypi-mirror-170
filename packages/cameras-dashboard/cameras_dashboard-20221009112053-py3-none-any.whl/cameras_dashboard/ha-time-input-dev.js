const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, f as fireEvent, n } from './main-dev.js';
import { u as useAmPm } from './auth-dev.js';
import './ha-base-time-input-dev.js';

_decorate([n("ha-time-input")],function(_initialize,_LitElement){class HaTimeInput extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaTimeInput,d:[{kind:"field",decorators:[e({attribute:false})],key:"locale",value:void 0},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[e({type:Boolean,attribute:"enable-second"})],key:"enableSecond",value(){return false;}},{kind:"method",key:"render",value:function render(){var _this$value;const useAMPM=useAmPm(this.locale);const parts=((_this$value=this.value)===null||_this$value===void 0?void 0:_this$value.split(":"))||[];let hours=parts[0];const numberHours=Number(parts[0]);if(numberHours&&useAMPM&&numberHours>12&&numberHours<24){hours=String(numberHours-12).padStart(2,"0");}if(useAMPM&&numberHours===0){hours="12";}return $`
      <ha-base-time-input
        .label=${this.label}
        .hours=${Number(hours)}
        .minutes=${Number(parts[1])}
        .seconds=${Number(parts[2])}
        .format=${useAMPM?12:24}
        .amPm=${useAMPM&&(numberHours>=12?"PM":"AM")}
        .disabled=${this.disabled}
        @value-changed=${this._timeChanged}
        .enableSecond=${this.enableSecond}
      ></ha-base-time-input>
    `;}},{kind:"method",key:"_timeChanged",value:function _timeChanged(ev){ev.stopPropagation();const eventValue=ev.detail.value;const useAMPM=useAmPm(this.locale);let hours=eventValue.hours||0;if(eventValue&&useAMPM){if(eventValue.amPm==="PM"&&hours<12){hours+=12;}if(eventValue.amPm==="AM"&&hours===12){hours=0;}}const value=`${hours.toString().padStart(2,"0")}:${eventValue.minutes?eventValue.minutes.toString().padStart(2,"0"):"00"}:${eventValue.seconds?eventValue.seconds.toString().padStart(2,"0"):"00"}`;if(value===this.value){return;}this.value=value;fireEvent(this,"change");fireEvent(this,"value-changed",{value});}}]};},s);
