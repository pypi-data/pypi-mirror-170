const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, j as _get, k as _getPrototypeOf, f as fireEvent, $, r, n } from './main-dev.js';
import './ha-circular-progress-dev.js';
import { as as STATE_NOT_RUNNING } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './repeat-dev.js';

let HuiStartingCard=_decorate([n("hui-starting-card")],function(_initialize,_LitElement){class HuiStartingCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiStartingCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 2;}},{kind:"method",key:"setConfig",value:function setConfig(_config){// eslint-disable-next-line
}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(HuiStartingCard.prototype),"updated",this).call(this,changedProperties);if(!changedProperties.has("hass")||!this.hass.config){return;}if(this.hass.config.state!==STATE_NOT_RUNNING){fireEvent(this,"config-refresh");}}},{kind:"method",key:"render",value:function render(){if(!this.hass){return $``;}return $`
      <div class="content">
        <ha-circular-progress active></ha-circular-progress>
        ${this.hass.localize("ui.panel.lovelace.cards.starting.description")}
      </div>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
        height: calc(100vh - var(--header-height));
      }
      ha-circular-progress {
        padding-bottom: 20px;
      }
      .content {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
    `;}}]};},s);

export { HuiStartingCard };
