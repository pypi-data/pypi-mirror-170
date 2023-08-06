const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, b as memoizeOne, $, f as fireEvent, r, n } from './main-dev.js';
import { v as navigate } from './ha-more-info-dialog-dev.js';
import './ha-map-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const showZoneEditor=data=>{navigate("/config/zone/new");};

_decorate([n("more-info-person")],function(_initialize,_LitElement){class MoreInfoPerson extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoPerson,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"field",key:"_entityArray",value(){return memoizeOne(entityId=>[entityId]);}},{kind:"method",key:"render",value:function render(){var _this$hass$user;if(!this.hass||!this.stateObj){return $``;}return $`
      ${this.stateObj.attributes.latitude&&this.stateObj.attributes.longitude?$`
            <ha-map
              .hass=${this.hass}
              .entities=${this._entityArray(this.stateObj.entity_id)}
              autoFit
            ></ha-map>
          `:""}
      ${!__DEMO__&&(_this$hass$user=this.hass.user)!==null&&_this$hass$user!==void 0&&_this$hass$user.is_admin&&this.stateObj.state==="not_home"&&this.stateObj.attributes.latitude&&this.stateObj.attributes.longitude?$`
            <div class="actions">
              <mwc-button @click=${this._handleAction}>
                ${this.hass.localize("ui.dialogs.more_info_control.person.create_zone")}
              </mwc-button>
            </div>
          `:""}
      <ha-attributes
        .hass=${this.hass}
        .stateObj=${this.stateObj}
        extra-filters="id,user_id,editable"
      ></ha-attributes>
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(){showZoneEditor({latitude:this.stateObj.attributes.latitude,longitude:this.stateObj.attributes.longitude});fireEvent(this,"hass-more-info",{entityId:null});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .flex {
        display: flex;
        justify-content: space-between;
      }
      .actions {
        margin: 8px 0;
        text-align: right;
      }
      ha-map {
        margin-top: 16px;
        margin-bottom: 16px;
      }
    `;}}]};},s);
