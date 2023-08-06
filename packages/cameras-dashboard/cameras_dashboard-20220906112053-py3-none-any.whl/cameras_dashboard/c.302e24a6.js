import{_ as i,c as e,d as a,t,$ as c,f as o,n as s}from"./main-d07cb663.js";import{al as n,am as r,an as l,ao as d,ap as h,aq as m}from"./c.fc0bbf07.js";import"./c.ae68c3e2.js";import{a as f}from"./c.ebfe053a.js";import{b as u}from"./c.885af130.js";import{c as p}from"./c.70b58286.js";import"./c.95ef015c.js";import"./c.6c5cb033.js";import"./c.9c88d99b.js";import"./c.d294c310.js";import"./c.6dd7f489.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.c8cf0377.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";import"./c.5fe2e3ab.js";import"./c.2036cb65.js";import"./c.65b9d701.js";import"./c.c245ec1a.js";import"./c.c9178224.js";import"./c.bd9a7167.js";import"./c.1ded644c.js";import"./c.da136530.js";import"./c.fb31f48a.js";import"./c.2ff699c8.js";import"./c.650fd31d.js";import"./c.2465bf13.js";import"./c.3a0ccb1a.js";import"./c.f9f3b7e4.js";const g=n(u,r({entity:l(d()),image:l(d()),name:l(d()),camera_image:l(d()),camera_view:l(d()),aspect_ratio:l(d()),tap_action:l(f),hold_action:l(f),show_name:l(h()),show_state:l(h()),theme:l(d())})),_=[{name:"entity",required:!0,selector:{entity:{domain:"camera"}}},{name:"name",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"camera_view",selector:{select:{options:["auto","live"]}}}]}];let v=i([s("hui-picture-camera-card-editor")],(function(i,e){return{F:class extends e{constructor(...e){super(...e),i(this)}},d:[{kind:"field",decorators:[a({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(i){m(i,g),this._config=i}},{kind:"get",key:"_tap_action",value:function(){return this._config.tap_action||{action:"more-info"}}},{kind:"get",key:"_hold_action",value:function(){return this._config.hold_action}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return c``;const i=["more-info","toggle","navigate","call-service","none"],e={show_state:!0,show_name:!0,camera_view:"auto",...this._config};return c`
      <ha-form
        .hass=${this.hass}
        .data=${e}
        .schema=${_}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <!-- <div class="card-config">
        <div class="side-by-side">
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${i}
            .configValue=${"tap_action"}
            @value-changed=${this._changed}
          ></hui-action-editor>
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${i}
            .configValue=${"hold_action"}
            @value-changed=${this._changed}
          ></hui-action-editor>
        </div>
      </div> -->
    `}},{kind:"method",key:"_valueChanged",value:function(i){o(this,"config-changed",{config:i.detail.value})}},{kind:"method",key:"_changed",value:function(i){if(!this._config||!this.hass)return;const e=i.target,a=i.detail.value;this[`_${e.configValue}`]!==a&&(!1===a||a?this._config={...this._config,[e.configValue]:a}:(this._config={...this._config},delete this._config[e.configValue]),o(this,"config-changed",{config:this._config}))}},{kind:"field",key:"_computeLabelCallback",value(){return i=>"entity"===i.name?this.hass.localize("ui.panel.lovelace.editor.card.generic.entity"):this.hass.localize(`ui.panel.lovelace.editor.card.generic.${i.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.picture-entity.${i.name}`)}},{kind:"field",static:!0,key:"styles",value:()=>p}]}}),e);export{v as HuiPictureEntityCardEditor};
