const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { dA as o, ah as __decorate, d as e$1, bq as ariaProperty, c as s, $, z as o$1, I as i, Q as l, r, n, _ as _decorate, j as _get, k as _getPrototypeOf } from './main-dev.js';

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function e(e){return o({descriptor:r=>({get(){var r,o;return null!==(o=null===(r=this.renderRoot)||void 0===r?void 0:r.querySelectorAll(e))&&void 0!==o?o:[];},enumerable:!0,configurable:!0})});}

/** @soyCompatible */class CircularProgressBase extends s{constructor(){super(...arguments);this.indeterminate=false;this.progress=0;this.density=0;this.closed=false;}open(){this.closed=false;}close(){this.closed=true;}/**
     * @soyTemplate
     */render(){/** @classMap */const classes={'mdc-circular-progress--closed':this.closed,'mdc-circular-progress--indeterminate':this.indeterminate};const containerSideLength=48+this.density*4;/** @styleMap */const styles={'width':`${containerSideLength}px`,'height':`${containerSideLength}px`};return $`
      <div
        class="mdc-circular-progress ${o$1(classes)}"
        style="${i(styles)}"
        role="progressbar"
        aria-label="${l(this.ariaLabel)}"
        aria-valuemin="0"
        aria-valuemax="1"
        aria-valuenow="${l(this.indeterminate?undefined:this.progress)}">
        ${this.renderDeterminateContainer()}
        ${this.renderIndeterminateContainer()}
      </div>`;}/**
     * @soyTemplate
     */renderDeterminateContainer(){const sideLength=48+this.density*4;const center=sideLength/2;const circleRadius=this.density>=-3?18+this.density*11/6:12.5+(this.density+3)*5/4;const circumference=2*3.1415926*circleRadius;const determinateStrokeDashOffset=(1-this.progress)*circumference;const strokeWidth=this.density>=-3?4+this.density*(1/3):3+(this.density+3)*(1/6);return $`
      <div class="mdc-circular-progress__determinate-container">
        <svg class="mdc-circular-progress__determinate-circle-graphic"
             viewBox="0 0 ${sideLength} ${sideLength}">
          <circle class="mdc-circular-progress__determinate-track"
                  cx="${center}" cy="${center}" r="${circleRadius}"
                  stroke-width="${strokeWidth}"></circle>
          <circle class="mdc-circular-progress__determinate-circle"
                  cx="${center}" cy="${center}" r="${circleRadius}"
                  stroke-dasharray="${2*3.1415926*circleRadius}"
                  stroke-dashoffset="${determinateStrokeDashOffset}"
                  stroke-width="${strokeWidth}"></circle>
        </svg>
      </div>`;}/**
     * @soyTemplate
     */renderIndeterminateContainer(){return $`
      <div class="mdc-circular-progress__indeterminate-container">
        <div class="mdc-circular-progress__spinner-layer">
          ${this.renderIndeterminateSpinnerLayer()}
        </div>
      </div>`;}/**
     * @soyTemplate
     */renderIndeterminateSpinnerLayer(){const sideLength=48+this.density*4;const center=sideLength/2;const circleRadius=this.density>=-3?18+this.density*11/6:12.5+(this.density+3)*5/4;const circumference=2*3.1415926*circleRadius;const halfCircumference=0.5*circumference;const strokeWidth=this.density>=-3?4+this.density*(1/3):3+(this.density+3)*(1/6);return $`
        <div class="mdc-circular-progress__circle-clipper mdc-circular-progress__circle-left">
          <svg class="mdc-circular-progress__indeterminate-circle-graphic"
               viewBox="0 0 ${sideLength} ${sideLength}">
            <circle cx="${center}" cy="${center}" r="${circleRadius}"
                    stroke-dasharray="${circumference}"
                    stroke-dashoffset="${halfCircumference}"
                    stroke-width="${strokeWidth}"></circle>
          </svg>
        </div>
        <div class="mdc-circular-progress__gap-patch">
          <svg class="mdc-circular-progress__indeterminate-circle-graphic"
               viewBox="0 0 ${sideLength} ${sideLength}">
            <circle cx="${center}" cy="${center}" r="${circleRadius}"
                    stroke-dasharray="${circumference}"
                    stroke-dashoffset="${halfCircumference}"
                    stroke-width="${strokeWidth*0.8}"></circle>
          </svg>
        </div>
        <div class="mdc-circular-progress__circle-clipper mdc-circular-progress__circle-right">
          <svg class="mdc-circular-progress__indeterminate-circle-graphic"
               viewBox="0 0 ${sideLength} ${sideLength}">
            <circle cx="${center}" cy="${center}" r="${circleRadius}"
                    stroke-dasharray="${circumference}"
                    stroke-dashoffset="${halfCircumference}"
                    stroke-width="${strokeWidth}"></circle>
          </svg>
        </div>`;}update(changedProperties){super.update(changedProperties);// Bound progress value in interval [0, 1].
if(changedProperties.has('progress')){if(this.progress>1){this.progress=1;}if(this.progress<0){this.progress=0;}}}}__decorate([e$1({type:Boolean,reflect:true})],CircularProgressBase.prototype,"indeterminate",void 0);__decorate([e$1({type:Number,reflect:true})],CircularProgressBase.prototype,"progress",void 0);__decorate([e$1({type:Number,reflect:true})],CircularProgressBase.prototype,"density",void 0);__decorate([e$1({type:Boolean,reflect:true})],CircularProgressBase.prototype,"closed",void 0);__decorate([ariaProperty,e$1({type:String,attribute:'aria-label'})],CircularProgressBase.prototype,"ariaLabel",void 0);

const styles=r`.mdc-circular-progress__determinate-circle,.mdc-circular-progress__indeterminate-circle-graphic{stroke:#6200ee;stroke:var(--mdc-theme-primary, #6200ee)}.mdc-circular-progress__determinate-track{stroke:transparent}@keyframes mdc-circular-progress-container-rotate{to{transform:rotate(360deg)}}@keyframes mdc-circular-progress-spinner-layer-rotate{12.5%{transform:rotate(135deg)}25%{transform:rotate(270deg)}37.5%{transform:rotate(405deg)}50%{transform:rotate(540deg)}62.5%{transform:rotate(675deg)}75%{transform:rotate(810deg)}87.5%{transform:rotate(945deg)}100%{transform:rotate(1080deg)}}@keyframes mdc-circular-progress-color-1-fade-in-out{from{opacity:.99}25%{opacity:.99}26%{opacity:0}89%{opacity:0}90%{opacity:.99}to{opacity:.99}}@keyframes mdc-circular-progress-color-2-fade-in-out{from{opacity:0}15%{opacity:0}25%{opacity:.99}50%{opacity:.99}51%{opacity:0}to{opacity:0}}@keyframes mdc-circular-progress-color-3-fade-in-out{from{opacity:0}40%{opacity:0}50%{opacity:.99}75%{opacity:.99}76%{opacity:0}to{opacity:0}}@keyframes mdc-circular-progress-color-4-fade-in-out{from{opacity:0}65%{opacity:0}75%{opacity:.99}90%{opacity:.99}to{opacity:0}}@keyframes mdc-circular-progress-left-spin{from{transform:rotate(265deg)}50%{transform:rotate(130deg)}to{transform:rotate(265deg)}}@keyframes mdc-circular-progress-right-spin{from{transform:rotate(-265deg)}50%{transform:rotate(-130deg)}to{transform:rotate(-265deg)}}.mdc-circular-progress{display:inline-flex;position:relative;direction:ltr;line-height:0;transition:opacity 250ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-circular-progress__determinate-container,.mdc-circular-progress__indeterminate-circle-graphic,.mdc-circular-progress__indeterminate-container,.mdc-circular-progress__spinner-layer{position:absolute;width:100%;height:100%}.mdc-circular-progress__determinate-container{transform:rotate(-90deg)}.mdc-circular-progress__indeterminate-container{font-size:0;letter-spacing:0;white-space:nowrap;opacity:0}.mdc-circular-progress__determinate-circle-graphic,.mdc-circular-progress__indeterminate-circle-graphic{fill:transparent}.mdc-circular-progress__determinate-circle{transition:stroke-dashoffset 500ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-circular-progress__gap-patch{position:absolute;top:0;left:47.5%;box-sizing:border-box;width:5%;height:100%;overflow:hidden}.mdc-circular-progress__gap-patch .mdc-circular-progress__indeterminate-circle-graphic{left:-900%;width:2000%;transform:rotate(180deg)}.mdc-circular-progress__circle-clipper{display:inline-flex;position:relative;width:50%;height:100%;overflow:hidden}.mdc-circular-progress__circle-clipper .mdc-circular-progress__indeterminate-circle-graphic{width:200%}.mdc-circular-progress__circle-right .mdc-circular-progress__indeterminate-circle-graphic{left:-100%}.mdc-circular-progress--indeterminate .mdc-circular-progress__determinate-container{opacity:0}.mdc-circular-progress--indeterminate .mdc-circular-progress__indeterminate-container{opacity:1}.mdc-circular-progress--indeterminate .mdc-circular-progress__indeterminate-container{animation:mdc-circular-progress-container-rotate 1568.2352941176ms linear infinite}.mdc-circular-progress--indeterminate .mdc-circular-progress__spinner-layer{animation:mdc-circular-progress-spinner-layer-rotate 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--indeterminate .mdc-circular-progress__color-1{animation:mdc-circular-progress-spinner-layer-rotate 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both,mdc-circular-progress-color-1-fade-in-out 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--indeterminate .mdc-circular-progress__color-2{animation:mdc-circular-progress-spinner-layer-rotate 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both,mdc-circular-progress-color-2-fade-in-out 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--indeterminate .mdc-circular-progress__color-3{animation:mdc-circular-progress-spinner-layer-rotate 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both,mdc-circular-progress-color-3-fade-in-out 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--indeterminate .mdc-circular-progress__color-4{animation:mdc-circular-progress-spinner-layer-rotate 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both,mdc-circular-progress-color-4-fade-in-out 5332ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--indeterminate .mdc-circular-progress__circle-left .mdc-circular-progress__indeterminate-circle-graphic{animation:mdc-circular-progress-left-spin 1333ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--indeterminate .mdc-circular-progress__circle-right .mdc-circular-progress__indeterminate-circle-graphic{animation:mdc-circular-progress-right-spin 1333ms cubic-bezier(0.4, 0, 0.2, 1) infinite both}.mdc-circular-progress--closed{opacity:0}:host{display:inline-flex}.mdc-circular-progress__determinate-track{stroke:transparent;stroke:var(--mdc-circular-progress-track-color, transparent)}`;

/** @soyCompatible */let CircularProgress=class CircularProgress extends CircularProgressBase{};CircularProgress.styles=[styles];CircularProgress=__decorate([n('mwc-circular-progress')],CircularProgress);

_decorate([n("ha-circular-progress")],function(_initialize,_CircularProgress){class HaCircularProgress extends _CircularProgress{constructor(...args){super(...args);_initialize(this);}}return {F:HaCircularProgress,d:[{kind:"field",decorators:[e$1({type:Boolean})],key:"active",value(){return false;}},{kind:"field",decorators:[e$1()],key:"alt",value(){return "Loading";}},{kind:"field",decorators:[e$1()],key:"size",value(){return "medium";}},{kind:"set",key:"density",value:// @ts-ignore
function density(_){// just a dummy
}},{kind:"get",key:"density",value:function density(){switch(this.size){case"tiny":return -8;case"small":return -5;case"medium":return 0;case"large":return 5;default:return 0;}}// @ts-ignore
},{kind:"set",key:"indeterminate",value:function indeterminate(_){// just a dummy
}},{kind:"get",key:"indeterminate",value:function indeterminate(){return this.active;}},{kind:"get",static:true,key:"styles",value:function styles(){return [_get(_getPrototypeOf(HaCircularProgress),"styles",this),r`
        :host {
          overflow: hidden;
        }
      `];}}]};},CircularProgress);

export { e };
