const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, n } from './main-dev.js';
import { h as UNAVAILABLE_STATES } from './auth-dev.js';
import './stop_propagation-dev.js';

_decorate([n("more-info-counter")],function(_initialize,_LitElement){class MoreInfoCounter extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoCounter,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}const disabled=UNAVAILABLE_STATES.includes(this.stateObj.state);return $`
      <div class="actions">
        <mwc-button
          .action=${"increment"}
          @click=${this._handleActionClick}
          .disabled=${disabled}
        >
          ${this.hass.localize("ui.card.counter.actions.increment")}
        </mwc-button>
        <mwc-button
          .action=${"decrement"}
          @click=${this._handleActionClick}
          .disabled=${disabled}
        >
          ${this.hass.localize("ui.card.counter.actions.decrement")}
        </mwc-button>
        <mwc-button
          .action=${"reset"}
          @click=${this._handleActionClick}
          .disabled=${disabled}
        >
          ${this.hass.localize("ui.card.counter.actions.reset")}
        </mwc-button>
      </div>
    `;}},{kind:"method",key:"_handleActionClick",value:function _handleActionClick(e){const action=e.currentTarget.action;this.hass.callService("counter",action,{entity_id:this.stateObj.entity_id});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .actions {
        margin: 8px 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
      }
    `;}}]};},s);
