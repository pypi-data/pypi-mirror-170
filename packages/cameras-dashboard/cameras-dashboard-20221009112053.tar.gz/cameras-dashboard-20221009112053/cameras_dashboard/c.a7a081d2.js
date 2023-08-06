import{_ as t,c as a,t as e,d as i,$ as o,L as n,r as s,n as r}from"./main-d07cb663.js";import{j as d}from"./c.fc0bbf07.js";import{Q as c,R as h,V as l,T as p}from"./c.37525831.js";t([r("hui-buttons-base")],(function(t,a){return{F:class extends a{constructor(...a){super(...a),t(this)}},d:[{kind:"field",decorators:[e()],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"configEntities",value:void 0},{kind:"method",key:"render",value:function(){return o`
      <div class="ha-scrollbar">
        ${(this.configEntities||[]).map((t=>{const a=this.hass.states[t.entity],e=t.show_name&&a||t.name&&!1!==t.show_name?t.name||d(a):"";return o`
            <ha-chip
              @action=${this._handleAction}
              .actionHandler=${c({hasHold:h(t.hold_action),hasDoubleClick:h(t.double_tap_action)})}
              .config=${t}
              tabindex="0"
              .hasIcon=${!1!==t.show_icon}
              .noText=${!e}
            >
              ${!1!==t.show_icon?o`
                    <state-badge
                      title=${l(this.hass,t)}
                      .hass=${this.hass}
                      .stateObj=${a}
                      .overrideIcon=${t.icon}
                      .overrideImage=${t.image}
                      class=${e?"":"no-text"}
                      stateColor
                      slot="icon"
                    ></state-badge>
                  `:""}
              ${e}
            </ha-chip>
          `}))}
      </div>
    `}},{kind:"method",key:"_handleAction",value:function(t){const a=t.currentTarget.config;p(this,this.hass,a,t.detail.action)}},{kind:"get",static:!0,key:"styles",value:function(){return[n,s`
        .ha-scrollbar {
          padding: 8px;
          padding-top: var(--padding-top, 8px);
          padding-bottom: var(--padding-bottom, 8px);
          width: 100%;
          overflow-x: auto;
          overflow-y: hidden;
          white-space: nowrap;
          box-sizing: border-box;
          display: flex;
          flex-wrap: wrap;
        }
        state-badge {
          display: inline-flex;
          line-height: inherit;
          color: var(--secondary-text-color);
          align-items: center;
          justify-content: center;
          width: 24px;
          height: 24px;
          margin-left: -4px;
          margin-top: -2px;
        }
        state-badge.no-text {
          width: 26px;
          height: 26px;
          margin-left: -3px;
          margin-top: -3px;
        }
        ha-chip {
          padding: 4px;
        }
        @media all and (max-width: 450px), all and (max-height: 500px) {
          .ha-scrollbar {
            flex-wrap: nowrap;
          }
        }
      `]}}]}}),a);
