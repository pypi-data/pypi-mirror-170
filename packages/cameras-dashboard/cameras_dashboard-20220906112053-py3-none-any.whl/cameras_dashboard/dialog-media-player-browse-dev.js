const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { N as _defineProperty, _ as _decorate, c as s, d as e, t, $, j as _get, k as _getPrototypeOf, b as memoizeOne, f as fireEvent, eQ as buttonLinkStyle, r, n, G as i, z as o, I as i$1, a5 as mdiPlay, dF as mdiPlus, eR as mdiArrowUpRight, Q as l, K as e$2, o as haStyle, eS as mdiFolderEdit, eq as mdiArrowLeft, at as mdiClose, ax as haStyleDialog } from './main-dev.js';
import { a as computeRTLDirection } from './ha-header-bar-dev.js';
import { aW as translationMetadata, a9 as showAlertDialog, ay as MediaClassBrowserSettings, aX as BROWSER_PLAYER, aY as browseMediaPlayer, Q as installResizeObserver, a5 as getSignedPath } from './auth-dev.js';
import { e as e$1 } from './ha-circular-progress-dev.js';
import { s as stopPropagation, d as debounce } from './stop_propagation-dev.js';
import { b as brandsUrl, e as extractDomainFromBrandUrl } from './brands-url-dev.js';
import { d as documentationUrl } from './documentation-url-dev.js';
import './ha-entity-picker-dev.js';
import { c as caseInsensitiveStringCompare } from './compare-dev.js';

const browseLocalMediaPlayer=(hass,mediaContentId)=>hass.callWS({type:"media_source/browse_media",media_content_id:mediaContentId});const isLocalMediaSourceContentId=mediaId=>mediaId.startsWith("media-source://media_source");const uploadLocalMedia=async(hass,media_content_id,file)=>{const fd=new FormData();fd.append("media_content_id",media_content_id);fd.append("file",file);const resp=await hass.fetchWithAuth("/api/media_source/local_source/upload",{method:"POST",body:fd});if(resp.status===413){throw new Error(`Uploaded file is too large (${file.name})`);}else if(resp.status!==200){throw new Error("Unknown error");}return resp.json();};const removeLocalMedia=async(hass,media_content_id)=>hass.callWS({type:"media_source/local_source/remove",media_content_id});

const TTS_MEDIA_SOURCE_PREFIX="media-source://tts/";const isTTSMediaSource=mediaContentId=>mediaContentId.startsWith(TTS_MEDIA_SOURCE_PREFIX);

class Storage{constructor(subscribe=true){_defineProperty(this,"_storage",{});_defineProperty(this,"_listeners",{});if(!subscribe){return;}window.addEventListener("storage",ev=>{if(ev.key&&this.hasKey(ev.key)){this._storage[ev.key]=ev.newValue?JSON.parse(ev.newValue):ev.newValue;if(this._listeners[ev.key]){this._listeners[ev.key].forEach(listener=>listener(ev.oldValue?JSON.parse(ev.oldValue):ev.oldValue,this._storage[ev.key]));}}});}addFromStorage(storageKey){if(!this._storage[storageKey]){const data=window.localStorage.getItem(storageKey);if(data){this._storage[storageKey]=JSON.parse(data);}}}subscribeChanges(storageKey,callback){if(this._listeners[storageKey]){this._listeners[storageKey].push(callback);}else {this._listeners[storageKey]=[callback];}return ()=>{this.unsubscribeChanges(storageKey,callback);};}unsubscribeChanges(storageKey,callback){if(!(storageKey in this._listeners)){return;}const index=this._listeners[storageKey].indexOf(callback);if(index!==-1){this._listeners[storageKey].splice(index,1);}}hasKey(storageKey){return storageKey in this._storage;}getValue(storageKey){return this._storage[storageKey];}setValue(storageKey,value){this._storage[storageKey]=value;try{window.localStorage.setItem(storageKey,JSON.stringify(value));}catch(err){// Safari in private mode doesn't allow localstorage
}}}const subscribeStorage=new Storage();const LocalStorage=(storageKey,property,subscribe=true,propertyOptions)=>clsElement=>{const storage=subscribe?subscribeStorage:new Storage(false);const key=String(clsElement.key);storageKey=storageKey||String(clsElement.key);const initVal=clsElement.initializer?clsElement.initializer():undefined;storage.addFromStorage(storageKey);const subscribeChanges=el=>storage.subscribeChanges(storageKey,oldValue=>{el.requestUpdate(clsElement.key,oldValue);});const getValue=()=>storage.hasKey(storageKey)?storage.getValue(storageKey):initVal;const setValue=(el,value)=>{let oldValue;if(property){oldValue=getValue();}storage.setValue(storageKey,value);if(property){el.requestUpdate(clsElement.key,oldValue);}};return {kind:"method",placement:"prototype",key:clsElement.key,descriptor:{set(value){setValue(this,value);},get(){return getValue();},enumerable:true,configurable:true},finisher(cls){if(property&&subscribe){const connectedCallback=cls.prototype.connectedCallback;const disconnectedCallback=cls.prototype.disconnectedCallback;cls.prototype.connectedCallback=function(){connectedCallback.call(this);this[`__unbsubLocalStorage${key}`]=subscribeChanges(this);};cls.prototype.disconnectedCallback=function(){disconnectedCallback.call(this);this[`__unbsubLocalStorage${key}`]();};}if(property){cls.createProperty(clsElement.key,{noAccessor:true,...propertyOptions});}}};};

const fetchCloudStatus=hass=>hass.callWS({type:"cloud/status"});const updateCloudPref=(hass,prefs)=>hass.callWS({type:"cloud/update_prefs",...prefs});

const getCloudTTSInfo=hass=>hass.callWS({type:"cloud/tts/info"});const getCloudTtsLanguages=info=>{const languages=[];if(!info){return languages;}const seen=new Set();for(const[lang]of info.languages){if(seen.has(lang)){continue;}seen.add(lang);let label=lang;if(lang in translationMetadata.translations){label=translationMetadata.translations[lang].nativeName;}else {const[langFamily,dialect]=lang.split("-");if(langFamily in translationMetadata.translations){label=`${translationMetadata.translations[langFamily].nativeName}`;if(langFamily.toLowerCase()!==dialect.toLowerCase()){label+=` (${dialect})`;}}}languages.push([lang,label]);}return languages.sort((a,b)=>caseInsensitiveStringCompare(a[1],b[1]));};const getCloudTtsSupportedGenders=(language,info,localize)=>{const genders=[];if(!info){return genders;}for(const[curLang,gender]of info.languages){if(curLang===language){genders.push([gender,localize(`ui.panel.media-browser.tts.gender_${gender}`)||localize(`ui.panel.config.cloud.account.tts.${gender}`)||gender]);}}return genders.sort((a,b)=>caseInsensitiveStringCompare(a[1],b[1]));};

_decorate([n("ha-browse-media-tts")],function(_initialize,_LitElement){class BrowseMediaTTS extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:BrowseMediaTTS,d:[{kind:"field",decorators:[e()],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"item",value:void 0},{kind:"field",decorators:[e()],key:"action",value:void 0},{kind:"field",decorators:[t()],key:"_cloudDefaultOptions",value:void 0},{kind:"field",decorators:[t()],key:"_cloudOptions",value:void 0},{kind:"field",decorators:[t()],key:"_cloudTTSInfo",value:void 0},{kind:"field",decorators:[LocalStorage("cloudTtsTryMessage",true,false)],key:"_message",value:void 0},{kind:"method",key:"render",value:function render(){var _this$hass$user;return $`<ha-card>
      <div class="card-content">
        <ha-textarea
          autogrow
          .label=${this.hass.localize("ui.components.media-browser.tts.message")}
          .value=${this._message||this.hass.localize("ui.components.media-browser.tts.example_message",{name:((_this$hass$user=this.hass.user)===null||_this$hass$user===void 0?void 0:_this$hass$user.name)||""})}
        >
        </ha-textarea>
        ${this._cloudDefaultOptions?this._renderCloudOptions():""}
      </div>
      <div class="card-actions">
        ${this._cloudDefaultOptions&&(this._cloudDefaultOptions[0]!==this._cloudOptions[0]||this._cloudDefaultOptions[1]!==this._cloudOptions[1])?$`
              <button class="link" @click=${this._storeDefaults}>
                ${this.hass.localize("ui.components.media-browser.tts.set_as_default")}
              </button>
            `:$`<span></span>`}

        <mwc-button @click=${this._ttsClicked}>
          ${this.hass.localize(`ui.components.media-browser.tts.action_${this.action}`)}
        </mwc-button>
      </div>
    </ha-card> `;}},{kind:"method",key:"_renderCloudOptions",value:function _renderCloudOptions(){if(!this._cloudTTSInfo||!this._cloudOptions){return "";}const languages=this.getLanguages(this._cloudTTSInfo);const selectedVoice=this._cloudOptions;const genders=this.getSupportedGenders(selectedVoice[0],this._cloudTTSInfo,this.hass.localize);return $`
      <div class="cloud-options">
        <ha-select
          fixedMenuPosition
          naturalMenuWidth
          .label=${this.hass.localize("ui.components.media-browser.tts.language")}
          .value=${selectedVoice[0]}
          @selected=${this._handleLanguageChange}
          @closed=${stopPropagation}
        >
          ${languages.map(([key,label])=>$`<mwc-list-item .value=${key}>${label}</mwc-list-item>`)}
        </ha-select>

        <ha-select
          fixedMenuPosition
          naturalMenuWidth
          .label=${this.hass.localize("ui.components.media-browser.tts.gender")}
          .value=${selectedVoice[1]}
          @selected=${this._handleGenderChange}
          @closed=${stopPropagation}
        >
          ${genders.map(([key,label])=>$`<mwc-list-item .value=${key}>${label}</mwc-list-item>`)}
        </ha-select>
      </div>
    `;}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){var _querySelector;_get(_getPrototypeOf(BrowseMediaTTS.prototype),"willUpdate",this).call(this,changedProps);if(changedProps.has("item")){if(this.item.media_content_id){const params=new URLSearchParams(this.item.media_content_id.split("?")[1]);const message=params.get("message");const language=params.get("language");const gender=params.get("gender");if(message){this._message=message;}if(language&&gender){this._cloudOptions=[language,gender];}}if(this.isCloudItem&&!this._cloudTTSInfo){getCloudTTSInfo(this.hass).then(info=>{this._cloudTTSInfo=info;});fetchCloudStatus(this.hass).then(status=>{if(status.logged_in){this._cloudDefaultOptions=status.prefs.tts_default_voice;if(!this._cloudOptions){this._cloudOptions={...this._cloudDefaultOptions};}}});}}if(changedProps.has("message")){return;}// Re-rendering can reset message because textarea content is newer than local storage.
// But we don't want to write every keystroke to local storage.
// So instead we just do it when we're going to render.
const message=(_querySelector=this.shadowRoot.querySelector("ha-textarea"))===null||_querySelector===void 0?void 0:_querySelector.value;if(message!==undefined&&message!==this._message){this._message=message;}}},{kind:"method",key:"_handleLanguageChange",value:async function _handleLanguageChange(ev){if(ev.target.value===this._cloudOptions[0]){return;}this._cloudOptions=[ev.target.value,this._cloudOptions[1]];}},{kind:"method",key:"_handleGenderChange",value:async function _handleGenderChange(ev){if(ev.target.value===this._cloudOptions[1]){return;}this._cloudOptions=[this._cloudOptions[0],ev.target.value];}},{kind:"field",key:"getLanguages",value(){return memoizeOne(getCloudTtsLanguages);}},{kind:"field",key:"getSupportedGenders",value(){return memoizeOne(getCloudTtsSupportedGenders);}},{kind:"get",key:"isCloudItem",value:function isCloudItem(){return this.item.media_content_id.startsWith("media-source://tts/cloud");}},{kind:"method",key:"_ttsClicked",value:async function _ttsClicked(){const message=this.shadowRoot.querySelector("ha-textarea").value;this._message=message;const item={...this.item};const query=new URLSearchParams();query.append("message",message);if(this._cloudOptions){query.append("language",this._cloudOptions[0]);query.append("gender",this._cloudOptions[1]);}item.media_content_id=`${item.media_content_id.split("?")[0]}?${query.toString()}`;item.can_play=true;item.title=message;fireEvent(this,"tts-picked",{item});}},{kind:"method",key:"_storeDefaults",value:async function _storeDefaults(){const oldDefaults=this._cloudDefaultOptions;this._cloudDefaultOptions=[...this._cloudOptions];try{await updateCloudPref(this.hass,{tts_default_voice:this._cloudDefaultOptions});}catch(err){this._cloudDefaultOptions=oldDefaults;showAlertDialog(this,{text:this.hass.localize("ui.components.media-browser.tts.faild_to_store_defaults",{error:err.message||err})});}}},{kind:"field",static:true,key:"styles",value(){return [buttonLinkStyle,r`
      :host {
        margin: 16px auto;
        padding: 0 8px;
        display: flex;
        flex-direction: column;
        max-width: 400px;
      }
      .cloud-options {
        margin-top: 16px;
        display: flex;
        justify-content: space-between;
      }
      .cloud-options ha-select {
        width: 48%;
      }
      ha-textarea {
        width: 100%;
      }
      button.link {
        color: var(--primary-color);
      }
      .card-actions {
        display: flex;
        justify-content: space-between;
      }
    `];}}]};},s);

_decorate([n("ha-media-player-browse")],function(_initialize,_LitElement){class HaMediaPlayerBrowse extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaMediaPlayerBrowse,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"entityId",value:void 0},{kind:"field",decorators:[e()],key:"action",value(){return "play";}},{kind:"field",decorators:[e({type:Boolean})],key:"dialog",value(){return false;}},{kind:"field",decorators:[e()],key:"navigateIds",value:void 0},{kind:"field",decorators:[e({type:Boolean,attribute:"narrow",reflect:true})],key:"_narrow",value(){return false;}},{kind:"field",decorators:[e({type:Boolean,attribute:"scroll",reflect:true})],key:"_scrolled",value(){return false;}},{kind:"field",decorators:[t()],key:"_error",value:void 0},{kind:"field",decorators:[t()],key:"_parentItem",value:void 0},{kind:"field",decorators:[t()],key:"_currentItem",value:void 0},{kind:"field",decorators:[i(".header")],key:"_header",value:void 0},{kind:"field",decorators:[i(".content")],key:"_content",value:void 0},{kind:"field",decorators:[e$1(".lazythumbnail")],key:"_thumbnails",value:void 0},{kind:"field",key:"_headerOffsetHeight",value(){return 0;}},{kind:"field",key:"_resizeObserver",value:void 0},{kind:"field",key:"_intersectionObserver",value:void 0},{kind:"method",key:"connectedCallback",value:// @ts-ignore
function connectedCallback(){_get(_getPrototypeOf(HaMediaPlayerBrowse.prototype),"connectedCallback",this).call(this);this.updateComplete.then(()=>this._attachResizeObserver());}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){if(this._resizeObserver){this._resizeObserver.disconnect();}if(this._intersectionObserver){this._intersectionObserver.disconnect();}}},{kind:"method",key:"refresh",value:async function refresh(){const currentId=this.navigateIds[this.navigateIds.length-1];try{this._currentItem=await this._fetchData(this.entityId,currentId.media_content_id,currentId.media_content_type);// Update the parent with latest item.
fireEvent(this,"media-browsed",{ids:this.navigateIds,current:this._currentItem});}catch(err){this._setError(err);}}},{kind:"method",key:"play",value:function play(){var _this$_currentItem;if((_this$_currentItem=this._currentItem)!==null&&_this$_currentItem!==void 0&&_this$_currentItem.can_play){this._runAction(this._currentItem);}}},{kind:"method",key:"render",value:function render(){if(this._error){return $`
        <div class="container">${this._renderError(this._error)}</div>
      `;}if(!this._currentItem){return $`<ha-circular-progress active></ha-circular-progress>`;}const currentItem=this._currentItem;const subtitle=this.hass.localize(`ui.components.media-browser.class.${currentItem.media_class}`);const children=currentItem.children||[];const mediaClass=MediaClassBrowserSettings[currentItem.media_class];const childrenMediaClass=currentItem.children_media_class?MediaClassBrowserSettings[currentItem.children_media_class]:MediaClassBrowserSettings.directory;return $`
              ${currentItem.can_play?$` <div
                      class="header ${o({"no-img":!currentItem.thumbnail,"no-dialog":!this.dialog})}"
                      @transitionend=${this._setHeaderHeight}
                    >
                      <div class="header-content">
                        ${currentItem.thumbnail?$`
                              <div
                                class="img"
                                style=${i$1({backgroundImage:currentItem.thumbnail?`url(${currentItem.thumbnail})`:"none"})}
                              >
                                ${this._narrow&&currentItem!==null&&currentItem!==void 0&&currentItem.can_play?$`
                                      <ha-fab
                                        mini
                                        .item=${currentItem}
                                        @click=${this._actionClicked}
                                      >
                                        <ha-svg-icon
                                          slot="icon"
                                          .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                                          .path=${this.action==="play"?mdiPlay:mdiPlus}
                                        ></ha-svg-icon>
                                        ${this.hass.localize(`ui.components.media-browser.${this.action}`)}
                                      </ha-fab>
                                    `:""}
                              </div>
                            `:$``}
                        <div class="header-info">
                          <div class="breadcrumb">
                            <h1 class="title">${currentItem.title}</h1>
                            ${subtitle?$` <h2 class="subtitle">${subtitle}</h2> `:""}
                          </div>
                          ${currentItem.can_play&&(!currentItem.thumbnail||!this._narrow)?$`
                                <mwc-button
                                  raised
                                  .item=${currentItem}
                                  @click=${this._actionClicked}
                                >
                                  <ha-svg-icon
                                    .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                                    .path=${this.action==="play"?mdiPlay:mdiPlus}
                                  ></ha-svg-icon>
                                  ${this.hass.localize(`ui.components.media-browser.${this.action}`)}
                                </mwc-button>
                              `:""}
                        </div>
                      </div>
                    </div>`:""}
          <div
            class="content"
            @scroll=${this._scroll}
            @touchmove=${this._scroll}
          >
            ${this._error?$`
                    <div class="container">
                      ${this._renderError(this._error)}
                    </div>
                  `:isTTSMediaSource(currentItem.media_content_id)?$`
                    <ha-browse-media-tts
                      .item=${currentItem}
                      .hass=${this.hass}
                      .action=${this.action}
                      @tts-picked=${this._ttsPicked}
                    ></ha-browse-media-tts>
                  `:!children.length&&!currentItem.not_shown?$`
                    <div class="container no-items">
                      ${currentItem.media_content_id==="media-source://media_source/local/."?$`
                            <div class="highlight-add-button">
                              <span>
                                <ha-svg-icon
                                  .path=${mdiArrowUpRight}
                                ></ha-svg-icon>
                              </span>
                              <span>
                                ${this.hass.localize("ui.components.media-browser.file_management.highlight_button")}
                              </span>
                            </div>
                          `:this.hass.localize("ui.components.media-browser.no_items")}
                    </div>
                  `:childrenMediaClass.layout==="grid"?$`
                    <div
                      class="children ${o({portrait:childrenMediaClass.thumbnail_ratio==="portrait"})}"
                    >
                      ${children.map(child=>$`
                          <div
                            class="child"
                            .item=${child}
                            @click=${this._childClicked}
                          >
                            <ha-card outlined>
                              <div class="thumbnail">
                                ${child.thumbnail?$`
                                      <div
                                        class="${["app","directory"].includes(child.media_class)?"centered-image":""} image lazythumbnail"
                                        data-src=${child.thumbnail}
                                      ></div>
                                    `:$`
                                      <div class="icon-holder image">
                                        <ha-svg-icon
                                          class="folder"
                                          .path=${MediaClassBrowserSettings[child.media_class==="directory"?child.children_media_class||child.media_class:child.media_class].icon}
                                        ></ha-svg-icon>
                                      </div>
                                    `}
                                ${child.can_play?$`
                                      <ha-icon-button
                                        class="play ${o({can_expand:child.can_expand})}"
                                        .item=${child}
                                        .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                                        .path=${this.action==="play"?mdiPlay:mdiPlus}
                                        @click=${this._actionClicked}
                                      ></ha-icon-button>
                                    `:""}
                              </div>
                              <div class="title">
                                ${child.title}
                                <paper-tooltip
                                  fitToVisibleBounds
                                  position="top"
                                  offset="4"
                                  >${child.title}</paper-tooltip
                                >
                              </div>
                            </ha-card>
                          </div>
                        `)}
                      ${currentItem.not_shown?$`
                            <div class="grid not-shown">
                              <div class="title">
                                ${this.hass.localize("ui.components.media-browser.not_shown",{count:currentItem.not_shown})}
                              </div>
                            </div>
                          `:""}
                    </div>
                  `:$`
                    <mwc-list>
                      ${children.map(child=>$`
                          <mwc-list-item
                            @click=${this._childClicked}
                            .item=${child}
                            .graphic=${mediaClass.show_list_images?"medium":"avatar"}
                            dir=${computeRTLDirection(this.hass)}
                          >
                            <div
                              class=${o({graphic:true,lazythumbnail:mediaClass.show_list_images===true})}
                              data-src=${l(mediaClass.show_list_images&&child.thumbnail?child.thumbnail:undefined)}
                              slot="graphic"
                            >
                              <ha-icon-button
                                class="play ${o({show:!mediaClass.show_list_images||!child.thumbnail})}"
                                .item=${child}
                                .label=${this.hass.localize(`ui.components.media-browser.${this.action}-media`)}
                                .path=${this.action==="play"?mdiPlay:mdiPlus}
                                @click=${this._actionClicked}
                              ></ha-icon-button>
                            </div>
                            <span class="title">${child.title}</span>
                          </mwc-list-item>
                          <li divider role="separator"></li>
                        `)}
                      ${currentItem.not_shown?$`
                            <mwc-list-item
                              noninteractive
                              class="not-shown"
                              .graphic=${mediaClass.show_list_images?"medium":"avatar"}
                              dir=${computeRTLDirection(this.hass)}
                            >
                              <span class="title">
                                ${this.hass.localize("ui.components.media-browser.not_shown",{count:currentItem.not_shown})}
                              </span>
                            </mwc-list-item>
                          `:""}
                    </mwc-list>
                  `}
          </div>
        </div>
      </div>
    `;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){this._measureCard();this._attachResizeObserver();}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.size>1||!changedProps.has("hass")){return true;}const oldHass=changedProps.get("hass");return oldHass===undefined||oldHass.localize!==this.hass.localize;}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){var _this$_content;_get(_getPrototypeOf(HaMediaPlayerBrowse.prototype),"willUpdate",this).call(this,changedProps);if(changedProps.has("entityId")){this._setError(undefined);}else if(!changedProps.has("navigateIds")){// Neither entity ID or navigateIDs changed, nothing to fetch
return;}this._setError(undefined);const oldNavigateIds=changedProps.get("navigateIds");const navigateIds=this.navigateIds;// We're navigating. Reset the shizzle.
(_this$_content=this._content)===null||_this$_content===void 0?void 0:_this$_content.scrollTo(0,0);this._scrolled=false;const oldCurrentItem=this._currentItem;const oldParentItem=this._parentItem;this._currentItem=undefined;this._parentItem=undefined;const currentId=navigateIds[navigateIds.length-1];const parentId=navigateIds.length>1?navigateIds[navigateIds.length-2]:undefined;let currentProm;let parentProm;// See if we can take loading shortcuts if navigating to parent or child
if(!changedProps.has("entityId")){if(// Check if we navigated to a child
oldNavigateIds&&navigateIds.length===oldNavigateIds.length+1&&oldNavigateIds.every((oldVal,idx)=>{const curVal=navigateIds[idx];return curVal.media_content_id===oldVal.media_content_id&&curVal.media_content_type===oldVal.media_content_type;})){parentProm=Promise.resolve(oldCurrentItem);}else if(// Check if we navigated to a parent
oldNavigateIds&&navigateIds.length===oldNavigateIds.length-1&&navigateIds.every((curVal,idx)=>{const oldVal=oldNavigateIds[idx];return curVal.media_content_id===oldVal.media_content_id&&curVal.media_content_type===oldVal.media_content_type;})){currentProm=Promise.resolve(oldParentItem);}}// Fetch current
if(!currentProm){currentProm=this._fetchData(this.entityId,currentId.media_content_id,currentId.media_content_type);}currentProm.then(item=>{this._currentItem=item;fireEvent(this,"media-browsed",{ids:navigateIds,current:item});},err=>{// When we change entity ID, we will first try to see if the new entity is
// able to resolve the new path. If that results in an error, browse the root.
const isNewEntityWithSamePath=oldNavigateIds&&changedProps.has("entityId")&&navigateIds.length===oldNavigateIds.length&&oldNavigateIds.every((oldItem,idx)=>navigateIds[idx].media_content_id===oldItem.media_content_id&&navigateIds[idx].media_content_type===oldItem.media_content_type);if(isNewEntityWithSamePath){fireEvent(this,"media-browsed",{ids:[{media_content_id:undefined,media_content_type:undefined}],replace:true});}else {this._setError(err);}});// Fetch parent
if(!parentProm&&parentId!==undefined){parentProm=this._fetchData(this.entityId,parentId.media_content_id,parentId.media_content_type);}if(parentProm){parentProm.then(parent=>{this._parentItem=parent;});}}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HaMediaPlayerBrowse.prototype),"updated",this).call(this,changedProps);if(changedProps.has("_scrolled")){this._animateHeaderHeight();}else if(changedProps.has("_currentItem")){this._setHeaderHeight();this._attachIntersectionObserver();}}},{kind:"method",key:"_actionClicked",value:function _actionClicked(ev){ev.stopPropagation();const item=ev.currentTarget.item;this._runAction(item);}},{kind:"method",key:"_runAction",value:function _runAction(item){fireEvent(this,"media-picked",{item,navigateIds:this.navigateIds});}},{kind:"method",key:"_ttsPicked",value:function _ttsPicked(ev){ev.stopPropagation();const navigateIds=this.navigateIds.slice(0,-1);navigateIds.push(ev.detail.item);fireEvent(this,"media-picked",{...ev.detail,navigateIds});}},{kind:"method",key:"_childClicked",value:async function _childClicked(ev){const target=ev.currentTarget;const item=target.item;if(!item){return;}if(!item.can_expand){this._runAction(item);return;}fireEvent(this,"media-browsed",{ids:[...this.navigateIds,item]});}},{kind:"method",key:"_fetchData",value:async function _fetchData(entityId,mediaContentId,mediaContentType){return entityId!==BROWSER_PLAYER?browseMediaPlayer(this.hass,entityId,mediaContentId,mediaContentType):browseLocalMediaPlayer(this.hass,mediaContentId);}},{kind:"method",key:"_measureCard",value:function _measureCard(){this._narrow=(this.dialog?window.innerWidth:this.offsetWidth)<450;}},{kind:"method",key:"_attachResizeObserver",value:async function _attachResizeObserver(){if(!this._resizeObserver){await installResizeObserver();this._resizeObserver=new ResizeObserver(debounce(()=>this._measureCard(),250,false));}this._resizeObserver.observe(this);}/**
   * Load thumbnails for images on demand as they become visible.
   */},{kind:"method",key:"_attachIntersectionObserver",value:async function _attachIntersectionObserver(){if(!("IntersectionObserver"in window)||!this._thumbnails){return;}if(!this._intersectionObserver){this._intersectionObserver=new IntersectionObserver(async(entries,observer)=>{await Promise.all(entries.map(async entry=>{if(!entry.isIntersecting){return;}const thumbnailCard=entry.target;let thumbnailUrl=thumbnailCard.dataset.src;if(!thumbnailUrl){return;}if(thumbnailUrl.startsWith("/")){// Thumbnails served by local API require authentication
const signedPath=await getSignedPath(this.hass,thumbnailUrl);thumbnailUrl=signedPath.path;}else if(thumbnailUrl.startsWith("https://brands.home-assistant.io")){var _this$hass$themes;// The backend is not aware of the theme used by the users,
// so we rewrite the URL to show a proper icon
thumbnailUrl=brandsUrl({domain:extractDomainFromBrandUrl(thumbnailUrl),type:"icon",useFallback:true,darkOptimized:(_this$hass$themes=this.hass.themes)===null||_this$hass$themes===void 0?void 0:_this$hass$themes.darkMode});}thumbnailCard.style.backgroundImage=`url(${thumbnailUrl})`;observer.unobserve(thumbnailCard);// loaded, so no need to observe anymore
}));});}const observer=this._intersectionObserver;for(const thumbnailCard of this._thumbnails){observer.observe(thumbnailCard);}}},{kind:"method",key:"_closeDialogAction",value:function _closeDialogAction(){fireEvent(this,"close-dialog");}},{kind:"method",key:"_setError",value:function _setError(error){if(!this.dialog){this._error=error;return;}if(!error){return;}this._closeDialogAction();showAlertDialog(this,{title:this.hass.localize("ui.components.media-browser.media_browsing_error"),text:this._renderError(error)});}},{kind:"method",key:"_renderError",value:function _renderError(err){if(err.message==="Media directory does not exist."){return $`
        <h2>
          ${this.hass.localize("ui.components.media-browser.no_local_media_found")}
        </h2>
        <p>
          ${this.hass.localize("ui.components.media-browser.no_media_folder")}
          <br />
          ${this.hass.localize("ui.components.media-browser.setup_local_help","documentation",$`<a
              href=${documentationUrl(this.hass)}
              target="_blank"
              rel="noreferrer"
              >${this.hass.localize("ui.components.media-browser.documentation")}</a
            >`)}
          <br />
          ${this.hass.localize("ui.components.media-browser.local_media_files")}
        </p>
      `;}return $`<span class="error">${err.message}</span>`;}},{kind:"method",key:"_setHeaderHeight",value:async function _setHeaderHeight(){await this.updateComplete;const header=this._header;const content=this._content;if(!header||!content){return;}this._headerOffsetHeight=header.offsetHeight;content.style.marginTop=`${this._headerOffsetHeight}px`;content.style.maxHeight=`calc(var(--media-browser-max-height, 100%) - ${this._headerOffsetHeight}px)`;}},{kind:"method",key:"_animateHeaderHeight",value:function _animateHeaderHeight(){let start;const animate=time=>{if(start===undefined){start=time;}const elapsed=time-start;this._setHeaderHeight();if(elapsed<400){requestAnimationFrame(animate);}};requestAnimationFrame(animate);}},{kind:"method",decorators:[e$2({passive:true})],key:"_scroll",value:function _scroll(ev){const content=ev.currentTarget;if(!this._scrolled&&content.scrollTop>this._headerOffsetHeight){this._scrolled=true;}else if(this._scrolled&&content.scrollTop<this._headerOffsetHeight){this._scrolled=false;}}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyle,r`
        :host {
          display: flex;
          flex-direction: column;
          position: relative;
        }

        ha-circular-progress {
          --mdc-theme-primary: var(--primary-color);
          display: flex;
          justify-content: center;
          margin: 40px;
        }

        .container {
          padding: 16px;
        }

        .no-items {
          padding-left: 32px;
        }

        .highlight-add-button {
          display: flex;
          flex-direction: row-reverse;
          margin-right: 48px;
        }

        .highlight-add-button ha-svg-icon {
          position: relative;
          top: -0.5em;
          margin-left: 8px;
        }

        .content {
          overflow-y: auto;
          box-sizing: border-box;
        }

        /* HEADER */

        .header {
          display: flex;
          justify-content: space-between;
          border-bottom: 1px solid var(--divider-color);
          background-color: var(--card-background-color);
          position: absolute;
          top: 0;
          right: 0;
          left: 0;
          z-index: 5;
          padding: 16px;
        }
        .header_button {
          position: relative;
          right: -8px;
        }
        .header-content {
          display: flex;
          flex-wrap: wrap;
          flex-grow: 1;
          align-items: flex-start;
        }
        .header-content .img {
          height: 175px;
          width: 175px;
          margin-right: 16px;
          background-size: cover;
          border-radius: 2px;
          transition: width 0.4s, height 0.4s;
        }
        .header-info {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          align-self: stretch;
          min-width: 0;
          flex: 1;
        }
        .header-info mwc-button {
          display: block;
          --mdc-theme-primary: var(--primary-color);
          padding-bottom: 16px;
        }
        .breadcrumb {
          display: flex;
          flex-direction: column;
          overflow: hidden;
          flex-grow: 1;
          padding-top: 16px;
        }
        .breadcrumb .title {
          font-size: 32px;
          line-height: 1.2;
          font-weight: bold;
          margin: 0;
          overflow: hidden;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          padding-right: 8px;
        }
        .breadcrumb .previous-title {
          font-size: 14px;
          padding-bottom: 8px;
          color: var(--secondary-text-color);
          overflow: hidden;
          text-overflow: ellipsis;
          cursor: pointer;
          --mdc-icon-size: 14px;
        }
        .breadcrumb .subtitle {
          font-size: 16px;
          overflow: hidden;
          text-overflow: ellipsis;
          margin-bottom: 0;
          transition: height 0.5s, margin 0.5s;
        }

        .not-shown {
          font-style: italic;
          color: var(--secondary-text-color);
        }

        .grid.not-shown {
          display: flex;
          align-items: center;
          text-align: center;
        }

        /* ============= CHILDREN ============= */

        mwc-list {
          --mdc-list-vertical-padding: 0;
          --mdc-list-item-graphic-margin: 0;
          --mdc-theme-text-icon-on-background: var(--secondary-text-color);
          margin-top: 10px;
        }

        mwc-list li:last-child {
          display: none;
        }

        mwc-list li[divider] {
          border-bottom-color: var(--divider-color);
        }

        .children {
          display: grid;
          grid-template-columns: repeat(
            auto-fit,
            minmax(var(--media-browse-item-size, 175px), 0.1fr)
          );
          grid-gap: 16px;
          padding: 16px;
        }

        :host([dialog]) .children {
          grid-template-columns: repeat(
            auto-fit,
            minmax(var(--media-browse-item-size, 175px), 0.33fr)
          );
        }

        .child {
          display: flex;
          flex-direction: column;
          cursor: pointer;
        }

        ha-card {
          position: relative;
          width: 100%;
          box-sizing: border-box;
        }

        .children ha-card .thumbnail {
          width: 100%;
          position: relative;
          box-sizing: border-box;
          transition: padding-bottom 0.1s ease-out;
          padding-bottom: 100%;
        }

        .portrait.children ha-card .thumbnail {
          padding-bottom: 150%;
        }

        ha-card .image {
          border-radius: 3px 3px 0 0;
        }

        .image {
          position: absolute;
          top: 0;
          right: 0;
          left: 0;
          bottom: 0;
          background-size: cover;
          background-repeat: no-repeat;
          background-position: center;
        }

        .centered-image {
          margin: 0 8px;
          background-size: contain;
        }

        .children ha-card .icon-holder {
          display: flex;
          justify-content: center;
          align-items: center;
        }

        .child .folder {
          color: var(--secondary-text-color);
          --mdc-icon-size: calc(var(--media-browse-item-size, 175px) * 0.4);
        }

        .child .play {
          position: absolute;
          transition: color 0.5s;
          border-radius: 50%;
          top: calc(50% - 50px);
          right: calc(50% - 35px);
          opacity: 0;
          transition: opacity 0.1s ease-out;
        }

        .child .play:not(.can_expand) {
          --mdc-icon-button-size: 70px;
          --mdc-icon-size: 48px;
        }

        ha-card:hover .play {
          opacity: 1;
        }

        ha-card:hover .play:not(.can_expand) {
          color: var(--primary-color);
        }

        ha-card:hover .play.can_expand {
          bottom: 8px;
        }

        .child .play.can_expand {
          background-color: rgba(var(--rgb-card-background-color), 0.5);
          top: auto;
          bottom: 0px;
          right: 8px;
          transition: bottom 0.1s ease-out, opacity 0.1s ease-out;
        }

        .child .play:hover {
          color: var(--primary-color);
        }

        ha-card:hover .lazythumbnail {
          opacity: 0.5;
        }

        .child .title {
          font-size: 16px;
          padding-top: 16px;
          padding-left: 2px;
          overflow: hidden;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 1;
          text-overflow: ellipsis;
        }

        .child ha-card .title {
          margin-bottom: 16px;
          padding-left: 16px;
        }

        mwc-list-item .graphic {
          background-size: contain;
          border-radius: 2px;
          display: flex;
          align-content: center;
          align-items: center;
          line-height: initial;
        }

        mwc-list-item .graphic .play {
          opacity: 0;
          transition: all 0.5s;
          background-color: rgba(var(--rgb-card-background-color), 0.5);
          border-radius: 50%;
          --mdc-icon-button-size: 40px;
        }

        mwc-list-item:hover .graphic .play {
          opacity: 1;
          color: var(--primary-text-color);
        }

        mwc-list-item .graphic .play.show {
          opacity: 1;
          background-color: transparent;
        }

        mwc-list-item .title {
          margin-left: 16px;
        }
        mwc-list-item[dir="rtl"] .title {
          margin-right: 16px;
          margin-left: 0;
        }

        /* ============= Narrow ============= */

        :host([narrow]) {
          padding: 0;
        }

        :host([narrow]) .media-source {
          padding: 0 24px;
        }

        :host([narrow]) .children {
          grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) !important;
        }

        :host([narrow]) .breadcrumb .title {
          font-size: 24px;
        }
        :host([narrow]) .header {
          padding: 0;
        }
        :host([narrow]) .header.no-dialog {
          display: block;
        }
        :host([narrow]) .header_button {
          position: absolute;
          top: 14px;
          right: 8px;
        }
        :host([narrow]) .header-content {
          flex-direction: column;
          flex-wrap: nowrap;
        }
        :host([narrow]) .header-content .img {
          height: auto;
          width: 100%;
          margin-right: 0;
          padding-bottom: 50%;
          margin-bottom: 8px;
          position: relative;
          background-position: center;
          border-radius: 0;
          transition: width 0.4s, height 0.4s, padding-bottom 0.4s;
        }
        ha-fab {
          position: absolute;
          --mdc-theme-secondary: var(--primary-color);
          bottom: -20px;
          right: 20px;
        }
        :host([narrow]) .header-info mwc-button {
          margin-top: 16px;
          margin-bottom: 8px;
        }
        :host([narrow]) .header-info {
          padding: 0 16px 8px;
        }

        /* ============= Scroll ============= */
        :host([scroll]) .breadcrumb .subtitle {
          height: 0;
          margin: 0;
        }
        :host([scroll]) .breadcrumb .title {
          -webkit-line-clamp: 1;
        }
        :host(:not([narrow])[scroll]) .header:not(.no-img) ha-icon-button {
          align-self: center;
        }
        :host([scroll]) .header-info mwc-button,
        .no-img .header-info mwc-button {
          padding-right: 4px;
        }
        :host([scroll][narrow]) .no-img .header-info mwc-button {
          padding-right: 16px;
        }
        :host([scroll]) .header-info {
          flex-direction: row;
        }
        :host([scroll]) .header-info mwc-button {
          align-self: center;
          margin-top: 0;
          margin-bottom: 0;
          padding-bottom: 0;
        }
        :host([scroll][narrow]) .no-img .header-info {
          flex-direction: row-reverse;
        }
        :host([scroll][narrow]) .header-info {
          padding: 20px 24px 10px 24px;
          align-items: center;
        }
        :host([scroll]) .header-content {
          align-items: flex-end;
          flex-direction: row;
        }
        :host([scroll]) .header-content .img {
          height: 75px;
          width: 75px;
        }
        :host([scroll]) .breadcrumb {
          padding-top: 0;
          align-self: center;
        }
        :host([scroll][narrow]) .header-content .img {
          height: 100px;
          width: 100px;
          padding-bottom: initial;
          margin-bottom: 0;
        }
        :host([scroll]) ha-fab {
          bottom: 0px;
          right: -24px;
          --mdc-fab-box-shadow: none;
          --mdc-theme-secondary: rgba(var(--rgb-primary-color), 0.5);
        }
      `];}}]};},s);

const showMediaManageDialog=(element,dialogParams)=>{fireEvent(element,"show-dialog",{dialogTag:"dialog-media-manage",dialogImport:()=>import('./dialog-media-manage-dev.js'),dialogParams});};

_decorate([n("ha-media-manage-button")],function(_initialize,_LitElement){class MediaManageButton extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MediaManageButton,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"currentItem",value:void 0},{kind:"field",decorators:[t()],key:"_uploading",value(){return 0;}},{kind:"method",key:"render",value:function render(){if(!this.currentItem||!isLocalMediaSourceContentId(this.currentItem.media_content_id||"")){return $``;}return $`
      <mwc-button
        .label=${this.hass.localize("ui.components.media-browser.file_management.manage")}
        @click=${this._manage}
      >
        <ha-svg-icon .path=${mdiFolderEdit} slot="icon"></ha-svg-icon>
      </mwc-button>
    `;}},{kind:"method",key:"_manage",value:function _manage(){showMediaManageDialog(this,{currentItem:this.currentItem,onClose:()=>fireEvent(this,"media-refresh")});}},{kind:"field",static:true,key:"styles",value(){return r`
    mwc-button {
      /* We use icon + text to show disabled state */
      --mdc-button-disabled-ink-color: --mdc-theme-primary;
    }

    ha-svg-icon[slot="icon"],
    ha-circular-progress[slot="icon"] {
      vertical-align: middle;
    }
  `;}}]};},s);

_decorate([n("dialog-media-player-browse")],function(_initialize,_LitElement){class DialogMediaPlayerBrowse extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:DialogMediaPlayerBrowse,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_currentItem",value:void 0},{kind:"field",decorators:[t()],key:"_navigateIds",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[i("ha-media-player-browse")],key:"_browser",value:void 0},{kind:"method",key:"showDialog",value:function showDialog(params){this._params=params;this._navigateIds=params.navigateIds||[{media_content_id:undefined,media_content_type:undefined}];}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._params=undefined;this._navigateIds=undefined;this._currentItem=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"method",key:"render",value:function render(){if(!this._params||!this._navigateIds){return $``;}return $`
      <ha-dialog
        open
        scrimClickAction
        escapeKeyAction
        hideActions
        flexContent
        .heading=${!this._currentItem?this.hass.localize("ui.components.media-browser.media-player-browser"):this._currentItem.title}
        @closed=${this.closeDialog}
      >
        <ha-header-bar slot="heading">
          ${this._navigateIds.length>1?$`
                <ha-icon-button
                  slot="navigationIcon"
                  .path=${mdiArrowLeft}
                  @click=${this._goBack}
                ></ha-icon-button>
              `:""}
          <span slot="title">
            ${!this._currentItem?this.hass.localize("ui.components.media-browser.media-player-browser"):this._currentItem.title}
          </span>

          <ha-media-manage-button
            slot="actionItems"
            .hass=${this.hass}
            .currentItem=${this._currentItem}
            @media-refresh=${this._refreshMedia}
          ></ha-media-manage-button>
          <ha-icon-button
            .label=${this.hass.localize("ui.dialogs.generic.close")}
            .path=${mdiClose}
            dialogAction="close"
            slot="actionItems"
            class="header_button"
            dir=${computeRTLDirection(this.hass)}
          ></ha-icon-button>
        </ha-header-bar>
        <ha-media-player-browse
          dialog
          .hass=${this.hass}
          .entityId=${this._params.entityId}
          .navigateIds=${this._navigateIds}
          .action=${this._action}
          @close-dialog=${this.closeDialog}
          @media-picked=${this._mediaPicked}
          @media-browsed=${this._mediaBrowsed}
        ></ha-media-player-browse>
      </ha-dialog>
    `;}},{kind:"method",key:"_goBack",value:function _goBack(){var _this$_navigateIds;this._navigateIds=(_this$_navigateIds=this._navigateIds)===null||_this$_navigateIds===void 0?void 0:_this$_navigateIds.slice(0,-1);this._currentItem=undefined;}},{kind:"method",key:"_mediaBrowsed",value:function _mediaBrowsed(ev){this._navigateIds=ev.detail.ids;this._currentItem=ev.detail.current;}},{kind:"method",key:"_mediaPicked",value:function _mediaPicked(ev){this._params.mediaPickedCallback(ev.detail);if(this._action!=="play"){this.closeDialog();}}},{kind:"get",key:"_action",value:function _action(){return this._params.action||"play";}},{kind:"method",key:"_refreshMedia",value:function _refreshMedia(){this._browser.refresh();}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyleDialog,r`
        ha-dialog {
          --dialog-z-index: 8;
          --dialog-content-padding: 0;
        }

        ha-media-player-browse {
          --media-browser-max-height: calc(100vh - 65px);
        }

        @media (min-width: 800px) {
          ha-dialog {
            --mdc-dialog-max-width: 800px;
            --dialog-surface-position: fixed;
            --dialog-surface-top: 40px;
            --mdc-dialog-max-height: calc(100vh - 72px);
          }
          ha-media-player-browse {
            position: initial;
            --media-browser-max-height: 100vh - 137px;
            width: 700px;
          }
        }

        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
          border-bottom: 1px solid var(--divider-color, rgba(0, 0, 0, 0.12));
        }

        ha-media-manage-button {
          --mdc-theme-primary: var(--mdc-theme-on-primary);
        }
      `];}}]};},s);

var dialogMediaPlayerBrowse = /*#__PURE__*/Object.freeze({
  __proto__: null
});

export { browseLocalMediaPlayer as b, dialogMediaPlayerBrowse as d, isLocalMediaSourceContentId as i, removeLocalMedia as r, uploadLocalMedia as u };
