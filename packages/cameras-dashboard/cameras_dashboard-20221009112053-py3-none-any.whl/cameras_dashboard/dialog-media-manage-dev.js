const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { e, J as t, w as w$1, _ as _decorate, c as s, d as e$1, t as t$1, $ as $$1, eV as mdiUpload, f as fireEvent, r as r$1, n as n$1, at as mdiClose, dJ as mdiDelete, ax as haStyleDialog } from './main-dev.js';
import { A as d, a9 as showAlertDialog, ay as MediaClassBrowserSettings, J as showConfirmationDialog } from './auth-dev.js';
import { c } from './repeat-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';
import { i as isLocalMediaSourceContentId, u as uploadLocalMedia, r as removeLocalMedia, b as browseLocalMediaPlayer } from './dialog-media-player-browse-dev.js';
import './ha-circular-progress-dev.js';
import './ha-check-list-item-dev.js';
import './stop_propagation-dev.js';
import './brands-url-dev.js';
import './documentation-url-dev.js';
import './ha-entity-picker-dev.js';
import './ha-combo-box-dev.js';
import './compare-dev.js';
import './mwc-checkbox.css-dev.js';

const i=new WeakMap();

let h=0;const r=new Map(),n=new WeakSet(),a=()=>new Promise(t=>requestAnimationFrame(t)),g=(t,i)=>{const s=t-i;return 0===s?void 0:s;},w=(t,i)=>{const s=t/i;return 1===s?void 0:s;},A={left:(t,i)=>{const s=g(t,i);return {value:s,transform:s&&`translateX(${s}px)`};},top:(t,i)=>{const s=g(t,i);return {value:s,transform:s&&`translateY(${s}px)`};},width:(t,i)=>{const s=w(t,i);return {value:s,transform:s&&`scaleX(${s})`};},height:(t,i)=>{const s=w(t,i);return {value:s,transform:s&&`scaleY(${s})`};}},b={duration:333,easing:"ease-in-out"},j=["left","top","width","height","opacity","color","background"],x=new WeakMap();class S extends d{constructor(t$1){if(super(t$1),this.t=null,this.i=null,this.o=!0,this.shouldLog=!1,t$1.type===t.CHILD)throw Error("The `animate` directive must be used in attribute position.");this.createFinished();}createFinished(){var t;null===(t=this.resolveFinished)||void 0===t||t.call(this),this.finished=new Promise(t=>{this.h=t;});}async resolveFinished(){var t;null===(t=this.h)||void 0===t||t.call(this),this.h=void 0;}render(i){return w$1;}getController(){return i.get(this.l);}isDisabled(){var t;return this.options.disabled||(null===(t=this.getController())||void 0===t?void 0:t.disabled);}update(t,[i]){var s;const e=void 0===this.l;return e&&(this.l=null===(s=t.options)||void 0===s?void 0:s.host,this.l.addController(this),this.element=t.element,x.set(this.element,this)),this.optionsOrCallback=i,(e||"function"!=typeof i)&&this.u(i),this.render(i);}u(t){var i,s;t=null!=t?t:{};const e=this.getController();void 0!==e&&((t={...e.defaultOptions,...t}).keyframeOptions={...e.defaultOptions.keyframeOptions,...t.keyframeOptions}),null!==(i=(s=t).properties)&&void 0!==i||(s.properties=j),this.options=t;}v(){const t={},i=this.element.getBoundingClientRect(),s=getComputedStyle(this.element);return this.options.properties.forEach(e=>{var o;const h=null!==(o=i[e])&&void 0!==o?o:A[e]?void 0:s[e],r=Number(h);t[e]=isNaN(r)?h+"":r;}),t;}p(){let t,i=!0;return this.options.guard&&(t=this.options.guard(),i=((t,i)=>{if(Array.isArray(t)){if(Array.isArray(i)&&i.length===t.length&&t.every((t,s)=>t===i[s]))return !1;}else if(i===t)return !1;return !0;})(t,this.m)),this.o=this.l.hasUpdated&&!this.isDisabled()&&!this.isAnimating()&&i&&this.element.isConnected,this.o&&(this.m=Array.isArray(t)?Array.from(t):t),this.o;}hostUpdate(){var t;"function"==typeof this.optionsOrCallback&&this.u(this.optionsOrCallback()),this.p()&&(this.g=this.v(),this.t=null!==(t=this.t)&&void 0!==t?t:this.element.parentNode,this.i=this.element.nextSibling);}async hostUpdated(){if(!this.o||!this.element.isConnected||this.options.skipInitial&&!this.isHostRendered)return;let t;this.prepare(),await a;const i=this._(),s=this.A(this.options.keyframeOptions,i),e=this.v();if(void 0!==this.g){const{from:s,to:o}=this.O(this.g,e,i);this.log("measured",[this.g,e,s,o]),t=this.calculateKeyframes(s,o);}else {const s=r.get(this.options.inId);if(s){r.delete(this.options.inId);const{from:o,to:n}=this.O(s,e,i);t=this.calculateKeyframes(o,n),t=this.options.in?[{...this.options.in[0],...t[0]},...this.options.in.slice(1),t[1]]:t,h++,t.forEach(t=>t.zIndex=h);}else this.options.in&&(t=[...this.options.in,{}]);}this.animate(t,s);}resetStyles(){var t;void 0!==this.P&&(this.element.setAttribute("style",null!==(t=this.P)&&void 0!==t?t:""),this.P=void 0);}commitStyles(){var t,i;this.P=this.element.getAttribute("style"),null===(t=this.webAnimation)||void 0===t||t.commitStyles(),null===(i=this.webAnimation)||void 0===i||i.cancel();}reconnected(){}async disconnected(){var t;if(!this.o)return;if(void 0!==this.options.id&&r.set(this.options.id,this.g),void 0===this.options.out)return;if(this.prepare(),await a(),null===(t=this.t)||void 0===t?void 0:t.isConnected){const t=this.i&&this.i.parentNode===this.t?this.i:null;if(this.t.insertBefore(this.element,t),this.options.stabilizeOut){const t=this.v();this.log("stabilizing out");const i=this.g.left-t.left,s=this.g.top-t.top;!("static"===getComputedStyle(this.element).position)||0===i&&0===s||(this.element.style.position="relative"),0!==i&&(this.element.style.left=i+"px"),0!==s&&(this.element.style.top=s+"px");}}const i=this.A(this.options.keyframeOptions);await this.animate(this.options.out,i),this.element.remove();}prepare(){this.createFinished();}start(){var t,i;null===(i=(t=this.options).onStart)||void 0===i||i.call(t,this);}didFinish(t){var i,s;t&&(null===(s=(i=this.options).onComplete)||void 0===s||s.call(i,this)),this.g=void 0,this.animatingProperties=void 0,this.frames=void 0,this.resolveFinished();}_(){const t=[];for(let i=this.element.parentNode;i;i=null==i?void 0:i.parentNode){const s=x.get(i);s&&!s.isDisabled()&&s&&t.push(s);}return t;}get isHostRendered(){const t=n.has(this.l);return t||this.l.updateComplete.then(()=>{n.add(this.l);}),t;}A(t,i=this._()){const s={...b};return i.forEach(t=>Object.assign(s,t.options.keyframeOptions)),Object.assign(s,t),s;}O(t,i,s){t={...t},i={...i};const e=s.map(t=>t.animatingProperties).filter(t=>void 0!==t);let o=1,h=1;return void 0!==e&&(e.forEach(t=>{t.width&&(o/=t.width),t.height&&(h/=t.height);}),void 0!==t.left&&void 0!==i.left&&(t.left=o*t.left,i.left=o*i.left),void 0!==t.top&&void 0!==i.top&&(t.top=h*t.top,i.top=h*i.top)),{from:t,to:i};}calculateKeyframes(t,i,s=!1){var e;const o={},h={};let r=!1;const n={};for(const s in i){const a=t[s],l=i[s];if(s in A){const t=A[s];if(void 0===a||void 0===l)continue;const i=t(a,l);void 0!==i.transform&&(n[s]=i.value,r=!0,o.transform=`${null!==(e=o.transform)&&void 0!==e?e:""} ${i.transform}`);}else a!==l&&void 0!==a&&void 0!==l&&(r=!0,o[s]=a,h[s]=l);}return o.transformOrigin=h.transformOrigin=s?"center center":"top left",this.animatingProperties=n,r?[o,h]:void 0;}async animate(t,i=this.options.keyframeOptions){this.start(),this.frames=t;let s=!1;if(!this.isAnimating()&&!this.isDisabled()&&(this.options.onFrames&&(this.frames=t=this.options.onFrames(this),this.log("modified frames",t)),void 0!==t)){this.log("animate",[t,i]),s=!0,this.webAnimation=this.element.animate(t,i);const e=this.getController();null==e||e.add(this);try{await this.webAnimation.finished;}catch(t){}null==e||e.remove(this);}return this.didFinish(s),s;}isAnimating(){var t,i;return "running"===(null===(t=this.webAnimation)||void 0===t?void 0:t.playState)||(null===(i=this.webAnimation)||void 0===i?void 0:i.pending);}log(t,i){this.shouldLog&&!this.isDisabled()&&console.log(t,this.options.id,i);}}const $=e(S);

_decorate([n$1("ha-media-upload-button")],function(_initialize,_LitElement){class MediaUploadButton extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MediaUploadButton,d:[{kind:"field",decorators:[e$1({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e$1()],key:"currentItem",value:void 0},{kind:"field",decorators:[t$1()],key:"_uploading",value(){return 0;}},{kind:"method",key:"render",value:function render(){if(!this.currentItem||!isLocalMediaSourceContentId(this.currentItem.media_content_id||"")){return $$1``;}return $$1`
      <mwc-button
        .label=${this._uploading>0?this.hass.localize("ui.components.media-browser.file_management.uploading",{count:this._uploading}):this.hass.localize("ui.components.media-browser.file_management.add_media")}
        .disabled=${this._uploading>0}
        @click=${this._startUpload}
      >
        ${this._uploading>0?$$1`
              <ha-circular-progress
                size="tiny"
                active
                alt=""
                slot="icon"
              ></ha-circular-progress>
            `:$$1` <ha-svg-icon .path=${mdiUpload} slot="icon"></ha-svg-icon> `}
      </mwc-button>
    `;}},{kind:"method",key:"_startUpload",value:async function _startUpload(){if(this._uploading>0){return;}const input=document.createElement("input");input.type="file";input.accept="audio/*,video/*,image/*";input.multiple=true;input.addEventListener("change",async()=>{fireEvent(this,"uploading");const files=input.files;document.body.removeChild(input);const target=this.currentItem.media_content_id;for(let i=0;i<files.length;i++){this._uploading=files.length-i;try{// eslint-disable-next-line no-await-in-loop
await uploadLocalMedia(this.hass,target,files[i]);}catch(err){showAlertDialog(this,{text:this.hass.localize("ui.components.media-browser.file_management.upload_failed",{reason:err.message||err})});break;}}this._uploading=0;fireEvent(this,"media-refresh");},{once:true});// https://stackoverflow.com/questions/47664777/javascript-file-input-onchange-not-working-ios-safari-only
input.style.display="none";document.body.append(input);input.click();}},{kind:"field",static:true,key:"styles",value(){return r$1`
    mwc-button {
      /* We use icon + text to show disabled state */
      --mdc-button-disabled-ink-color: --mdc-theme-primary;
    }

    ha-svg-icon[slot="icon"],
    ha-circular-progress[slot="icon"] {
      vertical-align: middle;
    }
  `;}}]};},s);

_decorate([n$1("dialog-media-manage")],function(_initialize,_LitElement){class DialogMediaManage extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:DialogMediaManage,d:[{kind:"field",decorators:[e$1({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t$1()],key:"_currentItem",value:void 0},{kind:"field",decorators:[t$1()],key:"_params",value:void 0},{kind:"field",decorators:[t$1()],key:"_uploading",value(){return false;}},{kind:"field",decorators:[t$1()],key:"_deleting",value(){return false;}},{kind:"field",decorators:[t$1()],key:"_selected",value(){return new Set();}},{kind:"field",key:"_filesChanged",value(){return false;}},{kind:"method",key:"showDialog",value:function showDialog(params){this._params=params;this._refreshMedia();}},{kind:"method",key:"closeDialog",value:function closeDialog(){if(this._filesChanged&&this._params.onClose){this._params.onClose();}this._params=undefined;this._currentItem=undefined;this._uploading=false;this._deleting=false;this._filesChanged=false;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"method",key:"render",value:function render(){var _this$_currentItem,_this$_currentItem$ch,_this$_currentItem2,_this$_currentItem2$c;if(!this._params){return $$1``;}const children=((_this$_currentItem=this._currentItem)===null||_this$_currentItem===void 0?void 0:(_this$_currentItem$ch=_this$_currentItem.children)===null||_this$_currentItem$ch===void 0?void 0:_this$_currentItem$ch.filter(child=>!child.can_expand))||[];let fileIndex=0;return $$1`
      <ha-dialog
        open
        scrimClickAction
        escapeKeyAction
        hideActions
        flexContent
        .heading=${this._params.currentItem.title}
        @closed=${this.closeDialog}
      >
        <ha-header-bar slot="heading">
          ${this._selected.size===0?$$1`
                <span slot="title">
                  ${this.hass.localize("ui.components.media-browser.file_management.title")}
                </span>

                <ha-media-upload-button
                  .disabled=${this._deleting}
                  .hass=${this.hass}
                  .currentItem=${this._params.currentItem}
                  @uploading=${this._startUploading}
                  @media-refresh=${this._doneUploading}
                  slot="actionItems"
                ></ha-media-upload-button>
                ${this._uploading?"":$$1`
                      <ha-icon-button
                        .label=${this.hass.localize("ui.dialogs.generic.close")}
                        .path=${mdiClose}
                        dialogAction="close"
                        slot="actionItems"
                        class="header_button"
                        dir=${computeRTLDirection(this.hass)}
                      ></ha-icon-button>
                    `}
              `:$$1`
                <mwc-button
                  class="danger"
                  slot="title"
                  .disabled=${this._deleting}
                  .label=${this.hass.localize(`ui.components.media-browser.file_management.${this._deleting?"deleting":"delete"}`,{count:this._selected.size})}
                  @click=${this._handleDelete}
                >
                  <ha-svg-icon .path=${mdiDelete} slot="icon"></ha-svg-icon>
                </mwc-button>

                ${this._deleting?"":$$1`
                      <mwc-button
                        slot="actionItems"
                        .label=${`Deselect all`}
                        @click=${this._handleDeselectAll}
                      >
                        <ha-svg-icon
                          .path=${mdiClose}
                          slot="icon"
                        ></ha-svg-icon>
                      </mwc-button>
                    `}
              `}
        </ha-header-bar>
        ${!this._currentItem?$$1`
              <div class="refresh">
                <ha-circular-progress active></ha-circular-progress>
              </div>
            `:!children.length?$$1`<div class="no-items">
              <p>
                ${this.hass.localize("ui.components.media-browser.file_management.no_items")}
              </p>
              ${(_this$_currentItem2=this._currentItem)!==null&&_this$_currentItem2!==void 0&&(_this$_currentItem2$c=_this$_currentItem2.children)!==null&&_this$_currentItem2$c!==void 0&&_this$_currentItem2$c.length?$$1`<span class="folders"
                    >${this.hass.localize("ui.components.media-browser.file_management.folders_not_supported")}</span
                  >`:""}
            </div>`:$$1`
              <mwc-list multi @selected=${this._handleSelected}>
                ${c(children,item=>item.media_content_id,item=>{const icon=$$1`
                      <ha-svg-icon
                        slot="graphic"
                        .path=${MediaClassBrowserSettings[item.media_class==="directory"?item.children_media_class||item.media_class:item.media_class].icon}
                      ></ha-svg-icon>
                    `;return $$1`
                      <ha-check-list-item
                        ${$({id:item.media_content_id,skipInitial:true})}
                        graphic="icon"
                        .disabled=${this._uploading||this._deleting}
                        .selected=${this._selected.has(fileIndex++)}
                        .item=${item}
                      >
                        ${icon} ${item.title}
                      </ha-check-list-item>
                    `;})}
              </mwc-list>
            `}
      </ha-dialog>
    `;}},{kind:"method",key:"_handleSelected",value:function _handleSelected(ev){this._selected=ev.detail.index;}},{kind:"method",key:"_startUploading",value:function _startUploading(){this._uploading=true;this._filesChanged=true;}},{kind:"method",key:"_doneUploading",value:function _doneUploading(){this._uploading=false;this._refreshMedia();}},{kind:"method",key:"_handleDeselectAll",value:function _handleDeselectAll(){if(this._selected.size){this._selected=new Set();}}},{kind:"method",key:"_handleDelete",value:async function _handleDelete(){if(!(await showConfirmationDialog(this,{text:this.hass.localize("ui.components.media-browser.file_management.confirm_delete",{count:this._selected.size}),warning:true}))){return;}this._filesChanged=true;this._deleting=true;const toDelete=[];let fileIndex=0;this._currentItem.children.forEach(item=>{if(item.can_expand){return;}if(this._selected.has(fileIndex++)){toDelete.push(item);}});try{await Promise.all(toDelete.map(async item=>{await removeLocalMedia(this.hass,item.media_content_id);this._currentItem={...this._currentItem,children:this._currentItem.children.filter(i=>i!==item)};}));}finally{this._deleting=false;this._selected=new Set();}}},{kind:"method",key:"_refreshMedia",value:async function _refreshMedia(){this._selected=new Set();this._currentItem=undefined;this._currentItem=await browseLocalMediaPlayer(this.hass,this._params.currentItem.media_content_id);}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyleDialog,r$1`
        ha-dialog {
          --dialog-z-index: 8;
          --dialog-content-padding: 0;
        }

        @media (min-width: 800px) {
          ha-dialog {
            --mdc-dialog-max-width: 800px;
            --dialog-surface-position: fixed;
            --dialog-surface-top: 40px;
            --mdc-dialog-max-height: calc(100vh - 72px);
          }
        }

        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
          border-bottom: 1px solid var(--divider-color, rgba(0, 0, 0, 0.12));
        }

        ha-media-upload-button,
        mwc-button {
          --mdc-theme-primary: var(--mdc-theme-on-primary);
        }

        .danger {
          --mdc-theme-primary: var(--error-color);
        }

        ha-svg-icon[slot="icon"] {
          vertical-align: middle;
        }

        .refresh {
          display: flex;
          height: 200px;
          justify-content: center;
          align-items: center;
        }

        .no-items {
          text-align: center;
          padding: 16px;
        }
        .folders {
          color: var(--secondary-text-color);
          font-style: italic;
        }
      `];}}]};},s);
