const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, t, $, r, n } from './main-dev.js';
import { d as dump } from './js-yaml-dev.js';
import './stop_propagation-dev.js';

let HuiErrorCard=_decorate([n("hui-error-card")],function(_initialize,_LitElement){class HuiErrorCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiErrorCard,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 4;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this._config){return $``;}let dumped;if(this._config.origConfig){try{dumped=dump(this._config.origConfig);}catch(err){dumped=`[Error dumping ${this._config.origConfig}]`;}}return $`<ha-alert alert-type="error" .title=${this._config.error}>
      ${dumped?$`<pre>${dumped}</pre>`:""}
    </ha-alert>`;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      pre {
        font-family: var(--code-font-family, monospace);
        white-space: break-spaces;
        user-select: text;
        display: none;
      }
    `;}}]};},s);

export { HuiErrorCard };
