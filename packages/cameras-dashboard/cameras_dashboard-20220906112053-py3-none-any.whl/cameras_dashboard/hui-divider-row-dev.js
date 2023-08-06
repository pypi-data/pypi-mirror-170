const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, t, $, I as i, r, n } from './main-dev.js';

_decorate([n("hui-divider-row")],function(_initialize,_LitElement){class HuiDividerRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiDividerRow,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Error in card configuration.");}this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this._config){return $``;}return $`<div
      style=${this._config.style?i(this._config.style):""}
    ></div>`;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      div {
        height: 1px;
        background-color: var(--entities-divider-color, var(--divider-color));
      }
    `;}}]};},s);
