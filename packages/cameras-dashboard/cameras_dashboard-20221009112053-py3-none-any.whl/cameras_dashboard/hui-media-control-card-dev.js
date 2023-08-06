const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { ah as __decorate, G as i, d as e, t, c as s, $, z as o, I as i$1, Q as l, r, n, eK as getRGBContrastRatio, _ as _decorate, j as _get, k as _getPrototypeOf, ag as mdiDotsVertical, d$ as mdiPlayBoxMultiple, S as applyThemesOnElement, f as fireEvent } from './main-dev.js';
import { O as createCommonjsModule, P as unwrapExports, h as UNAVAILABLE_STATES, s as supportsFeature, _ as SUPPORT_TURN_ON, af as computeMediaControls, T as computeMediaDescription, q as cleanupMediaTitle, j as computeStateName, ag as SUPPORT_BROWSE_MEDIA, aS as SUPPORT_SEEK, Q as installResizeObserver, aT as getCurrentProgress } from './auth-dev.js';
import { d as debounce } from './stop_propagation-dev.js';
import { s as showMediaBrowserDialog } from './show-media-browser-dialog-dev.js';
import { W as findEntities, Z as createEntityNotFoundWarning, X as hasConfigOrEntityChanged } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

/**
 * @license
 * Copyright 2021 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */ /**
 * TypeScript version of the decorator
 * @see https://www.typescriptlang.org/docs/handbook/decorators.html#property-decorators
 */function tsDecorator(prototype,name,descriptor){const constructor=prototype.constructor;if(!descriptor){/**
         * lit uses internal properties with two leading underscores to
         * provide storage for accessors
         */const litInternalPropertyKey=`__${name}`;descriptor=constructor.getPropertyDescriptor(name,litInternalPropertyKey);if(!descriptor){throw new Error('@ariaProperty must be used after a @property decorator');}}// descriptor must exist at this point, reassign so typescript understands
const propDescriptor=descriptor;let attribute='';if(!propDescriptor.set){throw new Error(`@ariaProperty requires a setter for ${name}`);}// TODO(b/202853219): Remove this check when internal tooling is
// compatible
// tslint:disable-next-line:no-any bail if applied to internal generated class
if(prototype.dispatchWizEvent){return descriptor;}const wrappedDescriptor={configurable:true,enumerable:true,set(value){if(attribute===''){const options=constructor.getPropertyOptions(name);// if attribute is not a string, use `name` instead
attribute=typeof options.attribute==='string'?options.attribute:name;}if(this.hasAttribute(attribute)){this.removeAttribute(attribute);}propDescriptor.set.call(this,value);}};if(propDescriptor.get){wrappedDescriptor.get=function(){return propDescriptor.get.call(this);};}return wrappedDescriptor;}/**
 * A property decorator proxies an aria attribute to an internal node
 *
 * This decorator is only intended for use with ARIA attributes, such as `role`
 * and `aria-label` due to screenreader needs.
 *
 * Upon first render, `@ariaProperty` will remove the attribute from the host
 * element to prevent screenreaders from reading the host instead of the
 * internal node.
 *
 * This decorator should only be used for non-Symbol public fields decorated
 * with `@property`, or on a setter with an optional getter.
 *
 * @example
 * ```ts
 * class MyElement {
 *   @ariaProperty
 *   @property({ type: String, attribute: 'aria-label' })
 *   ariaLabel!: string;
 * }
 * ```
 * @category Decorator
 * @ExportDecoratedItems
 */function ariaProperty(protoOrDescriptor,name,// tslint:disable-next-line:no-any any is required as a return type from decorators
descriptor){if(name!==undefined){return tsDecorator(protoOrDescriptor,name,descriptor);}else {throw new Error('@ariaProperty only supports TypeScript Decorators');}}

/** @soyCompatible */class LinearProgressBase extends s{constructor(){super(...arguments);this.indeterminate=false;this.progress=0;this.buffer=1;this.reverse=false;this.closed=false;this.stylePrimaryHalf='';this.stylePrimaryFull='';this.styleSecondaryQuarter='';this.styleSecondaryHalf='';this.styleSecondaryFull='';this.animationReady=true;this.closedAnimationOff=false;this.resizeObserver=null;}connectedCallback(){super.connectedCallback();// if detached and reattached
if(this.rootEl){this.attachResizeObserver();}}/**
     * @soyTemplate
     */render(){/** @classMap */const classes={'mdc-linear-progress--closed':this.closed,'mdc-linear-progress--closed-animation-off':this.closedAnimationOff,'mdc-linear-progress--indeterminate':this.indeterminate,// needed for controller-less render
'mdc-linear-progress--animation-ready':this.animationReady};/** @styleMap */const rootStyles={'--mdc-linear-progress-primary-half':this.stylePrimaryHalf,'--mdc-linear-progress-primary-half-neg':this.stylePrimaryHalf!==''?`-${this.stylePrimaryHalf}`:'','--mdc-linear-progress-primary-full':this.stylePrimaryFull,'--mdc-linear-progress-primary-full-neg':this.stylePrimaryFull!==''?`-${this.stylePrimaryFull}`:'','--mdc-linear-progress-secondary-quarter':this.styleSecondaryQuarter,'--mdc-linear-progress-secondary-quarter-neg':this.styleSecondaryQuarter!==''?`-${this.styleSecondaryQuarter}`:'','--mdc-linear-progress-secondary-half':this.styleSecondaryHalf,'--mdc-linear-progress-secondary-half-neg':this.styleSecondaryHalf!==''?`-${this.styleSecondaryHalf}`:'','--mdc-linear-progress-secondary-full':this.styleSecondaryFull,'--mdc-linear-progress-secondary-full-neg':this.styleSecondaryFull!==''?`-${this.styleSecondaryFull}`:''};/** @styleMap */const bufferBarStyles={'flex-basis':this.indeterminate?'100%':`${this.buffer*100}%`};/** @styleMap */const primaryBarStyles={transform:this.indeterminate?'scaleX(1)':`scaleX(${this.progress})`};return $`
      <div
          role="progressbar"
          class="mdc-linear-progress ${o(classes)}"
          style="${i$1(rootStyles)}"
          dir="${l(this.reverse?'rtl':undefined)}"
          aria-label="${l(this.ariaLabel)}"
          aria-valuemin="0"
          aria-valuemax="1"
          aria-valuenow="${l(this.indeterminate?undefined:this.progress)}"
        @transitionend="${this.syncClosedState}">
        <div class="mdc-linear-progress__buffer">
          <div
            class="mdc-linear-progress__buffer-bar"
            style=${i$1(bufferBarStyles)}>
          </div>
          <div class="mdc-linear-progress__buffer-dots"></div>
        </div>
        <div
            class="mdc-linear-progress__bar mdc-linear-progress__primary-bar"
            style=${i$1(primaryBarStyles)}>
          <span class="mdc-linear-progress__bar-inner"></span>
        </div>
        <div class="mdc-linear-progress__bar mdc-linear-progress__secondary-bar">
          <span class="mdc-linear-progress__bar-inner"></span>
        </div>
      </div>`;}update(changedProperties){// - When showing the indicator, enable animations immediately.
// - On first render, disable the animation immediately.
// - For normal calls to hide the component, let transitionend event trigger
//   disabling of animations instead (see render method), so that animation
//   does not jump in the middle of fade out.
if(changedProperties.has('closed')&&(!this.closed||changedProperties.get('closed')===undefined)){this.syncClosedState();}super.update(changedProperties);}async firstUpdated(changed){super.firstUpdated(changed);this.attachResizeObserver();}syncClosedState(){this.closedAnimationOff=this.closed;}updated(changed){// restart animation for timing if reverse changed and is indeterminate.
// don't restart here if indeterminate has changed as well because we don't
// want to incur an extra style recalculation
if(!changed.has('indeterminate')&&changed.has('reverse')&&this.indeterminate){this.restartAnimation();}// Recaclulate the animation css custom props and restart the calculation
// if this is not the first render cycle, otherwise, resize observer init
// will already handle this and prevent unnecessary rerender + style recalc
// but resize observer will not update animation vals while determinate
if(changed.has('indeterminate')&&changed.get('indeterminate')!==undefined&&this.indeterminate&&window.ResizeObserver){this.calculateAndSetAnimationDimensions(this.rootEl.offsetWidth);}super.updated(changed);}disconnectedCallback(){if(this.resizeObserver){this.resizeObserver.disconnect();this.resizeObserver=null;}super.disconnectedCallback();}attachResizeObserver(){if(window.ResizeObserver){this.resizeObserver=new window.ResizeObserver(entries=>{if(!this.indeterminate){return;}for(const entry of entries){if(entry.contentRect){const width=entry.contentRect.width;this.calculateAndSetAnimationDimensions(width);}}});this.resizeObserver.observe(this.rootEl);return;}this.resizeObserver=null;}calculateAndSetAnimationDimensions(width){const primaryHalf=width*0.8367142;const primaryFull=width*2.00611057;const secondaryQuarter=width*0.37651913;const secondaryHalf=width*0.84386165;const secondaryFull=width*1.60277782;this.stylePrimaryHalf=`${primaryHalf}px`;this.stylePrimaryFull=`${primaryFull}px`;this.styleSecondaryQuarter=`${secondaryQuarter}px`;this.styleSecondaryHalf=`${secondaryHalf}px`;this.styleSecondaryFull=`${secondaryFull}px`;// need to restart animation for custom props to apply to keyframes
this.restartAnimation();}async restartAnimation(){this.animationReady=false;await this.updateComplete;await new Promise(requestAnimationFrame);this.animationReady=true;await this.updateComplete;}open(){this.closed=false;}close(){this.closed=true;}}__decorate([i('.mdc-linear-progress')],LinearProgressBase.prototype,"rootEl",void 0);__decorate([e({type:Boolean,reflect:true})],LinearProgressBase.prototype,"indeterminate",void 0);__decorate([e({type:Number})],LinearProgressBase.prototype,"progress",void 0);__decorate([e({type:Number})],LinearProgressBase.prototype,"buffer",void 0);__decorate([e({type:Boolean,reflect:true})],LinearProgressBase.prototype,"reverse",void 0);__decorate([e({type:Boolean,reflect:true})],LinearProgressBase.prototype,"closed",void 0);__decorate([ariaProperty,e({attribute:'aria-label'})],LinearProgressBase.prototype,"ariaLabel",void 0);__decorate([t()],LinearProgressBase.prototype,"stylePrimaryHalf",void 0);__decorate([t()],LinearProgressBase.prototype,"stylePrimaryFull",void 0);__decorate([t()],LinearProgressBase.prototype,"styleSecondaryQuarter",void 0);__decorate([t()],LinearProgressBase.prototype,"styleSecondaryHalf",void 0);__decorate([t()],LinearProgressBase.prototype,"styleSecondaryFull",void 0);__decorate([t()],LinearProgressBase.prototype,"animationReady",void 0);__decorate([t()],LinearProgressBase.prototype,"closedAnimationOff",void 0);

const styles=r`@keyframes mdc-linear-progress-primary-indeterminate-translate{0%{transform:translateX(0)}20%{animation-timing-function:cubic-bezier(0.5, 0, 0.701732, 0.495819);transform:translateX(0)}59.15%{animation-timing-function:cubic-bezier(0.302435, 0.381352, 0.55, 0.956352);transform:translateX(83.67142%);transform:translateX(var(--mdc-linear-progress-primary-half, 83.67142%))}100%{transform:translateX(200.611057%);transform:translateX(var(--mdc-linear-progress-primary-full, 200.611057%))}}@keyframes mdc-linear-progress-primary-indeterminate-scale{0%{transform:scaleX(0.08)}36.65%{animation-timing-function:cubic-bezier(0.334731, 0.12482, 0.785844, 1);transform:scaleX(0.08)}69.15%{animation-timing-function:cubic-bezier(0.06, 0.11, 0.6, 1);transform:scaleX(0.661479)}100%{transform:scaleX(0.08)}}@keyframes mdc-linear-progress-secondary-indeterminate-translate{0%{animation-timing-function:cubic-bezier(0.15, 0, 0.515058, 0.409685);transform:translateX(0)}25%{animation-timing-function:cubic-bezier(0.31033, 0.284058, 0.8, 0.733712);transform:translateX(37.651913%);transform:translateX(var(--mdc-linear-progress-secondary-quarter, 37.651913%))}48.35%{animation-timing-function:cubic-bezier(0.4, 0.627035, 0.6, 0.902026);transform:translateX(84.386165%);transform:translateX(var(--mdc-linear-progress-secondary-half, 84.386165%))}100%{transform:translateX(160.277782%);transform:translateX(var(--mdc-linear-progress-secondary-full, 160.277782%))}}@keyframes mdc-linear-progress-secondary-indeterminate-scale{0%{animation-timing-function:cubic-bezier(0.205028, 0.057051, 0.57661, 0.453971);transform:scaleX(0.08)}19.15%{animation-timing-function:cubic-bezier(0.152313, 0.196432, 0.648374, 1.004315);transform:scaleX(0.457104)}44.15%{animation-timing-function:cubic-bezier(0.257759, -0.003163, 0.211762, 1.38179);transform:scaleX(0.72796)}100%{transform:scaleX(0.08)}}@keyframes mdc-linear-progress-buffering{from{transform:rotate(180deg) translateX(-10px)}}@keyframes mdc-linear-progress-primary-indeterminate-translate-reverse{0%{transform:translateX(0)}20%{animation-timing-function:cubic-bezier(0.5, 0, 0.701732, 0.495819);transform:translateX(0)}59.15%{animation-timing-function:cubic-bezier(0.302435, 0.381352, 0.55, 0.956352);transform:translateX(-83.67142%);transform:translateX(var(--mdc-linear-progress-primary-half-neg, -83.67142%))}100%{transform:translateX(-200.611057%);transform:translateX(var(--mdc-linear-progress-primary-full-neg, -200.611057%))}}@keyframes mdc-linear-progress-secondary-indeterminate-translate-reverse{0%{animation-timing-function:cubic-bezier(0.15, 0, 0.515058, 0.409685);transform:translateX(0)}25%{animation-timing-function:cubic-bezier(0.31033, 0.284058, 0.8, 0.733712);transform:translateX(-37.651913%);transform:translateX(var(--mdc-linear-progress-secondary-quarter-neg, -37.651913%))}48.35%{animation-timing-function:cubic-bezier(0.4, 0.627035, 0.6, 0.902026);transform:translateX(-84.386165%);transform:translateX(var(--mdc-linear-progress-secondary-half-neg, -84.386165%))}100%{transform:translateX(-160.277782%);transform:translateX(var(--mdc-linear-progress-secondary-full-neg, -160.277782%))}}@keyframes mdc-linear-progress-buffering-reverse{from{transform:translateX(-10px)}}.mdc-linear-progress{position:relative;width:100%;transform:translateZ(0);outline:1px solid transparent;overflow:hidden;transition:opacity 250ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}@media screen and (forced-colors: active){.mdc-linear-progress{outline-color:CanvasText}}.mdc-linear-progress__bar{position:absolute;width:100%;height:100%;animation:none;transform-origin:top left;transition:transform 250ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-linear-progress__bar-inner{display:inline-block;position:absolute;width:100%;animation:none;border-top-style:solid}.mdc-linear-progress__buffer{display:flex;position:absolute;width:100%;height:100%}.mdc-linear-progress__buffer-dots{background-repeat:repeat-x;flex:auto;transform:rotate(180deg);animation:mdc-linear-progress-buffering 250ms infinite linear}.mdc-linear-progress__buffer-bar{flex:0 1 100%;transition:flex-basis 250ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-linear-progress__primary-bar{transform:scaleX(0)}.mdc-linear-progress__secondary-bar{display:none}.mdc-linear-progress--indeterminate .mdc-linear-progress__bar{transition:none}.mdc-linear-progress--indeterminate .mdc-linear-progress__primary-bar{left:-145.166611%}.mdc-linear-progress--indeterminate .mdc-linear-progress__secondary-bar{left:-54.888891%;display:block}.mdc-linear-progress--indeterminate.mdc-linear-progress--animation-ready .mdc-linear-progress__primary-bar{animation:mdc-linear-progress-primary-indeterminate-translate 2s infinite linear}.mdc-linear-progress--indeterminate.mdc-linear-progress--animation-ready .mdc-linear-progress__primary-bar>.mdc-linear-progress__bar-inner{animation:mdc-linear-progress-primary-indeterminate-scale 2s infinite linear}.mdc-linear-progress--indeterminate.mdc-linear-progress--animation-ready .mdc-linear-progress__secondary-bar{animation:mdc-linear-progress-secondary-indeterminate-translate 2s infinite linear}.mdc-linear-progress--indeterminate.mdc-linear-progress--animation-ready .mdc-linear-progress__secondary-bar>.mdc-linear-progress__bar-inner{animation:mdc-linear-progress-secondary-indeterminate-scale 2s infinite linear}[dir=rtl] .mdc-linear-progress:not([dir=ltr]) .mdc-linear-progress__bar,.mdc-linear-progress[dir=rtl]:not([dir=ltr]) .mdc-linear-progress__bar{right:0;-webkit-transform-origin:center right;transform-origin:center right}[dir=rtl] .mdc-linear-progress:not([dir=ltr]).mdc-linear-progress--animation-ready .mdc-linear-progress__primary-bar,.mdc-linear-progress[dir=rtl]:not([dir=ltr]).mdc-linear-progress--animation-ready .mdc-linear-progress__primary-bar{animation-name:mdc-linear-progress-primary-indeterminate-translate-reverse}[dir=rtl] .mdc-linear-progress:not([dir=ltr]).mdc-linear-progress--animation-ready .mdc-linear-progress__secondary-bar,.mdc-linear-progress[dir=rtl]:not([dir=ltr]).mdc-linear-progress--animation-ready .mdc-linear-progress__secondary-bar{animation-name:mdc-linear-progress-secondary-indeterminate-translate-reverse}[dir=rtl] .mdc-linear-progress:not([dir=ltr]) .mdc-linear-progress__buffer-dots,.mdc-linear-progress[dir=rtl]:not([dir=ltr]) .mdc-linear-progress__buffer-dots{animation:mdc-linear-progress-buffering-reverse 250ms infinite linear;transform:rotate(0)}[dir=rtl] .mdc-linear-progress:not([dir=ltr]).mdc-linear-progress--indeterminate .mdc-linear-progress__primary-bar,.mdc-linear-progress[dir=rtl]:not([dir=ltr]).mdc-linear-progress--indeterminate .mdc-linear-progress__primary-bar{right:-145.166611%;left:auto}[dir=rtl] .mdc-linear-progress:not([dir=ltr]).mdc-linear-progress--indeterminate .mdc-linear-progress__secondary-bar,.mdc-linear-progress[dir=rtl]:not([dir=ltr]).mdc-linear-progress--indeterminate .mdc-linear-progress__secondary-bar{right:-54.888891%;left:auto}.mdc-linear-progress--closed{opacity:0}.mdc-linear-progress--closed-animation-off .mdc-linear-progress__buffer-dots{animation:none}.mdc-linear-progress--closed-animation-off.mdc-linear-progress--indeterminate .mdc-linear-progress__bar,.mdc-linear-progress--closed-animation-off.mdc-linear-progress--indeterminate .mdc-linear-progress__bar .mdc-linear-progress__bar-inner{animation:none}.mdc-linear-progress__bar-inner{border-color:#6200ee;border-color:var(--mdc-theme-primary, #6200ee)}.mdc-linear-progress__buffer-dots{background-image:url("data:image/svg+xml,%3Csvg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' enable-background='new 0 0 5 2' xml:space='preserve' viewBox='0 0 5 2' preserveAspectRatio='none slice'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23e6e6e6'/%3E%3C/svg%3E")}.mdc-linear-progress__buffer-bar{background-color:#e6e6e6}.mdc-linear-progress{height:4px}.mdc-linear-progress__bar-inner{border-top-width:4px}.mdc-linear-progress__buffer-dots{background-size:10px 4px}:host{display:block}.mdc-linear-progress__buffer-bar{background-color:#e6e6e6;background-color:var(--mdc-linear-progress-buffer-color, #e6e6e6)}.mdc-linear-progress__buffer-dots{background-image:url("data:image/svg+xml,%3Csvg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' enable-background='new 0 0 5 2' xml:space='preserve' viewBox='0 0 5 2' preserveAspectRatio='none slice'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23e6e6e6'/%3E%3C/svg%3E");background-image:var(--mdc-linear-progress-buffering-dots-image, url("data:image/svg+xml,%3Csvg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' enable-background='new 0 0 5 2' xml:space='preserve' viewBox='0 0 5 2' preserveAspectRatio='none slice'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23e6e6e6'/%3E%3C/svg%3E"))}`;

/** @soyCompatible */let LinearProgress=class LinearProgress extends LinearProgressBase{};LinearProgress.styles=[styles];LinearProgress=__decorate([n('mwc-linear-progress')],LinearProgress);

var vibrant=createCommonjsModule(function(module,exports){(function webpackUniversalModuleDefinition(root,factory){module.exports=factory();})(window,function(){return(/******/function(modules){// webpackBootstrap
/******/ // The module cache
/******/var installedModules={};/******/ /******/ // The require function
/******/function __webpack_require__(moduleId){/******/ /******/ // Check if module is in cache
/******/if(installedModules[moduleId]){/******/return installedModules[moduleId].exports;/******/}/******/ // Create a new module (and put it into the cache)
/******/var module=installedModules[moduleId]={/******/i:moduleId,/******/l:false,/******/exports:{}/******/};/******/ /******/ // Execute the module function
/******/modules[moduleId].call(module.exports,module,module.exports,__webpack_require__);/******/ /******/ // Flag the module as loaded
/******/module.l=true;/******/ /******/ // Return the exports of the module
/******/return module.exports;/******/}/******/ /******/ /******/ // expose the modules object (__webpack_modules__)
/******/__webpack_require__.m=modules;/******/ /******/ // expose the module cache
/******/__webpack_require__.c=installedModules;/******/ /******/ // define getter function for harmony exports
/******/__webpack_require__.d=function(exports,name,getter){/******/if(!__webpack_require__.o(exports,name)){/******/Object.defineProperty(exports,name,{enumerable:true,get:getter});/******/}/******/};/******/ /******/ // define __esModule on exports
/******/__webpack_require__.r=function(exports){/******/if(typeof Symbol!=='undefined'&&Symbol.toStringTag){/******/Object.defineProperty(exports,Symbol.toStringTag,{value:'Module'});/******/}/******/Object.defineProperty(exports,'__esModule',{value:true});/******/};/******/ /******/ // create a fake namespace object
/******/ // mode & 1: value is a module id, require it
/******/ // mode & 2: merge all properties of value into the ns
/******/ // mode & 4: return value when already ns object
/******/ // mode & 8|1: behave like require
/******/__webpack_require__.t=function(value,mode){/******/if(mode&1)value=__webpack_require__(value);/******/if(mode&8)return value;/******/if(mode&4&&typeof value==='object'&&value&&value.__esModule)return value;/******/var ns=Object.create(null);/******/__webpack_require__.r(ns);/******/Object.defineProperty(ns,'default',{enumerable:true,value:value});/******/if(mode&2&&typeof value!='string')for(var key in value)__webpack_require__.d(ns,key,function(key){return value[key];}.bind(null,key));/******/return ns;/******/};/******/ /******/ // getDefaultExport function for compatibility with non-harmony modules
/******/__webpack_require__.n=function(module){/******/var getter=module&&module.__esModule?/******/function getDefault(){return module['default'];}:/******/function getModuleExports(){return module;};/******/__webpack_require__.d(getter,'a',getter);/******/return getter;/******/};/******/ /******/ // Object.prototype.hasOwnProperty.call
/******/__webpack_require__.o=function(object,property){return Object.prototype.hasOwnProperty.call(object,property);};/******/ /******/ // __webpack_public_path__
/******/__webpack_require__.p="";/******/ /******/ /******/ // Load entry module and return exports
/******/return __webpack_require__(__webpack_require__.s=10);/******/}/************************************************************************/ /******/([/* 0 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});exports.assignDeep=exports.mapValues=void 0;function mapValues(o,mapper){var result={};for(var key in o){if(o.hasOwnProperty(key)){var v=o[key];result[key]=mapper(v);}}return result;}exports.mapValues=mapValues;/**
 * Overwrite values or properties on objects and lists recursively.
 * A shallow copy will be created for each array value.
 */function assignDeep(target){var sources=[];for(var _i=1;_i<arguments.length;_i++){sources[_i-1]=arguments[_i];}sources.forEach(function(s){if(!s)return;for(var key in s){if(s.hasOwnProperty(key)){var v=s[key];if(Array.isArray(v)){// Shallow copy
target[key]=v.slice(0);}else if(typeof v==='object'){if(!target[key])target[key]={};assignDeep(target[key],v);}else {target[key]=v;}}}});return target;}exports.assignDeep=assignDeep;/***/},/* 1 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};Object.defineProperty(exports,"__esModule",{value:true});var options_1=__webpack_require__(7);var builder_1=__importDefault(__webpack_require__(8));var utils_1=__webpack_require__(0);var Vibrant=/** @class */function(){function Vibrant(_src,opts){this._src=_src;this.opts=utils_1.assignDeep({},Vibrant.DefaultOpts,opts);}Vibrant.use=function(pipeline){this._pipeline=pipeline;};Vibrant.from=function(src){return new builder_1.default(src);};Object.defineProperty(Vibrant.prototype,"result",{get:function(){return this._result;},enumerable:false,configurable:true});Vibrant.prototype._process=function(image,opts){this.opts.quantizer;image.scaleDown(this.opts);var processOpts=options_1.buildProcessOptions(this.opts,opts);return Vibrant._pipeline.process(image.getImageData(),processOpts);};Vibrant.prototype.palette=function(){return this.swatches();};Vibrant.prototype.swatches=function(){throw new Error('Method deprecated. Use `Vibrant.result.palettes[name]` instead');};Vibrant.prototype.getPalette=function(){var _this=this;var arg0=arguments[0];var arg1=arguments[1];var name=typeof arg0==='string'?arg0:'default';var cb=typeof arg0==='string'?arg1:arg0;var image=new this.opts.ImageClass();return image.load(this._src).then(function(image){return _this._process(image,{generators:[name]});}).then(function(result){_this._result=result;return result.palettes[name];}).then(function(res){image.remove();if(cb){cb(undefined,res);}return res;}).catch(function(err){image.remove();if(cb){cb(err);}return Promise.reject(err);});};Vibrant.prototype.getPalettes=function(){var _this=this;var arg0=arguments[0];var arg1=arguments[1];var names=Array.isArray(arg0)?arg0:['*'];var cb=Array.isArray(arg0)?arg1:arg0;var image=new this.opts.ImageClass();return image.load(this._src).then(function(image){return _this._process(image,{generators:names});}).then(function(result){_this._result=result;return result.palettes;}).then(function(res){image.remove();if(cb){cb(undefined,res);}return res;}).catch(function(err){image.remove();if(cb){cb(err);}return Promise.reject(err);});};Vibrant.DefaultOpts={colorCount:64,quality:5,filters:[]};return Vibrant;}();exports.default=Vibrant;/***/},/* 2 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});exports.applyFilters=exports.ImageBase=void 0;var ImageBase=/** @class */function(){function ImageBase(){}ImageBase.prototype.scaleDown=function(opts){var width=this.getWidth();var height=this.getHeight();var ratio=1;if(opts.maxDimension>0){var maxSide=Math.max(width,height);if(maxSide>opts.maxDimension)ratio=opts.maxDimension/maxSide;}else {ratio=1/opts.quality;}if(ratio<1)this.resize(width*ratio,height*ratio,ratio);};return ImageBase;}();exports.ImageBase=ImageBase;function applyFilters(imageData,filters){if(filters.length>0){var pixels=imageData.data;var n=pixels.length/4;var offset=void 0;var r=void 0;var g=void 0;var b=void 0;var a=void 0;for(var i=0;i<n;i++){offset=i*4;r=pixels[offset+0];g=pixels[offset+1];b=pixels[offset+2];a=pixels[offset+3];// Mark ignored color
for(var j=0;j<filters.length;j++){if(!filters[j](r,g,b,a)){pixels[offset+3]=0;break;}}}}return imageData;}exports.applyFilters=applyFilters;/***/},/* 3 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});exports.Swatch=void 0;var converter_1=__webpack_require__(4);var Swatch=/** @class */function(){function Swatch(rgb,population){this._rgb=rgb;this._population=population;}Swatch.applyFilters=function(colors,filters){return filters.length>0?colors.filter(function(_a){var r=_a.r,g=_a.g,b=_a.b;for(var j=0;j<filters.length;j++){if(!filters[j](r,g,b,255))return false;}return true;}):colors;};/**
     * Make a value copy of a swatch based on a previous one. Returns a new Swatch instance
     * @param {Swatch} swatch
     */Swatch.clone=function(swatch){return new Swatch(swatch._rgb,swatch._population);};Object.defineProperty(Swatch.prototype,"r",{/**
         * The red value in the RGB value
         */get:function(){return this._rgb[0];},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"g",{/**
         * The green value in the RGB value
         */get:function(){return this._rgb[1];},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"b",{/**
         * The blue value in the RGB value
         */get:function(){return this._rgb[2];},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"rgb",{/**
         * The color value as a rgb value
         */get:function(){return this._rgb;},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"hsl",{/**
         * The color value as a hsl value
         */get:function(){if(!this._hsl){var _a=this._rgb,r=_a[0],g=_a[1],b=_a[2];this._hsl=converter_1.rgbToHsl(r,g,b);}return this._hsl;},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"hex",{/**
         * The color value as a hex string
         */get:function(){if(!this._hex){var _a=this._rgb,r=_a[0],g=_a[1],b=_a[2];this._hex=converter_1.rgbToHex(r,g,b);}return this._hex;},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"population",{get:function(){return this._population;},enumerable:false,configurable:true});/**
     * Get the JSON object for the swatch
     */Swatch.prototype.toJSON=function(){return {rgb:this.rgb,population:this.population};};/**
     * Get the color value as a rgb value
     * @deprecated Use property instead
     */ // TODO: deprecate internally, use property instead
Swatch.prototype.getRgb=function(){return this._rgb;};/**
     * Get the color value as a hsl value
     * @deprecated Use property instead
     */ // TODO: deprecate internally, use property instead
Swatch.prototype.getHsl=function(){return this.hsl;};/**
     * @deprecated Use property instead
     */ // TODO: deprecate internally, use property instead
Swatch.prototype.getPopulation=function(){return this._population;};/**
     * Get the color value as a hex string
     * @deprecated Use property instead
     */ // TODO: deprecate internally, use property instead
Swatch.prototype.getHex=function(){return this.hex;};Swatch.prototype.getYiq=function(){if(!this._yiq){var rgb=this._rgb;this._yiq=(rgb[0]*299+rgb[1]*587+rgb[2]*114)/1000;}return this._yiq;};Object.defineProperty(Swatch.prototype,"titleTextColor",{get:function(){if(this._titleTextColor){this._titleTextColor=this.getYiq()<200?'#fff':'#000';}return this._titleTextColor;},enumerable:false,configurable:true});Object.defineProperty(Swatch.prototype,"bodyTextColor",{get:function(){if(this._bodyTextColor){this._bodyTextColor=this.getYiq()<150?'#fff':'#000';}return this._bodyTextColor;},enumerable:false,configurable:true});Swatch.prototype.getTitleTextColor=function(){return this.titleTextColor;};Swatch.prototype.getBodyTextColor=function(){return this.bodyTextColor;};return Swatch;}();exports.Swatch=Swatch;/***/},/* 4 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});exports.getColorDiffStatus=exports.hexDiff=exports.rgbDiff=exports.deltaE94=exports.rgbToCIELab=exports.xyzToCIELab=exports.rgbToXyz=exports.hslToRgb=exports.rgbToHsl=exports.rgbToHex=exports.hexToRgb=exports.DELTAE94_DIFF_STATUS=void 0;exports.DELTAE94_DIFF_STATUS={NA:0,PERFECT:1,CLOSE:2,GOOD:10,SIMILAR:50};/**
 * Converts hex string to RGB
 * @param hex - The hex value you with to get the RGB value of
 * @returns an array in the order of `red, green, blue` numerical values
 */function hexToRgb(hex){var m=/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);if(!m)throw new RangeError("'"+hex+"' is not a valid hex color");return [m[1],m[2],m[3]].map(function(s){return parseInt(s,16);});}exports.hexToRgb=hexToRgb;/**
 * Given values for an RGB color convert to and return a valid HEX string
 * @param r - Red value in RGB
 * @param g - Green value in RGB
 * @param b - Blue value in RGB
 * @returns a valid hex string with pre-pending pound sign
 */function rgbToHex(r,g,b){return '#'+((1<<24)+(r<<16)+(g<<8)+b).toString(16).slice(1,7);}exports.rgbToHex=rgbToHex;/**
 * Given values for an RGB color convert to and return a valid HSL value
 * @param r - Red value in RGB
 * @param g - Green value in RGB
 * @param b - Blue value in RGB
 * @returns an array in the order of `hue, saturation, light` numerical values
 */function rgbToHsl(r,g,b){r/=255;g/=255;b/=255;var max=Math.max(r,g,b);var min=Math.min(r,g,b);var h=0;var s=0;var l=(max+min)/2;if(max!==min){var d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r:h=(g-b)/d+(g<b?6:0);break;case g:h=(b-r)/d+2;break;case b:h=(r-g)/d+4;break;}h/=6;}return [h,s,l];}exports.rgbToHsl=rgbToHsl;function hslToRgb(h,s,l){var r;var g;var b;function hue2rgb(p,q,t){if(t<0)t+=1;if(t>1)t-=1;if(t<1/6)return p+(q-p)*6*t;if(t<1/2)return q;if(t<2/3)return p+(q-p)*(2/3-t)*6;return p;}if(s===0){r=g=b=l;}else {var q=l<0.5?l*(1+s):l+s-l*s;var p=2*l-q;r=hue2rgb(p,q,h+1/3);g=hue2rgb(p,q,h);b=hue2rgb(p,q,h-1/3);}return [r*255,g*255,b*255];}exports.hslToRgb=hslToRgb;function rgbToXyz(r,g,b){r/=255;g/=255;b/=255;r=r>0.04045?Math.pow((r+0.005)/1.055,2.4):r/12.92;g=g>0.04045?Math.pow((g+0.005)/1.055,2.4):g/12.92;b=b>0.04045?Math.pow((b+0.005)/1.055,2.4):b/12.92;r*=100;g*=100;b*=100;var x=r*0.4124+g*0.3576+b*0.1805;var y=r*0.2126+g*0.7152+b*0.0722;var z=r*0.0193+g*0.1192+b*0.9505;return [x,y,z];}exports.rgbToXyz=rgbToXyz;function xyzToCIELab(x,y,z){var REF_X=95.047;var REF_Y=100;var REF_Z=108.883;x/=REF_X;y/=REF_Y;z/=REF_Z;x=x>0.008856?Math.pow(x,1/3):7.787*x+16/116;y=y>0.008856?Math.pow(y,1/3):7.787*y+16/116;z=z>0.008856?Math.pow(z,1/3):7.787*z+16/116;var L=116*y-16;var a=500*(x-y);var b=200*(y-z);return [L,a,b];}exports.xyzToCIELab=xyzToCIELab;function rgbToCIELab(r,g,b){var _a=rgbToXyz(r,g,b),x=_a[0],y=_a[1],z=_a[2];return xyzToCIELab(x,y,z);}exports.rgbToCIELab=rgbToCIELab;function deltaE94(lab1,lab2){var WEIGHT_L=1;var WEIGHT_C=1;var WEIGHT_H=1;var L1=lab1[0],a1=lab1[1],b1=lab1[2];var L2=lab2[0],a2=lab2[1],b2=lab2[2];var dL=L1-L2;var da=a1-a2;var db=b1-b2;var xC1=Math.sqrt(a1*a1+b1*b1);var xC2=Math.sqrt(a2*a2+b2*b2);var xDL=L2-L1;var xDC=xC2-xC1;var xDE=Math.sqrt(dL*dL+da*da+db*db);var xDH=Math.sqrt(xDE)>Math.sqrt(Math.abs(xDL))+Math.sqrt(Math.abs(xDC))?Math.sqrt(xDE*xDE-xDL*xDL-xDC*xDC):0;var xSC=1+0.045*xC1;var xSH=1+0.015*xC1;xDL/=WEIGHT_L;xDC/=WEIGHT_C*xSC;xDH/=WEIGHT_H*xSH;return Math.sqrt(xDL*xDL+xDC*xDC+xDH*xDH);}exports.deltaE94=deltaE94;function rgbDiff(rgb1,rgb2){var lab1=rgbToCIELab.apply(undefined,rgb1);var lab2=rgbToCIELab.apply(undefined,rgb2);return deltaE94(lab1,lab2);}exports.rgbDiff=rgbDiff;function hexDiff(hex1,hex2){var rgb1=hexToRgb(hex1);var rgb2=hexToRgb(hex2);return rgbDiff(rgb1,rgb2);}exports.hexDiff=hexDiff;function getColorDiffStatus(d){if(d<exports.DELTAE94_DIFF_STATUS.NA){return 'N/A';}// Not perceptible by human eyes
if(d<=exports.DELTAE94_DIFF_STATUS.PERFECT){return 'Perfect';}// Perceptible through close observation
if(d<=exports.DELTAE94_DIFF_STATUS.CLOSE){return 'Close';}// Perceptible at a glance
if(d<=exports.DELTAE94_DIFF_STATUS.GOOD){return 'Good';}// Colors are more similar than opposite
if(d<exports.DELTAE94_DIFF_STATUS.SIMILAR){return 'Similar';}return 'Wrong';}exports.getColorDiffStatus=getColorDiffStatus;/***/},/* 5 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};var config_1=__importDefault(__webpack_require__(6));var image_browser_1=__importDefault(__webpack_require__(9));config_1.default.DefaultOpts.ImageClass=image_browser_1.default;module.exports=config_1.default;/***/},/* 6 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};Object.defineProperty(exports,"__esModule",{value:true});var core_1=__importDefault(__webpack_require__(1));core_1.default.DefaultOpts.quantizer='mmcq';core_1.default.DefaultOpts.generators=['default'];core_1.default.DefaultOpts.filters=['default'];exports.default=core_1.default;/***/},/* 7 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});exports.buildProcessOptions=void 0;var utils_1=__webpack_require__(0);function buildProcessOptions(opts,override){var colorCount=opts.colorCount,quantizer=opts.quantizer,generators=opts.generators,filters=opts.filters;// Merge with common quantizer options
var commonQuantizerOpts={colorCount:colorCount};var q=typeof quantizer==='string'?{name:quantizer,options:{}}:quantizer;q.options=utils_1.assignDeep({},commonQuantizerOpts,q.options);return utils_1.assignDeep({},{quantizer:q,generators:generators,filters:filters},override);}exports.buildProcessOptions=buildProcessOptions;/***/},/* 8 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};Object.defineProperty(exports,"__esModule",{value:true});var _1=__importDefault(__webpack_require__(1));var utils_1=__webpack_require__(0);var Builder=/** @class */function(){function Builder(src,opts){if(opts===void 0){opts={};}this._src=src;this._opts=utils_1.assignDeep({},_1.default.DefaultOpts,opts);}Builder.prototype.maxColorCount=function(n){this._opts.colorCount=n;return this;};Builder.prototype.maxDimension=function(d){this._opts.maxDimension=d;return this;};Builder.prototype.addFilter=function(name){if(!this._opts.filters){this._opts.filters=[name];}else {this._opts.filters.push(name);}return this;};Builder.prototype.removeFilter=function(name){if(this._opts.filters){var i=this._opts.filters.indexOf(name);if(i>0)this._opts.filters.splice(i);}return this;};Builder.prototype.clearFilters=function(){this._opts.filters=[];return this;};Builder.prototype.quality=function(q){this._opts.quality=q;return this;};Builder.prototype.useImageClass=function(imageClass){this._opts.ImageClass=imageClass;return this;};Builder.prototype.useGenerator=function(generator,options){if(!this._opts.generators)this._opts.generators=[];this._opts.generators.push(options?{name:generator,options:options}:generator);return this;};Builder.prototype.useQuantizer=function(quantizer,options){this._opts.quantizer=options?{name:quantizer,options:options}:quantizer;return this;};Builder.prototype.build=function(){return new _1.default(this._src,this._opts);};Builder.prototype.getPalette=function(cb){return this.build().getPalette(cb);};Builder.prototype.getSwatches=function(cb){return this.build().getPalette(cb);};return Builder;}();exports.default=Builder;/***/},/* 9 */ /***/function(module,exports,__webpack_require__){var __extends=this&&this.__extends||function(){var extendStatics=function(d,b){extendStatics=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(d,b){d.__proto__=b;}||function(d,b){for(var p in b)if(b.hasOwnProperty(p))d[p]=b[p];};return extendStatics(d,b);};return function(d,b){extendStatics(d,b);function __(){this.constructor=d;}d.prototype=b===null?Object.create(b):(__.prototype=b.prototype,new __());};}();Object.defineProperty(exports,"__esModule",{value:true});var image_1=__webpack_require__(2);function isRelativeUrl(url){var u=new URL(url,location.href);return u.protocol===location.protocol&&u.host===location.host&&u.port===location.port;}function isSameOrigin(a,b){var ua=new URL(a);var ub=new URL(b);// https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
return ua.protocol===ub.protocol&&ua.hostname===ub.hostname&&ua.port===ub.port;}var BrowserImage=/** @class */function(_super){__extends(BrowserImage,_super);function BrowserImage(){return _super!==null&&_super.apply(this,arguments)||this;}BrowserImage.prototype._initCanvas=function(){var img=this.image;var canvas=this._canvas=document.createElement('canvas');var context=canvas.getContext('2d');if(!context)throw new ReferenceError('Failed to create canvas context');this._context=context;canvas.className='@vibrant/canvas';canvas.style.display='none';this._width=canvas.width=img.width;this._height=canvas.height=img.height;context.drawImage(img,0,0);document.body.appendChild(canvas);};BrowserImage.prototype.load=function(image){var _this=this;var img;var src;if(typeof image==='string'){img=document.createElement('img');src=image;if(!isRelativeUrl(src)&&!isSameOrigin(window.location.href,src)){img.crossOrigin='anonymous';}img.src=src;}else if(image instanceof HTMLImageElement){img=image;src=image.src;}else {return Promise.reject(new Error("Cannot load buffer as an image in browser"));}this.image=img;return new Promise(function(resolve,reject){var onImageLoad=function(){_this._initCanvas();resolve(_this);};if(img.complete){// Already loaded
onImageLoad();}else {img.onload=onImageLoad;img.onerror=function(e){return reject(new Error("Fail to load image: "+src));};}});};BrowserImage.prototype.clear=function(){this._context.clearRect(0,0,this._width,this._height);};BrowserImage.prototype.update=function(imageData){this._context.putImageData(imageData,0,0);};BrowserImage.prototype.getWidth=function(){return this._width;};BrowserImage.prototype.getHeight=function(){return this._height;};BrowserImage.prototype.resize=function(targetWidth,targetHeight,ratio){var _a=this,canvas=_a._canvas,context=_a._context,img=_a.image;this._width=canvas.width=targetWidth;this._height=canvas.height=targetHeight;context.scale(ratio,ratio);context.drawImage(img,0,0);};BrowserImage.prototype.getPixelCount=function(){return this._width*this._height;};BrowserImage.prototype.getImageData=function(){return this._context.getImageData(0,0,this._width,this._height);};BrowserImage.prototype.remove=function(){if(this._canvas&&this._canvas.parentNode){this._canvas.parentNode.removeChild(this._canvas);}};return BrowserImage;}(image_1.ImageBase);exports.default=BrowserImage;/***/},/* 10 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};var Vibrant=__webpack_require__(5);var pipeline_1=__importDefault(__webpack_require__(11));Vibrant.use(pipeline_1.default);module.exports=Vibrant;/***/},/* 11 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};Object.defineProperty(exports,"__esModule",{value:true});var quantizer_mmcq_1=__importDefault(__webpack_require__(12));var generator_default_1=__importDefault(__webpack_require__(16));var pipeline_1=__webpack_require__(17);var pipeline=new pipeline_1.BasicPipeline().filter.register('default',function(r,g,b,a){return a>=125&&!(r>250&&g>250&&b>250);}).quantizer.register('mmcq',quantizer_mmcq_1.default).generator.register('default',generator_default_1.default);exports.default=pipeline;/***/},/* 12 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};Object.defineProperty(exports,"__esModule",{value:true});var color_1=__webpack_require__(3);var vbox_1=__importDefault(__webpack_require__(13));var pqueue_1=__importDefault(__webpack_require__(15));var fractByPopulations=0.75;function _splitBoxes(pq,target){var lastSize=pq.size();while(pq.size()<target){var vbox=pq.pop();if(vbox&&vbox.count()>0){var _a=vbox.split(),vbox1=_a[0],vbox2=_a[1];pq.push(vbox1);if(vbox2&&vbox2.count()>0)pq.push(vbox2);// No more new boxes, converged
if(pq.size()===lastSize){break;}else {lastSize=pq.size();}}else {break;}}}var MMCQ=function(pixels,opts){if(pixels.length===0||opts.colorCount<2||opts.colorCount>256){throw new Error('Wrong MMCQ parameters');}var vbox=vbox_1.default.build(pixels);vbox.histogram.colorCount;var pq=new pqueue_1.default(function(a,b){return a.count()-b.count();});pq.push(vbox);// first set of colors, sorted by population
_splitBoxes(pq,fractByPopulations*opts.colorCount);// Re-order
var pq2=new pqueue_1.default(function(a,b){return a.count()*a.volume()-b.count()*b.volume();});pq2.contents=pq.contents;// next set - generate the median cuts using the (npix * vol) sorting.
_splitBoxes(pq2,opts.colorCount-pq2.size());// calculate the actual colors
return generateSwatches(pq2);};function generateSwatches(pq){var swatches=[];while(pq.size()){var v=pq.pop();var color=v.avg();color[0];color[1];color[2];swatches.push(new color_1.Swatch(color,v.count()));}return swatches;}exports.default=MMCQ;/***/},/* 13 */ /***/function(module,exports,__webpack_require__){var __importDefault=this&&this.__importDefault||function(mod){return mod&&mod.__esModule?mod:{"default":mod};};Object.defineProperty(exports,"__esModule",{value:true});var histogram_1=__importDefault(__webpack_require__(14));var SIGBITS=5;var RSHIFT=8-SIGBITS;var VBox=/** @class */function(){function VBox(r1,r2,g1,g2,b1,b2,histogram){this.histogram=histogram;this._volume=-1;this._count=-1;// NOTE: dimension will be mutated by split operation.
//       It must be specified explicitly, not from histogram
this.dimension={r1:r1,r2:r2,g1:g1,g2:g2,b1:b1,b2:b2};}VBox.build=function(pixels){var h=new histogram_1.default(pixels,{sigBits:SIGBITS});var rmin=h.rmin,rmax=h.rmax,gmin=h.gmin,gmax=h.gmax,bmin=h.bmin,bmax=h.bmax;return new VBox(rmin,rmax,gmin,gmax,bmin,bmax,h);};VBox.prototype.invalidate=function(){this._volume=this._count=-1;this._avg=null;};VBox.prototype.volume=function(){if(this._volume<0){var _a=this.dimension,r1=_a.r1,r2=_a.r2,g1=_a.g1,g2=_a.g2,b1=_a.b1,b2=_a.b2;this._volume=(r2-r1+1)*(g2-g1+1)*(b2-b1+1);}return this._volume;};VBox.prototype.count=function(){if(this._count<0){var _a=this.histogram,hist=_a.hist,getColorIndex=_a.getColorIndex;var _b=this.dimension,r1=_b.r1,r2=_b.r2,g1=_b.g1,g2=_b.g2,b1=_b.b1,b2=_b.b2;var c=0;for(var r=r1;r<=r2;r++){for(var g=g1;g<=g2;g++){for(var b=b1;b<=b2;b++){var index=getColorIndex(r,g,b);c+=hist[index];}}}this._count=c;}return this._count;};VBox.prototype.clone=function(){var histogram=this.histogram;var _a=this.dimension,r1=_a.r1,r2=_a.r2,g1=_a.g1,g2=_a.g2,b1=_a.b1,b2=_a.b2;return new VBox(r1,r2,g1,g2,b1,b2,histogram);};VBox.prototype.avg=function(){if(!this._avg){var _a=this.histogram,hist=_a.hist,getColorIndex=_a.getColorIndex;var _b=this.dimension,r1=_b.r1,r2=_b.r2,g1=_b.g1,g2=_b.g2,b1=_b.b1,b2=_b.b2;var ntot=0;var mult=1<<8-SIGBITS;var rsum=void 0;var gsum=void 0;var bsum=void 0;rsum=gsum=bsum=0;for(var r=r1;r<=r2;r++){for(var g=g1;g<=g2;g++){for(var b=b1;b<=b2;b++){var index=getColorIndex(r,g,b);var h=hist[index];ntot+=h;rsum+=h*(r+0.5)*mult;gsum+=h*(g+0.5)*mult;bsum+=h*(b+0.5)*mult;}}}if(ntot){this._avg=[~~(rsum/ntot),~~(gsum/ntot),~~(bsum/ntot)];}else {this._avg=[~~(mult*(r1+r2+1)/2),~~(mult*(g1+g2+1)/2),~~(mult*(b1+b2+1)/2)];}}return this._avg;};VBox.prototype.contains=function(rgb){var r=rgb[0],g=rgb[1],b=rgb[2];var _a=this.dimension,r1=_a.r1,r2=_a.r2,g1=_a.g1,g2=_a.g2,b1=_a.b1,b2=_a.b2;r>>=RSHIFT;g>>=RSHIFT;b>>=RSHIFT;return r>=r1&&r<=r2&&g>=g1&&g<=g2&&b>=b1&&b<=b2;};VBox.prototype.split=function(){var _a=this.histogram,hist=_a.hist,getColorIndex=_a.getColorIndex;var _b=this.dimension,r1=_b.r1,r2=_b.r2,g1=_b.g1,g2=_b.g2,b1=_b.b1,b2=_b.b2;var count=this.count();if(!count)return [];if(count===1)return [this.clone()];var rw=r2-r1+1;var gw=g2-g1+1;var bw=b2-b1+1;var maxw=Math.max(rw,gw,bw);var accSum=null;var sum;var total;sum=total=0;var maxd=null;if(maxw===rw){maxd='r';accSum=new Uint32Array(r2+1);for(var r=r1;r<=r2;r++){sum=0;for(var g=g1;g<=g2;g++){for(var b=b1;b<=b2;b++){var index=getColorIndex(r,g,b);sum+=hist[index];}}total+=sum;accSum[r]=total;}}else if(maxw===gw){maxd='g';accSum=new Uint32Array(g2+1);for(var g=g1;g<=g2;g++){sum=0;for(var r=r1;r<=r2;r++){for(var b=b1;b<=b2;b++){var index=getColorIndex(r,g,b);sum+=hist[index];}}total+=sum;accSum[g]=total;}}else {maxd='b';accSum=new Uint32Array(b2+1);for(var b=b1;b<=b2;b++){sum=0;for(var r=r1;r<=r2;r++){for(var g=g1;g<=g2;g++){var index=getColorIndex(r,g,b);sum+=hist[index];}}total+=sum;accSum[b]=total;}}var splitPoint=-1;var reverseSum=new Uint32Array(accSum.length);for(var i=0;i<accSum.length;i++){var d=accSum[i];if(splitPoint<0&&d>total/2)splitPoint=i;reverseSum[i]=total-d;}var vbox=this;function doCut(d){var dim1=d+'1';var dim2=d+'2';var d1=vbox.dimension[dim1];var d2=vbox.dimension[dim2];var vbox1=vbox.clone();var vbox2=vbox.clone();var left=splitPoint-d1;var right=d2-splitPoint;if(left<=right){d2=Math.min(d2-1,~~(splitPoint+right/2));d2=Math.max(0,d2);}else {d2=Math.max(d1,~~(splitPoint-1-left/2));d2=Math.min(vbox.dimension[dim2],d2);}while(!accSum[d2])d2++;var c2=reverseSum[d2];while(!c2&&accSum[d2-1])c2=reverseSum[--d2];vbox1.dimension[dim2]=d2;vbox2.dimension[dim1]=d2+1;return [vbox1,vbox2];}return doCut(maxd);};return VBox;}();exports.default=VBox;/***/},/* 14 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});var Histogram=/** @class */function(){function Histogram(pixels,opts){this.pixels=pixels;this.opts=opts;var sigBits=opts.sigBits;var getColorIndex=function(r,g,b){return (r<<2*sigBits)+(g<<sigBits)+b;};this.getColorIndex=getColorIndex;var rshift=8-sigBits;var hn=1<<3*sigBits;var hist=new Uint32Array(hn);var rmax;var rmin;var gmax;var gmin;var bmax;var bmin;var r;var g;var b;var a;rmax=gmax=bmax=0;rmin=gmin=bmin=Number.MAX_VALUE;var n=pixels.length/4;var i=0;while(i<n){var offset=i*4;i++;r=pixels[offset+0];g=pixels[offset+1];b=pixels[offset+2];a=pixels[offset+3];// Ignored pixels' alpha is marked as 0 in filtering stage
if(a===0)continue;r=r>>rshift;g=g>>rshift;b=b>>rshift;var index=getColorIndex(r,g,b);hist[index]+=1;if(r>rmax)rmax=r;if(r<rmin)rmin=r;if(g>gmax)gmax=g;if(g<gmin)gmin=g;if(b>bmax)bmax=b;if(b<bmin)bmin=b;}this._colorCount=hist.reduce(function(total,c){return c>0?total+1:total;},0);this.hist=hist;this.rmax=rmax;this.rmin=rmin;this.gmax=gmax;this.gmin=gmin;this.bmax=bmax;this.bmin=bmin;}Object.defineProperty(Histogram.prototype,"colorCount",{get:function(){return this._colorCount;},enumerable:false,configurable:true});return Histogram;}();exports.default=Histogram;/***/},/* 15 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});var PQueue=/** @class */function(){function PQueue(comparator){this._comparator=comparator;this.contents=[];this._sorted=false;}PQueue.prototype._sort=function(){if(!this._sorted){this.contents.sort(this._comparator);this._sorted=true;}};PQueue.prototype.push=function(item){this.contents.push(item);this._sorted=false;};PQueue.prototype.peek=function(index){this._sort();index=typeof index==='number'?index:this.contents.length-1;return this.contents[index];};PQueue.prototype.pop=function(){this._sort();return this.contents.pop();};PQueue.prototype.size=function(){return this.contents.length;};PQueue.prototype.map=function(mapper){this._sort();return this.contents.map(mapper);};return PQueue;}();exports.default=PQueue;/***/},/* 16 */ /***/function(module,exports,__webpack_require__){Object.defineProperty(exports,"__esModule",{value:true});var color_1=__webpack_require__(3);var converter_1=__webpack_require__(4);var DefaultOpts={targetDarkLuma:0.26,maxDarkLuma:0.45,minLightLuma:0.55,targetLightLuma:0.74,minNormalLuma:0.3,targetNormalLuma:0.5,maxNormalLuma:0.7,targetMutesSaturation:0.3,maxMutesSaturation:0.4,targetVibrantSaturation:1.0,minVibrantSaturation:0.35,weightSaturation:3,weightLuma:6.5,weightPopulation:0.5};function _findMaxPopulation(swatches){var p=0;swatches.forEach(function(s){p=Math.max(p,s.population);});return p;}function _isAlreadySelected(palette,s){return palette.Vibrant===s||palette.DarkVibrant===s||palette.LightVibrant===s||palette.Muted===s||palette.DarkMuted===s||palette.LightMuted===s;}function _createComparisonValue(saturation,targetSaturation,luma,targetLuma,population,maxPopulation,opts){function weightedMean(){var values=[];for(var _i=0;_i<arguments.length;_i++){values[_i]=arguments[_i];}var sum=0;var weightSum=0;for(var i=0;i<values.length;i+=2){var value=values[i];var weight=values[i+1];sum+=value*weight;weightSum+=weight;}return sum/weightSum;}function invertDiff(value,targetValue){return 1-Math.abs(value-targetValue);}return weightedMean(invertDiff(saturation,targetSaturation),opts.weightSaturation,invertDiff(luma,targetLuma),opts.weightLuma,population/maxPopulation,opts.weightPopulation);}function _findColorVariation(palette,swatches,maxPopulation,targetLuma,minLuma,maxLuma,targetSaturation,minSaturation,maxSaturation,opts){var max=null;var maxValue=0;swatches.forEach(function(swatch){var _a=swatch.hsl,s=_a[1],l=_a[2];if(s>=minSaturation&&s<=maxSaturation&&l>=minLuma&&l<=maxLuma&&!_isAlreadySelected(palette,swatch)){var value=_createComparisonValue(s,targetSaturation,l,targetLuma,swatch.population,maxPopulation,opts);if(max===null||value>maxValue){max=swatch;maxValue=value;}}});return max;}function _generateVariationColors(swatches,maxPopulation,opts){var palette={Vibrant:null,DarkVibrant:null,LightVibrant:null,Muted:null,DarkMuted:null,LightMuted:null};// mVibrantSwatch = findColor(TARGET_NORMAL_LUMA, MIN_NORMAL_LUMA, MAX_NORMAL_LUMA,
//     TARGET_VIBRANT_SATURATION, MIN_VIBRANT_SATURATION, 1f)
palette.Vibrant=_findColorVariation(palette,swatches,maxPopulation,opts.targetNormalLuma,opts.minNormalLuma,opts.maxNormalLuma,opts.targetVibrantSaturation,opts.minVibrantSaturation,1,opts);// mLightVibrantSwatch = findColor(TARGET_LIGHT_LUMA, MIN_LIGHT_LUMA, 1f,
//     TARGET_VIBRANT_SATURATION, MIN_VIBRANT_SATURATION, 1f)
palette.LightVibrant=_findColorVariation(palette,swatches,maxPopulation,opts.targetLightLuma,opts.minLightLuma,1,opts.targetVibrantSaturation,opts.minVibrantSaturation,1,opts);// mDarkVibrantSwatch = findColor(TARGET_DARK_LUMA, 0f, MAX_DARK_LUMA,
//     TARGET_VIBRANT_SATURATION, MIN_VIBRANT_SATURATION, 1f)
palette.DarkVibrant=_findColorVariation(palette,swatches,maxPopulation,opts.targetDarkLuma,0,opts.maxDarkLuma,opts.targetVibrantSaturation,opts.minVibrantSaturation,1,opts);// mMutedSwatch = findColor(TARGET_NORMAL_LUMA, MIN_NORMAL_LUMA, MAX_NORMAL_LUMA,
//     TARGET_MUTED_SATURATION, 0f, MAX_MUTED_SATURATION)
palette.Muted=_findColorVariation(palette,swatches,maxPopulation,opts.targetNormalLuma,opts.minNormalLuma,opts.maxNormalLuma,opts.targetMutesSaturation,0,opts.maxMutesSaturation,opts);// mLightMutedColor = findColor(TARGET_LIGHT_LUMA, MIN_LIGHT_LUMA, 1f,
//     TARGET_MUTED_SATURATION, 0f, MAX_MUTED_SATURATION)
palette.LightMuted=_findColorVariation(palette,swatches,maxPopulation,opts.targetLightLuma,opts.minLightLuma,1,opts.targetMutesSaturation,0,opts.maxMutesSaturation,opts);// mDarkMutedSwatch = findColor(TARGET_DARK_LUMA, 0f, MAX_DARK_LUMA,
//     TARGET_MUTED_SATURATION, 0f, MAX_MUTED_SATURATION)
palette.DarkMuted=_findColorVariation(palette,swatches,maxPopulation,opts.targetDarkLuma,0,opts.maxDarkLuma,opts.targetMutesSaturation,0,opts.maxMutesSaturation,opts);return palette;}function _generateEmptySwatches(palette,maxPopulation,opts){if(!palette.Vibrant&&!palette.DarkVibrant&&!palette.LightVibrant){if(!palette.DarkVibrant&&palette.DarkMuted){var _a=palette.DarkMuted.hsl,h=_a[0],s=_a[1],l=_a[2];l=opts.targetDarkLuma;palette.DarkVibrant=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}if(!palette.LightVibrant&&palette.LightMuted){var _b=palette.LightMuted.hsl,h=_b[0],s=_b[1],l=_b[2];l=opts.targetDarkLuma;palette.DarkVibrant=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}}if(!palette.Vibrant&&palette.DarkVibrant){var _c=palette.DarkVibrant.hsl,h=_c[0],s=_c[1],l=_c[2];l=opts.targetNormalLuma;palette.Vibrant=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}else if(!palette.Vibrant&&palette.LightVibrant){var _d=palette.LightVibrant.hsl,h=_d[0],s=_d[1],l=_d[2];l=opts.targetNormalLuma;palette.Vibrant=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}if(!palette.DarkVibrant&&palette.Vibrant){var _e=palette.Vibrant.hsl,h=_e[0],s=_e[1],l=_e[2];l=opts.targetDarkLuma;palette.DarkVibrant=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}if(!palette.LightVibrant&&palette.Vibrant){var _f=palette.Vibrant.hsl,h=_f[0],s=_f[1],l=_f[2];l=opts.targetLightLuma;palette.LightVibrant=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}if(!palette.Muted&&palette.Vibrant){var _g=palette.Vibrant.hsl,h=_g[0],s=_g[1],l=_g[2];l=opts.targetMutesSaturation;palette.Muted=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}if(!palette.DarkMuted&&palette.DarkVibrant){var _h=palette.DarkVibrant.hsl,h=_h[0],s=_h[1],l=_h[2];l=opts.targetMutesSaturation;palette.DarkMuted=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}if(!palette.LightMuted&&palette.LightVibrant){var _j=palette.LightVibrant.hsl,h=_j[0],s=_j[1],l=_j[2];l=opts.targetMutesSaturation;palette.LightMuted=new color_1.Swatch(converter_1.hslToRgb(h,s,l),0);}}var DefaultGenerator=function(swatches,opts){opts=Object.assign({},DefaultOpts,opts);var maxPopulation=_findMaxPopulation(swatches);var palette=_generateVariationColors(swatches,maxPopulation,opts);_generateEmptySwatches(palette,maxPopulation,opts);return palette;};exports.default=DefaultGenerator;/***/},/* 17 */ /***/function(module,exports,__webpack_require__){var __awaiter=this&&this.__awaiter||function(thisArg,_arguments,P,generator){function adopt(value){return value instanceof P?value:new P(function(resolve){resolve(value);});}return new(P||(P=Promise))(function(resolve,reject){function fulfilled(value){try{step(generator.next(value));}catch(e){reject(e);}}function rejected(value){try{step(generator["throw"](value));}catch(e){reject(e);}}function step(result){result.done?resolve(result.value):adopt(result.value).then(fulfilled,rejected);}step((generator=generator.apply(thisArg,_arguments||[])).next());});};var __generator=this&&this.__generator||function(thisArg,body){var _={label:0,sent:function(){if(t[0]&1)throw t[1];return t[1];},trys:[],ops:[]},f,y,t,g;return g={next:verb(0),"throw":verb(1),"return":verb(2)},typeof Symbol==="function"&&(g[Symbol.iterator]=function(){return this;}),g;function verb(n){return function(v){return step([n,v]);};}function step(op){if(f)throw new TypeError("Generator is already executing.");while(_)try{if(f=1,y&&(t=op[0]&2?y["return"]:op[0]?y["throw"]||((t=y["return"])&&t.call(y),0):y.next)&&!(t=t.call(y,op[1])).done)return t;if(y=0,t)op=[op[0]&2,t.value];switch(op[0]){case 0:case 1:t=op;break;case 4:_.label++;return {value:op[1],done:false};case 5:_.label++;y=op[1];op=[0];continue;case 7:op=_.ops.pop();_.trys.pop();continue;default:if(!(t=_.trys,t=t.length>0&&t[t.length-1])&&(op[0]===6||op[0]===2)){_=0;continue;}if(op[0]===3&&(!t||op[1]>t[0]&&op[1]<t[3])){_.label=op[1];break;}if(op[0]===6&&_.label<t[1]){_.label=t[1];t=op;break;}if(t&&_.label<t[2]){_.label=t[2];_.ops.push(op);break;}if(t[2])_.ops.pop();_.trys.pop();continue;}op=body.call(thisArg,_);}catch(e){op=[6,e];y=0;}finally{f=t=0;}if(op[0]&5)throw op[1];return {value:op[0]?op[1]:void 0,done:true};}};Object.defineProperty(exports,"__esModule",{value:true});exports.BasicPipeline=exports.Stage=void 0;var image_1=__webpack_require__(2);var Stage=/** @class */function(){function Stage(pipeline){this.pipeline=pipeline;this._map={};}Stage.prototype.names=function(){return Object.keys(this._map);};Stage.prototype.has=function(name){return !!this._map[name];};Stage.prototype.get=function(name){return this._map[name];};Stage.prototype.register=function(name,stageFn){this._map[name]=stageFn;return this.pipeline;};return Stage;}();exports.Stage=Stage;var BasicPipeline=/** @class */function(){function BasicPipeline(){this.filter=new Stage(this);this.quantizer=new Stage(this);this.generator=new Stage(this);}BasicPipeline.prototype._buildProcessTasks=function(_a){var _this=this;var filters=_a.filters,quantizer=_a.quantizer,generators=_a.generators;// Support wildcard for generators
if(generators.length===1&&generators[0]==='*'){generators=this.generator.names();}return {filters:filters.map(function(f){return createTask(_this.filter,f);}),quantizer:createTask(this.quantizer,quantizer),generators:generators.map(function(g){return createTask(_this.generator,g);})};function createTask(stage,o){var name;var options;if(typeof o==='string'){name=o;}else {name=o.name;options=o.options;}return {name:name,fn:stage.get(name),options:options};}};BasicPipeline.prototype.process=function(imageData,opts){return __awaiter(this,void 0,void 0,function(){var _a,filters,quantizer,generators,imageFilterData,colors,palettes;return __generator(this,function(_b){switch(_b.label){case 0:_a=this._buildProcessTasks(opts),filters=_a.filters,quantizer=_a.quantizer,generators=_a.generators;return [4/*yield*/,this._filterColors(filters,imageData)];case 1:imageFilterData=_b.sent();return [4/*yield*/,this._generateColors(quantizer,imageFilterData)];case 2:colors=_b.sent();return [4/*yield*/,this._generatePalettes(generators,colors)];case 3:palettes=_b.sent();return [2/*return*/,{colors:colors,palettes:palettes}];}});});};BasicPipeline.prototype._filterColors=function(filters,imageData){return Promise.resolve(image_1.applyFilters(imageData,filters.map(function(_a){var fn=_a.fn;return fn;})));};BasicPipeline.prototype._generateColors=function(quantizer,imageData){return Promise.resolve(quantizer.fn(imageData.data,quantizer.options));};BasicPipeline.prototype._generatePalettes=function(generators,colors){return __awaiter(this,void 0,void 0,function(){var promiseArr;return __generator(this,function(_a){switch(_a.label){case 0:return [4/*yield*/,Promise.all(generators.map(function(_a){var fn=_a.fn,options=_a.options;return Promise.resolve(fn(colors,options));}))// Map the values to the expected name
];case 1:promiseArr=_a.sent();// Map the values to the expected name
return [2/*return*/,Promise.resolve(promiseArr.reduce(function(promises,promiseVal,i){promises[generators[i].name]=promiseVal;return promises;},{}))];}});});};return BasicPipeline;}();exports.BasicPipeline=BasicPipeline;/***/}/******/]));});});var Vibrant = unwrapExports(vibrant);

// We import the minified bundle because the unminified bundle
const CONTRAST_RATIO=4.5;// How much the total diff between 2 RGB colors can be
// to be considered similar.
const COLOR_SIMILARITY_THRESHOLD=150;// For debug purposes, is being tree shaken.
const DEBUG_COLOR=__DEV__&&false;const logColor=(color,label=`${color.hex} - ${color.population}`)=>// eslint-disable-next-line no-console
console.log(`%c${label}`,`color: ${color.bodyTextColor}; background-color: ${color.hex}`);const customGenerator=colors=>{colors.sort((colorA,colorB)=>colorB.population-colorA.population);const backgroundColor=colors[0];let foregroundColor;const contrastRatios=new Map();const approvedContrastRatio=(hex,rgb)=>{if(!contrastRatios.has(hex)){contrastRatios.set(hex,getRGBContrastRatio(backgroundColor.rgb,rgb));}return contrastRatios.get(hex)>CONTRAST_RATIO;};// We take each next color and find one that has better contrast.
for(let i=1;i<colors.length&&foregroundColor===undefined;i++){// If this color matches, score, take it.
if(approvedContrastRatio(colors[i].hex,colors[i].rgb)){if(DEBUG_COLOR){logColor(colors[i],"PICKED");}foregroundColor=colors[i].rgb;break;}// This color has the wrong contrast ratio, but it is the right color.
// Let's find similar colors that might have the right contrast ratio
const currentColor=colors[i];if(DEBUG_COLOR){logColor(colors[i],"Finding similar color with better contrast");}for(let j=i+1;j<colors.length;j++){const compareColor=colors[j];// difference. 0 is same, 765 max difference
const diffScore=Math.abs(currentColor.rgb[0]-compareColor.rgb[0])+Math.abs(currentColor.rgb[1]-compareColor.rgb[1])+Math.abs(currentColor.rgb[2]-compareColor.rgb[2]);if(DEBUG_COLOR){logColor(colors[j],`${colors[j].hex} - ${diffScore}`);}if(diffScore>COLOR_SIMILARITY_THRESHOLD){continue;}if(approvedContrastRatio(compareColor.hex,compareColor.rgb)){if(DEBUG_COLOR){logColor(compareColor,"PICKED");}foregroundColor=compareColor.rgb;break;}}}if(foregroundColor===undefined){foregroundColor=// @ts-expect-error
backgroundColor.getYiq()<200?[255,255,255]:[0,0,0];}if(DEBUG_COLOR){// eslint-disable-next-line no-console
console.log();// eslint-disable-next-line no-console
console.log("%cPicked colors",`color: ${foregroundColor}; background-color: ${backgroundColor.hex}; font-weight: bold; padding: 16px;`);colors.forEach(color=>logColor(color));// eslint-disable-next-line no-console
console.log();}return {// We can't import Swatch constructor from the minified bundle, take it from background color.
// @ts-expect-error
foreground:new backgroundColor.constructor(foregroundColor,0),background:backgroundColor};};// Set our custom generator as the default.
Vibrant._pipeline.generator.register("default",customGenerator);const extractColors=(url,downsampleColors=16)=>new Vibrant(url,{colorCount:downsampleColors}).getPalette().then(({foreground,background})=>({background:background,foreground:foreground}));

_decorate([n("hui-marquee")],function(_initialize,_LitElement){class HuiMarquee extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiMarquee,d:[{kind:"field",decorators:[e()],key:"text",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"active",value:void 0},{kind:"field",decorators:[e({reflect:true,type:Boolean,attribute:"animating"})],key:"_animating",value(){return false;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(changedProps){_get(_getPrototypeOf(HuiMarquee.prototype),"firstUpdated",this).call(this,changedProps);// eslint-disable-next-line wc/no-self-class
this.addEventListener("mouseover",()=>this.classList.add("hovering"),{// Capture because we need to run before a parent sets active on us.
// Hovering will disable the overflow, allowing us to calc if we overflow.
capture:true});// eslint-disable-next-line wc/no-self-class
this.addEventListener("mouseout",()=>this.classList.remove("hovering"));}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(HuiMarquee.prototype),"updated",this).call(this,changedProperties);if(changedProperties.has("text")&&this._animating){this._animating=false;}if(changedProperties.has("active")&&this.active&&this.offsetWidth<this.scrollWidth){this._animating=true;}}},{kind:"method",key:"render",value:function render(){if(!this.text){return $``;}return $`
      <div class="marquee-inner" @animationiteration=${this._onIteration}>
        <span>${this.text}</span>
        ${this._animating?$` <span>${this.text}</span> `:""}
      </div>
    `;}},{kind:"method",key:"_onIteration",value:function _onIteration(){if(!this.active){this._animating=false;}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: flex;
        position: relative;
        align-items: center;
        height: 1.2em;
        contain: strict;
      }

      .marquee-inner {
        position: absolute;
        left: 0;
        right: 0;
        text-overflow: ellipsis;
        overflow: hidden;
      }

      :host(.hovering) .marquee-inner {
        text-overflow: initial;
        overflow: initial;
      }

      :host([animating]) .marquee-inner {
        left: initial;
        right: initial;
        animation: marquee 10s linear infinite;
      }

      :host([animating]) .marquee-inner span {
        padding-right: 16px;
      }

      @keyframes marquee {
        0% {
          transform: translateX(0%);
        }
        100% {
          transform: translateX(-50%);
        }
      }
    `;}}]};},s);

let HuiMediaControlCard=_decorate([n("hui-media-control-card")],function(_initialize,_LitElement){class HuiMediaControlCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiMediaControlCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-media-control-card-editor-dev.js');return document.createElement("hui-media-control-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const includeDomains=["media_player"];const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains);return {type:"media-control",entity:foundEntities[0]||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_foregroundColor",value:void 0},{kind:"field",decorators:[t()],key:"_backgroundColor",value:void 0},{kind:"field",decorators:[t()],key:"_narrow",value(){return false;}},{kind:"field",decorators:[t()],key:"_veryNarrow",value(){return false;}},{kind:"field",decorators:[t()],key:"_cardHeight",value(){return 0;}},{kind:"field",decorators:[i("mwc-linear-progress")],key:"_progressBar",value:void 0},{kind:"field",decorators:[t()],key:"_marqueeActive",value(){return false;}},{kind:"field",key:"_progressInterval",value:void 0},{kind:"field",key:"_resizeObserver",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config.entity||config.entity.split(".")[0]!=="media_player"){throw new Error("Missing media_player entity");}this._config=config;}},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiMediaControlCard.prototype),"connectedCallback",this).call(this);this.updateComplete.then(()=>this._attachObserver());if(!this.hass||!this._config){return;}const stateObj=this._stateObj;if(!stateObj){return;}if(!this._progressInterval&&this._showProgressBar&&stateObj.state==="playing"){this._progressInterval=window.setInterval(()=>this._updateProgressBar(),1000);}}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){if(this._progressInterval){clearInterval(this._progressInterval);this._progressInterval=undefined;}if(this._resizeObserver){this._resizeObserver.disconnect();}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const stateObj=this._stateObj;if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const imageStyle={"background-image":this._image?`url(${this.hass.hassUrl(this._image)})`:"none",width:`${this._cardHeight}px`,"background-color":this._backgroundColor||""};const gradientStyle={"background-image":`linear-gradient(to right, ${this._backgroundColor}, ${this._backgroundColor+"00"})`,width:`${this._cardHeight}px`};const entityState=stateObj.state;const isOffState=entityState==="off";const isUnavailable=UNAVAILABLE_STATES.includes(entityState)||entityState==="off"&&!supportsFeature(stateObj,SUPPORT_TURN_ON);const hasNoImage=!this._image;const controls=computeMediaControls(stateObj);const showControls=controls&&(!this._veryNarrow||isOffState||entityState==="idle"||entityState==="on");const mediaDescription=computeMediaDescription(stateObj);const mediaTitleClean=cleanupMediaTitle(stateObj.attributes.media_title);return $`
      <ha-card>
        <div
          class="background ${o({"no-image":hasNoImage,off:isOffState||isUnavailable,unavailable:isUnavailable})}"
        >
          <div
            class="color-block"
            style=${i$1({"background-color":this._backgroundColor||""})}
          ></div>
          <div
            class="no-img"
            style=${i$1({"background-color":this._backgroundColor||""})}
          ></div>
          <div class="image" style=${i$1(imageStyle)}></div>
          ${hasNoImage?"":$`
                <div
                  class="color-gradient"
                  style=${i$1(gradientStyle)}
                ></div>
              `}
        </div>
        <div
          class="player ${o({"no-image":hasNoImage,narrow:this._narrow&&!this._veryNarrow,off:isOffState||isUnavailable,"no-progress":this._veryNarrow||!this._showProgressBar,"no-controls":!showControls})}"
          style=${i$1({color:this._foregroundColor||""})}
        >
          <div class="top-info">
            <div class="icon-name">
              <ha-state-icon class="icon" .state=${stateObj}></ha-state-icon>
              <div>
                ${this._config.name||computeStateName(this.hass.states[this._config.entity])}
              </div>
            </div>
            <div>
              <ha-icon-button
                .path=${mdiDotsVertical}
                .label=${this.hass.localize("ui.panel.lovelace.cards.show_more_info")}
                class="more-info"
                @click=${this._handleMoreInfo}
              ></ha-icon-button>
            </div>
          </div>
          ${!isUnavailable&&(mediaDescription||mediaTitleClean||showControls)?$`
                <div>
                  <div class="title-controls">
                    ${!mediaDescription&&!mediaTitleClean?"":$`
                          <div class="media-info">
                            <hui-marquee
                              .text=${mediaTitleClean||mediaDescription}
                              .active=${this._marqueeActive}
                              @mouseover=${this._marqueeMouseOver}
                              @mouseleave=${this._marqueeMouseLeave}
                            ></hui-marquee>
                            ${!mediaTitleClean?"":mediaDescription}
                          </div>
                        `}
                    ${!showControls?"":$`
                          <div class="controls">
                            ${controls.map(control=>$`
                                <ha-icon-button
                                  .label=${this.hass.localize(`ui.card.media_player.${control.action}`)}
                                  .path=${control.icon}
                                  action=${control.action}
                                  @click=${this._handleClick}
                                >
                                </ha-icon-button>
                              `)}
                            ${supportsFeature(stateObj,SUPPORT_BROWSE_MEDIA)?$`
                                  <ha-icon-button
                                    class="browse-media"
                                    .label=${this.hass.localize("ui.card.media_player.browse_media")}
                                    .path=${mdiPlayBoxMultiple}
                                    @click=${this._handleBrowseMedia}
                                  ></ha-icon-button>
                                `:""}
                          </div>
                        `}
                  </div>
                  ${!this._showProgressBar?"":$`
                        <mwc-linear-progress
                          determinate
                          style=${i$1({"--mdc-theme-primary":this._foregroundColor||"var(--accent-color)",cursor:supportsFeature(stateObj,SUPPORT_SEEK)?"pointer":"initial"})}
                          @click=${this._handleSeek}
                        >
                        </mwc-linear-progress>
                      `}
                </div>
              `:""}
        </div>
      </ha-card>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){this._attachObserver();}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){var _oldHass$states$this$,_oldHass$states$this$2;_get(_getPrototypeOf(HuiMediaControlCard.prototype),"willUpdate",this).call(this,changedProps);if(!this.hasUpdated){this._measureCard();}if(!this._config||!this.hass||!changedProps.has("_config")&&!changedProps.has("hass")){return;}const stateObj=this._stateObj;if(!stateObj){if(this._progressInterval){clearInterval(this._progressInterval);this._progressInterval=undefined;}this._foregroundColor=undefined;this._backgroundColor=undefined;return;}const oldHass=changedProps.get("hass");const oldImage=(oldHass===null||oldHass===void 0?void 0:(_oldHass$states$this$=oldHass.states[this._config.entity])===null||_oldHass$states$this$===void 0?void 0:_oldHass$states$this$.attributes.entity_picture_local)||(oldHass===null||oldHass===void 0?void 0:(_oldHass$states$this$2=oldHass.states[this._config.entity])===null||_oldHass$states$this$2===void 0?void 0:_oldHass$states$this$2.attributes.entity_picture);if(!this._image){this._foregroundColor=undefined;this._backgroundColor=undefined;return;}if(this._image!==oldImage){this._setColors();}}},{kind:"method",key:"updated",value:function updated(changedProps){if(!this._config||!this.hass||!this._stateObj||!changedProps.has("_config")&&!changedProps.has("hass")){return;}const stateObj=this._stateObj;const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}this._updateProgressBar();if(!this._progressInterval&&this._showProgressBar&&stateObj.state==="playing"){this._progressInterval=window.setInterval(()=>this._updateProgressBar(),1000);}else if(this._progressInterval&&(!this._showProgressBar||stateObj.state!=="playing")){clearInterval(this._progressInterval);this._progressInterval=undefined;}}},{kind:"get",key:"_image",value:function _image(){if(!this.hass||!this._config){return undefined;}const stateObj=this._stateObj;if(!stateObj){return undefined;}return stateObj.attributes.entity_picture_local||stateObj.attributes.entity_picture;}},{kind:"get",key:"_showProgressBar",value:function _showProgressBar(){if(!this.hass||!this._config||this._narrow){return false;}const stateObj=this._stateObj;if(!stateObj){return false;}return (stateObj.state==="playing"||stateObj.state==="paused")&&"media_duration"in stateObj.attributes&&"media_position"in stateObj.attributes;}},{kind:"method",key:"_measureCard",value:function _measureCard(){const card=this.shadowRoot.querySelector("ha-card");if(!card){return;}this._narrow=card.offsetWidth<350;this._veryNarrow=card.offsetWidth<300;this._cardHeight=card.offsetHeight;}},{kind:"method",key:"_attachObserver",value:async function _attachObserver(){if(!this._resizeObserver){await installResizeObserver();this._resizeObserver=new ResizeObserver(debounce(()=>this._measureCard(),250,false));}const card=this.shadowRoot.querySelector("ha-card");// If we show an error or warning there is no ha-card
if(!card){return;}this._resizeObserver.observe(card);}},{kind:"method",key:"_handleMoreInfo",value:function _handleMoreInfo(){fireEvent(this,"hass-more-info",{entityId:this._config.entity});}},{kind:"method",key:"_handleBrowseMedia",value:function _handleBrowseMedia(){showMediaBrowserDialog(this,{action:"play",entityId:this._config.entity,mediaPickedCallback:pickedMedia=>this._playMedia(pickedMedia.item.media_content_id,pickedMedia.item.media_content_type)});}},{kind:"method",key:"_playMedia",value:function _playMedia(media_content_id,media_content_type){this.hass.callService("media_player","play_media",{entity_id:this._config.entity,media_content_id,media_content_type});}},{kind:"method",key:"_handleClick",value:function _handleClick(e){const action=e.currentTarget.getAttribute("action");this.hass.callService("media_player",action,{entity_id:this._config.entity});}},{kind:"method",key:"_updateProgressBar",value:function _updateProgressBar(){var _this$_stateObj;if(this._progressBar&&(_this$_stateObj=this._stateObj)!==null&&_this$_stateObj!==void 0&&_this$_stateObj.attributes.media_duration){this._progressBar.progress=getCurrentProgress(this._stateObj)/this._stateObj.attributes.media_duration;}}},{kind:"get",key:"_stateObj",value:function _stateObj(){return this.hass.states[this._config.entity];}},{kind:"method",key:"_handleSeek",value:function _handleSeek(e){const stateObj=this._stateObj;if(!supportsFeature(stateObj,SUPPORT_SEEK)){return;}const progressWidth=this._progressBar.offsetWidth;const percent=e.offsetX/progressWidth;const position=this._stateObj.attributes.media_duration*percent;this.hass.callService("media_player","media_seek",{entity_id:this._config.entity,seek_position:position});}},{kind:"method",key:"_setColors",value:async function _setColors(){if(!this._image){return;}try{const{foreground,background}=await extractColors(this.hass.hassUrl(this._image));this._backgroundColor=background.hex;this._foregroundColor=foreground.hex;}catch(err){// eslint-disable-next-line no-console
console.error("Error getting Image Colors",err);this._foregroundColor=undefined;this._backgroundColor=undefined;}}},{kind:"method",key:"_marqueeMouseOver",value:function _marqueeMouseOver(){if(!this._marqueeActive){this._marqueeActive=true;}}},{kind:"method",key:"_marqueeMouseLeave",value:function _marqueeMouseLeave(){if(this._marqueeActive){this._marqueeActive=false;}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        overflow: hidden;
        height: 100%;
      }

      .background {
        display: flex;
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        transition: filter 0.8s;
      }

      .color-block {
        background-color: var(--primary-color);
        transition: background-color 0.8s;
        width: 100%;
      }

      .color-gradient {
        position: absolute;
        background-image: linear-gradient(
          to right,
          var(--primary-color),
          transparent
        );
        height: 100%;
        right: 0;
        opacity: 1;
        transition: width 0.8s, opacity 0.8s linear 0.8s;
      }

      .image {
        background-color: var(--primary-color);
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        position: absolute;
        right: 0;
        height: 100%;
        opacity: 1;
        transition: width 0.8s, background-image 0.8s, background-color 0.8s,
          background-size 0.8s, opacity 0.8s linear 0.8s;
      }

      .no-image .image {
        opacity: 0;
      }

      .no-img {
        background-color: var(--primary-color);
        background-size: initial;
        background-repeat: no-repeat;
        background-position: center center;
        padding-bottom: 0;
        position: absolute;
        right: 0;
        height: 100%;
        background-image: url("/static/images/card_media_player_bg.png");
        width: 50%;
        transition: opacity 0.8s, background-color 0.8s;
      }

      .off .image,
      .off .color-gradient {
        opacity: 0;
        transition: opacity 0s, width 0.8s;
        width: 0;
      }

      .unavailable .no-img,
      .background:not(.off):not(.no-image) .no-img {
        opacity: 0;
      }

      .player {
        position: relative;
        padding: 16px;
        height: 100%;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        color: var(--text-primary-color);
        transition-property: color, padding;
        transition-duration: 0.4s;
      }

      .controls {
        padding: 8px 8px 8px 0;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        transition: padding, color;
        transition-duration: 0.4s;
        margin-left: -12px;
      }

      .controls > div {
        display: flex;
        align-items: center;
      }

      .controls ha-icon-button {
        --mdc-icon-button-size: 44px;
        --mdc-icon-size: 30px;
      }

      ha-icon-button[action="media_play"],
      ha-icon-button[action="media_play_pause"],
      ha-icon-button[action="media_pause"],
      ha-icon-button[action="media_stop"],
      ha-icon-button[action="turn_on"],
      ha-icon-button[action="turn_off"] {
        --mdc-icon-button-size: 56px;
        --mdc-icon-size: 40px;
      }

      ha-icon-button.browse-media {
        position: absolute;
        right: 4px;
        --mdc-icon-size: 24px;
      }

      .top-info {
        display: flex;
        justify-content: space-between;
      }

      .icon-name {
        display: flex;
        height: fit-content;
        align-items: center;
      }

      .icon-name ha-state-icon {
        padding-right: 8px;
      }

      .more-info {
        position: absolute;
        top: 4px;
        right: 4px;
      }

      .media-info {
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
      }

      hui-marquee {
        font-size: 1.2em;
        margin: 0px 0 4px;
      }

      .title-controls {
        padding-top: 16px;
      }

      mwc-linear-progress {
        width: 100%;
        margin-top: 4px;
        --mdc-linear-progress-buffer-color: rgba(200, 200, 200, 0.5);
      }

      .no-image .controls {
        padding: 0;
      }

      .off.background {
        filter: grayscale(1);
      }

      .narrow .controls,
      .no-progress .controls {
        padding-bottom: 0;
      }

      .narrow ha-icon-button {
        --mdc-icon-button-size: 40px;
        --mdc-icon-size: 28px;
      }

      .narrow ha-icon-button[action="media_play"],
      .narrow ha-icon-button[action="media_play_pause"],
      .narrow ha-icon-button[action="media_pause"],
      .narrow ha-icon-button[action="turn_on"] {
        --mdc-icon-button-size: 50px;
        --mdc-icon-size: 36px;
      }

      .narrow ha-icon-button.browse-media {
        --mdc-icon-size: 24px;
      }

      .no-progress.player:not(.no-controls) {
        padding-bottom: 0px;
      }
    `;}}]};},s);

export { HuiMediaControlCard };
