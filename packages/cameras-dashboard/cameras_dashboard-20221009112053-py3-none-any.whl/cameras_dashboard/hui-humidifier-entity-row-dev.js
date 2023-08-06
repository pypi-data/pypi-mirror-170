const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, n } from './main-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-humidifier-entity-row")],function(_initialize,_LitElement){class HuiHumidifierEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiHumidifierEntityRow,d:[{kind:"field",decorators:[e()],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.entity){throw new Error("Entity must be specified");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        .secondaryText=${stateObj.attributes.humidity?`${this.hass.localize("ui.card.humidifier.humidity")}:
            ${stateObj.attributes.humidity} %${stateObj.attributes.mode?` (${this.hass.localize(`state_attributes.humidifier.mode.${stateObj.attributes.mode}`)||stateObj.attributes.mode})`:""}`:""}
      >
        <ha-entity-toggle
          .hass=${this.hass}
          .stateObj=${stateObj}
        ></ha-entity-toggle>
      </hui-generic-entity-row>
    `;}}]};},s);
