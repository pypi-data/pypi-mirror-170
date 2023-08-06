import{_ as t,c as e,d as i,t as s,$ as n,r as a,n as c}from"./main-d07cb663.js";import{s as o}from"./c.95ef015c.js";import{j as h,h as r,k as d}from"./c.fc0bbf07.js";import{X as l,Z as u,$ as f}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";t([c("hui-input-select-entity-row")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t||!t.entity)throw new Error("Entity must be specified");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return l(this,t)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return n``;const t=this.hass.states[this._config.entity];return t?n`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        hideName
      >
        <ha-select
          .label=${this._config.name||h(t)}
          .value=${t.state}
          .disabled=${r.includes(t.state)}
          naturalMenuWidth
          @selected=${this._selectedChanged}
          @click=${o}
          @closed=${o}
        >
          ${t.attributes.options?t.attributes.options.map((t=>n`<mwc-list-item .value=${t}
                    >${t}</mwc-list-item
                  >`)):""}
        </ha-select>
      </hui-generic-entity-row>
    `:n`
        <hui-warning>
          ${u(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"field",static:!0,key:"styles",value:()=>a`
    hui-generic-entity-row {
      display: flex;
      align-items: center;
    }
    ha-select {
      width: 100%;
      --ha-select-min-width: 0;
    }
  `},{kind:"method",key:"_selectedChanged",value:function(t){const e=this.hass.states[this._config.entity],i=t.target.value;i!==e.state&&(d("light"),f(this.hass,e.entity_id,i))}}]}}),e);
