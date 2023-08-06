import{_ as e,c as i,d as t,t as a,$ as r,ez as o,r as s,n}from"./main-d07cb663.js";import{f as l}from"./c.fc0bbf07.js";import"./c.669a5799.js";import{g as c}from"./c.db8c8161.js";import{ac as d}from"./c.37525831.js";import{S as u}from"./c.65b9d701.js";import"./c.95ef015c.js";import"./c.c13d4687.js";import"./c.da136530.js";import"./c.655d6539.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";const g=[{level:-1,stroke:"var(--energy-grid-consumption-color)"},{level:0,stroke:"var(--energy-grid-return-color)"}];e([n("hui-energy-grid-neutrality-gauge-card")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"field",decorators:[a()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:()=>["_config"]},{kind:"method",key:"hassSubscribe",value:function(){var e;return[c(this.hass,{key:null===(e=this._config)||void 0===e?void 0:e.collection_key}).subscribe((e=>{this._data=e}))]}},{kind:"method",key:"getCardSize",value:function(){return 4}},{kind:"method",key:"setConfig",value:function(e){this._config=e}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return r``;if(!this._data)return r`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;const e=this._data.prefs.energy_sources.find((e=>"grid"===e.type));let i;if(!e)return r``;const t=d(this._data.stats,e.flow_from.map((e=>e.stat_energy_from))),a=d(this._data.stats,e.flow_to.map((e=>e.stat_energy_to)));return null!==t&&null!==a&&(i=a>t?1-t/a:a<t?-1*(1-a/t):0),r`
      <ha-card>
        ${void 0!==i?r`
              <ha-svg-icon id="info" .path=${o}></ha-svg-icon>
              <paper-tooltip animation-delay="0" for="info" position="left">
                <span>
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.energy_dependency")}
                  <br /><br />
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.color_explain")}
                </span>
              </paper-tooltip>

              <ha-gauge
                min="-1"
                max="1"
                .value=${i}
                .valueText=${l(Math.abs(a-t),this.hass.locale,{maximumFractionDigits:2})}
                .locale=${this.hass.locale}
                .levels=${g}
                label="kWh"
                needle
              ></ha-gauge>
              <div class="name">
                ${a>=t?this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.net_returned_grid"):this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.net_consumed_grid")}
              </div>
            `:this.hass.localize("ui.panel.lovelace.cards.energy.grid_neutrality_gauge.grid_neutrality_not_calculated")}
      </ha-card>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return s`
      ha-card {
        height: 100%;
        overflow: hidden;
        padding: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        box-sizing: border-box;
      }

      ha-gauge {
        width: 100%;
        max-width: 250px;
      }

      .name {
        text-align: center;
        line-height: initial;
        color: var(--primary-text-color);
        width: 100%;
        font-size: 15px;
        margin-top: 8px;
      }

      ha-svg-icon {
        position: absolute;
        right: 4px;
        top: 4px;
        color: var(--secondary-text-color);
      }
      paper-tooltip > span {
        font-size: 12px;
        line-height: 12px;
      }
      paper-tooltip {
        width: 80%;
        max-width: 250px;
        top: 8px !important;
      }
    `}}]}}),u(i));
