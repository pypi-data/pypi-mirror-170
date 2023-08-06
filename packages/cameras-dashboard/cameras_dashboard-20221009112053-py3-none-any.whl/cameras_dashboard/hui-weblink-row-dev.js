const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, t, $, Q as l, r, n } from './main-dev.js';

_decorate([n("hui-weblink-row")],function(_initialize,_LitElement){class HuiWeblinkRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiWeblinkRow,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.url){throw new Error("URL required");}this._config={icon:"hass:link",name:config.url,...config};}},{kind:"method",key:"render",value:function render(){if(!this._config){return $``;}return $`
      <a
        href=${this._config.url}
        target=${l(this._computeTargetValue())}
        rel="noreferrer"
        ?download=${this._config.download}
      >
        <ha-icon .icon=${this._config.icon}></ha-icon>
        <div .title=${this._config.name}>${this._config.name}</div>
      </a>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      a {
        display: flex;
        align-items: center;
        color: var(--accent-color);
      }
      ha-icon {
        padding: 8px;
        color: var(--paper-item-icon-color);
      }
      div {
        flex: 1;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-left: 16px;
      }
    `;}},{kind:"method",key:"_computeTargetValue",value:function _computeTargetValue(){return this._config&&(this._config.url.indexOf("://")!==-1||this._config.new_tab===true||this._config.download===true)?"_blank":undefined;}}]};},s);
