const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, r } from './main-dev.js';
import { z as isComponentLoaded, s as supportsFeature } from './auth-dev.js';
import { C as CAMERA_SUPPORT_STREAM, S as STREAM_TYPE_HLS, f as fetchCameraPrefs, u as updateCameraPrefs } from './ha-more-info-dialog-dev.js';
import './ha-checkbox-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './mwc-checkbox.css-dev.js';

let MoreInfoCamera=_decorate(null,function(_initialize,_LitElement){class MoreInfoCamera extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoCamera,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"field",decorators:[t()],key:"_cameraPrefs",value:void 0},{kind:"field",decorators:[t()],key:"_attached",value(){return false;}},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(MoreInfoCamera.prototype),"connectedCallback",this).call(this);this._attached=true;}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){_get(_getPrototypeOf(MoreInfoCamera.prototype),"disconnectedCallback",this).call(this);this._attached=false;}},{kind:"method",key:"render",value:function render(){if(!this._attached||!this.hass||!this.stateObj){return $``;}return $`
      <ha-camera-stream
        .hass=${this.hass}
        .stateObj=${this.stateObj}
        allow-exoplayer
        controls
      ></ha-camera-stream>
      ${this._cameraPrefs&&false?$`
            <ha-formfield label="Preload stream">
              <ha-checkbox
                .checked=${this._cameraPrefs.preload_stream}
                @change=${this._handleCheckboxChanged}
              >
              </ha-checkbox>
            </ha-formfield>
          `:undefined}
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){if(!changedProps.has("stateObj")){return;}const oldState=changedProps.get("stateObj");const oldEntityId=oldState?oldState.entity_id:undefined;const curEntityId=this.stateObj?this.stateObj.entity_id:undefined;// Same entity, ignore.
if(curEntityId===oldEntityId){return;}if(curEntityId&&isComponentLoaded(this.hass,"stream")&&supportsFeature(this.stateObj,CAMERA_SUPPORT_STREAM)&&// The stream component for HLS streams supports a server-side pre-load
// option that client initiated WebRTC streams do not
this.stateObj.attributes.frontend_stream_type===STREAM_TYPE_HLS){// Fetch in background while we set up the video.
this._fetchCameraPrefs();}}},{kind:"method",key:"_fetchCameraPrefs",value:async function _fetchCameraPrefs(){this._cameraPrefs=await fetchCameraPrefs(this.hass,this.stateObj.entity_id);}},{kind:"method",key:"_handleCheckboxChanged",value:async function _handleCheckboxChanged(ev){const checkbox=ev.currentTarget;try{this._cameraPrefs=await updateCameraPrefs(this.hass,this.stateObj.entity_id,{preload_stream:checkbox.checked});}catch(err){alert(err.message);checkbox.checked=!checkbox.checked;}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
        position: relative;
        padding-bottom: 20px;
      }
      ha-formfield {
        position: absolute;
        top: 0;
        right: 0;
        background-color: var(--secondary-background-color);
        padding-right: 16px;
        border-bottom-left-radius: 4px;
      }
    `;}}]};},s);customElements.define("more-info-camera",MoreInfoCamera);
