const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, z as o, r, n } from './main-dev.js';
import './ha-labeled-slider-dev.js';
import './stop_propagation-dev.js';
import './auth-dev.js';

/*
 * @appliesMixin EventsMixin
 */function trigger(element,type){if(!element||!type){return;}// Create and dispatch the event
const event=new Event(type,{bubbles:true});// Dispatch the event
element.dispatchEvent(event);}function getDecimalPlaces(value){const match=`${value}`.match(/(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/);if(!match){return 0;}return Math.max(0,// Number of digits right of decimal point.
(match[1]?match[1].length:0)-(// Adjust for scientific notation.
match[2]?+match[2]:0));}function round(number,step){if(step<1){const places=getDecimalPlaces(step);return parseFloat(number.toFixed(places));}return Math.round(number/step)*step;}_decorate([n("more-info-fan")],function(_initialize,_LitElement){class MoreInfoFan extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoFan,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"oscillationToggleChecked",value(){return false;}},{kind:"field",decorators:[e({type:String})],key:"percentageSliderValue",value(){return "0";}},{kind:"field",decorators:[e({attribute:false})],key:"actionRows",value(){return [];}},{kind:"field",decorators:[e({attribute:false})],key:"settingsOn",value(){return true;}},{kind:"method",key:"get",value:function get(event){const confthumbWidth=0;const input=event.target;const touch=event.changedTouches[0];const min=parseFloat(input.getAttribute("min"))||0;const max=parseFloat(input.getAttribute("max"))||100;const step=parseFloat(input.getAttribute("step"))||1;const delta=max-min;// Calculate percentage
let percent;const clientRect=input.getBoundingClientRect();const thumbWidth=100/clientRect.width*(confthumbWidth/2)/100;// Determine left percentage
{percent=100-100/clientRect.height*(touch.clientY-clientRect.top);}// Don't allow outside bounds
if(percent<0){percent=0;}else if(percent>100){percent=100;}// Factor in the thumb offset
if(percent<50){percent-=(100-percent*2)*thumbWidth;}else if(percent>50){percent+=(percent-50)*2*thumbWidth;}// Find the closest step to the mouse position
return min+round(delta*(percent/100),step);}},{kind:"method",key:"set",value:function set(event){// Prevent text highlight on iOS
event.preventDefault();// Set value
// eslint-disable-next-line no-param-reassign
event.target.value=this.get(event);// Trigger event
trigger(event.target,event.type==="touchend"?"change":"input");}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){if("ontouchstart"in document.documentElement){// console.log("firstUpdated", this.shadowRoot!.getElementById("iosSlider"));
const slider=this.shadowRoot.getElementById("iosSlider");slider.style.userSelect="none";slider.style.touchAction="manipulation";// Listen for events
["touchstart","touchmove","touchend"].forEach(type=>{slider.addEventListener(type,event=>this.set(event),false);});}}},{kind:"method",key:"render",value:function render(){var _this$stateObj;return $`
      <div class="sliderContent">
        <div class="range-holder">
          <input
            type="range"
            id="iosSlider"
            class="iosSlider ${o({// sliderOff: this.stateObj?.state === "off",
})}"
            list="steplist"
            step="33"
            value="0"
            min="0"
            max="99"
            style=" --slider-width: 150px;
              --slider-height: 378px; --slider-border-radius: 40px;
               --slider-thumb-color:#ddd;
              "
            .value=${((_this$stateObj=this.stateObj)===null||_this$stateObj===void 0?void 0:_this$stateObj.state)==="off"?String(0):String(this.percentageSliderValue)}
            @change=${this.percentageChanged}
          />
          <div class="datals">
            <span class="opt"></span>
            <span class="opt"></span>
            <span class="opt"></span>
          </div>
          <svg
            version="1.1"
            id="Camada_1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            x="0px"
            y="0px"
            viewBox="0 0 150 95"
            style="enable-background:new 0 0 150 95;"
            xml:space="preserve"
          >
            <path
              class="st0"
              d="M0,55c0,22.1,17.9,40,40,40h70c22.1,0,40-17.9,40-40V0H0V55z"
            />
          </svg>
        </div>
      </div>
    `;}},{kind:"method",key:"presetModeChanged",value:function presetModeChanged(ev){var _this$stateObj2,_this$stateObj3;const oldVal=(_this$stateObj2=this.stateObj)===null||_this$stateObj2===void 0?void 0:_this$stateObj2.attributes.preset_mode;const newVal=ev.target.value;if(!newVal||oldVal===newVal)return;this.hass.callService("fan","set_preset_mode",{entity_id:(_this$stateObj3=this.stateObj)===null||_this$stateObj3===void 0?void 0:_this$stateObj3.entity_id,preset_mode:newVal});}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){if(!changedProps.has("stateObj")){return;}const oldVal=changedProps.get("stateObj");const newVal=this.stateObj;if(newVal){this.oscillationToggleChecked=newVal.attributes.oscillating;this.percentageSliderValue=newVal.attributes.percentage;}if(newVal.state==="on"){// Don't change tab when the color mode changes
if((oldVal===null||oldVal===void 0?void 0:oldVal.entity_id)!==newVal.entity_id||(oldVal===null||oldVal===void 0?void 0:oldVal.attributes.percentage)!==newVal.attributes.percentage){this.oscillationToggleChecked=newVal.attributes.oscillating;this.percentageSliderValue=newVal.attributes.percentage;}else {this.percentageSliderValue="0";}}}},{kind:"method",key:"stopPropagation",value:function stopPropagation(ev){ev.stopPropagation();}},{kind:"method",key:"percentageChanged",value:function percentageChanged(ev){var _this$stateObj4;const oldVal=parseInt(this.stateObj.attributes.percentage,10);const newVal=ev.target.value;if(isNaN(newVal)||oldVal===newVal)return;this.percentageSliderValue=newVal;this.hass.callService("fan","set_percentage",{entity_id:(_this$stateObj4=this.stateObj)===null||_this$stateObj4===void 0?void 0:_this$stateObj4.entity_id,percentage:newVal});}},{kind:"method",key:"oscillationToggleChanged",value:function oscillationToggleChanged(ev){var _this$stateObj5,_this$stateObj6;const oldVal=(_this$stateObj5=this.stateObj)===null||_this$stateObj5===void 0?void 0:_this$stateObj5.attributes.oscillating;const newVal=ev.target.checked;if(oldVal===newVal)return;this.hass.callService("fan","oscillate",{entity_id:(_this$stateObj6=this.stateObj)===null||_this$stateObj6===void 0?void 0:_this$stateObj6.entity_id,oscillating:newVal});}},{kind:"method",key:"onDirectionReverse",value:function onDirectionReverse(){var _this$stateObj7;this.hass.callService("fan","set_direction",{entity_id:(_this$stateObj7=this.stateObj)===null||_this$stateObj7===void 0?void 0:_this$stateObj7.entity_id,direction:"reverse"});}},{kind:"method",key:"onDirectionForward",value:function onDirectionForward(){var _this$stateObj8;this.hass.callService("fan","set_direction",{entity_id:(_this$stateObj8=this.stateObj)===null||_this$stateObj8===void 0?void 0:_this$stateObj8.entity_id,direction:"forward"});}},{kind:"method",key:"computeIsRotatingReverse",value:function computeIsRotatingReverse(stateObj){return stateObj.attributes.direction==="reverse";}},{kind:"method",key:"computeIsRotatingForward",value:function computeIsRotatingForward(stateObj){return stateObj.attributes.direction==="forward";}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      #Camada_1 {
        position: absolute;
        bottom: 0;
        width: calc(100% + 1px);
        height: auto;
        /* right: calc(50% - (380px / 2)); */
        fill: grey;
        user-select: none;
        pointer-events: none;
      }

      .range-holder {
        --slider-height: 379px;
        --slider-width: 150px;
        height: var(--slider-height);
        width: var(--slider-width);
        position: relative;
        display: block;
        overflow: hidden;
      }
      .range-holder input[type="range"] {
        outline: 0;
        border: 0;
        border-radius: var(--slider-border-radius, 12px);
        width: var(--slider-height);
        margin: 0;
        transition: box-shadow 0.2s ease-in-out;
        -webkit-transform: rotate(270deg);
        -moz-transform: rotate(270deg);
        -o-transform: rotate(270deg);
        -ms-transform: rotate(270deg);
        transform: rotate(270deg);
        overflow: hidden;
        height: var(--slider-width);
        -webkit-appearance: none;
        background-color: var(--slider-track-color);
        position: absolute;
        top: calc(50% - (var(--slider-width) / 2));
        right: calc(50% - (var(--slider-height) / 2));
      }
      .range-holder input[type="range"]::-webkit-slider-runnable-track {
        height: var(--slider-width);
        -webkit-appearance: none;
        background-color: var(--slider-track-color);
        margin-top: -1px;
        transition: box-shadow 0.2s ease-in-out;
      }
      .range-holder input[type="range"]::-webkit-slider-thumb {
        width: calc(var(--slider-height) / 4);
        border-right: 10px solid var(--slider-color);
        border-left: 10px solid var(--slider-color);
        border-top: 20px solid var(--slider-color);
        border-bottom: 20px solid var(--slider-color);
        -webkit-appearance: none;
        height: 0px;
        cursor: grabbing;
        background: var(--slider-color);
        box-shadow: -350px 0 0 350px var(--slider-color),
          inset 0 0 0 80px var(--slider-thumb-color);
        border-radius: 0;
        transition: box-shadow 0.2s ease-in-out;
        position: relative;
        top: calc((var(--slider-width) - 80px) / 2);
      }
      .range-holder input[type="range"]::-moz-thumb-track {
        height: var(--slider-width);
        background-color: var(--slider-track-color);
        margin-top: -1px;
        transition: box-shadow 0.2s ease-in-out;
      }
      .range-holder input[type="range"]::-moz-range-thumb {
        width: 0px;
        border-right: 12px solid var(--slider-color);
        border-left: 12px solid var(--slider-color);
        border-top: 20px solid var(--slider-color);
        border-bottom: 20px solid var(--slider-color);
        height: calc(var(--slider-width) * 0.4);
        cursor: grabbing;
        background: var(--slider-color);
        box-shadow: -350px 0 0 350px var(--slider-color),
          inset 0 0 0 80px var(--slider-thumb-color);
        border-radius: 0;
        transition: box-shadow 0.2s ease-in-out;
        position: relative;
        top: calc((var(--slider-width) - 80px) / 2);
      }
      .iosSlider {
        --slider-color: var(--accent-color);
      }
      .sliderOff {
        --slider-color: grey;
      }
      .sliderContent {
        margin: 50px 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      @media only screen and (max-width: 600px) {
        .sliderContent {
          margin-top: 50%;
          margin-bottom: 50px;
          width: 100%;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
        }
      }
      .datals {
        height: 380px;
        width: 150px;
        display: grid;
        grid-template-columns: repeat(1, 100%);
        grid-template-rows: repeat(4, 25%);
        position: absolute;
        top: 0;
        /* right: calc(50% - (380px / 2)); */
        user-select: none;
        pointer-events: none;
      }

      .opt {
        content: "";
        display: block;
        border-bottom: 1px solid grey;
        width: 100%;
        z-index: 2;
        user-select: none;
        pointer-events: none;
      }

      .range__list__opt:before {
        content: "";
        display: block;
        width: 0;
        height: auto;
        padding-left: 3px;
        text-indent: 0;
      }
    `;}}]};},s);// customElements.define("more-info-fan", MoreInfoFan);
