import{_ as i,c as t,d as e,$ as o,Q as n,z as a,r as s,n as c}from"./main-d07cb663.js";import{Q as r,R as d,T as h}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";let l=i([c("hui-picture-header-footer")],(function(i,t){return{F:class extends t{constructor(...t){super(...t),i(this)}},d:[{kind:"method",static:!0,key:"getStubConfig",value:function(){return{image:"https://www.home-assistant.io/images/lovelace/header-footer/balloons-header.png",tap_action:{action:"none"},hold_action:{action:"none"}}}},{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"type",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(i){if(!i||!i.image)throw new Error("Image required");this._config=i}},{kind:"method",key:"shouldUpdate",value:function(i){return 1!==i.size||!i.has("hass")||!i.get("hass")}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return o``;const i=Boolean(this._config.tap_action||this._config.hold_action);return o`
      <img
        @action=${this._handleAction}
        .actionHandler=${r({hasHold:d(this._config.hold_action),hasDoubleClick:d(this._config.double_tap_action)})}
        tabindex=${n(i?0:void 0)}
        class=${a({clickable:i})}
        src=${this.hass.hassUrl(this._config.image)}
      />
    `}},{kind:"get",static:!0,key:"styles",value:function(){return s`
      img.clickable {
        cursor: pointer;
      }

      img {
        display: block;
        width: 100%;
      }
    `}},{kind:"method",key:"_handleAction",value:function(i){h(this,this.hass,this._config,i.detail.action)}}]}}),t);export{l as HuiPictureHeaderFooter};
