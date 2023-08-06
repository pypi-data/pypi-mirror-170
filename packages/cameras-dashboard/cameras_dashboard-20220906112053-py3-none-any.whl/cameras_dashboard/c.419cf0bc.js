import{_ as e,c as i,d as t,t as a,$ as s,f as o,r as n,n as l}from"./main-d07cb663.js";import{al as c,am as h,an as r,ao as d,aq as u,z as f}from"./c.fc0bbf07.js";import"./c.650fd31d.js";import{b as g}from"./c.885af130.js";import"./c.95ef015c.js";const v=c(g,h({title:r(d()),theme:r(d())}));let _=e([l("hui-shopping-list-card-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(e){u(e,v),this._config=e}},{kind:"get",key:"_title",value:function(){return this._config.title||""}},{kind:"get",key:"_theme",value:function(){return this._config.theme||""}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?s`
      <div class="card-config">
        ${f(this.hass,"shopping_list")?"":s`
              <div class="error">
                ${this.hass.localize("ui.panel.lovelace.editor.card.shopping-list.integration_not_loaded")}
              </div>
            `}
        <ha-textfield
          .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.title")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
          .value=${this._title}
          .configValue=${"title"}
          @input=${this._valueChanged}
        ></ha-textfield>
        <hui-theme-select-editor
          .hass=${this.hass}
          .value=${this._theme}
          .configValue=${"theme"}
          @value-changed=${this._valueChanged}
        ></hui-theme-select-editor>
      </div>
    `:s``}},{kind:"method",key:"_valueChanged",value:function(e){if(!this._config||!this.hass)return;const i=e.target;this[`_${i.configValue}`]!==i.value&&(i.configValue&&(""===i.value?(this._config={...this._config},delete this._config[i.configValue]):this._config={...this._config,[i.configValue]:i.value}),o(this,"config-changed",{config:this._config}))}},{kind:"get",static:!0,key:"styles",value:function(){return n`
      .error {
        color: var(--error-color);
      }
    `}}]}}),i);export{_ as HuiShoppingListEditor};
