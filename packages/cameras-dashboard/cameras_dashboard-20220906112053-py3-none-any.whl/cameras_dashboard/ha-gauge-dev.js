const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, af as y, I as i, r, n } from './main-dev.js';
import { f as formatNumber } from './auth-dev.js';
import { g as afterNextRender } from './stop_propagation-dev.js';

const normalize=(value,min,max)=>{if(isNaN(value)||isNaN(min)||isNaN(max)){// Not a number, return 0
return 0;}if(value>max)return max;if(value<min)return min;return value;};const getValueInPercentage=(value,min,max)=>{const newMax=max-min;const newVal=value-min;return 100*newVal/newMax;};

const getAngle=(value,min,max)=>{const percentage=getValueInPercentage(normalize(value,min,max),min,max);return percentage*180/100;};_decorate([n("ha-gauge")],function(_initialize,_LitElement){class Gauge extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:Gauge,d:[{kind:"field",decorators:[e({type:Number})],key:"min",value(){return 0;}},{kind:"field",decorators:[e({type:Number})],key:"max",value(){return 100;}},{kind:"field",decorators:[e({type:Number})],key:"value",value(){return 0;}},{kind:"field",decorators:[e({type:String})],key:"valueText",value:void 0},{kind:"field",decorators:[e()],key:"locale",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"needle",value:void 0},{kind:"field",decorators:[e()],key:"levels",value:void 0},{kind:"field",decorators:[e()],key:"label",value(){return "";}},{kind:"field",decorators:[t()],key:"_angle",value(){return 0;}},{kind:"field",decorators:[t()],key:"_updated",value(){return false;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(changedProperties){_get(_getPrototypeOf(Gauge.prototype),"firstUpdated",this).call(this,changedProperties);// Wait for the first render for the initial animation to work
afterNextRender(()=>{this._updated=true;this._angle=getAngle(this.value,this.min,this.max);this._rescale_svg();});}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(Gauge.prototype),"updated",this).call(this,changedProperties);if(!this._updated||!changedProperties.has("value")){return;}this._angle=getAngle(this.value,this.min,this.max);this._rescale_svg();}},{kind:"method",key:"render",value:function render(){return y`
      <svg viewBox="-50 -50 100 50" class="gauge">
        ${!this.needle||!this.levels?y`
           <path
          class="dial"
          d="M -40 0 A 40 40 0 0 1 40 0"
        ></path>
        `:""}

        ${this.levels?this.levels.sort((a,b)=>a.level-b.level).map((level,idx)=>{let firstPath;if(idx===0&&level.level!==this.min){const angle=getAngle(this.min,this.min,this.max);firstPath=y`<path
                        stroke="var(--accent-color)"
                        class="level"
                        d="M
                          ${0-40*Math.cos(angle*Math.PI/180)}
                          ${0-40*Math.sin(angle*Math.PI/180)}
                         A 40 40 0 0 1 40 0
                        "
                      ></path>`;}const angle=getAngle(level.level,this.min,this.max);return y`${firstPath}<path
                      stroke="${level.stroke}"
                      class="level"
                      d="M
                        ${0-40*Math.cos(angle*Math.PI/180)}
                        ${0-40*Math.sin(angle*Math.PI/180)}
                       A 40 40 0 0 1 40 0
                      "
                    ></path>`;}):""}
        ${this.needle?y`
            <!-- <path
                class="needle"
                d="M -25 -2.5 L -47.5 0 L -25 2.5 z"
                style=${i({transform:`rotate(${this._angle}deg)`})}
              > -->
              <!-- <path
                class="pointer"
                d="M -40 0 L -39.945 -0.142 z"
                style=${i({transform:`rotate(${this._angle}deg)`})}
              > -->
              <circle class="needle" style=${i({transform:`rotate(${this._angle}deg)`})} cx="-40" cy="0" r="5"/>

              `:y`<path
                class="value"
                d="M -40 0 A 40 40 0 1 0 40 0"
                style=${i({transform:`rotate(${this._angle}deg)`})}
              >`}
        </path>
        <path
          fill="var(--card-background-color, white)"
          opacity="1"
          d="M -46.6868 -8.7515 A 1 1 0 0 0 -32 -5.9878 L 31.9436 -5.9878 L 32.5 20 L -70 19 L -46.6868 -8.7515 M 31.9436 -5.9878 A 1 1 0 0 0 46.6868 -8.7515 L 64 20 L 32.5 20 L 31.9436 -5.9878"
        ></path>
      </svg>
      <svg class="text">
        <text class="value-text">
          ${this.valueText||formatNumber(this.value,this.locale)} ${this.label.substring(0,10)}
        </text>
      </svg>`;}},{kind:"method",key:"_rescale_svg",value:function _rescale_svg(){// Set the viewbox of the SVG containing the value to perfectly
// fit the text
// That way it will auto-scale correctly
const svgRoot=this.shadowRoot.querySelector(".text");const box=svgRoot.querySelector("text").getBBox();svgRoot.setAttribute("viewBox",`${box.x} ${box.y} ${box.width} ${box.height}`);}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        position: relative;
      }
      .dial {
        fill: none;
        stroke: var(--primary-background-color);
        stroke-width: 15;
        /* stroke-linecap: round; */
      }
      .value {
        fill: none;
        stroke-width: 15;
        stroke: var(--gauge-color);
        transition: all 1s cubic-bezier(0.19, 0.47, 0.25, 1) 0s;
        /* stroke-linecap: round; */
      }
      .pointer {
        fill: var(--primary-text-color);
        transition: all 1s ease 0s;
        stroke-width: 10;
        stroke-linecap: round;
      }
      .needle {
        fill: white;
        transition: all 1s ease 0s;
      }
      .level {
        fill: none;
        stroke-width: 15;
        /* stroke-linecap: round; */
      }
      .gauge {
        display: block;
      }
      .text {
        position: absolute;
        max-height: 40%;
        max-width: 120px;
        left: 50%;
        bottom: -6%;
        transform: translate(-50%, 0%);
      }
      .value-text {
        font-size: 1.2rem;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        max-width: 120px;
        fill: var(--primary-text-color);
        text-anchor: middle;
      }
    `;}}]};},s);
