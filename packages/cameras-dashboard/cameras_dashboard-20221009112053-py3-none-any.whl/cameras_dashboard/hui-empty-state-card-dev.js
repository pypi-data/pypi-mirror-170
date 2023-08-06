const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, n } from './main-dev.js';

let HuiEmptyStateCard=_decorate([n("hui-empty-state-card")],function(_initialize,_LitElement){class HuiEmptyStateCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEmptyStateCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 2;}},{kind:"method",key:"setConfig",value:function setConfig(_config){// eslint-disable-next-line
}},{kind:"method",key:"render",value:function render(){if(!this.hass){return $``;}return $`
      <ha-card
        .header=${this.hass.localize("ui.panel.lovelace.cards.empty_state.title")}
      >
        <div class="card-content">
          ${this.hass.localize("ui.panel.lovelace.cards.empty_state.no_devices")}
        </div>
        <div class="card-actions">
          <a href="/config/integrations">
            <mwc-button>
              ${this.hass.localize("ui.panel.lovelace.cards.empty_state.go_to_integrations_page")}
            </mwc-button>
          </a>
        </div>
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .content {
        margin-top: -1em;
        padding: 16px;
      }

      .card-actions a {
        text-decoration: none;
      }

      mwc-button {
        margin-left: -8px;
      }
    `;}}]};},s);

export { HuiEmptyStateCard };
