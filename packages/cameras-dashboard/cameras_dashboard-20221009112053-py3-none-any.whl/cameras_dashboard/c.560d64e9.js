import{_ as e,c as a,d as o,t as i,$ as t,ez as s,I as r,r as n,n as c}from"./main-d07cb663.js";import"./c.fc0bbf07.js";import"./c.669a5799.js";import{g as l,e as d}from"./c.db8c8161.js";import{ac as u}from"./c.37525831.js";import{S as p}from"./c.65b9d701.js";import{severityMap as h}from"./c.ae0b4992.js";import"./c.95ef015c.js";import"./c.c13d4687.js";import"./c.da136530.js";import"./c.655d6539.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";e([c("hui-energy-solar-consumed-gauge-card")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[o({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"_config",value:void 0},{kind:"field",decorators:[i()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:()=>["_config"]},{kind:"method",key:"hassSubscribe",value:function(){var e;return[l(this.hass,{key:null===(e=this._config)||void 0===e?void 0:e.collection_key}).subscribe((e=>{this._data=e}))]}},{kind:"method",key:"getCardSize",value:function(){return 4}},{kind:"method",key:"setConfig",value:function(e){this._config=e}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return t``;if(!this._data)return t`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;const e=this._data.prefs,a=d(e);if(!a.solar)return t``;const o=u(this._data.stats,a.solar.map((e=>e.stat_energy_from))),i=u(this._data.stats,a.grid[0].flow_to.map((e=>e.stat_energy_to)));let n;if(null!==i&&o){n=Math.max(0,o-i)/o*100}return t`
      <ha-card>
        ${void 0!==n?t`
              <ha-svg-icon id="info" .path=${s}></ha-svg-icon>
              <paper-tooltip animation-delay="0" for="info" position="left">
                <span>
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.solar_consumed_gauge.card_indicates_solar_energy_used")}
                  <br /><br />
                  ${this.hass.localize("ui.panel.lovelace.cards.energy.solar_consumed_gauge.card_indicates_solar_energy_used_charge_home_bat")}
                </span>
              </paper-tooltip>
              <ha-gauge
                min="0"
                max="100"
                .value=${n}
                .locale=${this.hass.locale}
                label="%"
                style=${r({"--gauge-color":this._computeSeverity(n)})}
              ></ha-gauge>
              <div class="name">
                ${this.hass.localize("ui.panel.lovelace.cards.energy.solar_consumed_gauge.self_consumed_solar_energy")}
              </div>
            `:0===o?this.hass.localize("ui.panel.lovelace.cards.energy.solar_consumed_gauge.not_produced_solar_energy"):this.hass.localize("ui.panel.lovelace.cards.energy.solar_consumed_gauge.self_consumed_solar_could_not_calc")}
      </ha-card>
    `}},{kind:"method",key:"_computeSeverity",value:function(e){return e>75?h.green:e<50?h.yellow:h.normal}},{kind:"get",static:!0,key:"styles",value:function(){return n`
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
    `}}]}}),p(a));
