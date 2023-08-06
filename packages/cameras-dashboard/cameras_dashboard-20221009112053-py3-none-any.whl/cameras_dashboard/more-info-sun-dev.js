const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, n } from './main-dev.js';
import { w as formatTime } from './ha-more-info-dialog-dev.js';
import { f as formatNumber } from './auth-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("more-info-sun")],function(_initialize,_LitElement){class MoreInfoSun extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoSun,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}const risingDate=new Date(this.stateObj.attributes.next_rising);const settingDate=new Date(this.stateObj.attributes.next_setting);const order=risingDate>settingDate?["set","ris"]:["ris","set"];return $`
      <hr />
      ${order.map(item=>$`
          <div class="row">
            <div class="key">
              <span
                >${item==="ris"?this.hass.localize("ui.dialogs.more_info_control.sun.rising"):this.hass.localize("ui.dialogs.more_info_control.sun.setting")}</span
              >
              <ha-relative-time
                .hass=${this.hass}
                .datetime=${item==="ris"?risingDate:settingDate}
              ></ha-relative-time>
            </div>
            <div class="value">
              ${formatTime(item==="ris"?risingDate:settingDate,this.hass.locale)}
            </div>
          </div>
        `)}
      <div class="row">
        <div class="key">
          ${this.hass.localize("ui.dialogs.more_info_control.sun.elevation")}
        </div>
        <div class="value">
          ${formatNumber(this.stateObj.attributes.elevation,this.hass.locale)}
        </div>
      </div>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .row {
        margin: 0;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
      }
      ha-relative-time {
        display: inline-block;
        white-space: nowrap;
      }
      hr {
        border-color: var(--divider-color);
        border-bottom: none;
        margin: 16px 0;
      }
    `;}}]};},s);
