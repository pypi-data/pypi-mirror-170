const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, t, $, r, n } from './main-dev.js';

_decorate([n("hui-text-row")],function(_initialize,_LitElement){class HuiTextRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiTextRow,d:[{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.name||!config.text){throw new Error("Name and text required");}this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this._config){return $``;}return $`
      <ha-icon .icon=${this._config.icon}></ha-icon>
      <div class="name" .title=${this._config.name}>${this._config.name}</div>
      <div class="text" .title=${this._config.text}>${this._config.text}</div>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: flex;
        align-items: center;
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
      }
      .name {
        margin-left: 16px;
      }
      .text {
        text-align: right;
      }
    `;}}]};},s);
