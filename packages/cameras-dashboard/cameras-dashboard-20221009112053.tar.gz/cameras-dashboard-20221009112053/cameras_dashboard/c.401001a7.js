import{_ as e,c as i,d as t,t as a,$ as n,f as s,n as o}from"./main-d07cb663.js";import{al as c,am as h,an as d,ao as l,aq as r}from"./c.fc0bbf07.js";import"./c.f2f631cd.js";import"./c.650fd31d.js";import{b as u}from"./c.885af130.js";import"./c.95ef015c.js";import"./c.dd4b7d4a.js";const f=c(u,h({entity:d(l()),theme:d(l())})),g=["media_player"];let m=e([o("hui-media-control-card-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(e){r(e,f),this._config=e}},{kind:"get",key:"_entity",value:function(){return this._config.entity||""}},{kind:"get",key:"_theme",value:function(){return this._config.theme||""}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?n`
      <div class="card-config">
        <ha-entity-picker
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})"
          .hass=${this.hass}
          .value=${this._entity}
          .configValue=${"entity"}
          .includeDomains=${g}
          @change=${this._valueChanged}
          allow-custom-entity
        ></ha-entity-picker>
        <!-- <hui-theme-select-editor
          .hass=${this.hass}
          .value=${this._theme}
          .configValue=${"theme"}
          @value-changed=${this._valueChanged}
        ></hui-theme-select-editor> -->
      </div>
    `:n``}},{kind:"method",key:"_valueChanged",value:function(e){if(!this._config||!this.hass)return;const i=e.target;this[`_${i.configValue}`]!==i.value&&(i.configValue&&(""===i.value?(this._config={...this._config},delete this._config[i.configValue]):this._config={...this._config,[i.configValue]:i.value}),s(this,"config-changed",{config:this._config}))}}]}}),i);export{m as HuiMediaControlCardEditor};
