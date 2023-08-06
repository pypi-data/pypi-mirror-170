const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, n } from './main-dev.js';
import { s as supportsFeature } from './auth-dev.js';
import './ha-more-info-dialog-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const REMOTE_SUPPORT_ACTIVITY=4;

const filterExtraAttributes="activity_list,current_activity";_decorate([n("more-info-remote")],function(_initialize,_LitElement){class MoreInfoRemote extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoRemote,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}const stateObj=this.stateObj;return $`
      ${supportsFeature(stateObj,REMOTE_SUPPORT_ACTIVITY)?$`
            <mwc-list
              .label=${this.hass.localize("ui.dialogs.more_info_control.remote.activity")}
              .value=${stateObj.attributes.current_activity}
              @selected=${this.handleActivityChanged}
              fixedMenuPosition
              naturalMenuWidth
              @closed=${stopPropagation}
            >
              ${stateObj.attributes.activity_list.map(activity=>$`
                  <mwc-list-item .value=${activity}>${activity}</mwc-list-item>
                `)}
            </mwc-list>
          `:""}

      <ha-attributes
        .hass=${this.hass}
        .stateObj=${this.stateObj}
        .extraFilters=${filterExtraAttributes}
      ></ha-attributes>
    `;}},{kind:"method",key:"handleActivityChanged",value:function handleActivityChanged(ev){const oldVal=this.stateObj.attributes.current_activity;const newVal=ev.target.value;if(!newVal||oldVal===newVal){return;}this.hass.callService("remote","turn_on",{entity_id:this.stateObj.entity_id,activity:newVal});}}]};},s);
