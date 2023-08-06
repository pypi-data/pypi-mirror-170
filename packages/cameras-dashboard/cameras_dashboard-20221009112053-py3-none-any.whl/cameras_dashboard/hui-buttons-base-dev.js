const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, t, d as e, $, L as haStyleScrollbar, r, n } from './main-dev.js';
import { j as computeStateName } from './auth-dev.js';
import { Q as actionHandler, R as hasAction, V as computeTooltip, T as handleAction } from './ha-more-info-dialog-dev.js';

_decorate([n("hui-buttons-base")],function(_initialize,_LitElement){class HuiButtonsBase extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiButtonsBase,d:[{kind:"field",decorators:[t()],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"configEntities",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      <div class="ha-scrollbar">
        ${(this.configEntities||[]).map(entityConf=>{const stateObj=this.hass.states[entityConf.entity];const name=entityConf.show_name&&stateObj||entityConf.name&&entityConf.show_name!==false?entityConf.name||computeStateName(stateObj):"";return $`
            <ha-chip
              @action=${this._handleAction}
              .actionHandler=${actionHandler({hasHold:hasAction(entityConf.hold_action),hasDoubleClick:hasAction(entityConf.double_tap_action)})}
              .config=${entityConf}
              tabindex="0"
              .hasIcon=${entityConf.show_icon!==false}
              .noText=${!name}
            >
              ${entityConf.show_icon!==false?$`
                    <state-badge
                      title=${computeTooltip(this.hass,entityConf)}
                      .hass=${this.hass}
                      .stateObj=${stateObj}
                      .overrideIcon=${entityConf.icon}
                      .overrideImage=${entityConf.image}
                      class=${name?"":"no-text"}
                      stateColor
                      slot="icon"
                    ></state-badge>
                  `:""}
              ${name}
            </ha-chip>
          `;})}
      </div>
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){const config=ev.currentTarget.config;handleAction(this,this.hass,config,ev.detail.action);}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyleScrollbar,r`
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
      `];}}]};},s);
