import{_ as e,c as t,d as i,t as s,j as a,k as n,$ as r,r as d,n as o}from"./main-d07cb663.js";import{X as h,Z as u,o as c}from"./c.37525831.js";import{a as l}from"./c.c11921c6.js";import{d as m}from"./c.95ef015c.js";import{a as f,Q as b}from"./c.fc0bbf07.js";import{s as v}from"./c.c1dd06c9.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";e([o("hui-number-entity-row")],(function(e,t){class o extends t{constructor(...t){super(...t),e(this)}}return{F:o,d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"field",key:"_loaded",value:void 0},{kind:"field",key:"_updated",value:void 0},{kind:"field",key:"_resizeObserver",value:void 0},{kind:"method",key:"setConfig",value:function(e){if(!e)throw new Error("Invalid configuration");this._config=e}},{kind:"method",key:"connectedCallback",value:function(){a(n(o.prototype),"connectedCallback",this).call(this),this._updated&&!this._loaded&&this._initialLoad(),this._attachObserver()}},{kind:"method",key:"disconnectedCallback",value:function(){var e;null===(e=this._resizeObserver)||void 0===e||e.disconnect()}},{kind:"method",key:"firstUpdated",value:function(){this._updated=!0,this.isConnected&&!this._loaded&&this._initialLoad(),this._attachObserver()}},{kind:"method",key:"shouldUpdate",value:function(e){return h(this,e)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return r``;const e=this.hass.states[this._config.entity];return e?r`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        ${"slider"===e.attributes.mode||"auto"===e.attributes.mode&&(Number(e.attributes.max)-Number(e.attributes.min))/Number(e.attributes.step)<=256?r`
              <div class="flex">
                <ha-slider
                  .disabled=${e.state===f}
                  .dir=${l(this.hass)}
                  .step=${Number(e.attributes.step)}
                  .min=${Number(e.attributes.min)}
                  .max=${Number(e.attributes.max)}
                  .value=${Number(e.state)}
                  pin
                  @change=${this._selectedValueChanged}
                  ignore-bar-touch
                ></ha-slider>
                <span class="state">
                  ${c(this.hass.localize,e,this.hass.locale,e.state)}
                </span>
              </div>
            `:r`
              <div class="flex state">
                <ha-textfield
                  autoValidate
                  .disabled=${e.state===f}
                  pattern="[0-9]+([\\.][0-9]+)?"
                  .step=${Number(e.attributes.step)}
                  .min=${Number(e.attributes.min)}
                  .max=${Number(e.attributes.max)}
                  .value=${e.state}
                  .suffix=${e.attributes.unit_of_measurement}
                  type="number"
                  @change=${this._selectedValueChanged}
                ></ha-textfield>
              </div>
            `}
      </hui-generic-entity-row>
    `:r`
        <hui-warning>
          ${u(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"get",static:!0,key:"styles",value:function(){return d`
      :host {
        cursor: pointer;
        display: block;
      }
      .flex {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        flex-grow: 2;
      }
      .state {
        min-width: 45px;
        text-align: end;
      }
      ha-textfield {
        text-align: end;
      }
      ha-slider {
        width: 100%;
        max-width: 200px;
      }
    `}},{kind:"method",key:"_initialLoad",value:async function(){this._loaded=!0,await this.updateComplete,this._measureCard()}},{kind:"method",key:"_measureCard",value:function(){if(!this.isConnected)return;const e=this.shadowRoot.querySelector(".state");e&&(e.hidden=this.clientWidth<=300)}},{kind:"method",key:"_attachObserver",value:async function(){this._resizeObserver||(await b(),this._resizeObserver=new ResizeObserver(m((()=>this._measureCard()),250,!1))),this.isConnected&&this._resizeObserver.observe(this)}},{kind:"method",key:"_selectedValueChanged",value:function(e){const t=this.hass.states[this._config.entity];e.target.value!==t.state&&v(this.hass,t.entity_id,e.target.value)}}]}}),t);
