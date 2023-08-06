import{_ as e,c as t,d as a,$ as i,f as o,n}from"./main-d07cb663.js";import{u as s}from"./c.fc0bbf07.js";import"./c.379373ef.js";e([n("ha-time-input")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[a({attribute:!1})],key:"locale",value:void 0},{kind:"field",decorators:[a()],key:"value",value:void 0},{kind:"field",decorators:[a()],key:"label",value:void 0},{kind:"field",decorators:[a({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[a({type:Boolean,attribute:"enable-second"})],key:"enableSecond",value:()=>!1},{kind:"method",key:"render",value:function(){var e;const t=s(this.locale),a=(null===(e=this.value)||void 0===e?void 0:e.split(":"))||[];let o=a[0];const n=Number(a[0]);return n&&t&&n>12&&n<24&&(o=String(n-12).padStart(2,"0")),t&&0===n&&(o="12"),i`
      <ha-base-time-input
        .label=${this.label}
        .hours=${Number(o)}
        .minutes=${Number(a[1])}
        .seconds=${Number(a[2])}
        .format=${t?12:24}
        .amPm=${t&&(n>=12?"PM":"AM")}
        .disabled=${this.disabled}
        @value-changed=${this._timeChanged}
        .enableSecond=${this.enableSecond}
      ></ha-base-time-input>
    `}},{kind:"method",key:"_timeChanged",value:function(e){e.stopPropagation();const t=e.detail.value,a=s(this.locale);let i=t.hours||0;t&&a&&("PM"===t.amPm&&i<12&&(i+=12),"AM"===t.amPm&&12===i&&(i=0));const n=`${i.toString().padStart(2,"0")}:${t.minutes?t.minutes.toString().padStart(2,"0"):"00"}:${t.seconds?t.seconds.toString().padStart(2,"0"):"00"}`;n!==this.value&&(this.value=n,o(this,"change"),o(this,"value-changed",{value:n}))}}]}}),t);
