const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, d$ as mdiPlayBoxMultiple, a9 as mdiVolumeOff, aa as mdiVolumeHigh, ab as mdiVolumeMinus, ac as mdiVolumePlus, e0 as mdiLoginVariant, bK as mdiMusicNote, r, n } from './main-dev.js';
import { af as computeMediaControls, s as supportsFeature, ag as SUPPORT_BROWSE_MEDIA, $ as SUPPORT_VOLUME_SET, a0 as SUPPORT_VOLUME_BUTTONS, a as UNAVAILABLE, U as UNKNOWN, a2 as SUPPORT_VOLUME_MUTE, ah as SUPPORT_SELECT_SOURCE, ai as SUPPORT_SELECT_SOUND_MODE, z as isComponentLoaded, aj as SUPPORT_PLAY_MEDIA } from './auth-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';
import { s as showMediaBrowserDialog } from './show-media-browser-dialog-dev.js';

_decorate([n("more-info-media_player")],function(_initialize,_LitElement){class MoreInfoMediaPlayer extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoMediaPlayer,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"method",key:"render",value:function render(){var _stateObj$attributes$,_stateObj$attributes$2;if(!this.stateObj){return $``;}const stateObj=this.stateObj;const controls=computeMediaControls(stateObj);return $`
      <div class="controls">
        <div class="basic-controls">
          ${!controls?"":controls.map(control=>$`
                  <ha-icon-button
                    action=${control.action}
                    @click=${this._handleClick}
                    .path=${control.icon}
                    .label=${this.hass.localize(`ui.card.media_player.${control.action}`)}
                  >
                  </ha-icon-button>
                `)}
        </div>
        ${supportsFeature(stateObj,SUPPORT_BROWSE_MEDIA)?$`
              <mwc-button
                .label=${this.hass.localize("ui.card.media_player.browse_media")}
                @click=${this._showBrowseMedia}
              >
                <ha-svg-icon
                  .path=${mdiPlayBoxMultiple}
                  slot="icon"
                ></ha-svg-icon>
              </mwc-button>
            `:""}
      </div>
      ${(supportsFeature(stateObj,SUPPORT_VOLUME_SET)||supportsFeature(stateObj,SUPPORT_VOLUME_BUTTONS))&&![UNAVAILABLE,UNKNOWN,"off"].includes(stateObj.state)?$`
            <div class="volume">
              ${supportsFeature(stateObj,SUPPORT_VOLUME_MUTE)?$`
                    <ha-icon-button
                      .path=${stateObj.attributes.is_volume_muted?mdiVolumeOff:mdiVolumeHigh}
                      @click=${this._toggleMute}
                    ></ha-icon-button>
                  `:""}
              ${supportsFeature(stateObj,SUPPORT_VOLUME_BUTTONS)?$`
                    <ha-icon-button
                      action="volume_down"
                      .path=${mdiVolumeMinus}
                      @click=${this._handleClick}
                    ></ha-icon-button>
                    <ha-icon-button
                      action="volume_up"
                      .path=${mdiVolumePlus}
                      @click=${this._handleClick}
                    ></ha-icon-button>
                  `:""}
              ${supportsFeature(stateObj,SUPPORT_VOLUME_SET)?$`
                    <ha-slider
                      id="input"
                      pin
                      ignore-bar-touch
                      .dir=${computeRTLDirection(this.hass)}
                      .value=${Number(stateObj.attributes.volume_level)*100}
                      @change=${this._selectedValueChanged}
                    ></ha-slider>
                  `:""}
            </div>
          `:""}
      ${![UNAVAILABLE,UNKNOWN,"off"].includes(stateObj.state)&&supportsFeature(stateObj,SUPPORT_SELECT_SOURCE)&&(_stateObj$attributes$=stateObj.attributes.source_list)!==null&&_stateObj$attributes$!==void 0&&_stateObj$attributes$.length?$`
            <div class="source-input">
              <ha-select
                .label=${this.hass.localize("ui.card.media_player.source")}
                icon
                .value=${stateObj.attributes.source}
                @selected=${this._handleSourceChanged}
                fixedMenuPosition
                naturalMenuWidth
                @closed=${stopPropagation}
              >
                ${stateObj.attributes.source_list.map(source=>$`
                      <mwc-list-item .value=${source}>${source}</mwc-list-item>
                    `)}
                <ha-svg-icon .path=${mdiLoginVariant} slot="icon"></ha-svg-icon>
              </ha-select>
            </div>
          `:""}
      ${supportsFeature(stateObj,SUPPORT_SELECT_SOUND_MODE)&&(_stateObj$attributes$2=stateObj.attributes.sound_mode_list)!==null&&_stateObj$attributes$2!==void 0&&_stateObj$attributes$2.length?$`
            <div class="sound-input">
              <ha-select
                .label=${this.hass.localize("ui.card.media_player.sound_mode")}
                .value=${stateObj.attributes.sound_mode}
                icon
                fixedMenuPosition
                naturalMenuWidth
                @selected=${this._handleSoundModeChanged}
                @closed=${stopPropagation}
              >
                ${stateObj.attributes.sound_mode_list.map(mode=>$`
                    <mwc-list-item .value=${mode}>${mode}</mwc-list-item>
                  `)}
                <ha-svg-icon .path=${mdiMusicNote} slot="icon"></ha-svg-icon>
              </ha-select>
            </div>
          `:""}
      ${isComponentLoaded(this.hass,"tts")&&supportsFeature(stateObj,SUPPORT_PLAY_MEDIA)?$`
            <div class="tts">
              Text to speech has moved to the media browser.
            </div>
          `:""}
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-icon-button[action="turn_off"],
      ha-icon-button[action="turn_on"],
      ha-slider {
        flex-grow: 1;
      }

      .controls {
        display: flex;
        align-items: center;
        --mdc-theme-primary: currentColor;
      }

      .basic-controls {
        flex-grow: 1;
      }

      .volume,
      .source-input,
      .sound-input {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }

      .source-input ha-select,
      .sound-input ha-select {
        margin-left: 10px;
        flex-grow: 1;
      }

      .tts {
        margin-top: 16px;
        font-style: italic;
      }

      mwc-button > ha-svg-icon {
        vertical-align: text-bottom;
      }
    `;}},{kind:"method",key:"_handleClick",value:function _handleClick(e){this.hass.callService("media_player",e.currentTarget.getAttribute("action"),{entity_id:this.stateObj.entity_id});}},{kind:"method",key:"_toggleMute",value:function _toggleMute(){this.hass.callService("media_player","volume_mute",{entity_id:this.stateObj.entity_id,is_volume_muted:!this.stateObj.attributes.is_volume_muted});}},{kind:"method",key:"_selectedValueChanged",value:function _selectedValueChanged(e){this.hass.callService("media_player","volume_set",{entity_id:this.stateObj.entity_id,volume_level:Number(e.currentTarget.getAttribute("value"))/100});}},{kind:"method",key:"_handleSourceChanged",value:function _handleSourceChanged(e){const newVal=e.target.value;if(!newVal||this.stateObj.attributes.source===newVal){return;}this.hass.callService("media_player","select_source",{entity_id:this.stateObj.entity_id,source:newVal});}},{kind:"method",key:"_handleSoundModeChanged",value:function _handleSoundModeChanged(e){var _this$stateObj;const newVal=e.target.value;if(!newVal||((_this$stateObj=this.stateObj)===null||_this$stateObj===void 0?void 0:_this$stateObj.attributes.sound_mode)===newVal){return;}this.hass.callService("media_player","select_sound_mode",{entity_id:this.stateObj.entity_id,sound_mode:newVal});}},{kind:"method",key:"_showBrowseMedia",value:function _showBrowseMedia(){showMediaBrowserDialog(this,{action:"play",entityId:this.stateObj.entity_id,mediaPickedCallback:pickedMedia=>this._playMedia(pickedMedia.item.media_content_id,pickedMedia.item.media_content_type)});}},{kind:"method",key:"_playMedia",value:function _playMedia(media_content_id,media_content_type){this.hass.callService("media_player","play_media",{entity_id:this.stateObj.entity_id,media_content_id,media_content_type});}}]};},s);
