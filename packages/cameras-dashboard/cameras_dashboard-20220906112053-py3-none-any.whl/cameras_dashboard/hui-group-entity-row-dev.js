const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import { e as computeDomain, L as DOMAINS_TOGGLE } from './auth-dev.js';
import { X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, o as computeStateDisplay } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-group-entity-row")],function(_initialize,_LitElement){class HuiGroupEntityRow extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGroupEntityRow,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"_computeCanToggle",value:function _computeCanToggle(hass,entityIds){return entityIds.some(entityId=>{const domain=computeDomain(entityId);if(domain==="group"){var _this$hass;return this._computeCanToggle(hass,(_this$hass=this.hass)===null||_this$hass===void 0?void 0:_this$hass.states[entityId].attributes.entity_id);}return DOMAINS_TOGGLE.has(domain);});}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}this._config=config;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}return $`
      <hui-generic-entity-row .hass=${this.hass} .config=${this._config}>
        ${this._computeCanToggle(this.hass,stateObj.attributes.entity_id)?$`
              <ha-entity-toggle
                .hass=${this.hass}
                .stateObj=${stateObj}
              ></ha-entity-toggle>
            `:$`
              <div class="text-content">
                ${computeStateDisplay(this.hass.localize,stateObj,this.hass.locale)}
              </div>
            `}
      </hui-generic-entity-row>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r``;}}]};},s);
