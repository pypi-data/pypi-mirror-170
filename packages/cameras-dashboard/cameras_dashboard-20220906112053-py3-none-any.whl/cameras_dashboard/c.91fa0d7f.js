import{_ as t,c as i,d as e,$ as s,n as a}from"./main-d07cb663.js";import{s as r}from"./c.fc0bbf07.js";import"./c.37525831.js";import{s as c}from"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([a("more-info-remote")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function(){if(!this.hass||!this.stateObj)return s``;const t=this.stateObj;return s`
      ${r(t,4)?s`
            <mwc-list
              .label=${this.hass.localize("ui.dialogs.more_info_control.remote.activity")}
              .value=${t.attributes.current_activity}
              @selected=${this.handleActivityChanged}
              fixedMenuPosition
              naturalMenuWidth
              @closed=${c}
            >
              ${t.attributes.activity_list.map((t=>s`
                  <mwc-list-item .value=${t}>${t}</mwc-list-item>
                `))}
            </mwc-list>
          `:""}

      <ha-attributes
        .hass=${this.hass}
        .stateObj=${this.stateObj}
        .extraFilters=${"activity_list,current_activity"}
      ></ha-attributes>
    `}},{kind:"method",key:"handleActivityChanged",value:function(t){const i=this.stateObj.attributes.current_activity,e=t.target.value;e&&i!==e&&this.hass.callService("remote","turn_on",{entity_id:this.stateObj.entity_id,activity:e})}}]}}),i);
