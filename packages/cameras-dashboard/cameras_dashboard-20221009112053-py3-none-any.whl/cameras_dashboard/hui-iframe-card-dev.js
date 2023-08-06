const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, I as i, r, n } from './main-dev.js';
import { ap as parseAspectRatio } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let HuiIframeCard=_decorate([n("hui-iframe-card")],function(_initialize,_LitElement){class HuiIframeCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiIframeCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-iframe-card-editor-dev.js');return document.createElement("hui-iframe-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {type:"iframe",url:"https://www.home-assistant.io",aspect_ratio:"50%"};}},{kind:"field",decorators:[e({type:Boolean,reflect:true})],key:"isPanel",value(){return false;}},{kind:"field",decorators:[e()],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){if(!this._config){return 5;}const aspectRatio=this._config.aspect_ratio?Number(this._config.aspect_ratio.replace("%","")):50;return 1+aspectRatio/25;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.url){throw new Error("URL required");}this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}let padding="";if(!this.isPanel&&this._config.aspect_ratio){const ratio=parseAspectRatio(this._config.aspect_ratio);if(ratio&&ratio.w>0&&ratio.h>0){padding=`${(100*ratio.h/ratio.w).toFixed(2)}%`;}}else if(!this.isPanel){padding="50%";}const target_protocol=new URL(this._config.url,location.toString()).protocol;if(location.protocol==="https:"&&target_protocol!=="https:"){return $`
        <ha-alert alert-type="error">
          ${this.hass.localize("ui.panel.lovelace.cards.iframe.error_secure_context",{target_protocol,context_protocol:location.protocol})}
        </ha-alert>
      `;}return $`
      <ha-card .header=${this._config.title}>
        <div
          id="root"
          style=${i({"padding-top":padding})}
        >
          <iframe
            src=${this._config.url}
            sandbox="allow-forms allow-modals allow-popups allow-pointer-lock allow-same-origin allow-scripts"
            allowfullscreen="true"
          ></iframe>
        </div>
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host([ispanel]) ha-card {
        width: 100%;
        height: 100%;
      }

      ha-card {
        overflow: hidden;
      }

      #root {
        width: 100%;
        position: relative;
      }

      :host([ispanel]) #root {
        height: 100%;
      }

      iframe {
        position: absolute;
        border: none;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
      }
    `;}}]};},s);

export { HuiIframeCard };
