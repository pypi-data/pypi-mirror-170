import{_ as i,c as e,d as t,t as a,$ as c,f as o,r as s,n}from"./main-d07cb663.js";import{al as r,am as l,an as d,ao as h,aq as f}from"./c.fc0bbf07.js";import"./c.ae68c3e2.js";import"./c.650fd31d.js";import{a as u}from"./c.ebfe053a.js";import{c as g}from"./c.70b58286.js";import{b as m}from"./c.885af130.js";import"./c.95ef015c.js";import"./c.6c5cb033.js";import"./c.9c88d99b.js";import"./c.d294c310.js";import"./c.6dd7f489.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.c8cf0377.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";import"./c.5fe2e3ab.js";import"./c.2036cb65.js";import"./c.65b9d701.js";import"./c.c245ec1a.js";import"./c.c9178224.js";import"./c.bd9a7167.js";import"./c.1ded644c.js";import"./c.da136530.js";import"./c.fb31f48a.js";import"./c.2ff699c8.js";import"./c.2465bf13.js";import"./c.3a0ccb1a.js";import"./c.f9f3b7e4.js";const p=r(m,l({image:d(h()),tap_action:d(u),hold_action:d(u)}));let _=i([n("hui-picture-card-editor")],(function(i,e){return{F:class extends e{constructor(...e){super(...e),i(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(i){f(i,p),this._config=i}},{kind:"get",key:"_image",value:function(){return this._config.image||""}},{kind:"get",key:"_tap_action",value:function(){return this._config.tap_action||{action:"none"}}},{kind:"get",key:"_hold_action",value:function(){return this._config.hold_action||{action:"none"}}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return c``;const i=["navigate","url","call-service","none"];return c`
      <div class="card-config">
        <ha-textfield
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.image")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})"
          .value=${this._image}
          .configValue=${"image"}
          @input=${this._valueChanged}
        ></ha-textfield>
        <!-- <hui-theme-select-editor
          .hass=${this.hass}
          .value=${this._theme}
          .configValue=${"theme"}
          @value-changed=${this._valueChanged}
        ></hui-theme-select-editor> -->
        <!-- <div class="side-by-side">
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${i}
            .configValue=${"tap_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${i}
            .configValue=${"hold_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
        </div> -->
      </div>
    `}},{kind:"method",key:"_valueChanged",value:function(i){if(!this._config||!this.hass)return;const e=i.target,t=i.detail.value;this[`_${e.configValue}`]!==e.value&&(e.configValue&&(!1===t||t?this._config={...this._config,[e.configValue]:t}:(this._config={...this._config},delete this._config[e.configValue])),o(this,"config-changed",{config:this._config}))}},{kind:"get",static:!0,key:"styles",value:function(){return[g,s`
        ha-textfield {
          display: block;
          margin-bottom: 8px;
        }
      `]}}]}}),e);export{_ as HuiPictureCardEditor};
