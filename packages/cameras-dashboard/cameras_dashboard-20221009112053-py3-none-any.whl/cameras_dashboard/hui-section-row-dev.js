const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, t, $, r, n } from './main-dev.js';

_decorate([n("hui-section-row")],function(_initialize,_LitElement){class HuiSectionRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiSectionRow,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this._config){return $``;}return $`
      <div class="divider"></div>
      ${this._config.label?$`
            <div class="label" .title=${this._config.label}>
              ${this._config.label}
            </div>
          `:$``}
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .label {
        color: var(--section-header-text-color, var(--primary-text-color));
        margin-left: 8px;
        margin-bottom: 8px;
        margin-top: 16px;
        font-weight: 500;
      }
      .divider {
        height: 1px;
        background-color: var(--entities-divider-color, var(--divider-color));
        margin-left: -16px;
        margin-right: -16px;
        margin-top: 8px;
      }
    `;}}]};},s);
