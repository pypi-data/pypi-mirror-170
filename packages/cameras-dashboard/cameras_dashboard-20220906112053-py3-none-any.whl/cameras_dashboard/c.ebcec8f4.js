import{_ as i,c as t,d as e,t as s,$ as o,z as n,Q as a,r as c,n as r}from"./main-d07cb663.js";import{X as h,Z as l,a6 as d,Q as f,R as u,o as p,z as g,a7 as m,T as _,a8 as v}from"./c.37525831.js";import{j as x,h as y,f as b}from"./c.fc0bbf07.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";i([r("hui-weather-entity-row")],(function(i,t){return{F:class extends t{constructor(...t){super(...t),i(this)}},d:[{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(i){if(null==i||!i.entity)throw new Error("Entity must be specified");this._config=i}},{kind:"method",key:"shouldUpdate",value:function(i){return h(this,i)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return o``;const i=this.hass.states[this._config.entity];if(!i)return o`
        <hui-warning>
          ${l(this.hass,this._config.entity)}
        </hui-warning>
      `;const t=!(this._config.tap_action&&"none"!==this._config.tap_action.action),e=d(i.state,this);return o`
      <div
        class="icon-image ${n({pointer:t})}"
        @action=${this._handleAction}
        .actionHandler=${f({hasHold:u(this._config.hold_action),hasDoubleClick:u(this._config.double_tap_action)})}
        tabindex=${a(t?"0":void 0)}
      >
        ${e||o`
          <ha-state-icon
            class="weather-icon"
            .state=${i}
          ></ha-state-icon>
        `}
      </div>
      <div
        class="info ${n({pointer:t})}"
        @action=${this._handleAction}
        .actionHandler=${f({hasHold:u(this._config.hold_action),hasDoubleClick:u(this._config.double_tap_action)})}
      >
        ${this._config.name||x(i)}
      </div>
      <div
        class="attributes ${n({pointer:t})}"
        @action=${this._handleAction}
        .actionHandler=${f({hasHold:u(this._config.hold_action),hasDoubleClick:u(this._config.double_tap_action)})}
      >
        <div>
          ${y.includes(i.state)?p(this.hass.localize,i,this.hass.locale):o`
                ${b(i.attributes.temperature,this.hass.locale)}
                ${g(this.hass,"temperature")}
              `}
        </div>
        <div class="secondary">
          ${m(this.hass,i)}
        </div>
      </div>
    `}},{kind:"method",key:"_handleAction",value:function(i){_(this,this.hass,this._config,i.detail.action)}},{kind:"get",static:!0,key:"styles",value:function(){return[v,c`
        :host {
          display: flex;
          align-items: center;
          flex-direction: row;
        }

        .info {
          margin-left: 16px;
          flex: 1 0 60px;
        }

        .info,
        .info > * {
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .icon-image {
          display: flex;
          align-items: center;
          min-width: 40px;
        }

        .icon-image > * {
          flex: 0 0 40px;
          height: 40px;
        }

        .icon-image:focus {
          outline: none;
          background-color: var(--divider-color);
          border-radius: 50%;
        }

        .weather-icon {
          --mdc-icon-size: 40px;
        }

        :host([rtl]) .flex {
          margin-left: 0;
          margin-right: 16px;
        }

        .pointer {
          cursor: pointer;
        }

        .attributes {
          display: flex;
          flex-direction: column;
          justify-content: center;
          text-align: right;
          margin-left: 8px;
        }

        .secondary {
          color: var(--secondary-text-color);
        }
      `]}}]}}),t);
