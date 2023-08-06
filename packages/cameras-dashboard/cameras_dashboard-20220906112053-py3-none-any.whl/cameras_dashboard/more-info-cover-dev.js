const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, G as i, $, z as o, r, n } from './main-dev.js';
import './ha-more-info-dialog-dev.js';
import './ha-labeled-slider-dev.js';
import { a as UNAVAILABLE, h as UNAVAILABLE_STATES } from './auth-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

//   "M3.4375 16.1041L13 6.56246L22.5625 16.1041L25.5 13.1666L13 0.666626L0.5 13.1666L3.4375 16.1041Z";
// const pause =
//   "M17.1667 29.5833H25.5V0.416626H17.1667V29.5833ZM0.5 29.5833H8.83333V0.416626H0.5V29.5833Z";
const arrowDown="M3.4375 0.391357L13 9.95386L22.5625 0.391357L25.5 3.34969L13 15.8497L0.5 3.34969L3.4375 0.391357Z";_decorate([n("more-info-cover")],function(_initialize,_LitElement){class MoreInfoCover extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoCover,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"field",decorators:[i(".sc-blind-selector-picker")],key:"picker",value:void 0},{kind:"field",decorators:[i(".sc-blind-selector-slide")],key:"slide",value:void 0},{kind:"field",decorators:[i(".sc-blind-selector-picture")],key:"picture",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"isUpdating",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"invertPercentage",value:void 0},{kind:"field",key:"maxPosition",value:void 0},{kind:"field",key:"minPosition",value:void 0},{kind:"method",key:"firstUpdated",value:function firstUpdated(){this.slide.style.height=this.maxPosition-this.minPosition+"px";["mousedown","touchstart","pointerdown"].forEach(type=>{var _this$picker;(_this$picker=this.picker)===null||_this$picker===void 0?void 0:_this$picker.addEventListener(type,this._mouseDown);});this.maxPosition=156;this.minPosition=0;this.isUpdating=false;}},{kind:"method",key:"render",value:function render(){if(!this.stateObj){return $``;}this.stateObj=this.hass.states[this.stateObj.entity_id];return $`
      <div
        class="sc-blind-position ${o({positionNull:this.stateObj.state===UNAVAILABLE})}"
        @change=${this.setPickerPosition(100-this.stateObj.attributes.current_position)}
      >
        ${this.stateObj.attributes.current_position} %
      </div>
      <div class="container">
        <div
          class="sc-blind-middle"
          .disabled=${UNAVAILABLE_STATES.includes(this.stateObj.state)}
        >
          <div class="sc-blind-selector">
            <div
              class="blindOpen ${o({"state-on":this.stateObj.state==="open"||this.stateObj.state==="opening"||this.stateObj.state==="closing","state-unavailable":this.stateObj.state===UNAVAILABLE})}"
            >
              <svg
                class="sc-blind-selector-picture
                ${o({"state-unavailable":this.stateObj.state===UNAVAILABLE})}"
                viewBox="0 0 50 50"
                height="100%"
                width="100%"
              >
                <path
                  d="M45.4199 5H5.08989C4.69989 5 4.38989 5.31 4.38989 5.7V44.88C4.38989 45.27 4.69989 45.58 5.08989 45.58H45.4199C45.8099 45.58 46.1199 45.27 46.1199 44.88V5.7C46.1199 5.31 45.7999 5 45.4199 5ZM24.7199 42.36C24.7199 42.63 24.4999 42.85 24.2299 42.85H6.52989C6.25989 42.85 6.03989 42.63 6.03989 42.36V7.71C6.03989 7.44 6.25989 7.22 6.52989 7.22H24.2299C24.4999 7.22 24.7199 7.44 24.7199 7.71V42.36ZM44.7999 43.35C44.7999 43.62 44.5799 43.84 44.3099 43.84H26.5299C26.2599 43.84 26.0399 43.62 26.0399 43.35V7.67C26.0399 7.4 26.2599 7.18 26.5299 7.18H44.2999C44.5699 7.18 44.7899 7.4 44.7899 7.67V43.35H44.7999Z"
                />
              </svg>
              <svg
                class="top-bar"
                viewBox="0 0 50 50"
                height="100%"
                width="100%"
              >
                <path
                  d="M45.83 8.21H4.66997C4.27997 8.21 3.96997 7.9 3.96997 7.51V5.45C3.96997 5.06 4.27997 4.75 4.66997 4.75H45.82C46.21 4.75 46.52 5.06 46.52 5.45V7.51C46.53 7.89 46.21 8.21 45.83 8.21Z"
                />
              </svg>
            </div>
            <div
              class="sc-blind-selector-slide
            ${o({"state-unavailable":this.stateObj.state===UNAVAILABLE})}"
            ></div>
            <svg
              class="sc-blind-selector-picker ${o({"state-unavailable":this.stateObj.state===UNAVAILABLE})}"
              viewBox="0 0 50 50"
              height="100%"
              width="100%"
            >
              <path
                d="M5.54004 44.58C5.54004 44.75 5.67004 44.88 5.84004 44.88H44.66C44.79 44.88 44.87 44.79 44.92 44.68C44.93 44.65 44.96 44.62 44.96 44.58V43.98H5.54004V44.58Z"
                fill="#B3B3B3"
              />
            </svg>
          </div>
          ${UNAVAILABLE_STATES.includes(this.stateObj.state)?$` <unavailable-icon
                class="icon-unavailable"
              ></unavailable-icon>`:$``}
          <div id="buttons">
            <div class="buttons">
              <button
                class="openButton ${o({"state-on":this.stateObj.state==="opening","state-unavailable":this.stateObj.state===UNAVAILABLE})}"
                .label=${this.hass.localize("ui.dialogs.more_info_control.opencover")}
                @click=${this.onOpenTap}
              >
                <ha-svg-icon
                  id="arrow-icon"
                  .path=${"M3.4375 16.1041L13 6.56246L22.5625 16.1041L25.5 13.1666L13 0.666626L0.5 13.1666L3.4375 16.1041Z"}
                >
                </ha-svg-icon>
              </button>
            </div>
            <div class="buttons">
              <button
                class="pause
                ${o({"state-unavailable":this.stateObj.state===UNAVAILABLE})}"
                .label=${this.hass.localize("ui.dialogs.more_info_control.stopcover")}
                @click=${this.onStopTap}
              >
                <ha-svg-icon
                  id="arrow-icon-middle"
                  .path=${"M17.1667 29.5833H25.5V0.416626H17.1667V29.5833ZM0.5 29.5833H8.83333V0.416626H0.5V29.5833Z"}
                >
                </ha-svg-icon>
              </button>
            </div>
            <div class="buttons">
              <button
                class="closeButton ${o({"state-on":this.stateObj.state==="closing","state-unavailable":this.stateObj.state===UNAVAILABLE})}"
                .label=${this.hass.localize("ui.dialogs.more_info_control.closecover")}
                .path=${arrowDown}
                @click=${this.onCloseTap}
              >
                <ha-svg-icon
                  id="arrow-icon"
                  .path=${"M3.4375 0.391357L13 9.95386L22.5625 0.391357L25.5 3.34969L13 15.8497L0.5 3.34969L3.4375 0.391357Z"}
                >
                </ha-svg-icon>
              </button>
            </div>
          </div>
        </div>
      </div>
    `;}},{kind:"method",key:"getPictureTop",value:function getPictureTop(picture){if(!picture){return null;}const pictureBox=picture.getBoundingClientRect();const body=document.body;const docEl=document.documentElement;const scrollTop=window.pageYOffset||docEl.scrollTop||body.scrollTop;const clientTop=docEl.clientTop||body.clientTop||0;const pictureTop=pictureBox.top+scrollTop-clientTop;return pictureTop;}},{kind:"method",key:"setPickerPosition",value:function setPickerPosition(position){let realPos=this.maxPosition/100*position;if(realPos<this.minPosition)realPos=this.minPosition;if(realPos>this.maxPosition)realPos=this.maxPosition;const posTop=realPos-(this.maxPosition-this.minPosition);const slideHeight=realPos-this.minPosition;if(!this.hasUpdated){this.updateComplete.then(()=>{if(this.picker&&this.slide){this.slide.style.height=slideHeight+"px";this.picker.style.top=posTop+"px";}});}else if(this.picker&&this.slide){this.slide.style.height=slideHeight+"px";this.picker.style.top=posTop+"px";}}},{kind:"field",key:"_mouseDown",value(){return event=>{var _this$shadowRoot,_this$shadowRoot2,_this$shadowRoot3,_this$shadowRoot4,_this$shadowRoot5,_this$shadowRoot6;if(event.cancelable){// Disable default drag event
event.preventDefault();}this.isUpdating=true;(_this$shadowRoot=this.shadowRoot)===null||_this$shadowRoot===void 0?void 0:_this$shadowRoot.addEventListener("mousemove",this._mouseMove);(_this$shadowRoot2=this.shadowRoot)===null||_this$shadowRoot2===void 0?void 0:_this$shadowRoot2.addEventListener("touchmove",this._mouseMove);(_this$shadowRoot3=this.shadowRoot)===null||_this$shadowRoot3===void 0?void 0:_this$shadowRoot3.addEventListener("pointermove",this._mouseMove);(_this$shadowRoot4=this.shadowRoot)===null||_this$shadowRoot4===void 0?void 0:_this$shadowRoot4.addEventListener("mouseup",this._mouseUp);(_this$shadowRoot5=this.shadowRoot)===null||_this$shadowRoot5===void 0?void 0:_this$shadowRoot5.addEventListener("touchend",this._mouseUp);(_this$shadowRoot6=this.shadowRoot)===null||_this$shadowRoot6===void 0?void 0:_this$shadowRoot6.addEventListener("pointerup",this._mouseUp);};}},{kind:"field",key:"_mouseMove",value(){return event=>{const newPosition=(event.pageY-this.getPictureTop(this.slide))*100/this.maxPosition;this===null||this===void 0?void 0:this.setPickerPosition(newPosition);};}},{kind:"field",key:"_mouseUp",value(){return event=>{this.isUpdating=false;this.updateComplete.then(()=>{var _this$shadowRoot7,_this$shadowRoot8,_this$shadowRoot9,_this$shadowRoot10,_this$shadowRoot11,_this$shadowRoot12;let newPosition=event.pageY-this.getPictureTop(this.slide);if(newPosition<this.minPosition)newPosition=this===null||this===void 0?void 0:this.minPosition;if(newPosition>this.maxPosition)newPosition=this===null||this===void 0?void 0:this.maxPosition;const percentagePosition=(newPosition-this.minPosition)*100/(this.maxPosition-this.minPosition);this===null||this===void 0?void 0:this.setPickerPosition(newPosition*100/this.maxPosition);if(this.invertPercentage){this.updateBlindPosition(this.hass,this.stateObj.entity_id,percentagePosition);}else {this.updateBlindPosition(this.hass,this.stateObj.entity_id,100-percentagePosition);}(_this$shadowRoot7=this.shadowRoot)===null||_this$shadowRoot7===void 0?void 0:_this$shadowRoot7.removeEventListener("mousemove",this._mouseMove);(_this$shadowRoot8=this.shadowRoot)===null||_this$shadowRoot8===void 0?void 0:_this$shadowRoot8.removeEventListener("touchmove",this._mouseMove);(_this$shadowRoot9=this.shadowRoot)===null||_this$shadowRoot9===void 0?void 0:_this$shadowRoot9.removeEventListener("pointermove",this._mouseMove);(_this$shadowRoot10=this.shadowRoot)===null||_this$shadowRoot10===void 0?void 0:_this$shadowRoot10.removeEventListener("mouseup",this._mouseUp);(_this$shadowRoot11=this.shadowRoot)===null||_this$shadowRoot11===void 0?void 0:_this$shadowRoot11.removeEventListener("touchend",this._mouseUp);(_this$shadowRoot12=this.shadowRoot)===null||_this$shadowRoot12===void 0?void 0:_this$shadowRoot12.removeEventListener("pointerup",this._mouseUp);});};}},{kind:"method",key:"updateBlindPosition",value:function updateBlindPosition(hass,entity,position){const blindPosition=Math.round(position);hass.callService("cover","set_cover_position",{entity_id:entity,position:blindPosition});}},{kind:"method",key:"onOpenTap",value:function onOpenTap(){this.hass.callService("cover","open_cover",{entity_id:this.stateObj.entity_id});}},{kind:"method",key:"onStopTap",value:function onStopTap(){this.hass.callService("cover","stop_cover",{entity_id:this.stateObj.entity_id});}},{kind:"method",key:"onCloseTap",value:function onCloseTap(){this.hass.callService("cover","close_cover",{entity_id:this.stateObj.entity_id});}},{kind:"field",key:"computeActiveState",value(){return stateObj=>stateObj===null||stateObj===void 0?void 0:stateObj.state;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .current_position,
      .tilt {
        max-height: 0px;
        overflow: hidden;
      }

      .has-set_position .current_position,
      .has-current_position .current_position,
      .has-open_tilt .tilt,
      .has-close_tilt .tilt,
      .has-stop_tilt .tilt,
      .has-set_tilt_position .tilt,
      .has-current_tilt_position .tilt {
        max-height: 208px;
      }

      .title {
        margin: 5px 0 8px;
        color: var(--primary-text-color);
      }
      svg {
        display: block;
        .state-on {
          transform: scale(0);
        }
      }

      .more-info {
        position: absolute;
        cursor: pointer;
        top: 0;
        right: 0;
        color: var(--secondary-text-color);
        z-index: 1;
      }

      .buttons:hover {
        cursor: pointer;
      }

      .hassbut.state-off {
        text-align: left;
      }

      .hassbut.state-on {
        text-align: left;
      }

      .hassbut {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .blind-closed {
        position: absolute;
        top: 0;
      }
      .ha-status-icon {
        display: flex;
        justify-content: center;
      }
      .sc-blind-selector {
        position: absolute;
        top: 5px;
        left: -33px;
        width: 210px;
        height: 210px;
      }
      .sc-blind-position {
        display: flex;
        color: var(--secondary-text-color);
        font-size: 18px;
        width: 100%;
        position: relative;
        top: 24px;
        justify-content: center;
      }
      .sc-blind-label {
        color: var(--primary-text-color);
        padding-top: 5px;
        height: 100%;
        padding-bottom: 23px;
        font-size: 2.3rem;
        font-weight: 450;
        white-space: nowrap;
        display: inline-block;
        overflow-x: hidden;
        max-width: 80%;
        text-overflow: ellipsis;
        justify-content: space-between;
      }
      .sc-blind-selector-picture {
        position: relative;
        fill: #666666;
      }
      .top-bar {
        position: absolute;
        fill: #666666;
        width: 100%;
        top: 0px;
        right: 0px;
      }
      .sc-blind-selector-slide {
        background-color: var(--slider-track-color);
        position: absolute;
        cursor: row-resize;
        height: 100%;
        max-width: 230px;
        min-width: 174px;
        max-height: 156px;
        top: 33px;
        left: 19px;
      }
      .sc-blind-selector-picker {
        cursor: row-resize;
        position: absolute;
        top: 0;
        width: 100%;
        height: 100%;
      }
      .sc-blind-middle {
        display: flex;
        align-items: center;
        position: relative;
        justify-content: center;
        width: 200px;
        height: 200px;
      }
      .window {
        overflow-y: hidden;
        width: 230px;
        height: 172px;
        position: absolute;
        left: 98px;
      }
      .container {
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 8px;
        margin-bottom: 25px;
      }
      #buttons {
        top: 22px;
        position: absolute;
        left: 170px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      .buttons {
        width: 43px;
        margin: 8px 0;
      }
      .state-div {
        align-items: left;
        padding-top: 19px;
        padding-bottom: 6px;
      }

      .name-div {
        align-items: left;
        padding: 12% 100% 1% 0%;
      }

      #arrow-icon {
        margin-top: 5px;
        height: 20px;
        width: 15px;
        fill: var(--card-background-color);
      }

      #arrow-icon-middle {
        height: 20px;
        width: 15px;
        fill: var(--card-background-color);
      }
      .more-info {
        position: absolute;
        cursor: pointer;
        top: 0;
        right: 0;
        border-radius: 100%;
        color: var(--secondary-text-color);
        z-index: 1;
      }

      @media only screen and (max-width: 600px) {
        #arrow-icon {
          margin-top: 4px;
          height: 20px;
          width: 15px;
          fill: var(--card-background-color);
        }
        #arrow-icon-middle {
          padding: 0;
          margin: 0;
          height: 20px;
          width: 15px;
          fill: var(--card-background-color);
        }
        .sc-blind-position {
          display: flex;
          color: var(--secondary-text-color);
          font-size: 18px;
          width: 100%;
          position: relative;
          top: 24px;
          justify-content: center;
        }
      }

      .positionNull {
        display: none;
      }
      button {
        background-color: var(--secondary-text-color);
        cursor: pointer;
        fill: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        visibility: visible;
        width: 43px;
        height: 43px;
        border-radius: 8px;
        border-width: 0;
      }
      .openButton.state-on {
        background-color: var(--header-card-picker-background) !important;
      }
      .openButton.state-on > #arrow-icon {
        fill: var(--accent-color);
      }
      .blindOpen.state-on > svg {
        fill: var(--accent-color);
      }
      .closeButton.state-on {
        background-color: var(--header-card-picker-background) !important;
      }
      .closeButton.state-on > #arrow-icon {
        fill: var(--accent-color);
      }
      .state-unavailable {
        color: var(--state-icon-unavailable-color, #bdbdbd);
        pointer-events: none;
      }
      .icon-unavailable {
        z-index: 1;
        position: absolute;
        top: 50%;
        left: 32%;
      }
      .pause:active,
      .blindOpen:active,
      .closeButton:active {
        background-color: var(--header-card-picker-background) !important;
      }
      .pause:active > #arrow-icon {
        fill: var(--accent-color);
      }
    `;}}]};},s);
