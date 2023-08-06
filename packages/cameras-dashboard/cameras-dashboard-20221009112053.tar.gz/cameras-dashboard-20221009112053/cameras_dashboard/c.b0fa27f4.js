import{_ as i,c as e,d as t,t as o,$ as s,f as a,n}from"./main-d07cb663.js";import{aq as c}from"./c.fc0bbf07.js";import"./c.f2f631cd.js";import"./c.95ef015c.js";import{g as h}from"./c.972893d2.js";import{c as l}from"./c.70b58286.js";import"./c.dd4b7d4a.js";import"./c.ebfe053a.js";import"./c.b0065faf.js";const r=["sensor"];let d=i([n("hui-graph-footer-editor")],(function(i,e){return{F:class extends e{constructor(...e){super(...e),i(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[o()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(i){c(i,h),this._config=i}},{kind:"get",key:"_entity",value:function(){return this._config.entity||""}},{kind:"get",key:"_detail",value:function(){var i;return null!==(i=this._config.detail)&&void 0!==i?i:1}},{kind:"get",key:"_hours_to_show",value:function(){return this._config.hours_to_show||24}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?s`
      <div class="card-config">
        <ha-entity-picker
          allow-custom-entity
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.required")})"
          .hass=${this.hass}
          .value=${this._entity}
          .configValue=${"entity"}
          .includeDomains=${r}
          @change=${this._valueChanged}
        ></ha-entity-picker>
        <div class="side-by-side">
          <ha-formfield
            label=${this.hass.localize("ui.panel.lovelace.editor.card.sensor.show_more_detail")}
          >
            <ha-switch
              .checked=${2===this._detail}
              .configValue=${"detail"}
              @change=${this._change}
            ></ha-switch>
          </ha-formfield>
          <ha-textfield
            type="number"
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hours_to_show")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .value=${this._hours_to_show}
            min="1"
            .configValue=${"hours_to_show"}
            @input=${this._valueChanged}
          ></ha-textfield>
        </div>
      </div>
    `:s``}},{kind:"method",key:"_change",value:function(i){if(!this._config||!this.hass)return;const e=i.target.checked?2:1;this._detail!==e&&(this._config={...this._config,detail:e},a(this,"config-changed",{config:this._config}))}},{kind:"method",key:"_valueChanged",value:function(i){if(!this._config||!this.hass)return;const e=i.target;if(this[`_${e.configValue}`]!==e.value){if(e.configValue)if(""===e.value||"number"===e.type&&isNaN(Number(e.value)))this._config={...this._config},delete this._config[e.configValue];else{let i=e.value;"number"===e.type&&(i=Number(i)),this._config={...this._config,[e.configValue]:i}}a(this,"config-changed",{config:this._config})}}},{kind:"get",static:!0,key:"styles",value:function(){return l}}]}}),e);export{d as HuiGraphFooterEditor};
