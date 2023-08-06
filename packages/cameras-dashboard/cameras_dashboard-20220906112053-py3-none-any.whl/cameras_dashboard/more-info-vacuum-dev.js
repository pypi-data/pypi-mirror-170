const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, am as mdiFan, r, n, a5 as mdiPlay, a6 as mdiPause, ad as mdiPlayPause, A as mdiStop, e1 as mdiTargetVariant, e2 as mdiMapMarker, e3 as mdiHomeMapMarker } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import { a as UNAVAILABLE, s as supportsFeature } from './auth-dev.js';
import './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const VACUUM_SUPPORT_PAUSE=4;const VACUUM_SUPPORT_STOP=8;const VACUUM_SUPPORT_RETURN_HOME=16;const VACUUM_SUPPORT_FAN_SPEED=32;const VACUUM_SUPPORT_BATTERY=64;const VACUUM_SUPPORT_STATUS=128;const VACUUM_SUPPORT_LOCATE=512;const VACUUM_SUPPORT_CLEAN_SPOT=1024;const VACUUM_SUPPORT_START=8192;

const VACUUM_COMMANDS=[{translationKey:"start",icon:mdiPlay,serviceName:"start",isVisible:stateObj=>supportsFeature(stateObj,VACUUM_SUPPORT_START)},{translationKey:"pause",icon:mdiPause,serviceName:"pause",isVisible:stateObj=>// We need also to check if Start is supported because if not we show play-pause
supportsFeature(stateObj,VACUUM_SUPPORT_START)&&supportsFeature(stateObj,VACUUM_SUPPORT_PAUSE)},{translationKey:"start_pause",icon:mdiPlayPause,serviceName:"start_pause",isVisible:stateObj=>// If start is supported, we don't show this button
!supportsFeature(stateObj,VACUUM_SUPPORT_START)&&supportsFeature(stateObj,VACUUM_SUPPORT_PAUSE)},{translationKey:"stop",icon:mdiStop,serviceName:"stop",isVisible:stateObj=>supportsFeature(stateObj,VACUUM_SUPPORT_STOP)},{translationKey:"clean_spot",icon:mdiTargetVariant,serviceName:"clean_spot",isVisible:stateObj=>supportsFeature(stateObj,VACUUM_SUPPORT_CLEAN_SPOT)},{translationKey:"locate",icon:mdiMapMarker,serviceName:"locate",isVisible:stateObj=>supportsFeature(stateObj,VACUUM_SUPPORT_LOCATE)},{translationKey:"return_home",icon:mdiHomeMapMarker,serviceName:"return_to_base",isVisible:stateObj=>supportsFeature(stateObj,VACUUM_SUPPORT_RETURN_HOME)}];_decorate([n("more-info-vacuum")],function(_initialize,_LitElement){class MoreInfoVacuum extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoVacuum,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}const stateObj=this.stateObj;const filterExtraAttributes="fan_speed,fan_speed_list,status,battery_level,battery_icon";return $`
      ${stateObj.state!==UNAVAILABLE?$` <div class="flex-horizontal">
            ${supportsFeature(stateObj,VACUUM_SUPPORT_STATUS)?$`
                  <div>
                    <span class="status-subtitle"
                      >${this.hass.localize("ui.dialogs.more_info_control.vacuum.status")}:
                    </span>
                    <span><strong>${stateObj.attributes.status}</strong></span>
                  </div>
                `:""}
            ${supportsFeature(stateObj,VACUUM_SUPPORT_BATTERY)&&stateObj.attributes.battery_level?$`
                  <div>
                    <span>
                      ${stateObj.attributes.battery_level} %
                      <ha-icon
                        .icon=${stateObj.attributes.battery_icon}
                      ></ha-icon>
                    </span>
                  </div>
                `:""}
          </div>`:""}
      ${VACUUM_COMMANDS.some(item=>item.isVisible(stateObj))?$`
            <div>
              <p></p>
              <div class="status-subtitle">
                ${this.hass.localize("ui.dialogs.more_info_control.vacuum.commands")}
              </div>
              <div class="flex-horizontal">
                ${VACUUM_COMMANDS.filter(item=>item.isVisible(stateObj)).map(item=>$`
                    <div>
                      <ha-icon-button
                        .path=${item.icon}
                        .entry=${item}
                        @click=${this.callService}
                        .label=${this.hass.localize(`ui.dialogs.more_info_control.vacuum.${item.translationKey}`)}
                        .disabled=${stateObj.state===UNAVAILABLE}
                      ></ha-icon-button>
                    </div>
                  `)}
              </div>
            </div>
          `:""}
      ${supportsFeature(stateObj,VACUUM_SUPPORT_FAN_SPEED)?$`
            <div>
              <div class="flex-horizontal">
                <ha-select
                  .label=${this.hass.localize("ui.dialogs.more_info_control.vacuum.fan_speed")}
                  .disabled=${stateObj.state===UNAVAILABLE}
                  .value=${stateObj.attributes.fan_speed}
                  @selected=${this.handleFanSpeedChanged}
                  fixedMenuPosition
                  naturalMenuWidth
                  @closed=${stopPropagation}
                >
                  ${stateObj.attributes.fan_speed_list.map(mode=>$`
                      <mwc-list-item .value=${mode}>${mode}</mwc-list-item>
                    `)}
                </ha-select>
                <div
                  style="justify-content: center; align-self: center; padding-top: 1.3em"
                >
                  <span>
                    <ha-svg-icon .path=${mdiFan}></ha-svg-icon>
                    ${stateObj.attributes.fan_speed}
                  </span>
                </div>
              </div>
              <p></p>
            </div>
          `:""}

      <ha-attributes
        .hass=${this.hass}
        .stateObj=${this.stateObj}
        .extraFilters=${filterExtraAttributes}
      ></ha-attributes>
    `;}},{kind:"method",key:"callService",value:function callService(ev){const entry=ev.target.entry;this.hass.callService("vacuum",entry.serviceName,{entity_id:this.stateObj.entity_id});}},{kind:"method",key:"handleFanSpeedChanged",value:function handleFanSpeedChanged(ev){const oldVal=this.stateObj.attributes.fan_speed;const newVal=ev.target.value;if(!newVal||oldVal===newVal){return;}this.hass.callService("vacuum","set_fan_speed",{entity_id:this.stateObj.entity_id,fan_speed:newVal});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        line-height: 1.5;
      }
      .status-subtitle {
        color: var(--secondary-text-color);
      }
      .flex-horizontal {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
      }
    `;}}]};},s);
