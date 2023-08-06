import{_ as a,c as t,d as e,$ as i,aI as l,f as s,r as o,n as d}from"./main-d07cb663.js";import{ae as n}from"./c.fc0bbf07.js";const r=()=>import("./c.980a8c16.js");a([d("ha-date-input")],(function(a,t){return{F:class extends t{constructor(...t){super(...t),a(this)}},d:[{kind:"field",decorators:[e({attribute:!1})],key:"locale",value:void 0},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"method",key:"render",value:function(){return i`<ha-textfield
      .label=${this.label}
      .disabled=${this.disabled}
      iconTrailing
      @click=${this._openDialog}
      .value=${this.value?n(new Date(this.value),this.locale):""}
    >
      <ha-svg-icon slot="trailingIcon" .path=${l}></ha-svg-icon>
    </ha-textfield>`}},{kind:"method",key:"_openDialog",value:function(){var a,t;this.disabled||(a=this,t={min:"1970-01-01",value:this.value,onChange:a=>this._valueChanged(a),locale:this.locale.language},s(a,"show-dialog",{dialogTag:"ha-dialog-date-picker",dialogImport:r,dialogParams:t}))}},{kind:"method",key:"_valueChanged",value:function(a){this.value!==a&&(this.value=a,s(this,"change"),s(this,"value-changed",{value:a}))}},{kind:"get",static:!0,key:"styles",value:function(){return o`
      ha-svg-icon {
        color: var(--secondary-text-color);
      }
    `}}]}}),t);const c=a=>`${a.attributes.year||"1970"}-${String(a.attributes.month||"01").padStart(2,"0")}-${String(a.attributes.day||"01").padStart(2,"0")}T${String(a.attributes.hour||"00").padStart(2,"0")}:${String(a.attributes.minute||"00").padStart(2,"0")}:${String(a.attributes.second||"00").padStart(2,"0")}`,u=(a,t,e,i)=>{const l={entity_id:t,time:e,date:i};a.callService(t.split(".",1)[0],"set_datetime",l)};export{u as a,c as s};
