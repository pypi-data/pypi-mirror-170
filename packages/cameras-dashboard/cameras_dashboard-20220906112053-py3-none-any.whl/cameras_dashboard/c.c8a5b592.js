import{_ as t,c as i,d as e,j as o,k as a,S as s,$ as n,Q as c,z as h,r,n as d}from"./main-d07cb663.js";import{Q as l,R as u,T as f}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";let m=t([d("hui-picture-card")],(function(t,i){class d extends i{constructor(...i){super(...i),t(this)}}return{F:d,d:[{kind:"method",static:!0,key:"getConfigElement",value:async function(){return await import("./c.308d250b.js"),document.createElement("hui-picture-card-editor")}},{kind:"method",static:!0,key:"getStubConfig",value:function(){return{type:"picture",image:"/local/logoauto_og.png",tap_action:{action:"none"},hold_action:{action:"none"}}}},{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 5}},{kind:"method",key:"setConfig",value:function(t){if(!t||!t.image)throw new Error("Image required");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return 1!==t.size||!t.has("hass")||!t.get("hass")}},{kind:"method",key:"updated",value:function(t){if(o(a(d.prototype),"updated",this).call(this,t),!this._config||!this.hass)return;const i=t.get("hass"),e=t.get("_config");i&&e&&i.themes===this.hass.themes&&e.theme===this._config.theme||s(this,this.hass.themes,this._config.theme)}},{kind:"method",key:"render",value:function(){return this._config&&this.hass?n`
      <ha-card
        @action=${this._handleAction}
        .actionHandler=${l({hasHold:u(this._config.hold_action),hasDoubleClick:u(this._config.double_tap_action)})}
        tabindex=${c(u(this._config.tap_action)?"0":void 0)}
        class=${h({clickable:Boolean(this._config.tap_action||this._config.hold_action||this._config.double_tap_action)})}
      >
        <img src=${this.hass.hassUrl(this._config.image)} />
      </ha-card>
    `:n``}},{kind:"get",static:!0,key:"styles",value:function(){return r`
      ha-card {
        overflow: hidden;
        height: 100%;
        border-radius: 1.5rem;
        display: flex;
        align-items: center;
      }

      ha-card.clickable {
        cursor: pointer;
      }

      img {
        display: block;
        width: 100%;
      }
    `}},{kind:"method",key:"_handleAction",value:function(t){f(this,this.hass,this._config,t.detail.action)}}]}}),i);export{m as HuiPictureCard};
