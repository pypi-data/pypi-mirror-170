import{_ as t,c as e,d as s,t as i,$ as a,r as n,n as c}from"./main-d07cb663.js";import{s as o}from"./c.95ef015c.js";import{j as r,a as h,k as l}from"./c.fc0bbf07.js";import{X as d,Z as u,a0 as f}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([c("hui-select-entity-row")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[s({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t||!t.entity)throw new Error("Entity must be specified");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return d(this,t)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return a``;const t=this.hass.states[this._config.entity];return t?a`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        hideName
      >
        <ha-select
          .label=${this._config.name||r(t)}
          .value=${t.state}
          .disabled=${t.state===h}
          naturalMenuWidth
          @selected=${this._selectedChanged}
          @click=${o}
          @closed=${o}
        >
          ${t.attributes.options?t.attributes.options.map((e=>a`
                    <mwc-list-item .value=${e}
                      >${t.attributes.device_class&&this.hass.localize(`component.select.state.${t.attributes.device_class}.${e}`)||this.hass.localize(`component.select.state._.${e}`)||e}
                    </mwc-list-item>
                  `)):""}
        </ha-select>
      </hui-generic-entity-row>
    `:a`
        <hui-warning>
          ${u(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"get",static:!0,key:"styles",value:function(){return n`
      hui-generic-entity-row {
        display: flex;
        align-items: center;
      }
      ha-select {
        width: 100%;
      }
    `}},{kind:"method",key:"_selectedChanged",value:function(t){const e=this.hass.states[this._config.entity],s=t.target.value;s!==e.state&&(l("light"),f(this.hass,e.entity_id,s))}}]}}),e);
