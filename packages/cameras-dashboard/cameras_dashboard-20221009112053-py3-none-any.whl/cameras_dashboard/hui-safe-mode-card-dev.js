const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, eM as mdiRefresh, j as _get, k as _getPrototypeOf, r, n } from './main-dev.js';

const fetchErrorLog=hass=>hass.callApi("GET","error_log");

let ErrorLogCard=_decorate(null,function(_initialize,_LitElement){class ErrorLogCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:ErrorLogCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"filter",value(){return "";}},{kind:"field",decorators:[t()],key:"_isLogLoaded",value(){return false;}},{kind:"field",decorators:[t()],key:"_errorHTML",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      <div class="error-log-intro">
        ${this._errorHTML?$`
              <ha-card>
                <ha-icon-button
                  .path=${mdiRefresh}
                  @click=${this._refreshErrorLog}
                  .label=${this.hass.localize("ui.common.refresh")}
                ></ha-icon-button>
                <div class="card-content error-log">${this._errorHTML}</div>
              </ha-card>
            `:$`
              <mwc-button raised @click=${this._refreshErrorLog}>
                ${this.hass.localize("ui.panel.config.logs.load_full_log")}
              </mwc-button>
            `}
      </div>
    `;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(changedProps){var _this$hass;_get(_getPrototypeOf(ErrorLogCard.prototype),"firstUpdated",this).call(this,changedProps);if((_this$hass=this.hass)!==null&&_this$hass!==void 0&&_this$hass.config.safe_mode){this.hass.loadFragmentTranslation("config");this._refreshErrorLog();}}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(ErrorLogCard.prototype),"updated",this).call(this,changedProps);if(changedProps.has("filter")&&this._isLogLoaded){this._refreshErrorLog();}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .error-log-intro {
        text-align: center;
        margin: 16px;
      }

      ha-icon-button {
        float: right;
      }

      .error-log {
        font-family: var(--code-font-family, monospace);
        clear: both;
        text-align: left;
        padding-top: 12px;
      }

      .error-log > div:hover {
        background-color: var(--secondary-background-color);
      }

      .error {
        color: var(--error-color);
      }

      .warning {
        color: var(--warning-color);
      }
    `;}},{kind:"method",key:"_refreshErrorLog",value:async function _refreshErrorLog(){this._errorHTML=this.hass.localize("ui.panel.config.logs.loading_log");const log=await fetchErrorLog(this.hass);this._isLogLoaded=true;this._errorHTML=log?log.split("\n").filter(entry=>{if(this.filter){return entry.toLowerCase().includes(this.filter.toLowerCase());}return entry;}).map(entry=>{if(entry.includes("INFO"))return $`<div class="info">${entry}</div>`;if(entry.includes("WARNING"))return $`<div class="warning">${entry}</div>`;if(entry.includes("ERROR")||entry.includes("FATAL")||entry.includes("CRITICAL"))return $`<div class="error">${entry}</div>`;return $`<div>${entry}</div>`;}):this.hass.localize("ui.panel.config.logs.no_errors");}}]};},s);customElements.define("error-log-card",ErrorLogCard);

let HuiSafeModeCard=_decorate([n("hui-safe-mode-card")],function(_initialize,_LitElement){class HuiSafeModeCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiSafeModeCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(_config){// No config necessary.
}},{kind:"method",key:"render",value:function render(){return $`
      <ha-card
        .header=${this.hass.localize("ui.panel.lovelace.cards.safe-mode.header")}
      >
        <div class="card-content">
          ${this.hass.localize("ui.panel.lovelace.cards.safe-mode.description")}
        </div>
        <error-log-card .hass=${this.hass}></error-log-card>
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        --ha-card-header-color: var(--primary-color);
      }
      error-log-card {
        display: block;
        padding-bottom: 16px;
      }
    `;}}]};},s);

export { HuiSafeModeCard };
