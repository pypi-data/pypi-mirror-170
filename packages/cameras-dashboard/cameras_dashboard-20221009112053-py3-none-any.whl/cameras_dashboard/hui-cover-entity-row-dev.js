const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, _ as isTiltOnly } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-cover-entity-row")],function(_initialize,_LitElement){class HuiCoverEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCoverEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        ${this._config.layout!=="medium"?isTiltOnly(stateObj)?$`
                <ha-cover-tilt-controls
                  .hass=${this.hass}
                  .stateObj=${stateObj}
                ></ha-cover-tilt-controls>
              `:$`
                <ha-cover-controls
                  .hass=${this.hass}
                  .stateObj=${stateObj}
                ></ha-cover-controls>
              `:$``}
      </hui-generic-entity-row>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-cover-controls,
      ha-cover-tilt-controls {
        margin-right: -0.57em;
      }
    `;}}]};},s);
