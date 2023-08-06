const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { U as __extends, V as __assign, ay as MDCFoundation, ah as __decorate, G as i, d as e, az as BaseElement, $, z as o, aA as addHasRemoveClass, r, n, aB as observer, t, R as e$1, K as e$2, T as RippleHandlers, aC as matches, aD as closest, _ as _decorate, j as _get, k as _getPrototypeOf, at as mdiClose, c as s, Z as o$1 } from './main-dev.js';

/**
 * @license
 * Copyright 2018 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */var cssClasses$2={ACTIVE:'mdc-tab-indicator--active',FADE:'mdc-tab-indicator--fade',NO_TRANSITION:'mdc-tab-indicator--no-transition'};var strings$2={CONTENT_SELECTOR:'.mdc-tab-indicator__content'};

var MDCTabIndicatorFoundation=/** @class */function(_super){__extends(MDCTabIndicatorFoundation,_super);function MDCTabIndicatorFoundation(adapter){return _super.call(this,__assign(__assign({},MDCTabIndicatorFoundation.defaultAdapter),adapter))||this;}Object.defineProperty(MDCTabIndicatorFoundation,"cssClasses",{get:function(){return cssClasses$2;},enumerable:false,configurable:true});Object.defineProperty(MDCTabIndicatorFoundation,"strings",{get:function(){return strings$2;},enumerable:false,configurable:true});Object.defineProperty(MDCTabIndicatorFoundation,"defaultAdapter",{get:function(){// tslint:disable:object-literal-sort-keys Methods should be in the same order as the adapter interface.
return {addClass:function(){return undefined;},removeClass:function(){return undefined;},computeContentClientRect:function(){return {top:0,right:0,bottom:0,left:0,width:0,height:0};},setContentStyleProperty:function(){return undefined;}};// tslint:enable:object-literal-sort-keys
},enumerable:false,configurable:true});MDCTabIndicatorFoundation.prototype.computeContentClientRect=function(){return this.adapter.computeContentClientRect();};return MDCTabIndicatorFoundation;}(MDCFoundation);

/* istanbul ignore next: subclass is not a branch statement */var MDCFadingTabIndicatorFoundation=/** @class */function(_super){__extends(MDCFadingTabIndicatorFoundation,_super);function MDCFadingTabIndicatorFoundation(){return _super!==null&&_super.apply(this,arguments)||this;}MDCFadingTabIndicatorFoundation.prototype.activate=function(){this.adapter.addClass(MDCTabIndicatorFoundation.cssClasses.ACTIVE);};MDCFadingTabIndicatorFoundation.prototype.deactivate=function(){this.adapter.removeClass(MDCTabIndicatorFoundation.cssClasses.ACTIVE);};return MDCFadingTabIndicatorFoundation;}(MDCTabIndicatorFoundation);var MDCFadingTabIndicatorFoundation$1 = MDCFadingTabIndicatorFoundation;

/* istanbul ignore next: subclass is not a branch statement */var MDCSlidingTabIndicatorFoundation=/** @class */function(_super){__extends(MDCSlidingTabIndicatorFoundation,_super);function MDCSlidingTabIndicatorFoundation(){return _super!==null&&_super.apply(this,arguments)||this;}MDCSlidingTabIndicatorFoundation.prototype.activate=function(previousIndicatorClientRect){// Early exit if no indicator is present to handle cases where an indicator
// may be activated without a prior indicator state
if(!previousIndicatorClientRect){this.adapter.addClass(MDCTabIndicatorFoundation.cssClasses.ACTIVE);return;}// This animation uses the FLIP approach. You can read more about it at the link below:
// https://aerotwist.com/blog/flip-your-animations/
// Calculate the dimensions based on the dimensions of the previous indicator
var currentClientRect=this.computeContentClientRect();var widthDelta=previousIndicatorClientRect.width/currentClientRect.width;var xPosition=previousIndicatorClientRect.left-currentClientRect.left;this.adapter.addClass(MDCTabIndicatorFoundation.cssClasses.NO_TRANSITION);this.adapter.setContentStyleProperty('transform',"translateX("+xPosition+"px) scaleX("+widthDelta+")");// Force repaint before updating classes and transform to ensure the transform properly takes effect
this.computeContentClientRect();this.adapter.removeClass(MDCTabIndicatorFoundation.cssClasses.NO_TRANSITION);this.adapter.addClass(MDCTabIndicatorFoundation.cssClasses.ACTIVE);this.adapter.setContentStyleProperty('transform','');};MDCSlidingTabIndicatorFoundation.prototype.deactivate=function(){this.adapter.removeClass(MDCTabIndicatorFoundation.cssClasses.ACTIVE);};return MDCSlidingTabIndicatorFoundation;}(MDCTabIndicatorFoundation);var MDCSlidingTabIndicatorFoundation$1 = MDCSlidingTabIndicatorFoundation;

class TabIndicatorBase extends BaseElement{constructor(){super(...arguments);this.icon='';this.fade=false;}get mdcFoundationClass(){return this.fade?MDCFadingTabIndicatorFoundation$1:MDCSlidingTabIndicatorFoundation$1;}render(){const contentClasses={'mdc-tab-indicator__content--icon':this.icon,'material-icons':this.icon,'mdc-tab-indicator__content--underline':!this.icon};return $`
      <span class="mdc-tab-indicator ${o({'mdc-tab-indicator--fade':this.fade})}">
        <span class="mdc-tab-indicator__content ${o(contentClasses)}">${this.icon}</span>
      </span>
      `;}updated(changedProperties){if(changedProperties.has('fade')){this.createFoundation();}}createAdapter(){return Object.assign(Object.assign({},addHasRemoveClass(this.mdcRoot)),{computeContentClientRect:()=>this.contentElement.getBoundingClientRect(),setContentStyleProperty:(prop,value)=>this.contentElement.style.setProperty(prop,value)});}computeContentClientRect(){return this.mdcFoundation.computeContentClientRect();}activate(previousIndicatorClientRect){this.mdcFoundation.activate(previousIndicatorClientRect);}deactivate(){this.mdcFoundation.deactivate();}}__decorate([i('.mdc-tab-indicator')],TabIndicatorBase.prototype,"mdcRoot",void 0);__decorate([i('.mdc-tab-indicator__content')],TabIndicatorBase.prototype,"contentElement",void 0);__decorate([e()],TabIndicatorBase.prototype,"icon",void 0);__decorate([e({type:Boolean})],TabIndicatorBase.prototype,"fade",void 0);

const styles$2=r`.material-icons{font-family:var(--mdc-icon-font, "Material Icons");font-weight:normal;font-style:normal;font-size:var(--mdc-icon-size, 24px);line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;-moz-osx-font-smoothing:grayscale;font-feature-settings:"liga"}.mdc-tab-indicator .mdc-tab-indicator__content--underline{border-color:#6200ee;border-color:var(--mdc-theme-primary, #6200ee)}.mdc-tab-indicator .mdc-tab-indicator__content--icon{color:#018786;color:var(--mdc-theme-secondary, #018786)}.mdc-tab-indicator .mdc-tab-indicator__content--underline{border-top-width:2px}.mdc-tab-indicator .mdc-tab-indicator__content--icon{height:34px;font-size:34px}.mdc-tab-indicator{display:flex;position:absolute;top:0;left:0;justify-content:center;width:100%;height:100%;pointer-events:none;z-index:1}.mdc-tab-indicator__content{transform-origin:left;opacity:0}.mdc-tab-indicator__content--underline{align-self:flex-end;box-sizing:border-box;width:100%;border-top-style:solid}.mdc-tab-indicator__content--icon{align-self:center;margin:0 auto}.mdc-tab-indicator--active .mdc-tab-indicator__content{opacity:1}.mdc-tab-indicator .mdc-tab-indicator__content{transition:250ms transform cubic-bezier(0.4, 0, 0.2, 1)}.mdc-tab-indicator--no-transition .mdc-tab-indicator__content{transition:none}.mdc-tab-indicator--fade .mdc-tab-indicator__content{transition:150ms opacity linear}.mdc-tab-indicator--active.mdc-tab-indicator--fade .mdc-tab-indicator__content{transition-delay:100ms}`;

let TabIndicator=class TabIndicator extends TabIndicatorBase{};TabIndicator.styles=[styles$2];TabIndicator=__decorate([n('mwc-tab-indicator')],TabIndicator);

/**
 * @license
 * Copyright 2018 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */var cssClasses$1={ACTIVE:'mdc-tab--active'};var strings$1={ARIA_SELECTED:'aria-selected',CONTENT_SELECTOR:'.mdc-tab__content',INTERACTED_EVENT:'MDCTab:interacted',RIPPLE_SELECTOR:'.mdc-tab__ripple',TABINDEX:'tabIndex',TAB_INDICATOR_SELECTOR:'.mdc-tab-indicator'};

var MDCTabFoundation=/** @class */function(_super){__extends(MDCTabFoundation,_super);function MDCTabFoundation(adapter){var _this=_super.call(this,__assign(__assign({},MDCTabFoundation.defaultAdapter),adapter))||this;_this.focusOnActivate=true;return _this;}Object.defineProperty(MDCTabFoundation,"cssClasses",{get:function(){return cssClasses$1;},enumerable:false,configurable:true});Object.defineProperty(MDCTabFoundation,"strings",{get:function(){return strings$1;},enumerable:false,configurable:true});Object.defineProperty(MDCTabFoundation,"defaultAdapter",{get:function(){// tslint:disable:object-literal-sort-keys Methods should be in the same order as the adapter interface.
return {addClass:function(){return undefined;},removeClass:function(){return undefined;},hasClass:function(){return false;},setAttr:function(){return undefined;},activateIndicator:function(){return undefined;},deactivateIndicator:function(){return undefined;},notifyInteracted:function(){return undefined;},getOffsetLeft:function(){return 0;},getOffsetWidth:function(){return 0;},getContentOffsetLeft:function(){return 0;},getContentOffsetWidth:function(){return 0;},focus:function(){return undefined;}};// tslint:enable:object-literal-sort-keys
},enumerable:false,configurable:true});MDCTabFoundation.prototype.handleClick=function(){// It's up to the parent component to keep track of the active Tab and
// ensure we don't activate a Tab that's already active.
this.adapter.notifyInteracted();};MDCTabFoundation.prototype.isActive=function(){return this.adapter.hasClass(cssClasses$1.ACTIVE);};/**
     * Sets whether the tab should focus itself when activated
     */MDCTabFoundation.prototype.setFocusOnActivate=function(focusOnActivate){this.focusOnActivate=focusOnActivate;};/**
     * Activates the Tab
     */MDCTabFoundation.prototype.activate=function(previousIndicatorClientRect){this.adapter.addClass(cssClasses$1.ACTIVE);this.adapter.setAttr(strings$1.ARIA_SELECTED,'true');this.adapter.setAttr(strings$1.TABINDEX,'0');this.adapter.activateIndicator(previousIndicatorClientRect);if(this.focusOnActivate){this.adapter.focus();}};/**
     * Deactivates the Tab
     */MDCTabFoundation.prototype.deactivate=function(){// Early exit
if(!this.isActive()){return;}this.adapter.removeClass(cssClasses$1.ACTIVE);this.adapter.setAttr(strings$1.ARIA_SELECTED,'false');this.adapter.setAttr(strings$1.TABINDEX,'-1');this.adapter.deactivateIndicator();};/**
     * Returns the dimensions of the Tab
     */MDCTabFoundation.prototype.computeDimensions=function(){var rootWidth=this.adapter.getOffsetWidth();var rootLeft=this.adapter.getOffsetLeft();var contentWidth=this.adapter.getContentOffsetWidth();var contentLeft=this.adapter.getContentOffsetLeft();return {contentLeft:rootLeft+contentLeft,contentRight:rootLeft+contentLeft+contentWidth,rootLeft:rootLeft,rootRight:rootLeft+rootWidth};};return MDCTabFoundation;}(MDCFoundation);var MDCTabFoundation$1 = MDCTabFoundation;

let tabIdCounter=0;class TabBase extends BaseElement{constructor(){super(...arguments);this.mdcFoundationClass=MDCTabFoundation$1;this.label='';this.icon='';this.hasImageIcon=false;this.isFadingIndicator=false;this.minWidth=false;this.isMinWidthIndicator=false;this.indicatorIcon='';this.stacked=false;this.focusOnActivate=true;this._active=false;this.initFocus=false;this.shouldRenderRipple=false;this.useStateLayerCustomProperties=false;this.rippleElement=null;this.rippleHandlers=new RippleHandlers(()=>{this.shouldRenderRipple=true;this.ripple.then(v=>this.rippleElement=v);return this.ripple;});}get active(){return this._active;}connectedCallback(){this.dir=document.dir;super.connectedCallback();}firstUpdated(){super.firstUpdated();// create an unique id
this.id=this.id||`mdc-tab-${++tabIdCounter}`;}render(){const classes={'mdc-tab--min-width':this.minWidth,'mdc-tab--stacked':this.stacked};let iconTemplate=$``;if(this.hasImageIcon||this.icon){// NOTE: MUST be on same line as spaces will cause vert alignment issues
// in IE
iconTemplate=$`
        <span class="mdc-tab__icon material-icons"><slot name="icon">${this.icon}</slot></span>`;}let labelTemplate=$``;if(this.label){labelTemplate=$`
        <span class="mdc-tab__text-label">${this.label}</span>`;}return $`
      <button
        @click="${this.handleClick}"
        class="mdc-tab ${o(classes)}"
        role="tab"
        aria-selected="false"
        tabindex="-1"
        @focus="${this.focus}"
        @blur="${this.handleBlur}"
        @mousedown="${this.handleRippleMouseDown}"
        @mouseenter="${this.handleRippleMouseEnter}"
        @mouseleave="${this.handleRippleMouseLeave}"
        @touchstart="${this.handleRippleTouchStart}"
        @touchend="${this.handleRippleDeactivate}"
        @touchcancel="${this.handleRippleDeactivate}">
        <span class="mdc-tab__content">
          ${iconTemplate}
          ${labelTemplate}
          ${this.isMinWidthIndicator?this.renderIndicator():''}
        </span>
        ${this.isMinWidthIndicator?'':this.renderIndicator()}
        ${this.renderRipple()}
      </button>`;}renderIndicator(){return $`<mwc-tab-indicator
        .icon="${this.indicatorIcon}"
        .fade="${this.isFadingIndicator}"></mwc-tab-indicator>`;}// TODO(dfreedm): Make this use selected as a param after Polymer/internal#739
/** @soyCompatible */renderRipple(){return this.shouldRenderRipple?$`<mwc-ripple primary
        .internalUseStateLayerCustomProperties="${this.useStateLayerCustomProperties}"></mwc-ripple>`:'';}createAdapter(){return Object.assign(Object.assign({},addHasRemoveClass(this.mdcRoot)),{setAttr:(attr,value)=>this.mdcRoot.setAttribute(attr,value),activateIndicator:async previousIndicatorClientRect=>{await this.tabIndicator.updateComplete;this.tabIndicator.activate(previousIndicatorClientRect);},deactivateIndicator:async()=>{await this.tabIndicator.updateComplete;this.tabIndicator.deactivate();},notifyInteracted:()=>this.dispatchEvent(new CustomEvent(MDCTabFoundation$1.strings.INTERACTED_EVENT,{detail:{tabId:this.id},bubbles:true,composed:true,cancelable:true})),getOffsetLeft:()=>this.offsetLeft,getOffsetWidth:()=>this.mdcRoot.offsetWidth,getContentOffsetLeft:()=>this._contentElement.offsetLeft,getContentOffsetWidth:()=>this._contentElement.offsetWidth,focus:()=>{if(this.initFocus){this.initFocus=false;}else {this.mdcRoot.focus();}}});}activate(clientRect){// happens only on initialization. We don't want to focus to prevent scroll
if(!clientRect){this.initFocus=true;}if(this.mdcFoundation){this.mdcFoundation.activate(clientRect);this.setActive(this.mdcFoundation.isActive());}else {// happens if this is called by tab-bar on initialization, but tab has not
// finished rendering.
this.updateComplete.then(()=>{this.mdcFoundation.activate(clientRect);this.setActive(this.mdcFoundation.isActive());});}}deactivate(){this.mdcFoundation.deactivate();this.setActive(this.mdcFoundation.isActive());}setActive(newValue){const oldValue=this.active;if(oldValue!==newValue){this._active=newValue;this.requestUpdate('active',oldValue);}}computeDimensions(){return this.mdcFoundation.computeDimensions();}computeIndicatorClientRect(){return this.tabIndicator.computeContentClientRect();}// NOTE: needed only for ShadyDOM where delegatesFocus is not implemented
focus(){this.mdcRoot.focus();this.handleFocus();}handleClick(){this.handleFocus();this.mdcFoundation.handleClick();}handleFocus(){this.handleRippleFocus();}handleBlur(){this.handleRippleBlur();}handleRippleMouseDown(event){const onUp=()=>{window.removeEventListener('mouseup',onUp);this.handleRippleDeactivate();};window.addEventListener('mouseup',onUp);this.rippleHandlers.startPress(event);}handleRippleTouchStart(event){this.rippleHandlers.startPress(event);}handleRippleDeactivate(){this.rippleHandlers.endPress();}handleRippleMouseEnter(){this.rippleHandlers.startHover();}handleRippleMouseLeave(){this.rippleHandlers.endHover();}handleRippleFocus(){this.rippleHandlers.startFocus();}handleRippleBlur(){this.rippleHandlers.endFocus();}get isRippleActive(){var _a;return ((_a=this.rippleElement)===null||_a===void 0?void 0:_a.isActive)||false;}}TabBase.shadowRootOptions={mode:'open',delegatesFocus:true};__decorate([i('.mdc-tab')],TabBase.prototype,"mdcRoot",void 0);__decorate([i('mwc-tab-indicator')],TabBase.prototype,"tabIndicator",void 0);__decorate([e()],TabBase.prototype,"label",void 0);__decorate([e()],TabBase.prototype,"icon",void 0);__decorate([e({type:Boolean})],TabBase.prototype,"hasImageIcon",void 0);__decorate([e({type:Boolean})],TabBase.prototype,"isFadingIndicator",void 0);__decorate([e({type:Boolean})],TabBase.prototype,"minWidth",void 0);__decorate([e({type:Boolean})],TabBase.prototype,"isMinWidthIndicator",void 0);__decorate([e({type:Boolean,reflect:true,attribute:'active'})],TabBase.prototype,"active",null);__decorate([e()],TabBase.prototype,"indicatorIcon",void 0);__decorate([e({type:Boolean})],TabBase.prototype,"stacked",void 0);__decorate([observer(async function(value){await this.updateComplete;this.mdcFoundation.setFocusOnActivate(value);}),e({type:Boolean})],TabBase.prototype,"focusOnActivate",void 0);__decorate([i('.mdc-tab__content')],TabBase.prototype,"_contentElement",void 0);__decorate([t()],TabBase.prototype,"shouldRenderRipple",void 0);__decorate([t()],TabBase.prototype,"useStateLayerCustomProperties",void 0);__decorate([e$1('mwc-ripple')],TabBase.prototype,"ripple",void 0);__decorate([e$2({passive:true})],TabBase.prototype,"handleRippleTouchStart",null);

const styles$1=r`.material-icons{font-family:var(--mdc-icon-font, "Material Icons");font-weight:normal;font-style:normal;font-size:var(--mdc-icon-size, 24px);line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;-moz-osx-font-smoothing:grayscale;font-feature-settings:"liga"}.mdc-tab{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-button-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-button-font-size, 0.875rem);line-height:2.25rem;line-height:var(--mdc-typography-button-line-height, 2.25rem);font-weight:500;font-weight:var(--mdc-typography-button-font-weight, 500);letter-spacing:0.0892857143em;letter-spacing:var(--mdc-typography-button-letter-spacing, 0.0892857143em);text-decoration:none;text-decoration:var(--mdc-typography-button-text-decoration, none);text-transform:uppercase;text-transform:var(--mdc-typography-button-text-transform, uppercase);position:relative}.mdc-tab .mdc-tab__text-label{color:rgba(0, 0, 0, 0.6)}.mdc-tab .mdc-tab__icon{color:rgba(0, 0, 0, 0.54);fill:currentColor}.mdc-tab__content{position:relative}.mdc-tab__icon{width:24px;height:24px;font-size:24px}.mdc-tab--active .mdc-tab__text-label{color:#6200ee;color:var(--mdc-theme-primary, #6200ee)}.mdc-tab--active .mdc-tab__icon{color:#6200ee;color:var(--mdc-theme-primary, #6200ee);fill:currentColor}.mdc-tab{background:none}.mdc-tab{min-width:90px;padding-right:24px;padding-left:24px;display:flex;flex:1 0 auto;justify-content:center;box-sizing:border-box;margin:0;padding-top:0;padding-bottom:0;border:none;outline:none;text-align:center;white-space:nowrap;cursor:pointer;-webkit-appearance:none;z-index:1}.mdc-tab::-moz-focus-inner{padding:0;border:0}.mdc-tab--min-width{flex:0 1 auto}.mdc-tab__content{display:flex;align-items:center;justify-content:center;height:inherit;pointer-events:none}.mdc-tab__text-label{transition:150ms color linear;display:inline-block;line-height:1;z-index:2}.mdc-tab__icon{transition:150ms color linear;z-index:2}.mdc-tab--stacked .mdc-tab__content{flex-direction:column;align-items:center;justify-content:center}.mdc-tab--stacked .mdc-tab__text-label{padding-top:6px;padding-bottom:4px}.mdc-tab--active .mdc-tab__text-label,.mdc-tab--active .mdc-tab__icon{transition-delay:100ms}.mdc-tab:not(.mdc-tab--stacked) .mdc-tab__icon+.mdc-tab__text-label{padding-left:8px;padding-right:0}[dir=rtl] .mdc-tab:not(.mdc-tab--stacked) .mdc-tab__icon+.mdc-tab__text-label,.mdc-tab:not(.mdc-tab--stacked) .mdc-tab__icon+.mdc-tab__text-label[dir=rtl]{padding-left:0;padding-right:8px}@keyframes mdc-ripple-fg-radius-in{from{animation-timing-function:cubic-bezier(0.4, 0, 0.2, 1);transform:translate(var(--mdc-ripple-fg-translate-start, 0)) scale(1)}to{transform:translate(var(--mdc-ripple-fg-translate-end, 0)) scale(var(--mdc-ripple-fg-scale, 1))}}@keyframes mdc-ripple-fg-opacity-in{from{animation-timing-function:linear;opacity:0}to{opacity:var(--mdc-ripple-fg-opacity, 0)}}@keyframes mdc-ripple-fg-opacity-out{from{animation-timing-function:linear;opacity:var(--mdc-ripple-fg-opacity, 0)}to{opacity:0}}.mdc-tab{--mdc-ripple-fg-size: 0;--mdc-ripple-left: 0;--mdc-ripple-top: 0;--mdc-ripple-fg-scale: 1;--mdc-ripple-fg-translate-end: 0;--mdc-ripple-fg-translate-start: 0;-webkit-tap-highlight-color:rgba(0,0,0,0)}.mdc-tab .mdc-tab__ripple::before,.mdc-tab .mdc-tab__ripple::after{position:absolute;border-radius:50%;opacity:0;pointer-events:none;content:""}.mdc-tab .mdc-tab__ripple::before{transition:opacity 15ms linear,background-color 15ms linear;z-index:1;z-index:var(--mdc-ripple-z-index, 1)}.mdc-tab .mdc-tab__ripple::after{z-index:0;z-index:var(--mdc-ripple-z-index, 0)}.mdc-tab.mdc-ripple-upgraded .mdc-tab__ripple::before{transform:scale(var(--mdc-ripple-fg-scale, 1))}.mdc-tab.mdc-ripple-upgraded .mdc-tab__ripple::after{top:0;left:0;transform:scale(0);transform-origin:center center}.mdc-tab.mdc-ripple-upgraded--unbounded .mdc-tab__ripple::after{top:var(--mdc-ripple-top, 0);left:var(--mdc-ripple-left, 0)}.mdc-tab.mdc-ripple-upgraded--foreground-activation .mdc-tab__ripple::after{animation:mdc-ripple-fg-radius-in 225ms forwards,mdc-ripple-fg-opacity-in 75ms forwards}.mdc-tab.mdc-ripple-upgraded--foreground-deactivation .mdc-tab__ripple::after{animation:mdc-ripple-fg-opacity-out 150ms;transform:translate(var(--mdc-ripple-fg-translate-end, 0)) scale(var(--mdc-ripple-fg-scale, 1))}.mdc-tab .mdc-tab__ripple::before,.mdc-tab .mdc-tab__ripple::after{top:calc(50% - 100%);left:calc(50% - 100%);width:200%;height:200%}.mdc-tab.mdc-ripple-upgraded .mdc-tab__ripple::after{width:var(--mdc-ripple-fg-size, 100%);height:var(--mdc-ripple-fg-size, 100%)}.mdc-tab .mdc-tab__ripple::before,.mdc-tab .mdc-tab__ripple::after{background-color:#6200ee;background-color:var(--mdc-ripple-color, var(--mdc-theme-primary, #6200ee))}.mdc-tab:hover .mdc-tab__ripple::before,.mdc-tab.mdc-ripple-surface--hover .mdc-tab__ripple::before{opacity:0.04;opacity:var(--mdc-ripple-hover-opacity, 0.04)}.mdc-tab.mdc-ripple-upgraded--background-focused .mdc-tab__ripple::before,.mdc-tab:not(.mdc-ripple-upgraded):focus .mdc-tab__ripple::before{transition-duration:75ms;opacity:0.12;opacity:var(--mdc-ripple-focus-opacity, 0.12)}.mdc-tab:not(.mdc-ripple-upgraded) .mdc-tab__ripple::after{transition:opacity 150ms linear}.mdc-tab:not(.mdc-ripple-upgraded):active .mdc-tab__ripple::after{transition-duration:75ms;opacity:0.12;opacity:var(--mdc-ripple-press-opacity, 0.12)}.mdc-tab.mdc-ripple-upgraded{--mdc-ripple-fg-opacity:var(--mdc-ripple-press-opacity, 0.12)}.mdc-tab__ripple{position:absolute;top:0;left:0;width:100%;height:100%;overflow:hidden;will-change:transform,opacity}:host{outline:none;flex:1 0 auto;display:flex;justify-content:center;-webkit-tap-highlight-color:transparent}.mdc-tab{height:var(--mdc-tab-height, 48px);margin-left:0;margin-right:0;padding-right:var(--mdc-tab-horizontal-padding, 24px);padding-left:var(--mdc-tab-horizontal-padding, 24px)}.mdc-tab--stacked{height:var(--mdc-tab-stacked-height, 72px)}.mdc-tab::-moz-focus-inner{border:0}.mdc-tab:not(.mdc-tab--stacked) .mdc-tab__icon+.mdc-tab__text-label{padding-left:8px;padding-right:0}[dir=rtl] .mdc-tab:not(.mdc-tab--stacked) .mdc-tab__icon+.mdc-tab__text-label,.mdc-tab:not(.mdc-tab--stacked) .mdc-tab__icon+.mdc-tab__text-label[dir=rtl]{padding-left:0;padding-right:8px}.mdc-tab:not(.mdc-tab--active) .mdc-tab__text-label{color:var(--mdc-tab-text-label-color-default, rgba(0, 0, 0, 0.6))}.mdc-tab:not(.mdc-tab--active) .mdc-tab__icon{color:var(--mdc-tab-color-default, rgba(0, 0, 0, 0.54))}`;

let Tab=class Tab extends TabBase{};Tab.styles=[styles$1];Tab=__decorate([n('mwc-tab')],Tab);

/**
 * @license
 * Copyright 2016 Google Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */(()=>{var _a,_b,_c;/* Symbols for private properties */const _blockingElements=Symbol();const _alreadyInertElements=Symbol();const _topElParents=Symbol();const _siblingsToRestore=Symbol();const _parentMO=Symbol();/* Symbols for private static methods */const _topChanged=Symbol();const _swapInertedSibling=Symbol();const _inertSiblings=Symbol();const _restoreInertedSiblings=Symbol();const _getParents=Symbol();const _getDistributedChildren=Symbol();const _isInertable=Symbol();const _handleMutations=Symbol();class BlockingElementsImpl{constructor(){/**
             * The blocking elements.
             */this[_a]=[];/**
             * Used to keep track of the parents of the top element, from the element
             * itself up to body. When top changes, the old top might have been removed
             * from the document, so we need to memoize the inerted parents' siblings
             * in order to restore their inerteness when top changes.
             */this[_b]=[];/**
             * Elements that are already inert before the first blocking element is
             * pushed.
             */this[_c]=new Set();}destructor(){// Restore original inertness.
this[_restoreInertedSiblings](this[_topElParents]);// Note we don't want to make these properties nullable on the class,
// since then we'd need non-null casts in many places. Calling a method on
// a BlockingElements instance after calling destructor will result in an
// exception.
const nullable=this;nullable[_blockingElements]=null;nullable[_topElParents]=null;nullable[_alreadyInertElements]=null;}get top(){const elems=this[_blockingElements];return elems[elems.length-1]||null;}push(element){if(!element||element===this.top){return;}// Remove it from the stack, we'll bring it to the top.
this.remove(element);this[_topChanged](element);this[_blockingElements].push(element);}remove(element){const i=this[_blockingElements].indexOf(element);if(i===-1){return false;}this[_blockingElements].splice(i,1);// Top changed only if the removed element was the top element.
if(i===this[_blockingElements].length){this[_topChanged](this.top);}return true;}pop(){const top=this.top;top&&this.remove(top);return top;}has(element){return this[_blockingElements].indexOf(element)!==-1;}/**
         * Sets `inert` to all document elements except the new top element, its
         * parents, and its distributed content.
         */[(_a=_blockingElements,_b=_topElParents,_c=_alreadyInertElements,_topChanged)](newTop){const toKeepInert=this[_alreadyInertElements];const oldParents=this[_topElParents];// No new top, reset old top if any.
if(!newTop){this[_restoreInertedSiblings](oldParents);toKeepInert.clear();this[_topElParents]=[];return;}const newParents=this[_getParents](newTop);// New top is not contained in the main document!
if(newParents[newParents.length-1].parentNode!==document.body){throw Error('Non-connected element cannot be a blocking element');}// Cast here because we know we'll call _inertSiblings on newParents
// below.
this[_topElParents]=newParents;const toSkip=this[_getDistributedChildren](newTop);// No previous top element.
if(!oldParents.length){this[_inertSiblings](newParents,toSkip,toKeepInert);return;}let i=oldParents.length-1;let j=newParents.length-1;// Find common parent. Index 0 is the element itself (so stop before it).
while(i>0&&j>0&&oldParents[i]===newParents[j]){i--;j--;}// If up the parents tree there are 2 elements that are siblings, swap
// the inerted sibling.
if(oldParents[i]!==newParents[j]){this[_swapInertedSibling](oldParents[i],newParents[j]);}// Restore old parents siblings inertness.
i>0&&this[_restoreInertedSiblings](oldParents.slice(0,i));// Make new parents siblings inert.
j>0&&this[_inertSiblings](newParents.slice(0,j),toSkip,null);}/**
         * Swaps inertness between two sibling elements.
         * Sets the property `inert` over the attribute since the inert spec
         * doesn't specify if it should be reflected.
         * https://html.spec.whatwg.org/multipage/interaction.html#inert
         */[_swapInertedSibling](oldInert,newInert){const siblingsToRestore=oldInert[_siblingsToRestore];// oldInert is not contained in siblings to restore, so we have to check
// if it's inertable and if already inert.
if(this[_isInertable](oldInert)&&!oldInert.inert){oldInert.inert=true;siblingsToRestore.add(oldInert);}// If newInert was already between the siblings to restore, it means it is
// inertable and must be restored.
if(siblingsToRestore.has(newInert)){newInert.inert=false;siblingsToRestore.delete(newInert);}newInert[_parentMO]=oldInert[_parentMO];newInert[_siblingsToRestore]=siblingsToRestore;oldInert[_parentMO]=undefined;oldInert[_siblingsToRestore]=undefined;}/**
         * Restores original inertness to the siblings of the elements.
         * Sets the property `inert` over the attribute since the inert spec
         * doesn't specify if it should be reflected.
         * https://html.spec.whatwg.org/multipage/interaction.html#inert
         */[_restoreInertedSiblings](elements){for(const element of elements){const mo=element[_parentMO];mo.disconnect();element[_parentMO]=undefined;const siblings=element[_siblingsToRestore];for(const sibling of siblings){sibling.inert=false;}element[_siblingsToRestore]=undefined;}}/**
         * Inerts the siblings of the elements except the elements to skip. Stores
         * the inerted siblings into the element's symbol `_siblingsToRestore`.
         * Pass `toKeepInert` to collect the already inert elements.
         * Sets the property `inert` over the attribute since the inert spec
         * doesn't specify if it should be reflected.
         * https://html.spec.whatwg.org/multipage/interaction.html#inert
         */[_inertSiblings](elements,toSkip,toKeepInert){for(const element of elements){// Assume element is not a Document, so it must have a parentNode.
const parent=element.parentNode;const children=parent.children;const inertedSiblings=new Set();for(let j=0;j<children.length;j++){const sibling=children[j];// Skip the input element, if not inertable or to be skipped.
if(sibling===element||!this[_isInertable](sibling)||toSkip&&toSkip.has(sibling)){continue;}// Should be collected since already inerted.
if(toKeepInert&&sibling.inert){toKeepInert.add(sibling);}else {sibling.inert=true;inertedSiblings.add(sibling);}}// Store the siblings that were inerted.
element[_siblingsToRestore]=inertedSiblings;// Observe only immediate children mutations on the parent.
const mo=new MutationObserver(this[_handleMutations].bind(this));element[_parentMO]=mo;let parentToObserve=parent;// If we're using the ShadyDOM polyfill, then our parent could be a
// shady root, which is an object that acts like a ShadowRoot, but isn't
// actually a node in the real DOM. Observe the real DOM parent instead.
const maybeShadyRoot=parentToObserve;if(maybeShadyRoot.__shady&&maybeShadyRoot.host){parentToObserve=maybeShadyRoot.host;}mo.observe(parentToObserve,{childList:true});}}/**
         * Handles newly added/removed nodes by toggling their inertness.
         * It also checks if the current top Blocking Element has been removed,
         * notifying and removing it.
         */[_handleMutations](mutations){const parents=this[_topElParents];const toKeepInert=this[_alreadyInertElements];for(const mutation of mutations){// If the target is a shadowRoot, get its host as we skip shadowRoots when
// computing _topElParents.
const target=mutation.target.host||mutation.target;const idx=target===document.body?parents.length:parents.indexOf(target);const inertedChild=parents[idx-1];const inertedSiblings=inertedChild[_siblingsToRestore];// To restore.
for(let i=0;i<mutation.removedNodes.length;i++){const sibling=mutation.removedNodes[i];if(sibling===inertedChild){console.info('Detected removal of the top Blocking Element.');this.pop();return;}if(inertedSiblings.has(sibling)){sibling.inert=false;inertedSiblings.delete(sibling);}}// To inert.
for(let i=0;i<mutation.addedNodes.length;i++){const sibling=mutation.addedNodes[i];if(!this[_isInertable](sibling)){continue;}if(toKeepInert&&sibling.inert){toKeepInert.add(sibling);}else {sibling.inert=true;inertedSiblings.add(sibling);}}}}/**
         * Returns if the element is inertable.
         */[_isInertable](element){return false===/^(style|template|script)$/.test(element.localName);}/**
         * Returns the list of newParents of an element, starting from element
         * (included) up to `document.body` (excluded).
         */[_getParents](element){const parents=[];let current=element;// Stop to body.
while(current&&current!==document.body){// Skip shadow roots.
if(current.nodeType===Node.ELEMENT_NODE){parents.push(current);}// ShadowDom v1
if(current.assignedSlot){// Collect slots from deepest slot to top.
while(current=current.assignedSlot){parents.push(current);}// Continue the search on the top slot.
current=parents.pop();continue;}current=current.parentNode||current.host;}return parents;}/**
         * Returns the distributed children of the element's shadow root.
         * Returns null if the element doesn't have a shadow root.
         */[_getDistributedChildren](element){const shadowRoot=element.shadowRoot;if(!shadowRoot){return null;}const result=new Set();let i;let j;let nodes;const slots=shadowRoot.querySelectorAll('slot');if(slots.length&&slots[0].assignedNodes){for(i=0;i<slots.length;i++){nodes=slots[i].assignedNodes({flatten:true});for(j=0;j<nodes.length;j++){if(nodes[j].nodeType===Node.ELEMENT_NODE){result.add(nodes[j]);}}}// No need to search for <content>.
}return result;}}document.$blockingElements=new BlockingElementsImpl();})();

var _createClass=function(){function defineProperties(target,props){for(var i=0;i<props.length;i++){var descriptor=props[i];descriptor.enumerable=descriptor.enumerable||false;descriptor.configurable=true;if("value"in descriptor)descriptor.writable=true;Object.defineProperty(target,descriptor.key,descriptor);}}return function(Constructor,protoProps,staticProps){if(protoProps)defineProperties(Constructor.prototype,protoProps);if(staticProps)defineProperties(Constructor,staticProps);return Constructor;};}();function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function");}}/**
 * This work is licensed under the W3C Software and Document License
 * (http://www.w3.org/Consortium/Legal/2015/copyright-software-and-document).
 */(function(){// Return early if we're not running inside of the browser.
if(typeof window==='undefined'){return;}// Convenience function for converting NodeLists.
/** @type {typeof Array.prototype.slice} */var slice=Array.prototype.slice;/**
   * IE has a non-standard name for "matches".
   * @type {typeof Element.prototype.matches}
   */var matches=Element.prototype.matches||Element.prototype.msMatchesSelector;/** @type {string} */var _focusableElementsString=['a[href]','area[href]','input:not([disabled])','select:not([disabled])','textarea:not([disabled])','button:not([disabled])','details','summary','iframe','object','embed','[contenteditable]'].join(',');/**
   * `InertRoot` manages a single inert subtree, i.e. a DOM subtree whose root element has an `inert`
   * attribute.
   *
   * Its main functions are:
   *
   * - to create and maintain a set of managed `InertNode`s, including when mutations occur in the
   *   subtree. The `makeSubtreeUnfocusable()` method handles collecting `InertNode`s via registering
   *   each focusable node in the subtree with the singleton `InertManager` which manages all known
   *   focusable nodes within inert subtrees. `InertManager` ensures that a single `InertNode`
   *   instance exists for each focusable node which has at least one inert root as an ancestor.
   *
   * - to notify all managed `InertNode`s when this subtree stops being inert (i.e. when the `inert`
   *   attribute is removed from the root node). This is handled in the destructor, which calls the
   *   `deregister` method on `InertManager` for each managed inert node.
   */var InertRoot=function(){/**
     * @param {!HTMLElement} rootElement The HTMLElement at the root of the inert subtree.
     * @param {!InertManager} inertManager The global singleton InertManager object.
     */function InertRoot(rootElement,inertManager){_classCallCheck(this,InertRoot);/** @type {!InertManager} */this._inertManager=inertManager;/** @type {!HTMLElement} */this._rootElement=rootElement;/**
       * @type {!Set<!InertNode>}
       * All managed focusable nodes in this InertRoot's subtree.
       */this._managedNodes=new Set();// Make the subtree hidden from assistive technology
if(this._rootElement.hasAttribute('aria-hidden')){/** @type {?string} */this._savedAriaHidden=this._rootElement.getAttribute('aria-hidden');}else {this._savedAriaHidden=null;}this._rootElement.setAttribute('aria-hidden','true');// Make all focusable elements in the subtree unfocusable and add them to _managedNodes
this._makeSubtreeUnfocusable(this._rootElement);// Watch for:
// - any additions in the subtree: make them unfocusable too
// - any removals from the subtree: remove them from this inert root's managed nodes
// - attribute changes: if `tabindex` is added, or removed from an intrinsically focusable
//   element, make that node a managed node.
this._observer=new MutationObserver(this._onMutation.bind(this));this._observer.observe(this._rootElement,{attributes:true,childList:true,subtree:true});}/**
     * Call this whenever this object is about to become obsolete.  This unwinds all of the state
     * stored in this object and updates the state of all of the managed nodes.
     */_createClass(InertRoot,[{key:'destructor',value:function destructor(){this._observer.disconnect();if(this._rootElement){if(this._savedAriaHidden!==null){this._rootElement.setAttribute('aria-hidden',this._savedAriaHidden);}else {this._rootElement.removeAttribute('aria-hidden');}}this._managedNodes.forEach(function(inertNode){this._unmanageNode(inertNode.node);},this);// Note we cast the nulls to the ANY type here because:
// 1) We want the class properties to be declared as non-null, or else we
//    need even more casts throughout this code. All bets are off if an
//    instance has been destroyed and a method is called.
// 2) We don't want to cast "this", because we want type-aware optimizations
//    to know which properties we're setting.
this._observer=/** @type {?} */null;this._rootElement=/** @type {?} */null;this._managedNodes=/** @type {?} */null;this._inertManager=/** @type {?} */null;}/**
       * @return {!Set<!InertNode>} A copy of this InertRoot's managed nodes set.
       */},{key:'_makeSubtreeUnfocusable',/**
       * @param {!Node} startNode
       */value:function _makeSubtreeUnfocusable(startNode){var _this2=this;composedTreeWalk(startNode,function(node){return _this2._visitNode(node);});var activeElement=document.activeElement;if(!document.body.contains(startNode)){// startNode may be in shadow DOM, so find its nearest shadowRoot to get the activeElement.
var node=startNode;/** @type {!ShadowRoot|undefined} */var root=undefined;while(node){if(node.nodeType===Node.DOCUMENT_FRAGMENT_NODE){root=/** @type {!ShadowRoot} */node;break;}node=node.parentNode;}if(root){activeElement=root.activeElement;}}if(startNode.contains(activeElement)){activeElement.blur();// In IE11, if an element is already focused, and then set to tabindex=-1
// calling blur() will not actually move the focus.
// To work around this we call focus() on the body instead.
if(activeElement===document.activeElement){document.body.focus();}}}/**
       * @param {!Node} node
       */},{key:'_visitNode',value:function _visitNode(node){if(node.nodeType!==Node.ELEMENT_NODE){return;}var element=/** @type {!HTMLElement} */node;// If a descendant inert root becomes un-inert, its descendants will still be inert because of
// this inert root, so all of its managed nodes need to be adopted by this InertRoot.
if(element!==this._rootElement&&element.hasAttribute('inert')){this._adoptInertRoot(element);}if(matches.call(element,_focusableElementsString)||element.hasAttribute('tabindex')){this._manageNode(element);}}/**
       * Register the given node with this InertRoot and with InertManager.
       * @param {!Node} node
       */},{key:'_manageNode',value:function _manageNode(node){var inertNode=this._inertManager.register(node,this);this._managedNodes.add(inertNode);}/**
       * Unregister the given node with this InertRoot and with InertManager.
       * @param {!Node} node
       */},{key:'_unmanageNode',value:function _unmanageNode(node){var inertNode=this._inertManager.deregister(node,this);if(inertNode){this._managedNodes['delete'](inertNode);}}/**
       * Unregister the entire subtree starting at `startNode`.
       * @param {!Node} startNode
       */},{key:'_unmanageSubtree',value:function _unmanageSubtree(startNode){var _this3=this;composedTreeWalk(startNode,function(node){return _this3._unmanageNode(node);});}/**
       * If a descendant node is found with an `inert` attribute, adopt its managed nodes.
       * @param {!HTMLElement} node
       */},{key:'_adoptInertRoot',value:function _adoptInertRoot(node){var inertSubroot=this._inertManager.getInertRoot(node);// During initialisation this inert root may not have been registered yet,
// so register it now if need be.
if(!inertSubroot){this._inertManager.setInert(node,true);inertSubroot=this._inertManager.getInertRoot(node);}inertSubroot.managedNodes.forEach(function(savedInertNode){this._manageNode(savedInertNode.node);},this);}/**
       * Callback used when mutation observer detects subtree additions, removals, or attribute changes.
       * @param {!Array<!MutationRecord>} records
       * @param {!MutationObserver} self
       */},{key:'_onMutation',value:function _onMutation(records,self){records.forEach(function(record){var target=/** @type {!HTMLElement} */record.target;if(record.type==='childList'){// Manage added nodes
slice.call(record.addedNodes).forEach(function(node){this._makeSubtreeUnfocusable(node);},this);// Un-manage removed nodes
slice.call(record.removedNodes).forEach(function(node){this._unmanageSubtree(node);},this);}else if(record.type==='attributes'){if(record.attributeName==='tabindex'){// Re-initialise inert node if tabindex changes
this._manageNode(target);}else if(target!==this._rootElement&&record.attributeName==='inert'&&target.hasAttribute('inert')){// If a new inert root is added, adopt its managed nodes and make sure it knows about the
// already managed nodes from this inert subroot.
this._adoptInertRoot(target);var inertSubroot=this._inertManager.getInertRoot(target);this._managedNodes.forEach(function(managedNode){if(target.contains(managedNode.node)){inertSubroot._manageNode(managedNode.node);}});}}},this);}},{key:'managedNodes',get:function get(){return new Set(this._managedNodes);}/** @return {boolean} */},{key:'hasSavedAriaHidden',get:function get(){return this._savedAriaHidden!==null;}/** @param {?string} ariaHidden */},{key:'savedAriaHidden',set:function set(ariaHidden){this._savedAriaHidden=ariaHidden;}/** @return {?string} */,get:function get(){return this._savedAriaHidden;}}]);return InertRoot;}();/**
   * `InertNode` initialises and manages a single inert node.
   * A node is inert if it is a descendant of one or more inert root elements.
   *
   * On construction, `InertNode` saves the existing `tabindex` value for the node, if any, and
   * either removes the `tabindex` attribute or sets it to `-1`, depending on whether the element
   * is intrinsically focusable or not.
   *
   * `InertNode` maintains a set of `InertRoot`s which are descendants of this `InertNode`. When an
   * `InertRoot` is destroyed, and calls `InertManager.deregister()`, the `InertManager` notifies the
   * `InertNode` via `removeInertRoot()`, which in turn destroys the `InertNode` if no `InertRoot`s
   * remain in the set. On destruction, `InertNode` reinstates the stored `tabindex` if one exists,
   * or removes the `tabindex` attribute if the element is intrinsically focusable.
   */var InertNode=function(){/**
     * @param {!Node} node A focusable element to be made inert.
     * @param {!InertRoot} inertRoot The inert root element associated with this inert node.
     */function InertNode(node,inertRoot){_classCallCheck(this,InertNode);/** @type {!Node} */this._node=node;/** @type {boolean} */this._overrodeFocusMethod=false;/**
       * @type {!Set<!InertRoot>} The set of descendant inert roots.
       *    If and only if this set becomes empty, this node is no longer inert.
       */this._inertRoots=new Set([inertRoot]);/** @type {?number} */this._savedTabIndex=null;/** @type {boolean} */this._destroyed=false;// Save any prior tabindex info and make this node untabbable
this.ensureUntabbable();}/**
     * Call this whenever this object is about to become obsolete.
     * This makes the managed node focusable again and deletes all of the previously stored state.
     */_createClass(InertNode,[{key:'destructor',value:function destructor(){this._throwIfDestroyed();if(this._node&&this._node.nodeType===Node.ELEMENT_NODE){var element=/** @type {!HTMLElement} */this._node;if(this._savedTabIndex!==null){element.setAttribute('tabindex',this._savedTabIndex);}else {element.removeAttribute('tabindex');}// Use `delete` to restore native focus method.
if(this._overrodeFocusMethod){delete element.focus;}}// See note in InertRoot.destructor for why we cast these nulls to ANY.
this._node=/** @type {?} */null;this._inertRoots=/** @type {?} */null;this._destroyed=true;}/**
       * @type {boolean} Whether this object is obsolete because the managed node is no longer inert.
       * If the object has been destroyed, any attempt to access it will cause an exception.
       */},{key:'_throwIfDestroyed',/**
       * Throw if user tries to access destroyed InertNode.
       */value:function _throwIfDestroyed(){if(this.destroyed){throw new Error('Trying to access destroyed InertNode');}}/** @return {boolean} */},{key:'ensureUntabbable',/** Save the existing tabindex value and make the node untabbable and unfocusable */value:function ensureUntabbable(){if(this.node.nodeType!==Node.ELEMENT_NODE){return;}var element=/** @type {!HTMLElement} */this.node;if(matches.call(element,_focusableElementsString)){if(/** @type {!HTMLElement} */element.tabIndex===-1&&this.hasSavedTabIndex){return;}if(element.hasAttribute('tabindex')){this._savedTabIndex=/** @type {!HTMLElement} */element.tabIndex;}element.setAttribute('tabindex','-1');if(element.nodeType===Node.ELEMENT_NODE){element.focus=function(){};this._overrodeFocusMethod=true;}}else if(element.hasAttribute('tabindex')){this._savedTabIndex=/** @type {!HTMLElement} */element.tabIndex;element.removeAttribute('tabindex');}}/**
       * Add another inert root to this inert node's set of managing inert roots.
       * @param {!InertRoot} inertRoot
       */},{key:'addInertRoot',value:function addInertRoot(inertRoot){this._throwIfDestroyed();this._inertRoots.add(inertRoot);}/**
       * Remove the given inert root from this inert node's set of managing inert roots.
       * If the set of managing inert roots becomes empty, this node is no longer inert,
       * so the object should be destroyed.
       * @param {!InertRoot} inertRoot
       */},{key:'removeInertRoot',value:function removeInertRoot(inertRoot){this._throwIfDestroyed();this._inertRoots['delete'](inertRoot);if(this._inertRoots.size===0){this.destructor();}}},{key:'destroyed',get:function get(){return(/** @type {!InertNode} */this._destroyed);}},{key:'hasSavedTabIndex',get:function get(){return this._savedTabIndex!==null;}/** @return {!Node} */},{key:'node',get:function get(){this._throwIfDestroyed();return this._node;}/** @param {?number} tabIndex */},{key:'savedTabIndex',set:function set(tabIndex){this._throwIfDestroyed();this._savedTabIndex=tabIndex;}/** @return {?number} */,get:function get(){this._throwIfDestroyed();return this._savedTabIndex;}}]);return InertNode;}();/**
   * InertManager is a per-document singleton object which manages all inert roots and nodes.
   *
   * When an element becomes an inert root by having an `inert` attribute set and/or its `inert`
   * property set to `true`, the `setInert` method creates an `InertRoot` object for the element.
   * The `InertRoot` in turn registers itself as managing all of the element's focusable descendant
   * nodes via the `register()` method. The `InertManager` ensures that a single `InertNode` instance
   * is created for each such node, via the `_managedNodes` map.
   */var InertManager=function(){/**
     * @param {!Document} document
     */function InertManager(document){_classCallCheck(this,InertManager);if(!document){throw new Error('Missing required argument; InertManager needs to wrap a document.');}/** @type {!Document} */this._document=document;/**
       * All managed nodes known to this InertManager. In a map to allow looking up by Node.
       * @type {!Map<!Node, !InertNode>}
       */this._managedNodes=new Map();/**
       * All inert roots known to this InertManager. In a map to allow looking up by Node.
       * @type {!Map<!Node, !InertRoot>}
       */this._inertRoots=new Map();/**
       * Observer for mutations on `document.body`.
       * @type {!MutationObserver}
       */this._observer=new MutationObserver(this._watchForInert.bind(this));// Add inert style.
addInertStyle(document.head||document.body||document.documentElement);// Wait for document to be loaded.
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',this._onDocumentLoaded.bind(this));}else {this._onDocumentLoaded();}}/**
     * Set whether the given element should be an inert root or not.
     * @param {!HTMLElement} root
     * @param {boolean} inert
     */_createClass(InertManager,[{key:'setInert',value:function setInert(root,inert){if(inert){if(this._inertRoots.has(root)){// element is already inert
return;}var inertRoot=new InertRoot(root,this);root.setAttribute('inert','');this._inertRoots.set(root,inertRoot);// If not contained in the document, it must be in a shadowRoot.
// Ensure inert styles are added there.
if(!this._document.body.contains(root)){var parent=root.parentNode;while(parent){if(parent.nodeType===11){addInertStyle(parent);}parent=parent.parentNode;}}}else {if(!this._inertRoots.has(root)){// element is already non-inert
return;}var _inertRoot=this._inertRoots.get(root);_inertRoot.destructor();this._inertRoots['delete'](root);root.removeAttribute('inert');}}/**
       * Get the InertRoot object corresponding to the given inert root element, if any.
       * @param {!Node} element
       * @return {!InertRoot|undefined}
       */},{key:'getInertRoot',value:function getInertRoot(element){return this._inertRoots.get(element);}/**
       * Register the given InertRoot as managing the given node.
       * In the case where the node has a previously existing inert root, this inert root will
       * be added to its set of inert roots.
       * @param {!Node} node
       * @param {!InertRoot} inertRoot
       * @return {!InertNode} inertNode
       */},{key:'register',value:function register(node,inertRoot){var inertNode=this._managedNodes.get(node);if(inertNode!==undefined){// node was already in an inert subtree
inertNode.addInertRoot(inertRoot);}else {inertNode=new InertNode(node,inertRoot);}this._managedNodes.set(node,inertNode);return inertNode;}/**
       * De-register the given InertRoot as managing the given inert node.
       * Removes the inert root from the InertNode's set of managing inert roots, and remove the inert
       * node from the InertManager's set of managed nodes if it is destroyed.
       * If the node is not currently managed, this is essentially a no-op.
       * @param {!Node} node
       * @param {!InertRoot} inertRoot
       * @return {?InertNode} The potentially destroyed InertNode associated with this node, if any.
       */},{key:'deregister',value:function deregister(node,inertRoot){var inertNode=this._managedNodes.get(node);if(!inertNode){return null;}inertNode.removeInertRoot(inertRoot);if(inertNode.destroyed){this._managedNodes['delete'](node);}return inertNode;}/**
       * Callback used when document has finished loading.
       */},{key:'_onDocumentLoaded',value:function _onDocumentLoaded(){// Find all inert roots in document and make them actually inert.
var inertElements=slice.call(this._document.querySelectorAll('[inert]'));inertElements.forEach(function(inertElement){this.setInert(inertElement,true);},this);// Comment this out to use programmatic API only.
this._observer.observe(this._document.body||this._document.documentElement,{attributes:true,subtree:true,childList:true});}/**
       * Callback used when mutation observer detects attribute changes.
       * @param {!Array<!MutationRecord>} records
       * @param {!MutationObserver} self
       */},{key:'_watchForInert',value:function _watchForInert(records,self){var _this=this;records.forEach(function(record){switch(record.type){case'childList':slice.call(record.addedNodes).forEach(function(node){if(node.nodeType!==Node.ELEMENT_NODE){return;}var inertElements=slice.call(node.querySelectorAll('[inert]'));if(matches.call(node,'[inert]')){inertElements.unshift(node);}inertElements.forEach(function(inertElement){this.setInert(inertElement,true);},_this);},_this);break;case'attributes':if(record.attributeName!=='inert'){return;}var target=/** @type {!HTMLElement} */record.target;var inert=target.hasAttribute('inert');_this.setInert(target,inert);break;}},this);}}]);return InertManager;}();/**
   * Recursively walk the composed tree from |node|.
   * @param {!Node} node
   * @param {(function (!HTMLElement))=} callback Callback to be called for each element traversed,
   *     before descending into child nodes.
   * @param {?ShadowRoot=} shadowRootAncestor The nearest ShadowRoot ancestor, if any.
   */function composedTreeWalk(node,callback,shadowRootAncestor){if(node.nodeType==Node.ELEMENT_NODE){var element=/** @type {!HTMLElement} */node;if(callback){callback(element);}// Descend into node:
// If it has a ShadowRoot, ignore all child elements - these will be picked
// up by the <content> or <shadow> elements. Descend straight into the
// ShadowRoot.
var shadowRoot=/** @type {!HTMLElement} */element.shadowRoot;if(shadowRoot){composedTreeWalk(shadowRoot,callback);return;}// If it is a <content> element, descend into distributed elements - these
// are elements from outside the shadow root which are rendered inside the
// shadow DOM.
if(element.localName=='content'){var content=/** @type {!HTMLContentElement} */element;// Verifies if ShadowDom v0 is supported.
var distributedNodes=content.getDistributedNodes?content.getDistributedNodes():[];for(var i=0;i<distributedNodes.length;i++){composedTreeWalk(distributedNodes[i],callback);}return;}// If it is a <slot> element, descend into assigned nodes - these
// are elements from outside the shadow root which are rendered inside the
// shadow DOM.
if(element.localName=='slot'){var slot=/** @type {!HTMLSlotElement} */element;// Verify if ShadowDom v1 is supported.
var _distributedNodes=slot.assignedNodes?slot.assignedNodes({flatten:true}):[];for(var _i=0;_i<_distributedNodes.length;_i++){composedTreeWalk(_distributedNodes[_i],callback);}return;}}// If it is neither the parent of a ShadowRoot, a <content> element, a <slot>
// element, nor a <shadow> element recurse normally.
var child=node.firstChild;while(child!=null){composedTreeWalk(child,callback);child=child.nextSibling;}}/**
   * Adds a style element to the node containing the inert specific styles
   * @param {!Node} node
   */function addInertStyle(node){if(node.querySelector('style#inert-style, link#inert-style')){return;}var style=document.createElement('style');style.setAttribute('id','inert-style');style.textContent='\n'+'[inert] {\n'+'  pointer-events: none;\n'+'  cursor: default;\n'+'}\n'+'\n'+'[inert], [inert] * {\n'+'  -webkit-user-select: none;\n'+'  -moz-user-select: none;\n'+'  -ms-user-select: none;\n'+'  user-select: none;\n'+'}\n';node.appendChild(style);}if(!HTMLElement.prototype.hasOwnProperty('inert')){/** @type {!InertManager} */var inertManager=new InertManager(document);Object.defineProperty(HTMLElement.prototype,'inert',{enumerable:true,/** @this {!HTMLElement} */get:function get(){return this.hasAttribute('inert');},/** @this {!HTMLElement} */set:function set(inert){inertManager.setInert(this,inert);}});}})();

/**
 * @license
 * Copyright 2016 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */var cssClasses={CLOSING:'mdc-dialog--closing',OPEN:'mdc-dialog--open',OPENING:'mdc-dialog--opening',SCROLLABLE:'mdc-dialog--scrollable',SCROLL_LOCK:'mdc-dialog-scroll-lock',STACKED:'mdc-dialog--stacked',FULLSCREEN:'mdc-dialog--fullscreen',// Class for showing a scroll divider on full-screen dialog header element.
// Should only be displayed on scrollable content, when the dialog content is
// scrolled "underneath" the header.
SCROLL_DIVIDER_HEADER:'mdc-dialog-scroll-divider-header',// Class for showing a scroll divider on a full-screen dialog footer element.
// Should only be displayed on scrolalble content, when the dialog content is
// obscured "underneath" the footer.
SCROLL_DIVIDER_FOOTER:'mdc-dialog-scroll-divider-footer',// The "surface scrim" is a scrim covering only the surface of a dialog. This
// is used in situations where a confirmation dialog is shown over an already
// opened full-screen dialog. On larger screen-sizes, the full-screen dialog
// is sized as a modal and so in these situations we display a "surface scrim"
// to prevent a "double scrim" (where the scrim from the secondary
// confirmation dialog would overlap with the scrim from the full-screen
// dialog).
SURFACE_SCRIM_SHOWN:'mdc-dialog__surface-scrim--shown',// "Showing" animating class for the surface-scrim.
SURFACE_SCRIM_SHOWING:'mdc-dialog__surface-scrim--showing',// "Hiding" animating class for the surface-scrim.
SURFACE_SCRIM_HIDING:'mdc-dialog__surface-scrim--hiding',// Class to hide a dialog's scrim (used in conjunction with a surface-scrim).
// Note that we only hide the original scrim rather than removing it entirely
// to prevent interactions with the content behind this scrim, and to capture
// scrim clicks.
SCRIM_HIDDEN:'mdc-dialog__scrim--hidden'};var strings={ACTION_ATTRIBUTE:'data-mdc-dialog-action',BUTTON_DEFAULT_ATTRIBUTE:'data-mdc-dialog-button-default',BUTTON_SELECTOR:'.mdc-dialog__button',CLOSED_EVENT:'MDCDialog:closed',CLOSE_ACTION:'close',CLOSING_EVENT:'MDCDialog:closing',CONTAINER_SELECTOR:'.mdc-dialog__container',CONTENT_SELECTOR:'.mdc-dialog__content',DESTROY_ACTION:'destroy',INITIAL_FOCUS_ATTRIBUTE:'data-mdc-dialog-initial-focus',OPENED_EVENT:'MDCDialog:opened',OPENING_EVENT:'MDCDialog:opening',SCRIM_SELECTOR:'.mdc-dialog__scrim',SUPPRESS_DEFAULT_PRESS_SELECTOR:['textarea','.mdc-menu .mdc-list-item','.mdc-menu .mdc-deprecated-list-item'].join(', '),SURFACE_SELECTOR:'.mdc-dialog__surface'};var numbers={DIALOG_ANIMATION_CLOSE_TIME_MS:75,DIALOG_ANIMATION_OPEN_TIME_MS:150};

/**
 * @license
 * Copyright 2020 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */ /**
 * AnimationFrame provides a user-friendly abstraction around requesting
 * and canceling animation frames.
 */var AnimationFrame=/** @class */function(){function AnimationFrame(){this.rafIDs=new Map();}/**
     * Requests an animation frame. Cancels any existing frame with the same key.
     * @param {string} key The key for this callback.
     * @param {FrameRequestCallback} callback The callback to be executed.
     */AnimationFrame.prototype.request=function(key,callback){var _this=this;this.cancel(key);var frameID=requestAnimationFrame(function(frame){_this.rafIDs.delete(key);// Callback must come *after* the key is deleted so that nested calls to
// request with the same key are not deleted.
callback(frame);});this.rafIDs.set(key,frameID);};/**
     * Cancels a queued callback with the given key.
     * @param {string} key The key for this callback.
     */AnimationFrame.prototype.cancel=function(key){var rafID=this.rafIDs.get(key);if(rafID){cancelAnimationFrame(rafID);this.rafIDs.delete(key);}};/**
     * Cancels all queued callback.
     */AnimationFrame.prototype.cancelAll=function(){var _this=this;// Need to use forEach because it's the only iteration method supported
// by IE11. Suppress the underscore because we don't need it.
// tslint:disable-next-line:enforce-name-casing
this.rafIDs.forEach(function(_,key){_this.cancel(key);});};/**
     * Returns the queue of unexecuted callback keys.
     */AnimationFrame.prototype.getQueue=function(){var queue=[];// Need to use forEach because it's the only iteration method supported
// by IE11. Suppress the underscore because we don't need it.
// tslint:disable-next-line:enforce-name-casing
this.rafIDs.forEach(function(_,key){queue.push(key);});return queue;};return AnimationFrame;}();

var AnimationKeys;(function(AnimationKeys){AnimationKeys["POLL_SCROLL_POS"]="poll_scroll_position";AnimationKeys["POLL_LAYOUT_CHANGE"]="poll_layout_change";})(AnimationKeys||(AnimationKeys={}));var MDCDialogFoundation=/** @class */function(_super){__extends(MDCDialogFoundation,_super);function MDCDialogFoundation(adapter){var _this=_super.call(this,__assign(__assign({},MDCDialogFoundation.defaultAdapter),adapter))||this;_this.dialogOpen=false;_this.isFullscreen=false;_this.animationFrame=0;_this.animationTimer=0;_this.escapeKeyAction=strings.CLOSE_ACTION;_this.scrimClickAction=strings.CLOSE_ACTION;_this.autoStackButtons=true;_this.areButtonsStacked=false;_this.suppressDefaultPressSelector=strings.SUPPRESS_DEFAULT_PRESS_SELECTOR;_this.animFrame=new AnimationFrame();_this.contentScrollHandler=function(){_this.handleScrollEvent();};_this.windowResizeHandler=function(){_this.layout();};_this.windowOrientationChangeHandler=function(){_this.layout();};return _this;}Object.defineProperty(MDCDialogFoundation,"cssClasses",{get:function(){return cssClasses;},enumerable:false,configurable:true});Object.defineProperty(MDCDialogFoundation,"strings",{get:function(){return strings;},enumerable:false,configurable:true});Object.defineProperty(MDCDialogFoundation,"numbers",{get:function(){return numbers;},enumerable:false,configurable:true});Object.defineProperty(MDCDialogFoundation,"defaultAdapter",{get:function(){return {addBodyClass:function(){return undefined;},addClass:function(){return undefined;},areButtonsStacked:function(){return false;},clickDefaultButton:function(){return undefined;},eventTargetMatches:function(){return false;},getActionFromEvent:function(){return '';},getInitialFocusEl:function(){return null;},hasClass:function(){return false;},isContentScrollable:function(){return false;},notifyClosed:function(){return undefined;},notifyClosing:function(){return undefined;},notifyOpened:function(){return undefined;},notifyOpening:function(){return undefined;},releaseFocus:function(){return undefined;},removeBodyClass:function(){return undefined;},removeClass:function(){return undefined;},reverseButtons:function(){return undefined;},trapFocus:function(){return undefined;},registerContentEventHandler:function(){return undefined;},deregisterContentEventHandler:function(){return undefined;},isScrollableContentAtTop:function(){return false;},isScrollableContentAtBottom:function(){return false;},registerWindowEventHandler:function(){return undefined;},deregisterWindowEventHandler:function(){return undefined;}};},enumerable:false,configurable:true});MDCDialogFoundation.prototype.init=function(){if(this.adapter.hasClass(cssClasses.STACKED)){this.setAutoStackButtons(false);}this.isFullscreen=this.adapter.hasClass(cssClasses.FULLSCREEN);};MDCDialogFoundation.prototype.destroy=function(){if(this.animationTimer){clearTimeout(this.animationTimer);this.handleAnimationTimerEnd();}if(this.isFullscreen){this.adapter.deregisterContentEventHandler('scroll',this.contentScrollHandler);}this.animFrame.cancelAll();this.adapter.deregisterWindowEventHandler('resize',this.windowResizeHandler);this.adapter.deregisterWindowEventHandler('orientationchange',this.windowOrientationChangeHandler);};MDCDialogFoundation.prototype.open=function(dialogOptions){var _this=this;this.dialogOpen=true;this.adapter.notifyOpening();this.adapter.addClass(cssClasses.OPENING);if(this.isFullscreen){// A scroll event listener is registered even if the dialog is not
// scrollable on open, since the window resize event, or orientation
// change may make the dialog scrollable after it is opened.
this.adapter.registerContentEventHandler('scroll',this.contentScrollHandler);}if(dialogOptions&&dialogOptions.isAboveFullscreenDialog){this.adapter.addClass(cssClasses.SCRIM_HIDDEN);}this.adapter.registerWindowEventHandler('resize',this.windowResizeHandler);this.adapter.registerWindowEventHandler('orientationchange',this.windowOrientationChangeHandler);// Wait a frame once display is no longer "none", to establish basis for
// animation
this.runNextAnimationFrame(function(){_this.adapter.addClass(cssClasses.OPEN);_this.adapter.addBodyClass(cssClasses.SCROLL_LOCK);_this.layout();_this.animationTimer=setTimeout(function(){_this.handleAnimationTimerEnd();_this.adapter.trapFocus(_this.adapter.getInitialFocusEl());_this.adapter.notifyOpened();},numbers.DIALOG_ANIMATION_OPEN_TIME_MS);});};MDCDialogFoundation.prototype.close=function(action){var _this=this;if(action===void 0){action='';}if(!this.dialogOpen){// Avoid redundant close calls (and events), e.g. from keydown on elements
// that inherently emit click
return;}this.dialogOpen=false;this.adapter.notifyClosing(action);this.adapter.addClass(cssClasses.CLOSING);this.adapter.removeClass(cssClasses.OPEN);this.adapter.removeBodyClass(cssClasses.SCROLL_LOCK);if(this.isFullscreen){this.adapter.deregisterContentEventHandler('scroll',this.contentScrollHandler);}this.adapter.deregisterWindowEventHandler('resize',this.windowResizeHandler);this.adapter.deregisterWindowEventHandler('orientationchange',this.windowOrientationChangeHandler);cancelAnimationFrame(this.animationFrame);this.animationFrame=0;clearTimeout(this.animationTimer);this.animationTimer=setTimeout(function(){_this.adapter.releaseFocus();_this.handleAnimationTimerEnd();_this.adapter.notifyClosed(action);},numbers.DIALOG_ANIMATION_CLOSE_TIME_MS);};/**
     * Used only in instances of showing a secondary dialog over a full-screen
     * dialog. Shows the "surface scrim" displayed over the full-screen dialog.
     */MDCDialogFoundation.prototype.showSurfaceScrim=function(){var _this=this;this.adapter.addClass(cssClasses.SURFACE_SCRIM_SHOWING);this.runNextAnimationFrame(function(){_this.adapter.addClass(cssClasses.SURFACE_SCRIM_SHOWN);});};/**
     * Used only in instances of showing a secondary dialog over a full-screen
     * dialog. Hides the "surface scrim" displayed over the full-screen dialog.
     */MDCDialogFoundation.prototype.hideSurfaceScrim=function(){this.adapter.removeClass(cssClasses.SURFACE_SCRIM_SHOWN);this.adapter.addClass(cssClasses.SURFACE_SCRIM_HIDING);};/**
     * Handles `transitionend` event triggered when surface scrim animation is
     * finished.
     */MDCDialogFoundation.prototype.handleSurfaceScrimTransitionEnd=function(){this.adapter.removeClass(cssClasses.SURFACE_SCRIM_HIDING);this.adapter.removeClass(cssClasses.SURFACE_SCRIM_SHOWING);};MDCDialogFoundation.prototype.isOpen=function(){return this.dialogOpen;};MDCDialogFoundation.prototype.getEscapeKeyAction=function(){return this.escapeKeyAction;};MDCDialogFoundation.prototype.setEscapeKeyAction=function(action){this.escapeKeyAction=action;};MDCDialogFoundation.prototype.getScrimClickAction=function(){return this.scrimClickAction;};MDCDialogFoundation.prototype.setScrimClickAction=function(action){this.scrimClickAction=action;};MDCDialogFoundation.prototype.getAutoStackButtons=function(){return this.autoStackButtons;};MDCDialogFoundation.prototype.setAutoStackButtons=function(autoStack){this.autoStackButtons=autoStack;};MDCDialogFoundation.prototype.getSuppressDefaultPressSelector=function(){return this.suppressDefaultPressSelector;};MDCDialogFoundation.prototype.setSuppressDefaultPressSelector=function(selector){this.suppressDefaultPressSelector=selector;};MDCDialogFoundation.prototype.layout=function(){var _this=this;this.animFrame.request(AnimationKeys.POLL_LAYOUT_CHANGE,function(){_this.layoutInternal();});};/** Handles click on the dialog root element. */MDCDialogFoundation.prototype.handleClick=function(evt){var isScrim=this.adapter.eventTargetMatches(evt.target,strings.SCRIM_SELECTOR);// Check for scrim click first since it doesn't require querying ancestors.
if(isScrim&&this.scrimClickAction!==''){this.close(this.scrimClickAction);}else {var action=this.adapter.getActionFromEvent(evt);if(action){this.close(action);}}};/** Handles keydown on the dialog root element. */MDCDialogFoundation.prototype.handleKeydown=function(evt){var isEnter=evt.key==='Enter'||evt.keyCode===13;if(!isEnter){return;}var action=this.adapter.getActionFromEvent(evt);if(action){// Action button callback is handled in `handleClick`,
// since space/enter keydowns on buttons trigger click events.
return;}// `composedPath` is used here, when available, to account for use cases
// where a target meant to suppress the default press behaviour
// may exist in a shadow root.
// For example, a textarea inside a web component:
// <mwc-dialog>
//   <horizontal-layout>
//     #shadow-root (open)
//       <mwc-textarea>
//         #shadow-root (open)
//           <textarea></textarea>
//       </mwc-textarea>
//   </horizontal-layout>
// </mwc-dialog>
var target=evt.composedPath?evt.composedPath()[0]:evt.target;var isDefault=this.suppressDefaultPressSelector?!this.adapter.eventTargetMatches(target,this.suppressDefaultPressSelector):true;if(isEnter&&isDefault){this.adapter.clickDefaultButton();}};/** Handles keydown on the document. */MDCDialogFoundation.prototype.handleDocumentKeydown=function(evt){var isEscape=evt.key==='Escape'||evt.keyCode===27;if(isEscape&&this.escapeKeyAction!==''){this.close(this.escapeKeyAction);}};/**
     * Handles scroll event on the dialog's content element -- showing a scroll
     * divider on the header or footer based on the scroll position. This handler
     * should only be registered on full-screen dialogs with scrollable content.
     */MDCDialogFoundation.prototype.handleScrollEvent=function(){var _this=this;// Since scroll events can fire at a high rate, we throttle these events by
// using requestAnimationFrame.
this.animFrame.request(AnimationKeys.POLL_SCROLL_POS,function(){_this.toggleScrollDividerHeader();_this.toggleScrollDividerFooter();});};MDCDialogFoundation.prototype.layoutInternal=function(){if(this.autoStackButtons){this.detectStackedButtons();}this.toggleScrollableClasses();};MDCDialogFoundation.prototype.handleAnimationTimerEnd=function(){this.animationTimer=0;this.adapter.removeClass(cssClasses.OPENING);this.adapter.removeClass(cssClasses.CLOSING);};/**
     * Runs the given logic on the next animation frame, using setTimeout to
     * factor in Firefox reflow behavior.
     */MDCDialogFoundation.prototype.runNextAnimationFrame=function(callback){var _this=this;cancelAnimationFrame(this.animationFrame);this.animationFrame=requestAnimationFrame(function(){_this.animationFrame=0;clearTimeout(_this.animationTimer);_this.animationTimer=setTimeout(callback,0);});};MDCDialogFoundation.prototype.detectStackedButtons=function(){// Remove the class first to let us measure the buttons' natural positions.
this.adapter.removeClass(cssClasses.STACKED);var areButtonsStacked=this.adapter.areButtonsStacked();if(areButtonsStacked){this.adapter.addClass(cssClasses.STACKED);}if(areButtonsStacked!==this.areButtonsStacked){this.adapter.reverseButtons();this.areButtonsStacked=areButtonsStacked;}};MDCDialogFoundation.prototype.toggleScrollableClasses=function(){// Remove the class first to let us measure the natural height of the
// content.
this.adapter.removeClass(cssClasses.SCROLLABLE);if(this.adapter.isContentScrollable()){this.adapter.addClass(cssClasses.SCROLLABLE);if(this.isFullscreen){// If dialog is full-screen and scrollable, check if a scroll divider
// should be shown.
this.toggleScrollDividerHeader();this.toggleScrollDividerFooter();}}};MDCDialogFoundation.prototype.toggleScrollDividerHeader=function(){if(!this.adapter.isScrollableContentAtTop()){this.adapter.addClass(cssClasses.SCROLL_DIVIDER_HEADER);}else if(this.adapter.hasClass(cssClasses.SCROLL_DIVIDER_HEADER)){this.adapter.removeClass(cssClasses.SCROLL_DIVIDER_HEADER);}};MDCDialogFoundation.prototype.toggleScrollDividerFooter=function(){if(!this.adapter.isScrollableContentAtBottom()){this.adapter.addClass(cssClasses.SCROLL_DIVIDER_FOOTER);}else if(this.adapter.hasClass(cssClasses.SCROLL_DIVIDER_FOOTER)){this.adapter.removeClass(cssClasses.SCROLL_DIVIDER_FOOTER);}};return MDCDialogFoundation;}(MDCFoundation);var MDCDialogFoundation$1 = MDCDialogFoundation;

/**
 * @license
 * Copyright 2019 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */ /**
 * Determine whether the current browser supports passive event listeners, and
 * if so, use them.
 */function applyPassive(globalObj){if(globalObj===void 0){globalObj=window;}return supportsPassiveOption(globalObj)?{passive:true}:false;}function supportsPassiveOption(globalObj){if(globalObj===void 0){globalObj=window;}// See
// https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
var passiveSupported=false;try{var options={// This function will be called when the browser
// attempts to access the passive property.
get passive(){passiveSupported=true;return false;}};var handler=function(){};globalObj.document.addEventListener('test',handler,options);globalObj.document.removeEventListener('test',handler,options);}catch(err){passiveSupported=false;}return passiveSupported;}

const blockingElements=document.$blockingElements;class DialogBase extends BaseElement{constructor(){super(...arguments);this.hideActions=false;this.stacked=false;this.heading='';this.scrimClickAction='close';this.escapeKeyAction='close';this.open=false;this.defaultAction='close';this.actionAttribute='dialogAction';this.initialFocusAttribute='dialogInitialFocus';this.initialSupressDefaultPressSelector='';this.mdcFoundationClass=MDCDialogFoundation$1;this.boundHandleClick=null;this.boundHandleKeydown=null;this.boundHandleDocumentKeydown=null;}set suppressDefaultPressSelector(selector){if(this.mdcFoundation){this.mdcFoundation.setSuppressDefaultPressSelector(selector);}else {this.initialSupressDefaultPressSelector=selector;}}/**
     * @export
     */get suppressDefaultPressSelector(){return this.mdcFoundation?this.mdcFoundation.getSuppressDefaultPressSelector():this.initialSupressDefaultPressSelector;}get primaryButton(){let assignedNodes=this.primarySlot.assignedNodes();assignedNodes=assignedNodes.filter(node=>node instanceof HTMLElement);const button=assignedNodes[0];return button?button:null;}emitNotification(name,action){const init={detail:action?{action}:{}};const ev=new CustomEvent(name,init);this.dispatchEvent(ev);}getInitialFocusEl(){const initFocusSelector=`[${this.initialFocusAttribute}]`;// only search light DOM. This typically handles all the cases
const lightDomQs=this.querySelector(initFocusSelector);if(lightDomQs){return lightDomQs;}// if not in light dom, search each flattened distributed node.
const primarySlot=this.primarySlot;const primaryNodes=primarySlot.assignedNodes({flatten:true});const primaryFocusElement=this.searchNodeTreesForAttribute(primaryNodes,this.initialFocusAttribute);if(primaryFocusElement){return primaryFocusElement;}const secondarySlot=this.secondarySlot;const secondaryNodes=secondarySlot.assignedNodes({flatten:true});const secondaryFocusElement=this.searchNodeTreesForAttribute(secondaryNodes,this.initialFocusAttribute);if(secondaryFocusElement){return secondaryFocusElement;}const contentSlot=this.contentSlot;const contentNodes=contentSlot.assignedNodes({flatten:true});const initFocusElement=this.searchNodeTreesForAttribute(contentNodes,this.initialFocusAttribute);return initFocusElement;}searchNodeTreesForAttribute(nodes,attribute){for(const node of nodes){if(!(node instanceof HTMLElement)){continue;}if(node.hasAttribute(attribute)){return node;}else {const selection=node.querySelector(`[${attribute}]`);if(selection){return selection;}}}return null;}createAdapter(){return Object.assign(Object.assign({},addHasRemoveClass(this.mdcRoot)),{addBodyClass:()=>document.body.style.overflow='hidden',removeBodyClass:()=>document.body.style.overflow='',areButtonsStacked:()=>this.stacked,clickDefaultButton:()=>{const primary=this.primaryButton;if(primary){primary.click();}},eventTargetMatches:(target,selector)=>target?matches(target,selector):false,getActionFromEvent:e=>{if(!e.target){return '';}const element=closest(e.target,`[${this.actionAttribute}]`);const action=element&&element.getAttribute(this.actionAttribute);return action;},getInitialFocusEl:()=>{return this.getInitialFocusEl();},isContentScrollable:()=>{const el=this.contentElement;return el?el.scrollHeight>el.offsetHeight:false;},notifyClosed:action=>this.emitNotification('closed',action),notifyClosing:action=>{if(!this.closingDueToDisconnect){// Don't set our open state to closed just because we were
// disconnected. That way if we get reconnected, we'll know to
// re-open.
this.open=false;}this.emitNotification('closing',action);},notifyOpened:()=>this.emitNotification('opened'),notifyOpening:()=>{this.open=true;this.emitNotification('opening');},reverseButtons:()=>{},releaseFocus:()=>{blockingElements.remove(this);},trapFocus:el=>{if(!this.isConnected){// this is the case where it is opened and closed and then removed
// from DOM before the animation has completed. Blocking Elements will
// throw if this is the case
return;}blockingElements.push(this);if(el){el.focus();}},registerContentEventHandler:(evtType,handler)=>{const el=this.contentElement;el.addEventListener(evtType,handler);},deregisterContentEventHandler:(evtType,handler)=>{const el=this.contentElement;el.removeEventListener(evtType,handler);},isScrollableContentAtTop:()=>{const el=this.contentElement;return el?el.scrollTop===0:false;},isScrollableContentAtBottom:()=>{const el=this.contentElement;return el?Math.ceil(el.scrollHeight-el.scrollTop)===el.clientHeight:false;},registerWindowEventHandler:(evtType,handler)=>{window.addEventListener(evtType,handler,applyPassive());},deregisterWindowEventHandler:(evtType,handler)=>{window.removeEventListener(evtType,handler,applyPassive());}});}render(){const classes={[cssClasses.STACKED]:this.stacked};let heading=$``;if(this.heading){heading=this.renderHeading();}const actionsClasses={'mdc-dialog__actions':!this.hideActions};return $`
    <div class="mdc-dialog ${o(classes)}"
        role="alertdialog"
        aria-modal="true"
        aria-labelledby="title"
        aria-describedby="content">
      <div class="mdc-dialog__container">
        <div class="mdc-dialog__surface">
          ${heading}
          <div id="content" class="mdc-dialog__content">
            <slot id="contentSlot"></slot>
          </div>
          <footer
              id="actions"
              class="${o(actionsClasses)}">
            <span>
              <slot name="secondaryAction"></slot>
            </span>
            <span>
             <slot name="primaryAction"></slot>
            </span>
          </footer>
        </div>
      </div>
      <div class="mdc-dialog__scrim"></div>
    </div>`;}renderHeading(){return $`
      <h2 id="title" class="mdc-dialog__title">${this.heading}</h2>`;}firstUpdated(){super.firstUpdated();this.mdcFoundation.setAutoStackButtons(true);if(this.initialSupressDefaultPressSelector){this.suppressDefaultPressSelector=this.initialSupressDefaultPressSelector;}else {this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,'mwc-textarea','mwc-menu mwc-list-item','mwc-select mwc-list-item'].join(', ');}this.boundHandleClick=this.mdcFoundation.handleClick.bind(this.mdcFoundation);this.boundHandleKeydown=this.mdcFoundation.handleKeydown.bind(this.mdcFoundation);this.boundHandleDocumentKeydown=this.mdcFoundation.handleDocumentKeydown.bind(this.mdcFoundation);}connectedCallback(){super.connectedCallback();if(this.open&&this.mdcFoundation&&!this.mdcFoundation.isOpen()){// We probably got disconnected while we were still open. Re-open,
// matching the behavior of native <dialog>.
this.setEventListeners();this.mdcFoundation.open();}}disconnectedCallback(){super.disconnectedCallback();if(this.open&&this.mdcFoundation){// If this dialog is opened and then disconnected, we want to close
// the foundation, so that 1) any pending timers are cancelled
// (in particular for trapFocus), and 2) if we reconnect, we can open
// the foundation again to retrigger animations and focus.
this.removeEventListeners();this.closingDueToDisconnect=true;this.mdcFoundation.close(this.currentAction||this.defaultAction);this.closingDueToDisconnect=false;this.currentAction=undefined;// When we close normally, the releaseFocus callback handles removing
// ourselves from the blocking elements stack. However, that callback
// happens on a delay, and when we are closing due to a disconnect we
// need to remove ourselves before the blocking element polyfill's
// mutation observer notices and logs a warning, since it's not valid to
// be in the blocking elements stack while disconnected.
blockingElements.remove(this);}}forceLayout(){this.mdcFoundation.layout();}focus(){const initialFocusEl=this.getInitialFocusEl();initialFocusEl&&initialFocusEl.focus();}blur(){if(!this.shadowRoot){return;}const activeEl=this.shadowRoot.activeElement;if(activeEl){if(activeEl instanceof HTMLElement){activeEl.blur();}}else {const root=this.getRootNode();const activeEl=root instanceof Document?root.activeElement:null;if(activeEl instanceof HTMLElement){activeEl.blur();}}}setEventListeners(){if(this.boundHandleClick){this.mdcRoot.addEventListener('click',this.boundHandleClick);}if(this.boundHandleKeydown){this.mdcRoot.addEventListener('keydown',this.boundHandleKeydown,applyPassive());}if(this.boundHandleDocumentKeydown){document.addEventListener('keydown',this.boundHandleDocumentKeydown,applyPassive());}}removeEventListeners(){if(this.boundHandleClick){this.mdcRoot.removeEventListener('click',this.boundHandleClick);}if(this.boundHandleKeydown){this.mdcRoot.removeEventListener('keydown',this.boundHandleKeydown);}if(this.boundHandleDocumentKeydown){document.removeEventListener('keydown',this.boundHandleDocumentKeydown);}}close(){this.open=false;}show(){this.open=true;}}__decorate([i('.mdc-dialog')],DialogBase.prototype,"mdcRoot",void 0);__decorate([i('slot[name="primaryAction"]')],DialogBase.prototype,"primarySlot",void 0);__decorate([i('slot[name="secondaryAction"]')],DialogBase.prototype,"secondarySlot",void 0);__decorate([i('#contentSlot')],DialogBase.prototype,"contentSlot",void 0);__decorate([i('.mdc-dialog__content')],DialogBase.prototype,"contentElement",void 0);__decorate([i('.mdc-container')],DialogBase.prototype,"conatinerElement",void 0);__decorate([e({type:Boolean})],DialogBase.prototype,"hideActions",void 0);__decorate([e({type:Boolean}),observer(function(){this.forceLayout();})],DialogBase.prototype,"stacked",void 0);__decorate([e({type:String})],DialogBase.prototype,"heading",void 0);__decorate([e({type:String}),observer(function(newAction){this.mdcFoundation.setScrimClickAction(newAction);})],DialogBase.prototype,"scrimClickAction",void 0);__decorate([e({type:String}),observer(function(newAction){this.mdcFoundation.setEscapeKeyAction(newAction);})],DialogBase.prototype,"escapeKeyAction",void 0);__decorate([e({type:Boolean,reflect:true}),observer(function(isOpen){// Check isConnected because we could have been disconnected before first
// update. If we're now closed, then we shouldn't start the MDC foundation
// opening animation. If we're now closed, then we've already closed the
// foundation in disconnectedCallback.
if(this.mdcFoundation&&this.isConnected){if(isOpen){this.setEventListeners();this.mdcFoundation.open();}else {this.removeEventListeners();this.mdcFoundation.close(this.currentAction||this.defaultAction);this.currentAction=undefined;}}})],DialogBase.prototype,"open",void 0);__decorate([e()],DialogBase.prototype,"defaultAction",void 0);__decorate([e()],DialogBase.prototype,"actionAttribute",void 0);__decorate([e()],DialogBase.prototype,"initialFocusAttribute",void 0);

const styles=r`.mdc-dialog .mdc-dialog__surface{background-color:#fff;background-color:var(--mdc-theme-surface, #fff)}.mdc-dialog .mdc-dialog__scrim{background-color:rgba(0,0,0,.32)}.mdc-dialog .mdc-dialog__surface-scrim{background-color:rgba(0,0,0,.32)}.mdc-dialog .mdc-dialog__title{color:rgba(0,0,0,.87)}.mdc-dialog .mdc-dialog__content{color:rgba(0,0,0,.6)}.mdc-dialog .mdc-dialog__close{color:#000;color:var(--mdc-theme-on-surface, #000)}.mdc-dialog .mdc-dialog__close .mdc-icon-button__ripple::before,.mdc-dialog .mdc-dialog__close .mdc-icon-button__ripple::after{background-color:#000;background-color:var(--mdc-ripple-color, var(--mdc-theme-on-surface, #000))}.mdc-dialog .mdc-dialog__close:hover .mdc-icon-button__ripple::before,.mdc-dialog .mdc-dialog__close.mdc-ripple-surface--hover .mdc-icon-button__ripple::before{opacity:0.04;opacity:var(--mdc-ripple-hover-opacity, 0.04)}.mdc-dialog .mdc-dialog__close.mdc-ripple-upgraded--background-focused .mdc-icon-button__ripple::before,.mdc-dialog .mdc-dialog__close:not(.mdc-ripple-upgraded):focus .mdc-icon-button__ripple::before{transition-duration:75ms;opacity:0.12;opacity:var(--mdc-ripple-focus-opacity, 0.12)}.mdc-dialog .mdc-dialog__close:not(.mdc-ripple-upgraded) .mdc-icon-button__ripple::after{transition:opacity 150ms linear}.mdc-dialog .mdc-dialog__close:not(.mdc-ripple-upgraded):active .mdc-icon-button__ripple::after{transition-duration:75ms;opacity:0.12;opacity:var(--mdc-ripple-press-opacity, 0.12)}.mdc-dialog .mdc-dialog__close.mdc-ripple-upgraded{--mdc-ripple-fg-opacity:var(--mdc-ripple-press-opacity, 0.12)}.mdc-dialog.mdc-dialog--scrollable .mdc-dialog__title,.mdc-dialog.mdc-dialog--scrollable .mdc-dialog__actions,.mdc-dialog.mdc-dialog--scrollable.mdc-dialog-scroll-divider-footer .mdc-dialog__actions{border-color:rgba(0,0,0,.12)}.mdc-dialog.mdc-dialog--scrollable .mdc-dialog__title{border-bottom:1px solid rgba(0,0,0,.12);margin-bottom:0}.mdc-dialog.mdc-dialog-scroll-divider-header.mdc-dialog--fullscreen .mdc-dialog__header{box-shadow:0px 3px 1px -2px rgba(0, 0, 0, 0.2),0px 2px 2px 0px rgba(0, 0, 0, 0.14),0px 1px 5px 0px rgba(0,0,0,.12)}.mdc-dialog .mdc-dialog__surface{border-radius:4px;border-radius:var(--mdc-shape-medium, 4px)}.mdc-dialog__surface{box-shadow:0px 11px 15px -7px rgba(0, 0, 0, 0.2),0px 24px 38px 3px rgba(0, 0, 0, 0.14),0px 9px 46px 8px rgba(0,0,0,.12)}.mdc-dialog__title{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-headline6-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:1.25rem;font-size:var(--mdc-typography-headline6-font-size, 1.25rem);line-height:2rem;line-height:var(--mdc-typography-headline6-line-height, 2rem);font-weight:500;font-weight:var(--mdc-typography-headline6-font-weight, 500);letter-spacing:0.0125em;letter-spacing:var(--mdc-typography-headline6-letter-spacing, 0.0125em);text-decoration:inherit;text-decoration:var(--mdc-typography-headline6-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-headline6-text-transform, inherit)}.mdc-dialog__content{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body1-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:1rem;font-size:var(--mdc-typography-body1-font-size, 1rem);line-height:1.5rem;line-height:var(--mdc-typography-body1-line-height, 1.5rem);font-weight:400;font-weight:var(--mdc-typography-body1-font-weight, 400);letter-spacing:0.03125em;letter-spacing:var(--mdc-typography-body1-letter-spacing, 0.03125em);text-decoration:inherit;text-decoration:var(--mdc-typography-body1-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body1-text-transform, inherit)}.mdc-elevation-overlay{position:absolute;border-radius:inherit;pointer-events:none;opacity:0;opacity:var(--mdc-elevation-overlay-opacity, 0);transition:opacity 280ms cubic-bezier(0.4, 0, 0.2, 1);background-color:#fff;background-color:var(--mdc-elevation-overlay-color, #fff)}.mdc-dialog,.mdc-dialog__scrim{position:fixed;top:0;left:0;align-items:center;justify-content:center;box-sizing:border-box;width:100%;height:100%}.mdc-dialog{display:none;z-index:7;z-index:var(--mdc-dialog-z-index, 7)}.mdc-dialog .mdc-dialog__content{padding:20px 24px 20px 24px}.mdc-dialog .mdc-dialog__surface{min-width:280px}@media(max-width: 592px){.mdc-dialog .mdc-dialog__surface{max-width:calc(100vw - 32px)}}@media(min-width: 592px){.mdc-dialog .mdc-dialog__surface{max-width:560px}}.mdc-dialog .mdc-dialog__surface{max-height:calc(100% - 32px)}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{max-width:none}@media(max-width: 960px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{max-height:560px;width:560px}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__close{right:-12px}}@media(max-width: 720px)and (max-width: 672px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{width:calc(100vw - 112px)}}@media(max-width: 720px)and (min-width: 672px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{width:560px}}@media(max-width: 720px)and (max-height: 720px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{max-height:calc(100vh - 160px)}}@media(max-width: 720px)and (min-height: 720px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{max-height:560px}}@media(max-width: 720px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__close{right:-12px}}@media(max-width: 720px)and (max-height: 400px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{height:100%;max-height:100vh;max-width:100vw;width:100vw;border-radius:0}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__close{order:-1;left:-12px}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__header{padding:0 16px 9px;justify-content:flex-start}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__title{margin-left:calc(16px - 2 * 12px)}}@media(max-width: 600px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{height:100%;max-height:100vh;max-width:100vw;width:100vw;border-radius:0}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__close{order:-1;left:-12px}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__header{padding:0 16px 9px;justify-content:flex-start}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__title{margin-left:calc(16px - 2 * 12px)}}@media(min-width: 960px){.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface{width:calc(100vw - 400px)}.mdc-dialog.mdc-dialog--fullscreen .mdc-dialog__surface .mdc-dialog__close{right:-12px}}.mdc-dialog.mdc-dialog__scrim--hidden .mdc-dialog__scrim{opacity:0}.mdc-dialog__scrim{opacity:0;z-index:-1}.mdc-dialog__container{display:flex;flex-direction:row;align-items:center;justify-content:space-around;box-sizing:border-box;height:100%;transform:scale(0.8);opacity:0;pointer-events:none}.mdc-dialog__surface{position:relative;display:flex;flex-direction:column;flex-grow:0;flex-shrink:0;box-sizing:border-box;max-width:100%;max-height:100%;pointer-events:auto;overflow-y:auto}.mdc-dialog__surface .mdc-elevation-overlay{width:100%;height:100%;top:0;left:0}[dir=rtl] .mdc-dialog__surface,.mdc-dialog__surface[dir=rtl]{text-align:right}@media screen and (forced-colors: active),(-ms-high-contrast: active){.mdc-dialog__surface{outline:2px solid windowText}}.mdc-dialog__surface::before{position:absolute;box-sizing:border-box;width:100%;height:100%;top:0;left:0;border:2px solid transparent;border-radius:inherit;content:"";pointer-events:none}@media screen and (-ms-high-contrast: active),screen and (-ms-high-contrast: none){.mdc-dialog__surface::before{content:none}}.mdc-dialog__title{display:block;margin-top:0;position:relative;flex-shrink:0;box-sizing:border-box;margin:0 0 1px;padding:0 24px 9px}.mdc-dialog__title::before{display:inline-block;width:0;height:40px;content:"";vertical-align:0}[dir=rtl] .mdc-dialog__title,.mdc-dialog__title[dir=rtl]{text-align:right}.mdc-dialog--scrollable .mdc-dialog__title{margin-bottom:1px;padding-bottom:15px}.mdc-dialog--fullscreen .mdc-dialog__header{align-items:baseline;border-bottom:1px solid transparent;display:inline-flex;justify-content:space-between;padding:0 24px 9px;z-index:1}.mdc-dialog--fullscreen .mdc-dialog__header .mdc-dialog__close{right:-12px}.mdc-dialog--fullscreen .mdc-dialog__title{margin-bottom:0;padding:0;border-bottom:0}.mdc-dialog--fullscreen.mdc-dialog--scrollable .mdc-dialog__title{border-bottom:0;margin-bottom:0}.mdc-dialog--fullscreen .mdc-dialog__close{top:5px}.mdc-dialog--fullscreen.mdc-dialog--scrollable .mdc-dialog__actions{border-top:1px solid transparent}.mdc-dialog__content{flex-grow:1;box-sizing:border-box;margin:0;overflow:auto;-webkit-overflow-scrolling:touch}.mdc-dialog__content>:first-child{margin-top:0}.mdc-dialog__content>:last-child{margin-bottom:0}.mdc-dialog__title+.mdc-dialog__content,.mdc-dialog__header+.mdc-dialog__content{padding-top:0}.mdc-dialog--scrollable .mdc-dialog__title+.mdc-dialog__content{padding-top:8px;padding-bottom:8px}.mdc-dialog__content .mdc-deprecated-list:first-child:last-child{padding:6px 0 0}.mdc-dialog--scrollable .mdc-dialog__content .mdc-deprecated-list:first-child:last-child{padding:0}.mdc-dialog__actions{display:flex;position:relative;flex-shrink:0;flex-wrap:wrap;align-items:center;justify-content:flex-end;box-sizing:border-box;min-height:52px;margin:0;padding:8px;border-top:1px solid transparent}.mdc-dialog--stacked .mdc-dialog__actions{flex-direction:column;align-items:flex-end}.mdc-dialog__button{margin-left:8px;margin-right:0;max-width:100%;text-align:right}[dir=rtl] .mdc-dialog__button,.mdc-dialog__button[dir=rtl]{margin-left:0;margin-right:8px}.mdc-dialog__button:first-child{margin-left:0;margin-right:0}[dir=rtl] .mdc-dialog__button:first-child,.mdc-dialog__button:first-child[dir=rtl]{margin-left:0;margin-right:0}[dir=rtl] .mdc-dialog__button,.mdc-dialog__button[dir=rtl]{text-align:left}.mdc-dialog--stacked .mdc-dialog__button:not(:first-child){margin-top:12px}.mdc-dialog--open,.mdc-dialog--opening,.mdc-dialog--closing{display:flex}.mdc-dialog--opening .mdc-dialog__scrim{transition:opacity 150ms linear}.mdc-dialog--opening .mdc-dialog__container{transition:opacity 75ms linear,transform 150ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-dialog--closing .mdc-dialog__scrim,.mdc-dialog--closing .mdc-dialog__container{transition:opacity 75ms linear}.mdc-dialog--closing .mdc-dialog__container{transform:none}.mdc-dialog--open .mdc-dialog__scrim{opacity:1}.mdc-dialog--open .mdc-dialog__container{transform:none;opacity:1}.mdc-dialog--open.mdc-dialog__surface-scrim--shown .mdc-dialog__surface-scrim{opacity:1;z-index:1}.mdc-dialog--open.mdc-dialog__surface-scrim--hiding .mdc-dialog__surface-scrim{transition:opacity 75ms linear}.mdc-dialog--open.mdc-dialog__surface-scrim--showing .mdc-dialog__surface-scrim{transition:opacity 150ms linear}.mdc-dialog__surface-scrim{display:none;opacity:0;position:absolute;width:100%;height:100%}.mdc-dialog__surface-scrim--shown .mdc-dialog__surface-scrim,.mdc-dialog__surface-scrim--showing .mdc-dialog__surface-scrim,.mdc-dialog__surface-scrim--hiding .mdc-dialog__surface-scrim{display:block}.mdc-dialog-scroll-lock{overflow:hidden}#actions:not(.mdc-dialog__actions){display:none}.mdc-dialog__surface{box-shadow:var(--mdc-dialog-box-shadow, 0px 11px 15px -7px rgba(0, 0, 0, 0.2), 0px 24px 38px 3px rgba(0, 0, 0, 0.14), 0px 9px 46px 8px rgba(0, 0, 0, 0.12))}@media(min-width: 560px){.mdc-dialog .mdc-dialog__surface{max-width:560px;max-width:var(--mdc-dialog-max-width, 560px)}}.mdc-dialog .mdc-dialog__scrim{background-color:rgba(0, 0, 0, 0.32);background-color:var(--mdc-dialog-scrim-color, rgba(0, 0, 0, 0.32))}.mdc-dialog .mdc-dialog__title{color:rgba(0, 0, 0, 0.87);color:var(--mdc-dialog-heading-ink-color, rgba(0, 0, 0, 0.87))}.mdc-dialog .mdc-dialog__content{color:rgba(0, 0, 0, 0.6);color:var(--mdc-dialog-content-ink-color, rgba(0, 0, 0, 0.6))}.mdc-dialog.mdc-dialog--scrollable .mdc-dialog__title,.mdc-dialog.mdc-dialog--scrollable .mdc-dialog__actions{border-color:rgba(0, 0, 0, 0.12);border-color:var(--mdc-dialog-scroll-divider-color, rgba(0, 0, 0, 0.12))}.mdc-dialog .mdc-dialog__surface{min-width:280px;min-width:var(--mdc-dialog-min-width, 280px)}.mdc-dialog .mdc-dialog__surface{max-height:var(--mdc-dialog-max-height, calc(100% - 32px))}#actions ::slotted(*){margin-left:8px;margin-right:0;max-width:100%;text-align:right}[dir=rtl] #actions ::slotted(*),#actions ::slotted(*[dir=rtl]){margin-left:0;margin-right:8px}[dir=rtl] #actions ::slotted(*),#actions ::slotted(*[dir=rtl]){text-align:left}.mdc-dialog--stacked #actions{flex-direction:column-reverse}.mdc-dialog--stacked #actions *:not(:last-child) ::slotted(*){flex-basis:.000000001px;margin-top:12px}`;

function computeRTL(hass){const lang=hass.language||"en";if(hass.translationMetadata.translations[lang]){return hass.translationMetadata.translations[lang].isRTL||false;}return false;}function computeRTLDirection(hass){return emitRTLDirection(computeRTL(hass));}function emitRTLDirection(rtl){return rtl?"rtl":"ltr";}

const createCloseHeading=(hass,title)=>$`
  <span class="header_title">${title}</span>
  <ha-icon-button
    .label=${hass.localize("ui.dialogs.generic.close")}
    .path=${mdiClose}
    dialogAction="close"
    class="header_button"
    dir=${computeRTLDirection(hass)}
  ></ha-icon-button>
`;_decorate([n("ha-dialog")],function(_initialize,_DialogBase){class HaDialog extends _DialogBase{constructor(...args){super(...args);_initialize(this);}}return {F:HaDialog,d:[{kind:"method",key:"scrollToPos",value:function scrollToPos(x,y){var _this$contentElement;(_this$contentElement=this.contentElement)===null||_this$contentElement===void 0?void 0:_this$contentElement.scrollTo(x,y);}},{kind:"method",key:"renderHeading",value:function renderHeading(){return $`<slot name="heading"> ${_get(_getPrototypeOf(HaDialog.prototype),"renderHeading",this).call(this)} </slot>`;}},{kind:"field",static:true,key:"styles",value(){return [styles,r`
      .mdc-dialog {
        --mdc-dialog-scroll-divider-color: var(--divider-color);
        z-index: var(--dialog-z-index, 7);
        -webkit-backdrop-filter: var(--dialog-backdrop-filter, none);
        backdrop-filter: var(--dialog-backdrop-filter, none);
      }
      .mdc-dialog__actions {
        /* flex-direction: row-reverse; */

        justify-content: space-between;
        padding-bottom: max(env(safe-area-inset-bottom), 8px);
      }
      .mdc-dialog__actions span:nth-child(1) {
        flex: var(--secondary-action-button-flex, unset);
      }
      .mdc-dialog__actions span:nth-child(2) {
        flex: var(--primary-action-button-flex, unset);
      }
      .mdc-dialog__container {
        align-items: var(--vertial-align-dialog, center);
      }
      .mdc-dialog__title::before {
        display: block;
        height: 20px;
      }
      .mdc-dialog .mdc-dialog__title {
        color: var(--primary-text-color);
      }
      .mdc-dialog .mdc-dialog__content {
        position: var(--dialog-content-position, relative);
        /* padding: var(--dialog-content-padding, 20px 24px); */
      }
      :host([hideactions]) .mdc-dialog .mdc-dialog__content {
        padding-bottom: max(
          var(--dialog-content-padding, 20px),
          env(safe-area-inset-bottom)
        );
      }
      .mdc-dialog .mdc-dialog__surface {
        position: var(--dialog-surface-position, relative);
        top: var(--dialog-surface-top);
        min-height: var(--mdc-dialog-min-height, auto);
        border-radius: 1.5rem;
      }
      @media all and (max-width: 450px), all and (max-height: 500px) {
        .mdc-dialog .mdc-dialog__surface {
          border-radius: var(--ha-dialog-border-radius, 0px);
        }
      }

      /* .mdc-dialog__surface {
        margin-top: 50px;
      } */
      :host([flexContent]) .mdc-dialog .mdc-dialog__content {
        display: flex;
        flex-direction: column;
      }
      #content {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      @media only screen and (max-width: 600px) {
        #content {
          display: flex;
          flex-direction: column;
          align-items: center;
        }
      }
      .header_button {
        position: absolute;
        right: 16px;
        top: 10px;
        text-decoration: none;
        color: inherit;
      }
      .header_title {
        margin-right: 40px;
      }
      [dir="rtl"].header_button {
        right: auto;
        left: 16px;
      }
      [dir="rtl"].header_title {
        margin-left: 40px;
        margin-right: 0px;
      }
    `];}}]};},DialogBase);

var topAppBarStyles = "/**\n * @license\n * Copyright Google LLC All Rights Reserved.\n *\n * Use of this source code is governed by an MIT-style license that can be\n * found in the LICENSE file at https://github.com/material-components/material-components-web/blob/master/LICENSE\n */\n.mdc-top-app-bar{background-color:#6200ee;background-color:var(--mdc-theme-primary, #6200ee);color:white;display:flex;position:fixed;flex-direction:column;justify-content:space-between;box-sizing:border-box;width:100%;z-index:4}.mdc-top-app-bar .mdc-top-app-bar__action-item,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon{color:#fff;color:var(--mdc-theme-on-primary, #fff)}.mdc-top-app-bar .mdc-top-app-bar__action-item::before,.mdc-top-app-bar .mdc-top-app-bar__action-item::after,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon::before,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon::after{background-color:#fff;background-color:var(--mdc-ripple-color, var(--mdc-theme-on-primary, #fff))}.mdc-top-app-bar .mdc-top-app-bar__action-item:hover::before,.mdc-top-app-bar .mdc-top-app-bar__action-item.mdc-ripple-surface--hover::before,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon:hover::before,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon.mdc-ripple-surface--hover::before{opacity:0.08;opacity:var(--mdc-ripple-hover-opacity, 0.08)}.mdc-top-app-bar .mdc-top-app-bar__action-item.mdc-ripple-upgraded--background-focused::before,.mdc-top-app-bar .mdc-top-app-bar__action-item:not(.mdc-ripple-upgraded):focus::before,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon.mdc-ripple-upgraded--background-focused::before,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon:not(.mdc-ripple-upgraded):focus::before{transition-duration:75ms;opacity:0.24;opacity:var(--mdc-ripple-focus-opacity, 0.24)}.mdc-top-app-bar .mdc-top-app-bar__action-item:not(.mdc-ripple-upgraded)::after,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon:not(.mdc-ripple-upgraded)::after{transition:opacity 150ms linear}.mdc-top-app-bar .mdc-top-app-bar__action-item:not(.mdc-ripple-upgraded):active::after,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon:not(.mdc-ripple-upgraded):active::after{transition-duration:75ms;opacity:0.24;opacity:var(--mdc-ripple-press-opacity, 0.24)}.mdc-top-app-bar .mdc-top-app-bar__action-item.mdc-ripple-upgraded,.mdc-top-app-bar .mdc-top-app-bar__navigation-icon.mdc-ripple-upgraded{--mdc-ripple-fg-opacity:var(--mdc-ripple-press-opacity, 0.24)}.mdc-top-app-bar__row{display:flex;position:relative;box-sizing:border-box;width:100%;height:64px}.mdc-top-app-bar__section{display:inline-flex;flex:1 1 auto;align-items:center;min-width:0;padding:8px 12px;z-index:1}.mdc-top-app-bar__section--align-start{justify-content:flex-start;order:-1}.mdc-top-app-bar__section--align-end{justify-content:flex-end;order:1}.mdc-top-app-bar__title{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-headline6-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:1.25rem;font-size:var(--mdc-typography-headline6-font-size, 1.25rem);line-height:2rem;line-height:var(--mdc-typography-headline6-line-height, 2rem);font-weight:500;font-weight:var(--mdc-typography-headline6-font-weight, 500);letter-spacing:0.0125em;letter-spacing:var(--mdc-typography-headline6-letter-spacing, 0.0125em);text-decoration:inherit;-webkit-text-decoration:var(--mdc-typography-headline6-text-decoration, inherit);text-decoration:var(--mdc-typography-headline6-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-headline6-text-transform, inherit);padding-left:20px;padding-right:0;text-overflow:ellipsis;white-space:nowrap;overflow:hidden;z-index:1}[dir=rtl] .mdc-top-app-bar__title,.mdc-top-app-bar__title[dir=rtl]{padding-left:0;padding-right:20px}.mdc-top-app-bar--short-collapsed{border-top-left-radius:0;border-top-right-radius:0;border-bottom-right-radius:24px;border-bottom-left-radius:0}[dir=rtl] .mdc-top-app-bar--short-collapsed,.mdc-top-app-bar--short-collapsed[dir=rtl]{border-top-left-radius:0;border-top-right-radius:0;border-bottom-right-radius:0;border-bottom-left-radius:24px}.mdc-top-app-bar--short{top:0;right:auto;left:0;width:100%;transition:width 250ms cubic-bezier(0.4, 0, 0.2, 1)}[dir=rtl] .mdc-top-app-bar--short,.mdc-top-app-bar--short[dir=rtl]{right:0;left:auto}.mdc-top-app-bar--short .mdc-top-app-bar__row{height:56px}.mdc-top-app-bar--short .mdc-top-app-bar__section{padding:4px}.mdc-top-app-bar--short .mdc-top-app-bar__title{transition:opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);opacity:1}.mdc-top-app-bar--short-collapsed{box-shadow:0px 2px 4px -1px rgba(0, 0, 0, 0.2),0px 4px 5px 0px rgba(0, 0, 0, 0.14),0px 1px 10px 0px rgba(0,0,0,.12);width:56px;transition:width 300ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-top-app-bar--short-collapsed .mdc-top-app-bar__title{display:none}.mdc-top-app-bar--short-collapsed .mdc-top-app-bar__action-item{transition:padding 150ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-top-app-bar--short-collapsed.mdc-top-app-bar--short-has-action-item{width:112px}.mdc-top-app-bar--short-collapsed.mdc-top-app-bar--short-has-action-item .mdc-top-app-bar__section--align-end{padding-left:0;padding-right:12px}[dir=rtl] .mdc-top-app-bar--short-collapsed.mdc-top-app-bar--short-has-action-item .mdc-top-app-bar__section--align-end,.mdc-top-app-bar--short-collapsed.mdc-top-app-bar--short-has-action-item .mdc-top-app-bar__section--align-end[dir=rtl]{padding-left:12px;padding-right:0}.mdc-top-app-bar--dense .mdc-top-app-bar__row{height:48px}.mdc-top-app-bar--dense .mdc-top-app-bar__section{padding:0 4px}.mdc-top-app-bar--dense .mdc-top-app-bar__title{padding-left:12px;padding-right:0}[dir=rtl] .mdc-top-app-bar--dense .mdc-top-app-bar__title,.mdc-top-app-bar--dense .mdc-top-app-bar__title[dir=rtl]{padding-left:0;padding-right:12px}.mdc-top-app-bar--prominent .mdc-top-app-bar__row{height:128px}.mdc-top-app-bar--prominent .mdc-top-app-bar__title{align-self:flex-end;padding-bottom:2px}.mdc-top-app-bar--prominent .mdc-top-app-bar__action-item,.mdc-top-app-bar--prominent .mdc-top-app-bar__navigation-icon{align-self:flex-start}.mdc-top-app-bar--fixed{transition:box-shadow 200ms linear}.mdc-top-app-bar--fixed-scrolled{box-shadow:0px 2px 4px -1px rgba(0, 0, 0, 0.2),0px 4px 5px 0px rgba(0, 0, 0, 0.14),0px 1px 10px 0px rgba(0,0,0,.12);transition:box-shadow 200ms linear}.mdc-top-app-bar--dense.mdc-top-app-bar--prominent .mdc-top-app-bar__row{height:96px}.mdc-top-app-bar--dense.mdc-top-app-bar--prominent .mdc-top-app-bar__section{padding:0 12px}.mdc-top-app-bar--dense.mdc-top-app-bar--prominent .mdc-top-app-bar__title{padding-left:20px;padding-right:0;padding-bottom:9px}[dir=rtl] .mdc-top-app-bar--dense.mdc-top-app-bar--prominent .mdc-top-app-bar__title,.mdc-top-app-bar--dense.mdc-top-app-bar--prominent .mdc-top-app-bar__title[dir=rtl]{padding-left:0;padding-right:20px}.mdc-top-app-bar--fixed-adjust{padding-top:64px}.mdc-top-app-bar--dense-fixed-adjust{padding-top:48px}.mdc-top-app-bar--short-fixed-adjust{padding-top:56px}.mdc-top-app-bar--prominent-fixed-adjust{padding-top:128px}.mdc-top-app-bar--dense-prominent-fixed-adjust{padding-top:96px}@media(max-width: 599px){.mdc-top-app-bar__row{height:56px}.mdc-top-app-bar__section{padding:4px}.mdc-top-app-bar--short{transition:width 200ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-top-app-bar--short-collapsed{transition:width 250ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-top-app-bar--short-collapsed .mdc-top-app-bar__section--align-end{padding-left:0;padding-right:12px}[dir=rtl] .mdc-top-app-bar--short-collapsed .mdc-top-app-bar__section--align-end,.mdc-top-app-bar--short-collapsed .mdc-top-app-bar__section--align-end[dir=rtl]{padding-left:12px;padding-right:0}.mdc-top-app-bar--prominent .mdc-top-app-bar__title{padding-bottom:6px}.mdc-top-app-bar--fixed-adjust{padding-top:56px}}\n\n/*# sourceMappingURL=mdc.top-app-bar.min.css.map*/";

_decorate([n("ha-header-bar")],function(_initialize,_LitElement){class HaHeaderBar extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaHeaderBar,d:[{kind:"method",key:"render",value:function render(){return $`<header class="mdc-top-app-bar">
      <div class="mdc-top-app-bar__row">
        <section
          class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start"
          id="navigation"
        >
          <slot name="navigationIcon"></slot>
          <span class="mdc-top-app-bar__title">
            <slot name="title"></slot>
          </span>
        </section>
        <section
          class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end"
          id="actions"
          role="toolbar"
        >
          <slot name="actionItems"></slot>
        </section>
      </div>
    </header>`;}},{kind:"get",static:true,key:"styles",value:function styles(){return [o$1(topAppBarStyles),r`
        .mdc-top-app-bar {
          position: static;
          color: var(--mdc-theme-on-primary, #fff);
          border-bottom: 1px solid var(--divider-color);
        }
      `];}}]};},s);

export { TabBase as T, computeRTLDirection as a, createCloseHeading as b, computeRTL as c, emitRTLDirection as e };
