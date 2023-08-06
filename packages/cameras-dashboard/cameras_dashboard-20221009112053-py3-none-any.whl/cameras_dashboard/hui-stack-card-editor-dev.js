const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { br as Polymer, q as html, er as Base, E as dom, dr as dashToCamelCase, _ as _decorate, c as s, d as e, t, G as i, $, dF as mdiPlus, eq as mdiArrowLeft, es as mdiArrowRight, dJ as mdiDelete, f as fireEvent, r, n } from './main-dev.js';
import { P as PaperInkyFocusBehavior, I as IronMeta, b as IronControlState, c as IronButtonState, e as PaperRippleBehavior, f as IronA11yKeysBehavior } from './stop_propagation-dev.js';
import { I as IronResizableBehavior } from './ha-more-info-dialog-dev.js';
import { al as assign, am as object, as as array, aw as any, an as optional, ao as string, aq as assert } from './auth-dev.js';
import './hui-card-picker-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { c as configElementStyle } from './config-elements-style-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './hui-element-editor-dev.js';
import './js-yaml-dev.js';
import './ha-code-editor-dev.js';
import './ha-form-dev.js';
import './dynamic-element-directive-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './entities-struct-dev.js';
import './action-struct-dev.js';

/**

The `iron-icon` element displays an icon. By default an icon renders as a 24px
square.

Example using src:

    <iron-icon src="star.png"></iron-icon>

Example setting size to 32px x 32px:

    <iron-icon class="big" src="big_star.png"></iron-icon>

    <style is="custom-style">
      .big {
        --iron-icon-height: 32px;
        --iron-icon-width: 32px;
      }
    </style>

The iron elements include several sets of icons. To use the default set of
icons, import `iron-icons.js` and use the `icon` attribute to specify an icon:

    <script type="module">
      import "@polymer/iron-icons/iron-icons.js";
    </script>

    <iron-icon icon="menu"></iron-icon>

To use a different built-in set of icons, import the specific
`iron-icons/<iconset>-icons.js`, and specify the icon as `<iconset>:<icon>`.
For example, to use a communication icon, you would use:

    <script type="module">
      import "@polymer/iron-icons/communication-icons.js";
    </script>

    <iron-icon icon="communication:email"></iron-icon>

You can also create custom icon sets of bitmap or SVG icons.

Example of using an icon named `cherry` from a custom iconset with the ID
`fruit`:

    <iron-icon icon="fruit:cherry"></iron-icon>

See `<iron-iconset>` and `<iron-iconset-svg>` for more information about how to
create a custom iconset.

See the `iron-icons` demo to see the icons available in the various iconsets.

### Styling

The following custom properties are available for styling:

Custom property | Description | Default
----------------|-------------|----------
`--iron-icon` | Mixin applied to the icon | {}
`--iron-icon-width` | Width of the icon | `24px`
`--iron-icon-height` | Height of the icon | `24px`
`--iron-icon-fill-color` | Fill color of the svg icon | `currentcolor`
`--iron-icon-stroke-color` | Stroke color of the svg icon | none

@group Iron Elements
@element iron-icon
@demo demo/index.html
@hero hero.svg
@homepage polymer.github.io
*/Polymer({_template:html`
    <style>
      :host {
        @apply --layout-inline;
        @apply --layout-center-center;
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        @apply --iron-icon;
      }

      :host([hidden]) {
        display: none;
      }
    </style>
`,is:'iron-icon',properties:{/**
     * The name of the icon to use. The name should be of the form:
     * `iconset_name:icon_name`.
     */icon:{type:String},/**
     * The name of the theme to used, if one is specified by the
     * iconset.
     */theme:{type:String},/**
     * If using iron-icon without an iconset, you can set the src to be
     * the URL of an individual icon image file. Note that this will take
     * precedence over a given icon attribute.
     */src:{type:String},/**
     * @type {!IronMeta}
     */_meta:{value:Base.create('iron-meta',{type:'iconset'})}},observers:['_updateIcon(_meta, isAttached)','_updateIcon(theme, isAttached)','_srcChanged(src, isAttached)','_iconChanged(icon, isAttached)'],_DEFAULT_ICONSET:'icons',_iconChanged:function(icon){var parts=(icon||'').split(':');this._iconName=parts.pop();this._iconsetName=parts.pop()||this._DEFAULT_ICONSET;this._updateIcon();},_srcChanged:function(src){this._updateIcon();},_usesIconset:function(){return this.icon||!this.src;},/** @suppress {visibility} */_updateIcon:function(){if(this._usesIconset()){if(this._img&&this._img.parentNode){dom(this.root).removeChild(this._img);}if(this._iconName===''){if(this._iconset){this._iconset.removeIcon(this);}}else if(this._iconsetName&&this._meta){this._iconset=/** @type {?Polymer.Iconset} */this._meta.byKey(this._iconsetName);if(this._iconset){this._iconset.applyIcon(this,this._iconName,this.theme);this.unlisten(window,'iron-iconset-added','_updateIcon');}else {this.listen(window,'iron-iconset-added','_updateIcon');}}}else {if(this._iconset){this._iconset.removeIcon(this);}if(!this._img){this._img=document.createElement('img');this._img.style.width='100%';this._img.style.height='100%';this._img.draggable=false;}this._img.src=this.src;dom(this.root).appendChild(this._img);}}});

/**
Material design: [Icon
toggles](https://www.google.com/design/spec/components/buttons.html#buttons-toggle-buttons)

`paper-icon-button` is a button with an image placed at the center. When the
user touches the button, a ripple effect emanates from the center of the button.

`paper-icon-button` does not include a default icon set. To use icons from the
default set, include `PolymerElements/iron-icons/iron-icons.html`, and use the
`icon` attribute to specify which icon from the icon set to use.

    <paper-icon-button icon="menu"></paper-icon-button>

See [`iron-iconset`](iron-iconset) for more information about
how to use a custom icon set.

Example:

    <script type="module">
      import '@polymer/iron-icons/iron-icons.js';
    </script>

    <paper-icon-button icon="favorite"></paper-icon-button>
    <paper-icon-button src="star.png"></paper-icon-button>

To use `paper-icon-button` as a link, wrap it in an anchor tag. Since
`paper-icon-button` will already receive focus, you may want to prevent the
anchor tag from receiving focus as well by setting its tabindex to -1.

    <a href="https://www.polymer-project.org" tabindex="-1">
      <paper-icon-button icon="polymer"></paper-icon-button>
    </a>

### Styling

Style the button with CSS as you would a normal DOM element. If you are using
the icons provided by `iron-icons`, they will inherit the foreground color of
the button.

    /* make a red "favorite" button *\/
    <paper-icon-button icon="favorite" style="color: red;"></paper-icon-button>

By default, the ripple is the same color as the foreground at 25% opacity. You
may customize the color using the `--paper-icon-button-ink-color` custom
property.

The following custom properties and mixins are available for styling:

Custom property | Description | Default
----------------|-------------|----------
`--paper-icon-button-disabled-text` | The color of the disabled button | `--disabled-text-color`
`--paper-icon-button-ink-color` | Selected/focus ripple color | `--primary-text-color`
`--paper-icon-button` | Mixin for a button | `{}`
`--paper-icon-button-disabled` | Mixin for a disabled button | `{}`
`--paper-icon-button-hover` | Mixin for button on hover | `{}`

@group Paper Elements
@element paper-icon-button
@demo demo/index.html
*/Polymer({is:'paper-icon-button',_template:html`
    <style>
      :host {
        display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        /*
          NOTE: Both values are needed, since some phones require the value to
          be \`transparent\`.
        */
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        /* Because of polymer/2558, this style has lower specificity than * */
        box-sizing: border-box !important;

        @apply --paper-icon-button;
      }

      :host #ink {
        color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
      }

      :host([disabled]) {
        color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        @apply --paper-icon-button-disabled;
      }

      :host([hidden]) {
        display: none !important;
      }

      :host(:hover) {
        @apply --paper-icon-button-hover;
      }

      iron-icon {
        --iron-icon-width: 100%;
        --iron-icon-height: 100%;
      }
    </style>

    <iron-icon id="icon" src="[[src]]" icon="[[icon]]"
               alt$="[[alt]]"></iron-icon>
  `,hostAttributes:{role:'button',tabindex:'0'},behaviors:[PaperInkyFocusBehavior],registered:function(){this._template.setAttribute('strip-whitespace','');},properties:{/**
     * The URL of an image for the icon. If the src property is specified,
     * the icon property should not be.
     */src:{type:String},/**
     * Specifies the icon name or index in the set of icons available in
     * the icon's icon set. If the icon property is specified,
     * the src property should not be.
     */icon:{type:String},/**
     * Specifies the alternate text for the button, for accessibility.
     */alt:{type:String,observer:'_altChanged'}},_altChanged:function(newValue,oldValue){var label=this.getAttribute('aria-label');// Don't stomp over a user-set aria-label.
if(!label||oldValue==label){this.setAttribute('aria-label',newValue);}}});

/**
 * The `iron-iconset-svg` element allows users to define their own icon sets
 * that contain svg icons. The svg icon elements should be children of the
 * `iron-iconset-svg` element. Multiple icons should be given distinct id's.
 *
 * Using svg elements to create icons has a few advantages over traditional
 * bitmap graphics like jpg or png. Icons that use svg are vector based so
 * they are resolution independent and should look good on any device. They
 * are stylable via css. Icons can be themed, colorized, and even animated.
 *
 * Example:
 *
 *     <iron-iconset-svg name="my-svg-icons" size="24">
 *       <svg>
 *         <defs>
 *           <g id="shape">
 *             <rect x="12" y="0" width="12" height="24" />
 *             <circle cx="12" cy="12" r="12" />
 *           </g>
 *         </defs>
 *       </svg>
 *     </iron-iconset-svg>
 *
 * This will automatically register the icon set "my-svg-icons" to the iconset
 * database.  To use these icons from within another element, make a
 * `iron-iconset` element and call the `byId` method
 * to retrieve a given iconset. To apply a particular icon inside an
 * element use the `applyIcon` method. For example:
 *
 *     iconset.applyIcon(iconNode, 'car');
 *
 * @element iron-iconset-svg
 * @demo demo/index.html
 * @implements {Polymer.Iconset}
 */Polymer({is:'iron-iconset-svg',properties:{/**
     * The name of the iconset.
     */name:{type:String,observer:'_nameChanged'},/**
     * The size of an individual icon. Note that icons must be square.
     */size:{type:Number,value:24},/**
     * Set to true to enable mirroring of icons where specified when they are
     * stamped. Icons that should be mirrored should be decorated with a
     * `mirror-in-rtl` attribute.
     *
     * NOTE: For performance reasons, direction will be resolved once per
     * document per iconset, so moving icons in and out of RTL subtrees will
     * not cause their mirrored state to change.
     */rtlMirroring:{type:Boolean,value:false},/**
     * Set to true to measure RTL based on the dir attribute on the body or
     * html elements (measured on document.body or document.documentElement as
     * available).
     */useGlobalRtlAttribute:{type:Boolean,value:false}},created:function(){this._meta=new IronMeta({type:'iconset',key:null,value:null});},attached:function(){this.style.display='none';},/**
   * Construct an array of all icon names in this iconset.
   *
   * @return {!Array} Array of icon names.
   */getIconNames:function(){this._icons=this._createIconMap();return Object.keys(this._icons).map(function(n){return this.name+':'+n;},this);},/**
   * Applies an icon to the given element.
   *
   * An svg icon is prepended to the element's shadowRoot if it exists,
   * otherwise to the element itself.
   *
   * If RTL mirroring is enabled, and the icon is marked to be mirrored in
   * RTL, the element will be tested (once and only once ever for each
   * iconset) to determine the direction of the subtree the element is in.
   * This direction will apply to all future icon applications, although only
   * icons marked to be mirrored will be affected.
   *
   * @method applyIcon
   * @param {Element} element Element to which the icon is applied.
   * @param {string} iconName Name of the icon to apply.
   * @return {?Element} The svg element which renders the icon.
   */applyIcon:function(element,iconName){// Remove old svg element
this.removeIcon(element);// install new svg element
var svg=this._cloneIcon(iconName,this.rtlMirroring&&this._targetIsRTL(element));if(svg){// insert svg element into shadow root, if it exists
var pde=dom(element.root||element);pde.insertBefore(svg,pde.childNodes[0]);return element._svgIcon=svg;}return null;},/**
   * Remove an icon from the given element by undoing the changes effected
   * by `applyIcon`.
   *
   * @param {Element} element The element from which the icon is removed.
   */removeIcon:function(element){// Remove old svg element
if(element._svgIcon){dom(element.root||element).removeChild(element._svgIcon);element._svgIcon=null;}},/**
   * Measures and memoizes the direction of the element. Note that this
   * measurement is only done once and the result is memoized for future
   * invocations.
   */_targetIsRTL:function(target){if(this.__targetIsRTL==null){if(this.useGlobalRtlAttribute){var globalElement=document.body&&document.body.hasAttribute('dir')?document.body:document.documentElement;this.__targetIsRTL=globalElement.getAttribute('dir')==='rtl';}else {if(target&&target.nodeType!==Node.ELEMENT_NODE){target=target.host;}this.__targetIsRTL=target&&window.getComputedStyle(target)['direction']==='rtl';}}return this.__targetIsRTL;},/**
   *
   * When name is changed, register iconset metadata
   *
   */_nameChanged:function(){this._meta.value=null;this._meta.key=this.name;this._meta.value=this;this.async(function(){this.fire('iron-iconset-added',this,{node:window});});},/**
   * Create a map of child SVG elements by id.
   *
   * @return {!Object} Map of id's to SVG elements.
   */_createIconMap:function(){// Objects chained to Object.prototype (`{}`) have members. Specifically,
// on FF there is a `watch` method that confuses the icon map, so we
// need to use a null-based object here.
var icons=Object.create(null);dom(this).querySelectorAll('[id]').forEach(function(icon){icons[icon.id]=icon;});return icons;},/**
   * Produce installable clone of the SVG element matching `id` in this
   * iconset, or `undefined` if there is no matching element.
   *
   * @return {Element} Returns an installable clone of the SVG element
   * matching `id`.
   */_cloneIcon:function(id,mirrorAllowed){// create the icon map on-demand, since the iconset itself has no discrete
// signal to know when it's children are fully parsed
this._icons=this._icons||this._createIconMap();return this._prepareSvgClone(this._icons[id],this.size,mirrorAllowed);},/**
   * @param {Element} sourceSvg
   * @param {number} size
   * @param {Boolean} mirrorAllowed
   * @return {Element}
   */_prepareSvgClone:function(sourceSvg,size,mirrorAllowed){if(sourceSvg){var content=sourceSvg.cloneNode(true),svg=document.createElementNS('http://www.w3.org/2000/svg','svg'),viewBox=content.getAttribute('viewBox')||'0 0 '+size+' '+size,cssText='pointer-events: none; display: block; width: 100%; height: 100%;';if(mirrorAllowed&&content.hasAttribute('mirror-in-rtl')){cssText+='-webkit-transform:scale(-1,1);transform:scale(-1,1);transform-origin:center;';}svg.setAttribute('viewBox',viewBox);svg.setAttribute('preserveAspectRatio','xMidYMid meet');svg.setAttribute('focusable','false');// TODO(dfreedm): `pointer-events: none` works around
// https://crbug.com/370136
// TODO(sjmiles): inline style may not be ideal, but avoids requiring a
// shadow-root
svg.style.cssText=cssText;svg.appendChild(content).removeAttribute('id');return svg;}return null;}});

const template=html`<iron-iconset-svg name="paper-tabs" size="24">
<svg><defs>
<g id="chevron-left"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g>
<g id="chevron-right"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g>
</defs></svg>
</iron-iconset-svg>`;document.head.appendChild(template.content);

/*
`paper-tab` is styled to look like a tab. It should be used in conjunction with
`paper-tabs`.

Example:

    <paper-tabs selected="0">
      <paper-tab>TAB 1</paper-tab>
      <paper-tab>TAB 2</paper-tab>
      <paper-tab>TAB 3</paper-tab>
    </paper-tabs>

### Styling

The following custom properties and mixins are available for styling:

Custom property | Description | Default
----------------|-------------|----------
`--paper-tab-ink` | Ink color | `--paper-yellow-a100`
`--paper-tab` | Mixin applied to the tab | `{}`
`--paper-tab-content` | Mixin applied to the tab content | `{}`
`--paper-tab-content-focused` | Mixin applied to the tab content when the tab is focused | `{}`
`--paper-tab-content-unselected` | Mixin applied to the tab content when the tab is not selected | `{}`

This element applies the mixin `--paper-font-common-base` but does not import
`paper-styles/typography.html`. In order to apply the `Roboto` font to this
element, make sure you've imported `paper-styles/typography.html`.
*/Polymer({_template:html`
    <style>
      :host {
        @apply --layout-inline;
        @apply --layout-center;
        @apply --layout-center-justified;
        @apply --layout-flex-auto;

        position: relative;
        padding: 0 12px;
        overflow: hidden;
        cursor: pointer;
        vertical-align: middle;

        @apply --paper-font-common-base;
        @apply --paper-tab;
      }

      :host(:focus) {
        outline: none;
      }

      :host([link]) {
        padding: 0;
      }

      .tab-content {
        height: 100%;
        transform: translateZ(0);
          -webkit-transform: translateZ(0);
        transition: opacity 0.1s cubic-bezier(0.4, 0.0, 1, 1);
        @apply --layout-horizontal;
        @apply --layout-center-center;
        @apply --layout-flex-auto;
        @apply --paper-tab-content;
      }

      :host(:not(.iron-selected)) > .tab-content {
        opacity: 0.8;

        @apply --paper-tab-content-unselected;
      }

      :host(:focus) .tab-content {
        opacity: 1;
        font-weight: 700;

        @apply --paper-tab-content-focused;
      }

      paper-ripple {
        color: var(--paper-tab-ink, var(--paper-yellow-a100));
      }

      .tab-content > ::slotted(a) {
        @apply --layout-flex-auto;

        height: 100%;
      }
    </style>

    <div class="tab-content">
      <slot></slot>
    </div>
`,is:'paper-tab',behaviors:[IronControlState,IronButtonState,PaperRippleBehavior],properties:{/**
     * If true, the tab will forward keyboard clicks (enter/space) to
     * the first anchor element found in its descendants
     */link:{type:Boolean,value:false,reflectToAttribute:true}},/** @private */hostAttributes:{role:'tab'},listeners:{down:'_updateNoink',tap:'_onTap'},attached:function(){this._updateNoink();},get _parentNoink(){var parent=dom(this).parentNode;return !!parent&&!!parent.noink;},_updateNoink:function(){this.noink=!!this.noink||!!this._parentNoink;},_onTap:function(event){if(this.link){var anchor=this.queryEffectiveChildren('a');if(!anchor){return;}// Don't get stuck in a loop delegating
// the listener from the child anchor
if(event.target===anchor){return;}anchor.click();}}});

class IronSelection{/**
   * @param {!Function} selectCallback
   * @suppress {missingProvide}
   */constructor(selectCallback){this.selection=[];this.selectCallback=selectCallback;}/**
   * Retrieves the selected item(s).
   *
   * @returns Returns the selected item(s). If the multi property is true,
   * `get` will return an array, otherwise it will return
   * the selected item or undefined if there is no selection.
   */get(){return this.multi?this.selection.slice():this.selection[0];}/**
   * Clears all the selection except the ones indicated.
   *
   * @param {Array} excludes items to be excluded.
   */clear(excludes){this.selection.slice().forEach(function(item){if(!excludes||excludes.indexOf(item)<0){this.setItemSelected(item,false);}},this);}/**
   * Indicates if a given item is selected.
   *
   * @param {*} item The item whose selection state should be checked.
   * @return {boolean} Returns true if `item` is selected.
   */isSelected(item){return this.selection.indexOf(item)>=0;}/**
   * Sets the selection state for a given item to either selected or deselected.
   *
   * @param {*} item The item to select.
   * @param {boolean} isSelected True for selected, false for deselected.
   */setItemSelected(item,isSelected){if(item!=null){if(isSelected!==this.isSelected(item)){// proceed to update selection only if requested state differs from
// current
if(isSelected){this.selection.push(item);}else {var i=this.selection.indexOf(item);if(i>=0){this.selection.splice(i,1);}}if(this.selectCallback){this.selectCallback(item,isSelected);}}}}/**
   * Sets the selection state for a given item. If the `multi` property
   * is true, then the selected state of `item` will be toggled; otherwise
   * the `item` will be selected.
   *
   * @param {*} item The item to select.
   */select(item){if(this.multi){this.toggle(item);}else if(this.get()!==item){this.setItemSelected(this.get(),false);this.setItemSelected(item,true);}}/**
   * Toggles the selection state for `item`.
   *
   * @param {*} item The item to toggle.
   */toggle(item){this.setItemSelected(item,!this.isSelected(item));}}

/**
 * @polymerBehavior
 */const IronSelectableBehavior={/**
   * Fired when iron-selector is activated (selected or deselected).
   * It is fired before the selected items are changed.
   * Cancel the event to abort selection.
   *
   * @event iron-activate
   */ /**
   * Fired when an item is selected
   *
   * @event iron-select
   */ /**
   * Fired when an item is deselected
   *
   * @event iron-deselect
   */ /**
   * Fired when the list of selectable items changes (e.g., items are
   * added or removed). The detail of the event is a mutation record that
   * describes what changed.
   *
   * @event iron-items-changed
   */properties:{/**
     * If you want to use an attribute value or property of an element for
     * `selected` instead of the index, set this to the name of the attribute
     * or property. Hyphenated values are converted to camel case when used to
     * look up the property of a selectable element. Camel cased values are
     * *not* converted to hyphenated values for attribute lookup. It's
     * recommended that you provide the hyphenated form of the name so that
     * selection works in both cases. (Use `attr-or-property-name` instead of
     * `attrOrPropertyName`.)
     */attrForSelected:{type:String,value:null},/**
     * Gets or sets the selected element. The default is to use the index of the
     * item.
     * @type {string|number}
     */selected:{type:String,notify:true},/**
     * Returns the currently selected item.
     *
     * @type {?Object}
     */selectedItem:{type:Object,readOnly:true,notify:true},/**
     * The event that fires from items when they are selected. Selectable
     * will listen for this event from items and update the selection state.
     * Set to empty string to listen to no events.
     */activateEvent:{type:String,value:'tap',observer:'_activateEventChanged'},/**
     * This is a CSS selector string.  If this is set, only items that match the
     * CSS selector are selectable.
     */selectable:String,/**
     * The class to set on elements when selected.
     */selectedClass:{type:String,value:'iron-selected'},/**
     * The attribute to set on elements when selected.
     */selectedAttribute:{type:String,value:null},/**
     * Default fallback if the selection based on selected with
     * `attrForSelected` is not found.
     */fallbackSelection:{type:String,value:null},/**
     * The list of items from which a selection can be made.
     */items:{type:Array,readOnly:true,notify:true,value:function(){return [];}},/**
     * The set of excluded elements where the key is the `localName`
     * of the element that will be ignored from the item list.
     *
     * @default {template: 1}
     */_excludedLocalNames:{type:Object,value:function(){return {'template':1,'dom-bind':1,'dom-if':1,'dom-repeat':1};}}},observers:['_updateAttrForSelected(attrForSelected)','_updateSelected(selected)','_checkFallback(fallbackSelection)'],created:function(){this._bindFilterItem=this._filterItem.bind(this);this._selection=new IronSelection(this._applySelection.bind(this));},attached:function(){this._observer=this._observeItems(this);this._addListener(this.activateEvent);},detached:function(){if(this._observer){dom(this).unobserveNodes(this._observer);}this._removeListener(this.activateEvent);},/**
   * Returns the index of the given item.
   *
   * @method indexOf
   * @param {Object} item
   * @returns Returns the index of the item
   */indexOf:function(item){return this.items?this.items.indexOf(item):-1;},/**
   * Selects the given value.
   *
   * @method select
   * @param {string|number} value the value to select.
   */select:function(value){this.selected=value;},/**
   * Selects the previous item.
   *
   * @method selectPrevious
   */selectPrevious:function(){var length=this.items.length;var index=length-1;if(this.selected!==undefined){index=(Number(this._valueToIndex(this.selected))-1+length)%length;}this.selected=this._indexToValue(index);},/**
   * Selects the next item.
   *
   * @method selectNext
   */selectNext:function(){var index=0;if(this.selected!==undefined){index=(Number(this._valueToIndex(this.selected))+1)%this.items.length;}this.selected=this._indexToValue(index);},/**
   * Selects the item at the given index.
   *
   * @method selectIndex
   */selectIndex:function(index){this.select(this._indexToValue(index));},/**
   * Force a synchronous update of the `items` property.
   *
   * NOTE: Consider listening for the `iron-items-changed` event to respond to
   * updates to the set of selectable items after updates to the DOM list and
   * selection state have been made.
   *
   * WARNING: If you are using this method, you should probably consider an
   * alternate approach. Synchronously querying for items is potentially
   * slow for many use cases. The `items` property will update asynchronously
   * on its own to reflect selectable items in the DOM.
   */forceSynchronousItemUpdate:function(){if(this._observer&&typeof this._observer.flush==='function'){// NOTE(bicknellr): `dom.flush` above is no longer sufficient to trigger
// `observeNodes` callbacks. Polymer 2.x returns an object from
// `observeNodes` with a `flush` that synchronously gives the callback any
// pending MutationRecords (retrieved with `takeRecords`). Any case where
// ShadyDOM flushes were expected to synchronously trigger item updates
// will now require calling `forceSynchronousItemUpdate`.
this._observer.flush();}else {this._updateItems();}},// UNUSED, FOR API COMPATIBILITY
get _shouldUpdateSelection(){return this.selected!=null;},_checkFallback:function(){this._updateSelected();},_addListener:function(eventName){this.listen(this,eventName,'_activateHandler');},_removeListener:function(eventName){this.unlisten(this,eventName,'_activateHandler');},_activateEventChanged:function(eventName,old){this._removeListener(old);this._addListener(eventName);},_updateItems:function(){var nodes=dom(this).queryDistributedElements(this.selectable||'*');nodes=Array.prototype.filter.call(nodes,this._bindFilterItem);this._setItems(nodes);},_updateAttrForSelected:function(){if(this.selectedItem){this.selected=this._valueForItem(this.selectedItem);}},_updateSelected:function(){this._selectSelected(this.selected);},_selectSelected:function(selected){if(!this.items){return;}var item=this._valueToItem(this.selected);if(item){this._selection.select(item);}else {this._selection.clear();}// Check for items, since this array is populated only when attached
// Since Number(0) is falsy, explicitly check for undefined
if(this.fallbackSelection&&this.items.length&&this._selection.get()===undefined){this.selected=this.fallbackSelection;}},_filterItem:function(node){return !this._excludedLocalNames[node.localName];},_valueToItem:function(value){return value==null?null:this.items[this._valueToIndex(value)];},_valueToIndex:function(value){if(this.attrForSelected){for(var i=0,item;item=this.items[i];i++){if(this._valueForItem(item)==value){return i;}}}else {return Number(value);}},_indexToValue:function(index){if(this.attrForSelected){var item=this.items[index];if(item){return this._valueForItem(item);}}else {return index;}},_valueForItem:function(item){if(!item){return null;}if(!this.attrForSelected){var i=this.indexOf(item);return i===-1?null:i;}var propValue=item[dashToCamelCase(this.attrForSelected)];return propValue!=undefined?propValue:item.getAttribute(this.attrForSelected);},_applySelection:function(item,isSelected){if(this.selectedClass){this.toggleClass(this.selectedClass,isSelected,item);}if(this.selectedAttribute){this.toggleAttribute(this.selectedAttribute,isSelected,item);}this._selectionChange();this.fire('iron-'+(isSelected?'select':'deselect'),{item:item});},_selectionChange:function(){this._setSelectedItem(this._selection.get());},// observe items change under the given node.
_observeItems:function(node){return dom(node).observeNodes(function(mutation){this._updateItems();this._updateSelected();// Let other interested parties know about the change so that
// we don't have to recreate mutation observers everywhere.
this.fire('iron-items-changed',mutation,{bubbles:false,cancelable:false});});},_activateHandler:function(e){var t=e.target;var items=this.items;while(t&&t!=this){var i=items.indexOf(t);if(i>=0){var value=this._indexToValue(i);this._itemActivate(value,t);return;}t=t.parentNode;}},_itemActivate:function(value,item){if(!this.fire('iron-activate',{selected:value,item:item},{cancelable:true}).defaultPrevented){this.select(value);}}};

/**
 * @polymerBehavior IronMultiSelectableBehavior
 */const IronMultiSelectableBehaviorImpl={properties:{/**
     * If true, multiple selections are allowed.
     */multi:{type:Boolean,value:false,observer:'multiChanged'},/**
     * Gets or sets the selected elements. This is used instead of `selected`
     * when `multi` is true.
     */selectedValues:{type:Array,notify:true,value:function(){return [];}},/**
     * Returns an array of currently selected items.
     */selectedItems:{type:Array,readOnly:true,notify:true,value:function(){return [];}}},observers:['_updateSelected(selectedValues.splices)'],/**
   * Selects the given value. If the `multi` property is true, then the selected
   * state of the `value` will be toggled; otherwise the `value` will be
   * selected.
   *
   * @method select
   * @param {string|number} value the value to select.
   */select:function(value){if(this.multi){this._toggleSelected(value);}else {this.selected=value;}},multiChanged:function(multi){this._selection.multi=multi;this._updateSelected();},// UNUSED, FOR API COMPATIBILITY
get _shouldUpdateSelection(){return this.selected!=null||this.selectedValues!=null&&this.selectedValues.length;},_updateAttrForSelected:function(){if(!this.multi){IronSelectableBehavior._updateAttrForSelected.apply(this);}else if(this.selectedItems&&this.selectedItems.length>0){this.selectedValues=this.selectedItems.map(function(selectedItem){return this._indexToValue(this.indexOf(selectedItem));},this).filter(function(unfilteredValue){return unfilteredValue!=null;},this);}},_updateSelected:function(){if(this.multi){this._selectMulti(this.selectedValues);}else {this._selectSelected(this.selected);}},_selectMulti:function(values){values=values||[];var selectedItems=(this._valuesToItems(values)||[]).filter(function(item){return item!==null&&item!==undefined;});// clear all but the current selected items
this._selection.clear(selectedItems);// select only those not selected yet
for(var i=0;i<selectedItems.length;i++){this._selection.setItemSelected(selectedItems[i],true);}// Check for items, since this array is populated only when attached
if(this.fallbackSelection&&!this._selection.get().length){var fallback=this._valueToItem(this.fallbackSelection);if(fallback){this.select(this.fallbackSelection);}}},_selectionChange:function(){var s=this._selection.get();if(this.multi){this._setSelectedItems(s);this._setSelectedItem(s.length?s[0]:null);}else {if(s!==null&&s!==undefined){this._setSelectedItems([s]);this._setSelectedItem(s);}else {this._setSelectedItems([]);this._setSelectedItem(null);}}},_toggleSelected:function(value){var i=this.selectedValues.indexOf(value);var unselected=i<0;if(unselected){this.push('selectedValues',value);}else {this.splice('selectedValues',i,1);}},_valuesToItems:function(values){return values==null?null:values.map(function(value){return this._valueToItem(value);},this);}};/** @polymerBehavior */const IronMultiSelectableBehavior=[IronSelectableBehavior,IronMultiSelectableBehaviorImpl];

/**
 * `IronMenuBehavior` implements accessible menu behavior.
 *
 * @demo demo/index.html
 * @polymerBehavior IronMenuBehavior
 */const IronMenuBehaviorImpl={properties:{/**
     * Returns the currently focused item.
     * @type {?Object}
     */focusedItem:{observer:'_focusedItemChanged',readOnly:true,type:Object},/**
     * The attribute to use on menu items to look up the item title. Typing the
     * first letter of an item when the menu is open focuses that item. If
     * unset, `textContent` will be used.
     */attrForItemTitle:{type:String},/**
     * @type {boolean}
     */disabled:{type:Boolean,value:false,observer:'_disabledChanged'}},/**
   * The list of keys has been taken from
   * https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/getModifierState
   * @private
   */_MODIFIER_KEYS:['Alt','AltGraph','CapsLock','Control','Fn','FnLock','Hyper','Meta','NumLock','OS','ScrollLock','Shift','Super','Symbol','SymbolLock'],/** @private */_SEARCH_RESET_TIMEOUT_MS:1000,/** @private */_previousTabIndex:0,hostAttributes:{'role':'menu'},observers:['_updateMultiselectable(multi)'],listeners:{'focus':'_onFocus','keydown':'_onKeydown','iron-items-changed':'_onIronItemsChanged'},/**
   * @type {!Object}
   */keyBindings:{'up':'_onUpKey','down':'_onDownKey','esc':'_onEscKey','shift+tab:keydown':'_onShiftTabDown'},attached:function(){this._resetTabindices();},/**
   * Selects the given value. If the `multi` property is true, then the selected
   * state of the `value` will be toggled; otherwise the `value` will be
   * selected.
   *
   * @param {string|number} value the value to select.
   */select:function(value){// Cancel automatically focusing a default item if the menu received focus
// through a user action selecting a particular item.
if(this._defaultFocusAsync){this.cancelAsync(this._defaultFocusAsync);this._defaultFocusAsync=null;}var item=this._valueToItem(value);if(item&&item.hasAttribute('disabled'))return;this._setFocusedItem(item);IronMultiSelectableBehaviorImpl.select.apply(this,arguments);},/**
   * Resets all tabindex attributes to the appropriate value based on the
   * current selection state. The appropriate value is `0` (focusable) for
   * the default selected item, and `-1` (not keyboard focusable) for all
   * other items. Also sets the correct initial values for aria-selected
   * attribute, true for default selected item and false for others.
   */_resetTabindices:function(){var firstSelectedItem=this.multi?this.selectedItems&&this.selectedItems[0]:this.selectedItem;this.items.forEach(function(item){item.setAttribute('tabindex',item===firstSelectedItem?'0':'-1');item.setAttribute('aria-selected',this._selection.isSelected(item));},this);},/**
   * Sets appropriate ARIA based on whether or not the menu is meant to be
   * multi-selectable.
   *
   * @param {boolean} multi True if the menu should be multi-selectable.
   */_updateMultiselectable:function(multi){if(multi){this.setAttribute('aria-multiselectable','true');}else {this.removeAttribute('aria-multiselectable');}},/**
   * Given a KeyboardEvent, this method will focus the appropriate item in the
   * menu (if there is a relevant item, and it is possible to focus it).
   *
   * @param {KeyboardEvent} event A KeyboardEvent.
   */_focusWithKeyboardEvent:function(event){// Make sure that the key pressed is not a modifier key.
// getModifierState is not being used, as it is not available in Safari
// earlier than 10.0.2 (https://trac.webkit.org/changeset/206725/webkit)
if(this._MODIFIER_KEYS.indexOf(event.key)!==-1)return;this.cancelDebouncer('_clearSearchText');var searchText=this._searchText||'';var key=event.key&&event.key.length==1?event.key:String.fromCharCode(event.keyCode);searchText+=key.toLocaleLowerCase();var searchLength=searchText.length;for(var i=0,item;item=this.items[i];i++){if(item.hasAttribute('disabled')){continue;}var attr=this.attrForItemTitle||'textContent';var title=(item[attr]||item.getAttribute(attr)||'').trim();if(title.length<searchLength){continue;}if(title.slice(0,searchLength).toLocaleLowerCase()==searchText){this._setFocusedItem(item);break;}}this._searchText=searchText;this.debounce('_clearSearchText',this._clearSearchText,this._SEARCH_RESET_TIMEOUT_MS);},_clearSearchText:function(){this._searchText='';},/**
   * Focuses the previous item (relative to the currently focused item) in the
   * menu, disabled items will be skipped.
   * Loop until length + 1 to handle case of single item in menu.
   */_focusPrevious:function(){var length=this.items.length;var curFocusIndex=Number(this.indexOf(this.focusedItem));for(var i=1;i<length+1;i++){var item=this.items[(curFocusIndex-i+length)%length];if(!item.hasAttribute('disabled')){var owner=dom(item).getOwnerRoot()||document;this._setFocusedItem(item);// Focus might not have worked, if the element was hidden or not
// focusable. In that case, try again.
if(dom(owner).activeElement==item){return;}}}},/**
   * Focuses the next item (relative to the currently focused item) in the
   * menu, disabled items will be skipped.
   * Loop until length + 1 to handle case of single item in menu.
   */_focusNext:function(){var length=this.items.length;var curFocusIndex=Number(this.indexOf(this.focusedItem));for(var i=1;i<length+1;i++){var item=this.items[(curFocusIndex+i)%length];if(!item.hasAttribute('disabled')){var owner=dom(item).getOwnerRoot()||document;this._setFocusedItem(item);// Focus might not have worked, if the element was hidden or not
// focusable. In that case, try again.
if(dom(owner).activeElement==item){return;}}}},/**
   * Mutates items in the menu based on provided selection details, so that
   * all items correctly reflect selection state.
   *
   * @param {Element} item An item in the menu.
   * @param {boolean} isSelected True if the item should be shown in a
   * selected state, otherwise false.
   */_applySelection:function(item,isSelected){if(isSelected){item.setAttribute('aria-selected','true');}else {item.setAttribute('aria-selected','false');}IronSelectableBehavior._applySelection.apply(this,arguments);},/**
   * Discretely updates tabindex values among menu items as the focused item
   * changes.
   *
   * @param {Element} focusedItem The element that is currently focused.
   * @param {?Element} old The last element that was considered focused, if
   * applicable.
   */_focusedItemChanged:function(focusedItem,old){old&&old.setAttribute('tabindex','-1');if(focusedItem&&!focusedItem.hasAttribute('disabled')&&!this.disabled){focusedItem.setAttribute('tabindex','0');focusedItem.focus();}},/**
   * A handler that responds to mutation changes related to the list of items
   * in the menu.
   *
   * @param {CustomEvent} event An event containing mutation records as its
   * detail.
   */_onIronItemsChanged:function(event){if(event.detail.addedNodes.length){this._resetTabindices();}},/**
   * Handler that is called when a shift+tab keypress is detected by the menu.
   *
   * @param {CustomEvent} event A key combination event.
   */_onShiftTabDown:function(event){var oldTabIndex=this.getAttribute('tabindex');IronMenuBehaviorImpl._shiftTabPressed=true;this._setFocusedItem(null);this.setAttribute('tabindex','-1');this.async(function(){this.setAttribute('tabindex',oldTabIndex);IronMenuBehaviorImpl._shiftTabPressed=false;// NOTE(cdata): polymer/polymer#1305
},1);},/**
   * Handler that is called when the menu receives focus.
   *
   * @param {FocusEvent} event A focus event.
   */_onFocus:function(event){if(IronMenuBehaviorImpl._shiftTabPressed){// do not focus the menu itself
return;}// Do not focus the selected tab if the deepest target is part of the
// menu element's local DOM and is focusable.
var rootTarget=/** @type {?HTMLElement} */dom(event).rootTarget;if(rootTarget!==this&&typeof rootTarget.tabIndex!=='undefined'&&!this.isLightDescendant(rootTarget)){return;}// clear the cached focus item
this._defaultFocusAsync=this.async(function(){// focus the selected item when the menu receives focus, or the first item
// if no item is selected
var firstSelectedItem=this.multi?this.selectedItems&&this.selectedItems[0]:this.selectedItem;this._setFocusedItem(null);if(firstSelectedItem){this._setFocusedItem(firstSelectedItem);}else if(this.items[0]){// We find the first none-disabled item (if one exists)
this._focusNext();}});},/**
   * Handler that is called when the up key is pressed.
   *
   * @param {CustomEvent} event A key combination event.
   */_onUpKey:function(event){// up and down arrows moves the focus
this._focusPrevious();event.detail.keyboardEvent.preventDefault();},/**
   * Handler that is called when the down key is pressed.
   *
   * @param {CustomEvent} event A key combination event.
   */_onDownKey:function(event){this._focusNext();event.detail.keyboardEvent.preventDefault();},/**
   * Handler that is called when the esc key is pressed.
   *
   * @param {CustomEvent} event A key combination event.
   */_onEscKey:function(event){var focusedItem=this.focusedItem;if(focusedItem){focusedItem.blur();}},/**
   * Handler that is called when a keydown event is detected.
   *
   * @param {KeyboardEvent} event A keyboard event.
   */_onKeydown:function(event){if(!this.keyboardEventMatchesKeys(event,'up down esc')){// all other keys focus the menu item starting with that character
this._focusWithKeyboardEvent(event);}event.stopPropagation();},// override _activateHandler
_activateHandler:function(event){IronSelectableBehavior._activateHandler.call(this,event);event.stopPropagation();},/**
   * Updates this element's tab index when it's enabled/disabled.
   * @param {boolean} disabled
   */_disabledChanged:function(disabled){if(disabled){this._previousTabIndex=this.hasAttribute('tabindex')?this.tabIndex:0;this.removeAttribute('tabindex');// No tabindex means not tab-able or select-able.
}else if(!this.hasAttribute('tabindex')){this.setAttribute('tabindex',this._previousTabIndex);}}};IronMenuBehaviorImpl._shiftTabPressed=false;/** @polymerBehavior */const IronMenuBehavior=[IronMultiSelectableBehavior,IronA11yKeysBehavior,IronMenuBehaviorImpl];

/**
 * `IronMenubarBehavior` implements accessible menubar behavior.
 *
 * @polymerBehavior IronMenubarBehavior
 */const IronMenubarBehaviorImpl={hostAttributes:{'role':'menubar'},/**
   * @type {!Object}
   */keyBindings:{'left':'_onLeftKey','right':'_onRightKey'},_onUpKey:function(event){this.focusedItem.click();event.detail.keyboardEvent.preventDefault();},_onDownKey:function(event){this.focusedItem.click();event.detail.keyboardEvent.preventDefault();},get _isRTL(){return window.getComputedStyle(this)['direction']==='rtl';},_onLeftKey:function(event){if(this._isRTL){this._focusNext();}else {this._focusPrevious();}event.detail.keyboardEvent.preventDefault();},_onRightKey:function(event){if(this._isRTL){this._focusPrevious();}else {this._focusNext();}event.detail.keyboardEvent.preventDefault();},_onKeydown:function(event){if(this.keyboardEventMatchesKeys(event,'up down left right esc')){return;}// all other keys focus the menu item starting with that character
this._focusWithKeyboardEvent(event);}};/** @polymerBehavior */const IronMenubarBehavior=[IronMenuBehavior,IronMenubarBehaviorImpl];

/**
Material design: [Tabs](https://www.google.com/design/spec/components/tabs.html)

`paper-tabs` makes it easy to explore and switch between different views or
functional aspects of an app, or to browse categorized data sets.

Use `selected` property to get or set the selected tab.

Example:

    <paper-tabs selected="0">
      <paper-tab>TAB 1</paper-tab>
      <paper-tab>TAB 2</paper-tab>
      <paper-tab>TAB 3</paper-tab>
    </paper-tabs>

See <a href="?active=paper-tab">paper-tab</a> for more information about
`paper-tab`.

A common usage for `paper-tabs` is to use it along with `iron-pages` to switch
between different views.

    <paper-tabs selected="{{selected}}">
      <paper-tab>Tab 1</paper-tab>
      <paper-tab>Tab 2</paper-tab>
      <paper-tab>Tab 3</paper-tab>
    </paper-tabs>

    <iron-pages selected="{{selected}}">
      <div>Page 1</div>
      <div>Page 2</div>
      <div>Page 3</div>
    </iron-pages>

To use links in tabs, add `link` attribute to `paper-tab` and put an `<a>`
element in `paper-tab` with a `tabindex` of -1.

Example:

<pre><code>
&lt;style is="custom-style">
  .link {
    &#64;apply --layout-horizontal;
    &#64;apply --layout-center-center;
  }
&lt;/style>

&lt;paper-tabs selected="0">
  &lt;paper-tab link>
    &lt;a href="#link1" class="link" tabindex="-1">TAB ONE&lt;/a>
  &lt;/paper-tab>
  &lt;paper-tab link>
    &lt;a href="#link2" class="link" tabindex="-1">TAB TWO&lt;/a>
  &lt;/paper-tab>
  &lt;paper-tab link>
    &lt;a href="#link3" class="link" tabindex="-1">TAB THREE&lt;/a>
  &lt;/paper-tab>
&lt;/paper-tabs>
</code></pre>

### Styling

The following custom properties and mixins are available for styling:

Custom property | Description | Default
----------------|-------------|----------
`--paper-tabs-selection-bar-color` | Color for the selection bar | `--paper-yellow-a100`
`--paper-tabs-selection-bar` | Mixin applied to the selection bar | `{}`
`--paper-tabs` | Mixin applied to the tabs | `{}`
`--paper-tabs-content` | Mixin applied to the content container of tabs | `{}`
`--paper-tabs-container` | Mixin applied to the layout container of tabs | `{}`

@demo demo/index.html
*/Polymer({_template:html`
    <style>
      :host {
        @apply --layout;
        @apply --layout-center;

        height: 48px;
        font-size: 14px;
        font-weight: 500;
        overflow: hidden;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;

        /* NOTE: Both values are needed, since some phones require the value to be \`transparent\`. */
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        @apply --paper-tabs;
      }

      :host(:dir(rtl)) {
        @apply --layout-horizontal-reverse;
      }

      #tabsContainer {
        position: relative;
        height: 100%;
        white-space: nowrap;
        overflow: hidden;
        @apply --layout-flex-auto;
        @apply --paper-tabs-container;
      }

      #tabsContent {
        height: 100%;
        -moz-flex-basis: auto;
        -ms-flex-basis: auto;
        flex-basis: auto;
        @apply --paper-tabs-content;
      }

      #tabsContent.scrollable {
        position: absolute;
        white-space: nowrap;
      }

      #tabsContent:not(.scrollable),
      #tabsContent.scrollable.fit-container {
        @apply --layout-horizontal;
      }

      #tabsContent.scrollable.fit-container {
        min-width: 100%;
      }

      #tabsContent.scrollable.fit-container > ::slotted(*) {
        /* IE - prevent tabs from compressing when they should scroll. */
        -ms-flex: 1 0 auto;
        -webkit-flex: 1 0 auto;
        flex: 1 0 auto;
      }

      .hidden {
        display: none;
      }

      .not-visible {
        opacity: 0;
        cursor: default;
      }

      paper-icon-button {
        width: 48px;
        height: 48px;
        padding: 12px;
        margin: 0 4px;
      }

      #selectionBar {
        position: absolute;
        height: 0;
        bottom: 0;
        left: 0;
        right: 0;
        border-bottom: 2px solid var(--paper-tabs-selection-bar-color, var(--paper-yellow-a100));
          -webkit-transform: scale(0);
        transform: scale(0);
          -webkit-transform-origin: left center;
        transform-origin: left center;
          transition: -webkit-transform;
        transition: transform;

        @apply --paper-tabs-selection-bar;
      }

      #selectionBar.align-bottom {
        top: 0;
        bottom: auto;
      }

      #selectionBar.expand {
        transition-duration: 0.15s;
        transition-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
      }

      #selectionBar.contract {
        transition-duration: 0.18s;
        transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
      }

      #tabsContent > ::slotted(:not(#selectionBar)) {
        height: 100%;
      }
    </style>

    <paper-icon-button icon="paper-tabs:chevron-left" class$="[[_computeScrollButtonClass(_leftHidden, scrollable, hideScrollButtons)]]" on-up="_onScrollButtonUp" on-down="_onLeftScrollButtonDown" tabindex="-1"></paper-icon-button>

    <div id="tabsContainer" on-track="_scroll" on-down="_down">
      <div id="tabsContent" class$="[[_computeTabsContentClass(scrollable, fitContainer)]]">
        <div id="selectionBar" class$="[[_computeSelectionBarClass(noBar, alignBottom)]]" on-transitionend="_onBarTransitionEnd"></div>
        <slot></slot>
      </div>
    </div>

    <paper-icon-button icon="paper-tabs:chevron-right" class$="[[_computeScrollButtonClass(_rightHidden, scrollable, hideScrollButtons)]]" on-up="_onScrollButtonUp" on-down="_onRightScrollButtonDown" tabindex="-1"></paper-icon-button>
`,is:'paper-tabs',behaviors:[IronResizableBehavior,IronMenubarBehavior],properties:{/**
     * If true, ink ripple effect is disabled. When this property is changed,
     * all descendant `<paper-tab>` elements have their `noink` property
     * changed to the new value as well.
     */noink:{type:Boolean,value:false,observer:'_noinkChanged'},/**
     * If true, the bottom bar to indicate the selected tab will not be shown.
     */noBar:{type:Boolean,value:false},/**
     * If true, the slide effect for the bottom bar is disabled.
     */noSlide:{type:Boolean,value:false},/**
     * If true, tabs are scrollable and the tab width is based on the label
     * width.
     */scrollable:{type:Boolean,value:false},/**
     * If true, tabs expand to fit their container. This currently only applies
     * when scrollable is true.
     */fitContainer:{type:Boolean,value:false},/**
     * If true, dragging on the tabs to scroll is disabled.
     */disableDrag:{type:Boolean,value:false},/**
     * If true, scroll buttons (left/right arrow) will be hidden for scrollable
     * tabs.
     */hideScrollButtons:{type:Boolean,value:false},/**
     * If true, the tabs are aligned to bottom (the selection bar appears at the
     * top).
     */alignBottom:{type:Boolean,value:false},selectable:{type:String,value:'paper-tab'},/**
     * If true, tabs are automatically selected when focused using the
     * keyboard.
     */autoselect:{type:Boolean,value:false},/**
     * The delay (in milliseconds) between when the user stops interacting
     * with the tabs through the keyboard and when the focused item is
     * automatically selected (if `autoselect` is true).
     */autoselectDelay:{type:Number,value:0},_step:{type:Number,value:10},_holdDelay:{type:Number,value:1},_leftHidden:{type:Boolean,value:false},_rightHidden:{type:Boolean,value:false},_previousTab:{type:Object}},/** @private */hostAttributes:{role:'tablist'},listeners:{'iron-resize':'_onTabSizingChanged','iron-items-changed':'_onTabSizingChanged','iron-select':'_onIronSelect','iron-deselect':'_onIronDeselect'},/**
   * @type {!Object}
   */keyBindings:{'left:keyup right:keyup':'_onArrowKeyup'},created:function(){this._holdJob=null;this._pendingActivationItem=undefined;this._pendingActivationTimeout=undefined;this._bindDelayedActivationHandler=this._delayedActivationHandler.bind(this);this.addEventListener('blur',this._onBlurCapture.bind(this),true);},ready:function(){this.setScrollDirection('y',this.$.tabsContainer);},detached:function(){this._cancelPendingActivation();},_noinkChanged:function(noink){var childTabs=dom(this).querySelectorAll('paper-tab');childTabs.forEach(noink?this._setNoinkAttribute:this._removeNoinkAttribute);},_setNoinkAttribute:function(element){element.setAttribute('noink','');},_removeNoinkAttribute:function(element){element.removeAttribute('noink');},_computeScrollButtonClass:function(hideThisButton,scrollable,hideScrollButtons){if(!scrollable||hideScrollButtons){return 'hidden';}if(hideThisButton){return 'not-visible';}return '';},_computeTabsContentClass:function(scrollable,fitContainer){return scrollable?'scrollable'+(fitContainer?' fit-container':''):' fit-container';},_computeSelectionBarClass:function(noBar,alignBottom){if(noBar){return 'hidden';}else if(alignBottom){return 'align-bottom';}return '';},// TODO(cdata): Add `track` response back in when gesture lands.
_onTabSizingChanged:function(){this.debounce('_onTabSizingChanged',function(){this._scroll();this._tabChanged(this.selectedItem);},10);},_onIronSelect:function(event){this._tabChanged(event.detail.item,this._previousTab);this._previousTab=event.detail.item;this.cancelDebouncer('tab-changed');},_onIronDeselect:function(event){this.debounce('tab-changed',function(){this._tabChanged(null,this._previousTab);this._previousTab=null;// See polymer/polymer#1305
},1);},_activateHandler:function(){// Cancel item activations scheduled by keyboard events when any other
// action causes an item to be activated (e.g. clicks).
this._cancelPendingActivation();IronMenuBehaviorImpl._activateHandler.apply(this,arguments);},/**
   * Activates an item after a delay (in milliseconds).
   */_scheduleActivation:function(item,delay){this._pendingActivationItem=item;this._pendingActivationTimeout=this.async(this._bindDelayedActivationHandler,delay);},/**
   * Activates the last item given to `_scheduleActivation`.
   */_delayedActivationHandler:function(){var item=this._pendingActivationItem;this._pendingActivationItem=undefined;this._pendingActivationTimeout=undefined;item.fire(this.activateEvent,null,{bubbles:true,cancelable:true});},/**
   * Cancels a previously scheduled item activation made with
   * `_scheduleActivation`.
   */_cancelPendingActivation:function(){if(this._pendingActivationTimeout!==undefined){this.cancelAsync(this._pendingActivationTimeout);this._pendingActivationItem=undefined;this._pendingActivationTimeout=undefined;}},_onArrowKeyup:function(event){if(this.autoselect){this._scheduleActivation(this.focusedItem,this.autoselectDelay);}},_onBlurCapture:function(event){// Cancel a scheduled item activation (if any) when that item is
// blurred.
if(event.target===this._pendingActivationItem){this._cancelPendingActivation();}},get _tabContainerScrollSize(){return Math.max(0,this.$.tabsContainer.scrollWidth-this.$.tabsContainer.offsetWidth);},_scroll:function(e,detail){if(!this.scrollable){return;}var ddx=detail&&-detail.ddx||0;this._affectScroll(ddx);},_down:function(e){// go one beat async to defeat IronMenuBehavior
// autorefocus-on-no-selection timeout
this.async(function(){if(this._defaultFocusAsync){this.cancelAsync(this._defaultFocusAsync);this._defaultFocusAsync=null;}},1);},_affectScroll:function(dx){this.$.tabsContainer.scrollLeft+=dx;var scrollLeft=this.$.tabsContainer.scrollLeft;this._leftHidden=scrollLeft===0;this._rightHidden=scrollLeft===this._tabContainerScrollSize;},_onLeftScrollButtonDown:function(){this._scrollToLeft();this._holdJob=setInterval(this._scrollToLeft.bind(this),this._holdDelay);},_onRightScrollButtonDown:function(){this._scrollToRight();this._holdJob=setInterval(this._scrollToRight.bind(this),this._holdDelay);},_onScrollButtonUp:function(){clearInterval(this._holdJob);this._holdJob=null;},_scrollToLeft:function(){this._affectScroll(-this._step);},_scrollToRight:function(){this._affectScroll(this._step);},_tabChanged:function(tab,old){if(!tab){// Remove the bar without animation.
this.$.selectionBar.classList.remove('expand');this.$.selectionBar.classList.remove('contract');this._positionBar(0,0);return;}var r=this.$.tabsContent.getBoundingClientRect();var w=r.width;var tabRect=tab.getBoundingClientRect();var tabOffsetLeft=tabRect.left-r.left;this._pos={width:this._calcPercent(tabRect.width,w),left:this._calcPercent(tabOffsetLeft,w)};if(this.noSlide||old==null){// Position the bar without animation.
this.$.selectionBar.classList.remove('expand');this.$.selectionBar.classList.remove('contract');this._positionBar(this._pos.width,this._pos.left);return;}var oldRect=old.getBoundingClientRect();var oldIndex=this.items.indexOf(old);var index=this.items.indexOf(tab);var m=5;// bar animation: expand
this.$.selectionBar.classList.add('expand');var moveRight=oldIndex<index;var isRTL=this._isRTL;if(isRTL){moveRight=!moveRight;}if(moveRight){this._positionBar(this._calcPercent(tabRect.left+tabRect.width-oldRect.left,w)-m,this._left);}else {this._positionBar(this._calcPercent(oldRect.left+oldRect.width-tabRect.left,w)-m,this._calcPercent(tabOffsetLeft,w)+m);}if(this.scrollable){this._scrollToSelectedIfNeeded(tabRect.width,tabOffsetLeft);}},_scrollToSelectedIfNeeded:function(tabWidth,tabOffsetLeft){var l=tabOffsetLeft-this.$.tabsContainer.scrollLeft;if(l<0){this.$.tabsContainer.scrollLeft+=l;}else {l+=tabWidth-this.$.tabsContainer.offsetWidth;if(l>0){this.$.tabsContainer.scrollLeft+=l;}}},_calcPercent:function(w,w0){return 100*w/w0;},_positionBar:function(width,left){width=width||0;left=left||0;this._width=width;this._left=left;this.transform('translateX('+left+'%) scaleX('+width/100+')',this.$.selectionBar);},_onBarTransitionEnd:function(e){var cl=this.$.selectionBar.classList;// bar animation: expand -> contract
if(cl.contains('expand')){cl.remove('expand');cl.add('contract');this._positionBar(this._pos.width,this._pos.left);// bar animation done
}else if(cl.contains('contract')){cl.remove('contract');}}});

const cardConfigStruct=assign(baseLovelaceCardConfig,object({cards:array(any()),title:optional(string())}));let HuiStackCardEditor=_decorate([n("hui-stack-card-editor")],function(_initialize,_LitElement){class HuiStackCardEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiStackCardEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"lovelace",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_selectedCard",value(){return 0;}},{kind:"field",decorators:[t()],key:"_GUImode",value(){return true;}},{kind:"field",decorators:[t()],key:"_guiModeAvailable",value(){return true;}},{kind:"field",decorators:[i("hui-card-element-editor")],key:"_cardEditorEl",value:void 0},{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"method",key:"focusYamlEditor",value:function focusYamlEditor(){var _this$_cardEditorEl;(_this$_cardEditorEl=this._cardEditorEl)===null||_this$_cardEditorEl===void 0?void 0:_this$_cardEditorEl.focusYamlEditor();}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const selected=this._selectedCard;const numcards=this._config.cards.length;return $`
      <div class="card-config">
        <!-- <div class="toolbar">
          <paper-tabs
            .selected=${selected}
            scrollable
            @iron-activate=${this._handleSelectedCard}
            ><span id="span">Cards:</span>
            ${this._config.cards.map((_card,i)=>$` <paper-tab> ${i+1} </paper-tab> `)}
            <paper-tab>
              <ha-svg-icon id="icon" .path=${mdiPlus}></ha-svg-icon>
            </paper-tab>
          </paper-tabs>
        </div> -->

        <div id="editor">
          ${selected<numcards?$`
                <div id="card-options">
                  <!-- <mwc-button
                    @click=${this._toggleMode}
                    .disabled=${!this._guiModeAvailable}
                    class="gui-mode-button"
                  >
                    ${this.hass.localize(!this._cardEditorEl||this._GUImode?"ui.panel.lovelace.editor.edit_card.show_code_editor":"ui.panel.lovelace.editor.edit_card.show_visual_editor")}
                  </mwc-button> -->
                  <div class="arrow">
                    <ha-icon-button
                      .disabled=${selected===0}
                      .label=${this.hass.localize("ui.panel.lovelace.editor.edit_card.move_before")}
                      .path=${mdiArrowLeft}
                      @click=${this._handleMove}
                      .move=${-1}
                    ></ha-icon-button>

                    <ha-icon-button
                      .label=${this.hass.localize("ui.panel.lovelace.editor.edit_card.move_after")}
                      .path=${mdiArrowRight}
                      .disabled=${selected===numcards-1}
                      @click=${this._handleMove}
                      .move=${1}
                    ></ha-icon-button>
                  </div>
                  <mwc-button @click=${this._handleDeleteCardV2} id="button">
                    ${this.hass.localize("ui.common.change_card")}
                  </mwc-button>
                  <ha-icon-button
                    .label=${this.hass.localize("ui.panel.lovelace.editor.edit_card.delete")}
                    .path=${mdiDelete}
                    @click=${this._handleDeleteCard}
                  ></ha-icon-button>
                </div>

                <hui-card-element-editor
                  .hass=${this.hass}
                  .value=${this._config.cards[selected]}
                  .lovelace=${this.lovelace}
                  @config-changed=${this._handleConfigChanged}
                ></hui-card-element-editor>
              `:$`
                <hui-card-picker
                  .hass=${this.hass}
                  .lovelace=${this.lovelace}
                  @config-changed=${this._handleCardPicked}
                  .virginity=${false}
                ></hui-card-picker>
              `}
        </div>
      </div>
    `;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){window.addEventListener("handle-selected-card",ev=>{this._handleSelectedCardV2(ev.detail.cardId);});}},{kind:"method",key:"_handleSelectedCard",value:function _handleSelectedCard(ev){if(ev.target.id==="add-card"){this._selectedCard=this._config.cards.length;return;}this._setMode(true);this._guiModeAvailable=true;this._selectedCard=parseInt(ev.detail.selected,10);fireEvent(this,"card-selected",{cardId:this._selectedCard});}},{kind:"method",key:"_handleSelectedCardV2",value:function _handleSelectedCardV2(index){this._setMode(true);this._guiModeAvailable=true;this._selectedCard=parseInt(index,10);fireEvent(this,"card-selected",{cardId:this._selectedCard});}},{kind:"method",key:"_handleConfigChanged",value:function _handleConfigChanged(ev){ev.stopPropagation();if(!this._config){return;}const cards=[...this._config.cards];cards[this._selectedCard]=ev.detail.config;this._config={...this._config,cards};this._guiModeAvailable=ev.detail.guiModeAvailable;fireEvent(this,"config-changed",{config:this._config});}},{kind:"method",key:"_handleCardPicked",value:function _handleCardPicked(ev){ev.stopPropagation();if(!this._config){return;}const config=ev.detail.config;const cards=[...this._config.cards,config];this._config={...this._config,cards};fireEvent(this,"config-changed",{config:this._config});fireEvent(this,"card-selected",{cardId:this._selectedCard});}},{kind:"method",key:"_handleDeleteCard",value:function _handleDeleteCard(){if(!this._config){return;}const cards=[...this._config.cards];cards.splice(this._selectedCard,1);this._config={...this._config,cards};this._selectedCard=Math.max(0,this._selectedCard-1);fireEvent(this,"config-changed",{config:this._config});fireEvent(this,"card-selected",{cardId:this._selectedCard});}},{kind:"method",key:"_handleDeleteCardV2",value:function _handleDeleteCardV2(){if(!this._config){return;}const cards=[...this._config.cards];cards.splice(this._selectedCard,1);this._config={...this._config,cards};this._selectedCard=this._config.cards.length;fireEvent(this,"config-changed",{config:this._config});fireEvent(this,"card-selected",{cardId:this._selectedCard});}},{kind:"method",key:"_handleMove",value:function _handleMove(ev){if(!this._config){return;}const move=ev.currentTarget.move;const source=this._selectedCard;const target=source+move;const cards=[...this._config.cards];const card=cards.splice(this._selectedCard,1)[0];cards.splice(target,0,card);this._config={...this._config,cards};this._selectedCard=target;fireEvent(this,"config-changed",{config:this._config});fireEvent(this,"card-selected",{cardId:this._selectedCard});}},{kind:"method",key:"_handleGUIModeChanged",value:function _handleGUIModeChanged(ev){ev.stopPropagation();this._GUImode=ev.detail.guiMode;this._guiModeAvailable=ev.detail.guiModeAvailable;}},{kind:"method",key:"_toggleMode",value:function _toggleMode(){var _this$_cardEditorEl2;(_this$_cardEditorEl2=this._cardEditorEl)===null||_this$_cardEditorEl2===void 0?void 0:_this$_cardEditorEl2.toggleMode();}},{kind:"method",key:"_setMode",value:function _setMode(value){this._GUImode=value;if(this._cardEditorEl){this._cardEditorEl.GUImode=value;}}},{kind:"get",static:true,key:"styles",value:function styles(){return [configElementStyle,r`
        .toolbar {
          display: flex;
          --paper-tabs-selection-bar-color: var(--primary-color);
          --paper-tab-ink: var(--primary-color);
        }
        paper-tabs {
          margin-top: 10px;
          height: 36px;
          display: flex;
          font-size: 14px;
          flex-grow: 1;
        }
        #add-card {
          max-width: 32px;
          padding: 0;
        }
        #span {
          font-size: 1.3rem;
        }
        #card-options {
          display: flex;
          justify-content: flex-end;
          width: 100%;
        }
        #button {
          margin-top: 7px;
        }
        mwc-button[raised] {
          --mdc-theme-primary: white;
          --mdc-theme-on-primary: var(--mdc-theme-secondary);
        }
        mwc-button, /* don't forget about flat */
        mwc-button[outlined] {
          --mdc-theme-primary: var(--mdc-theme-secondary);
        }
        .arrow {
          position: absolute;
          top: 15px;
          left: 0px;
        }
        #icon {
          border-radius: 100%;
          background-color: var(--mdc-theme-secondary, #018786);
        }
        #editor {
          border: 1px solid var(--divider-editor);
          padding: 20px;
          margin-top: 2vh;
          border-radius: 1.5rem;
          border-width: 0.07rem;
          /* border-color: var(--primary-text-color); */
          position: relative;
        }
        @media only screen and (max-width: 850px) {
          #editor {
            max-width: 326px;
          }
        }

        .gui-mode-button {
          margin-right: auto;
        }
      `];}}]};},s);

export { HuiStackCardEditor };
