const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, f as fireEvent, r, n, o as haStyle, at as mdiClose, dU as mdiTune, aw as replaceDialog, ax as haStyleDialog } from './main-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import { d } from './ha-more-info-dialog-dev.js';
import { d as dynamicElement } from './dynamic-element-directive-dev.js';
import { e as computeDomain, C as domainIcon, a8 as updateEntityRegistryEntry, a9 as showAlertDialog, J as showConfirmationDialog, a7 as removeEntityRegistryEntry, j as computeStateName, aa as getExtendedEntityRegistryEntry } from './auth-dev.js';
import { s as subscribeDeviceRegistry, a as subscribeAreaRegistry, u as updateDeviceRegistryEntry } from './device_registry-dev.js';
import { g as getConfigEntries } from './config_entries-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import { d as documentationUrl } from './documentation-url-dev.js';
import './stop_propagation-dev.js';
import './ha-area-picker-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './compare-dev.js';
import './ha-combo-box-dev.js';

const findRelated=(hass,itemType,itemId)=>hass.callWS({type:"search/related",item_type:itemType,item_id:itemId});

_decorate([n("ha-related-items")],function(_initialize,_SubscribeMixin){class HaRelatedItems extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HaRelatedItems,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"itemType",value:void 0},{kind:"field",decorators:[e()],key:"itemId",value:void 0},{kind:"field",decorators:[t()],key:"_entries",value:void 0},{kind:"field",decorators:[t()],key:"_devices",value:void 0},{kind:"field",decorators:[t()],key:"_areas",value:void 0},{kind:"field",decorators:[t()],key:"_related",value:void 0},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){return [subscribeDeviceRegistry(this.hass.connection,devices=>{this._devices=devices;}),subscribeAreaRegistry(this.hass.connection,areas=>{this._areas=areas;})];}},{kind:"method",key:"firstUpdated",value:function firstUpdated(changedProps){_get(_getPrototypeOf(HaRelatedItems.prototype),"firstUpdated",this).call(this,changedProps);getConfigEntries(this.hass).then(configEntries=>{this._entries=configEntries;});this.hass.loadBackendTranslation("title");}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HaRelatedItems.prototype),"updated",this).call(this,changedProps);if((changedProps.has("itemId")||changedProps.has("itemType"))&&this.itemId&&this.itemType){this._findRelated();}}},{kind:"method",key:"render",value:function render(){if(!this._related){return $``;}if(Object.keys(this._related).length===0){return $`
        ${this.hass.localize("ui.components.related-items.no_related_found")}
      `;}return $`
      ${this._related.config_entry&&this._entries?this._related.config_entry.map(relatedConfigEntryId=>{const entry=this._entries.find(configEntry=>configEntry.entry_id===relatedConfigEntryId);if(!entry){return "";}return $`
              <h3>
                ${this.hass.localize("ui.components.related-items.integration")}:
              </h3>
              <a
                href=${`/config/integrations#config_entry=${relatedConfigEntryId}`}
                @click=${this._navigateAwayClose}
              >
                ${this.hass.localize(`component.${entry.domain}.title`)}:
                ${entry.title}
              </a>
            `;}):""}
      ${this._related.device&&this._devices?this._related.device.map(relatedDeviceId=>{const device=this._devices.find(dev=>dev.id===relatedDeviceId);if(!device){return "";}return $`
              <h3>
                ${this.hass.localize("ui.components.related-items.device")}:
              </h3>
              <a
                href="/config/devices/device/${relatedDeviceId}"
                @click=${this._navigateAwayClose}
              >
                ${device.name_by_user||device.name}
              </a>
            `;}):""}
      ${this._related.area&&this._areas?this._related.area.map(relatedAreaId=>{const area=this._areas.find(ar=>ar.area_id===relatedAreaId);if(!area){return "";}return $`
              <h3>
                ${this.hass.localize("ui.components.related-items.area")}:
              </h3>
              <a
                href="/config/areas/area/${relatedAreaId}"
                @click=${this._navigateAwayClose}
              >
                ${area.name}
              </a>
            `;}):""}
      ${this._related.entity?$`
            <h3>
              ${this.hass.localize("ui.components.related-items.entity")}:
            </h3>
            <ul>
              ${this._related.entity.map(entityId=>{const entity=this.hass.states[entityId];if(!entity){return "";}return $`
                  <li>
                    <button
                      @click=${this._openMoreInfo}
                      .entityId=${entityId}
                      class="link"
                    >
                      ${entity.attributes.friendly_name||entityId}
                    </button>
                  </li>
                `;})}
            </ul>
          `:""}
      ${this._related.group?$`
            <h3>${this.hass.localize("ui.components.related-items.group")}:</h3>
            <ul>
              ${this._related.group.map(groupId=>{const group=this.hass.states[groupId];if(!group){return "";}return $`
                  <li>
                    <button
                      class="link"
                      @click=${this._openMoreInfo}
                      .entityId=${groupId}
                    >
                      ${group.attributes.friendly_name||group.entity_id}
                    </button>
                  </li>
                `;})}
            </ul>
          `:""}
      ${this._related.scene?$`
            <h3>${this.hass.localize("ui.components.related-items.scene")}:</h3>
            <ul>
              ${this._related.scene.map(sceneId=>{const scene=this.hass.states[sceneId];if(!scene){return "";}return $`
                  <li>
                    <button
                      class="link"
                      @click=${this._openMoreInfo}
                      .entityId=${sceneId}
                    >
                      ${scene.attributes.friendly_name||scene.entity_id}
                    </button>
                  </li>
                `;})}
            </ul>
          `:""}
      ${this._related.automation?$`
            <h3>
              ${this.hass.localize("ui.components.related-items.automation")}:
            </h3>
            <ul>
              ${this._related.automation.map(automationId=>{const automation=this.hass.states[automationId];if(!automation){return "";}return $`
                  <li>
                    <button
                      class="link"
                      @click=${this._openMoreInfo}
                      .entityId=${automationId}
                    >
                      ${automation.attributes.friendly_name||automation.entity_id}
                    </button>
                  </li>
                `;})}
            </ul>
          `:""}
      ${this._related.script?$`
            <h3>
              ${this.hass.localize("ui.components.related-items.script")}:
            </h3>
            <ul>
              ${this._related.script.map(scriptId=>{const script=this.hass.states[scriptId];if(!script){return "";}return $`
                  <li>
                    <button
                      class="link"
                      @click=${this._openMoreInfo}
                      .entityId=${scriptId}
                    >
                      ${script.attributes.friendly_name||script.entity_id}
                    </button>
                  </li>
                `;})}
            </ul>
          `:""}
    `;}},{kind:"method",key:"_navigateAwayClose",value:async function _navigateAwayClose(){// allow new page to open before closing dialog
await new Promise(resolve=>setTimeout(resolve,0));fireEvent(this,"close-dialog");}},{kind:"method",key:"_findRelated",value:async function _findRelated(){this._related=await findRelated(this.hass,this.itemType,this.itemId);await this.updateComplete;fireEvent(this,"iron-resize");}},{kind:"method",key:"_openMoreInfo",value:function _openMoreInfo(ev){const entityId=ev.target.entityId;fireEvent(this,"hass-more-info",{entityId});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      a {
        color: var(--accent-color);
      }
      button.link {
        color: var(--accent-color);
        text-align: left;
        cursor: pointer;
        background: none;
        border-width: initial;
        border-style: none;
        border-color: initial;
        border-image: initial;
        padding: 0px;
        font: inherit;
        text-decoration: underline;
      }
      h3 {
        font-family: var(--paper-font-title_-_font-family);
        -webkit-font-smoothing: var(
          --paper-font-title_-_-webkit-font-smoothing
        );
        font-size: var(--paper-font-title_-_font-size);
        font-weight: var(--paper-font-headline-_font-weight);
        letter-spacing: var(--paper-font-title_-_letter-spacing);
        line-height: var(--paper-font-title_-_line-height);
        opacity: var(--dark-primary-opacity);
      }
    `;}}]};},SubscribeMixin(s));

/** Platforms that have a settings tab. */const PLATFORMS_WITH_SETTINGS_TAB={input_number:"entity-settings-helper-tab",input_select:"entity-settings-helper-tab",input_text:"entity-settings-helper-tab",input_boolean:"entity-settings-helper-tab",input_datetime:"entity-settings-helper-tab",counter:"entity-settings-helper-tab",timer:"entity-settings-helper-tab",input_button:"entity-settings-helper-tab"};

const loadDeviceRegistryDetailDialog=()=>import('./dialog-device-registry-detail-dev.js');const showDeviceRegistryDetailDialog=(element,deviceRegistryDetailParams)=>{fireEvent(element,"show-dialog",{dialogTag:"dialog-device-registry-detail",dialogImport:loadDeviceRegistryDetailDialog,dialogParams:deviceRegistryDetailParams});};

const OVERRIDE_DEVICE_CLASSES={cover:["window","door","garage","gate"],binary_sensor:["window","door","garage_door","opening"]};_decorate([n("entity-registry-settings")],function(_initialize,_SubscribeMixin){class EntityRegistrySettings extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:EntityRegistrySettings,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"entry",value:void 0},{kind:"field",decorators:[t()],key:"_name",value:void 0},{kind:"field",decorators:[t()],key:"_icon",value:void 0},{kind:"field",decorators:[t()],key:"_entityId",value:void 0},{kind:"field",decorators:[t()],key:"_deviceClass",value:void 0},{kind:"field",decorators:[t()],key:"_areaId",value:void 0},{kind:"field",decorators:[t()],key:"_disabledBy",value:void 0},{kind:"field",key:"_deviceLookup",value:void 0},{kind:"field",decorators:[t()],key:"_device",value:void 0},{kind:"field",decorators:[t()],key:"_error",value:void 0},{kind:"field",decorators:[t()],key:"_submitting",value:void 0},{kind:"field",key:"_origEntityId",value:void 0},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){return [subscribeDeviceRegistry(this.hass.connection,devices=>{this._deviceLookup={};for(const device of devices){this._deviceLookup[device.id]=device;}if(this.entry.device_id){this._device=this._deviceLookup[this.entry.device_id];}})];}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(EntityRegistrySettings.prototype),"updated",this).call(this,changedProperties);if(changedProperties.has("entry")){this._error=undefined;this._name=this.entry.name||"";this._icon=this.entry.icon||"";this._deviceClass=this.entry.device_class||this.entry.original_device_class;this._origEntityId=this.entry.entity_id;this._areaId=this.entry.area_id;this._entityId=this.entry.entity_id;this._disabledBy=this.entry.disabled_by;this._device=this.entry.device_id&&this._deviceLookup?this._deviceLookup[this.entry.device_id]:undefined;}}},{kind:"method",key:"render",value:function render(){var _this$_device,_OVERRIDE_DEVICE_CLAS,_this$_device2,_this$_device3;if(this.entry.entity_id!==this._origEntityId){return $``;}const stateObj=this.hass.states[this.entry.entity_id];const domain=computeDomain(this.entry.entity_id);const invalidDomainUpdate=computeDomain(this._entityId.trim())!==domain;return $`
      ${!stateObj?$`
            <div class="container warning">
              ${this.hass.localize("ui.dialogs.entity_registry.editor.unavailable")}
              ${(_this$_device=this._device)!==null&&_this$_device!==void 0&&_this$_device.disabled_by?$`<br />${this.hass.localize("ui.dialogs.entity_registry.editor.device_disabled")}<br /><mwc-button @click=${this._openDeviceSettings}>
                      ${this.hass.localize("ui.dialogs.entity_registry.editor.open_device_settings")}
                    </mwc-button>`:""}
            </div>
          `:""}
      ${this._error?$`<ha-alert alert-type="error">${this._error}</ha-alert>`:""}
      <div class="form container">
        <ha-textfield
          .value=${this._name}
          .label=${this.hass.localize("ui.dialogs.entity_registry.editor.name")}
          .invalid=${invalidDomainUpdate}
          .disabled=${this._submitting}
          .placeholder=${this.entry.original_name}
          @input=${this._nameChanged}
        ></ha-textfield>
        <ha-icon-picker
          .value=${this._icon}
          @value-changed=${this._iconChanged}
          .label=${this.hass.localize("ui.dialogs.entity_registry.editor.icon")}
          .placeholder=${this.entry.original_icon||(stateObj===null||stateObj===void 0?void 0:stateObj.attributes.icon)}
          .fallbackPath=${!this._icon&&!(stateObj!==null&&stateObj!==void 0&&stateObj.attributes.icon)&&stateObj?domainIcon(computeDomain(stateObj.entity_id),stateObj):undefined}
          .disabled=${this._submitting}
        ></ha-icon-picker>
        ${(_OVERRIDE_DEVICE_CLAS=OVERRIDE_DEVICE_CLASSES[domain])!==null&&_OVERRIDE_DEVICE_CLAS!==void 0&&_OVERRIDE_DEVICE_CLAS.includes(this._deviceClass)||domain==="cover"&&this.entry.original_device_class===null?$`<ha-select
              .label=${this.hass.localize("ui.dialogs.entity_registry.editor.device_class")}
              .value=${this._deviceClass}
              @selected=${this._deviceClassChanged}
            >
              ${OVERRIDE_DEVICE_CLASSES[domain].map(deviceClass=>$`
                  <mwc-list-item .value=${deviceClass}>
                    ${this.hass.localize(`ui.dialogs.entity_registry.editor.device_classes.${domain}.${deviceClass}`)}
                  </mwc-list-item>
                `)}
            </ha-select>`:""}
        <ha-textfield
          error-message="Domain needs to stay the same"
          .value=${this._entityId}
          .label=${this.hass.localize("ui.dialogs.entity_registry.editor.entity_id")}
          .invalid=${invalidDomainUpdate}
          .disabled=${this._submitting}
          @input=${this._entityIdChanged}
        ></ha-textfield>
        ${!this.entry.device_id?$`<ha-area-picker
              .hass=${this.hass}
              .value=${this._areaId}
              @value-changed=${this._areaPicked}
            ></ha-area-picker>`:""}
        <div class="row">
          <ha-switch
            .checked=${!this._disabledBy}
            .disabled=${(_this$_device2=this._device)===null||_this$_device2===void 0?void 0:_this$_device2.disabled_by}
            @change=${this._disabledByChanged}
          >
          </ha-switch>
          <div>
            <div>
              ${this.hass.localize("ui.dialogs.entity_registry.editor.enabled_label")}
            </div>
            <div class="secondary">
              ${this._disabledBy&&this._disabledBy!=="user"?this.hass.localize("ui.dialogs.entity_registry.editor.enabled_cause","cause",this.hass.localize(`config_entry.disabled_by.${this._disabledBy}`)):""}
              ${this.hass.localize("ui.dialogs.entity_registry.editor.enabled_description")}
              <br />${this.hass.localize("ui.dialogs.entity_registry.editor.note")}
            </div>
          </div>
        </div>

        ${this.entry.device_id?$`<ha-expansion-panel
              .header=${this.hass.localize("ui.dialogs.entity_registry.editor.advanced")}
              outlined
            >
              <p>
                ${this.hass.localize("ui.dialogs.entity_registry.editor.area_note")}
              </p>
              ${this._areaId?$`<mwc-button @click=${this._clearArea}
                    >${this.hass.localize("ui.dialogs.entity_registry.editor.follow_device_area")}</mwc-button
                  >`:this._device?$`<mwc-button @click=${this._openDeviceSettings}
                    >${this.hass.localize("ui.dialogs.entity_registry.editor.change_device_area")}</mwc-button
                  >`:""}
              <ha-area-picker
                .hass=${this.hass}
                .value=${this._areaId}
                .placeholder=${(_this$_device3=this._device)===null||_this$_device3===void 0?void 0:_this$_device3.area_id}
                .label=${this.hass.localize("ui.dialogs.entity_registry.editor.area")}
                @value-changed=${this._areaPicked}
              ></ha-area-picker
            ></ha-expansion-panel>`:""}
      </div>
      <div class="buttons">
        <mwc-button
          class="warning"
          @click=${this._confirmDeleteEntry}
          .disabled=${this._submitting||!(stateObj&&stateObj.attributes.restored)}
        >
          ${this.hass.localize("ui.dialogs.entity_registry.editor.delete")}
        </mwc-button>
        <mwc-button
          @click=${this._updateEntry}
          .disabled=${invalidDomainUpdate||this._submitting}
        >
          ${this.hass.localize("ui.dialogs.entity_registry.editor.update")}
        </mwc-button>
      </div>
    `;}},{kind:"method",key:"_nameChanged",value:function _nameChanged(ev){this._error=undefined;this._name=ev.target.value;}},{kind:"method",key:"_iconChanged",value:function _iconChanged(ev){this._error=undefined;this._icon=ev.detail.value;}},{kind:"method",key:"_entityIdChanged",value:function _entityIdChanged(ev){this._error=undefined;this._entityId=ev.target.value;}},{kind:"method",key:"_deviceClassChanged",value:function _deviceClassChanged(ev){this._error=undefined;this._deviceClass=ev.target.value;}},{kind:"method",key:"_areaPicked",value:function _areaPicked(ev){this._error=undefined;this._areaId=ev.detail.value;}},{kind:"method",key:"_clearArea",value:function _clearArea(){this._error=undefined;this._areaId=null;}},{kind:"method",key:"_openDeviceSettings",value:function _openDeviceSettings(){showDeviceRegistryDetailDialog(this,{device:this._device,updateEntry:async updates=>{await updateDeviceRegistryEntry(this.hass,this._device.id,updates);}});}},{kind:"method",key:"_updateEntry",value:async function _updateEntry(){this._submitting=true;const params={name:this._name.trim()||null,icon:this._icon.trim()||null,area_id:this._areaId||null,device_class:this._deviceClass||null,new_entity_id:this._entityId.trim()};if(this.entry.disabled_by!==this._disabledBy&&(this._disabledBy===null||this._disabledBy==="user")){params.disabled_by=this._disabledBy;}try{const result=await updateEntityRegistryEntry(this.hass,this._origEntityId,params);if(result.require_restart){showAlertDialog(this,{text:this.hass.localize("ui.dialogs.entity_registry.editor.enabled_restart_confirm")});}if(result.reload_delay){showAlertDialog(this,{text:this.hass.localize("ui.dialogs.entity_registry.editor.enabled_delay_confirm","delay",result.reload_delay)});}fireEvent(this,"close-dialog");}catch(err){this._error=err.message||"Unknown error";}finally{this._submitting=false;}}},{kind:"method",key:"_confirmDeleteEntry",value:async function _confirmDeleteEntry(){if(!(await showConfirmationDialog(this,{text:this.hass.localize("ui.dialogs.entity_registry.editor.confirm_delete")}))){return;}this._submitting=true;try{await removeEntityRegistryEntry(this.hass,this._origEntityId);fireEvent(this,"close-dialog");}finally{this._submitting=false;}}},{kind:"method",key:"_disabledByChanged",value:function _disabledByChanged(ev){this._disabledBy=ev.target.checked?null:"user";}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyle,r`
        :host {
          display: block;
        }
        .container {
          padding: 20px 24px;
        }
        .form {
          margin-bottom: 53px;
        }
        .buttons {
          position: absolute;
          bottom: 0;
          width: calc(100% - 48px);
          box-sizing: border-box;
          border-top: 1px solid
            var(--mdc-dialog-scroll-divider-color, rgba(0, 0, 0, 0.12));
          display: flex;
          justify-content: space-between;
          padding: 8px;
          padding-bottom: max(env(safe-area-inset-bottom), 8px);
          background-color: var(--mdc-theme-surface, #fff);
        }
        ha-select {
          width: 100%;
        }
        ha-switch {
          margin-right: 16px;
        }
        ha-textfield {
          display: block;
          margin: 8px 0;
        }
        .row {
          margin: 8px 0;
          color: var(--primary-text-color);
          display: flex;
          align-items: center;
        }
        p {
          margin: 8px 0;
        }
      `];}}]};},SubscribeMixin(s));

let DialogEntityEditor=_decorate([n("dialog-entity-editor")],function(_initialize,_LitElement){class DialogEntityEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:DialogEntityEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[t()],key:"_entry",value:void 0},{kind:"field",decorators:[t()],key:"_curTab",value(){return "tab-settings";}},{kind:"field",decorators:[t()],key:"_extraTabs",value(){return {};}},{kind:"field",decorators:[t()],key:"_settingsElementTag",value:void 0},{kind:"field",key:"_curTabIndex",value(){return 0;}},{kind:"method",key:"showDialog",value:function showDialog(params){this._params=params;this._entry=undefined;this._settingsElementTag=undefined;this._extraTabs={};this._getEntityReg();}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._params=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"method",key:"render",value:function render(){if(!this._params||this._entry===undefined){return $``;}const entityId=this._params.entity_id;const entry=this._entry;const stateObj=this.hass.states[entityId];return $`
      <ha-dialog
        open
        .heading=${stateObj?computeStateName(stateObj):(entry===null||entry===void 0?void 0:entry.name)||entityId}
        hideActions
        @closed=${this.closeDialog}
        @close-dialog=${this.closeDialog}
      >
        <div slot="heading">
          <ha-header-bar>
            <ha-icon-button
              slot="navigationIcon"
              .label=${this.hass.localize("ui.dialogs.entity_registry.dismiss")}
              .path=${mdiClose}
              dialogAction="cancel"
            ></ha-icon-button>
            <span slot="title">
              ${stateObj?computeStateName(stateObj):(entry===null||entry===void 0?void 0:entry.name)||entityId}
            </span>
            ${stateObj?$`
                  <ha-icon-button
                    slot="actionItems"
                    .label=${this.hass.localize("ui.dialogs.entity_registry.control")}
                    .path=${mdiTune}
                    @click=${this._openMoreInfo}
                  ></ha-icon-button>
                `:""}
          </ha-header-bar>
          <mwc-tab-bar
            .activeIndex=${this._curTabIndex}
            @MDCTabBar:activated=${this._handleTabActivated}
            @MDCTab:interacted=${this._handleTabInteracted}
          >
            <mwc-tab
              id="tab-settings"
              .label=${this.hass.localize("ui.dialogs.entity_registry.settings")}
              dialogInitialFocus
            >
            </mwc-tab>
            ${Object.entries(this._extraTabs).map(([key,tab])=>$`
                <mwc-tab
                  id=${key}
                  .label=${this.hass.localize(tab.translationKey)||key}
                >
                </mwc-tab>
              `)}
            <mwc-tab
              id="tab-related"
              .label=${this.hass.localize("ui.dialogs.entity_registry.related")}
            >
            </mwc-tab>
          </mwc-tab-bar>
        </div>
        <div class="wrapper">${d(this._renderTab())}</div>
      </ha-dialog>
    `;}},{kind:"method",key:"_renderTab",value:function _renderTab(){switch(this._curTab){case"tab-settings":if(this._entry){if(this._settingsElementTag){return $`
              ${dynamicElement(this._settingsElementTag,{hass:this.hass,entry:this._entry,entityId:this._params.entity_id})}
            `;}return $``;}return $`
          <div class="content">
            ${this.hass.localize("ui.dialogs.entity_registry.no_unique_id","entity_id",this._params.entity_id,"faq_link",$`<a
                href=${documentationUrl(this.hass)}
                target="_blank"
                rel="noreferrer"
                >${this.hass.localize("ui.dialogs.entity_registry.faq")}</a
              >`)}
          </div>
        `;case"tab-related":return $`
          <ha-related-items
            class="content"
            .hass=${this.hass}
            .itemId=${this._params.entity_id}
            itemType="entity"
          ></ha-related-items>
        `;default:return $``;}}},{kind:"method",key:"_getEntityReg",value:async function _getEntityReg(){try{this._entry=await getExtendedEntityRegistryEntry(this.hass,this._params.entity_id);this._loadPlatformSettingTabs();}catch{this._entry=null;}}},{kind:"method",key:"_handleTabActivated",value:function _handleTabActivated(ev){this._curTabIndex=ev.detail.index;}},{kind:"method",key:"_handleTabInteracted",value:function _handleTabInteracted(ev){this._curTab=ev.detail.tabId;}},{kind:"method",key:"_loadPlatformSettingTabs",value:async function _loadPlatformSettingTabs(){if(!this._entry){return;}if(!Object.keys(PLATFORMS_WITH_SETTINGS_TAB).includes(this._entry.platform)){this._settingsElementTag="entity-registry-settings";return;}const tag=PLATFORMS_WITH_SETTINGS_TAB[this._entry.platform];await import(`./editor-tabs/settings/${tag}`);this._settingsElementTag=tag;}},{kind:"method",key:"_openMoreInfo",value:function _openMoreInfo(){replaceDialog();fireEvent(this,"hass-more-info",{entityId:this._params.entity_id});this.closeDialog();}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyleDialog,r`
        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
        }

        mwc-tab-bar {
          border-bottom: 1px solid
            var(--mdc-dialog-scroll-divider-color, rgba(0, 0, 0, 0.12));
        }

        ha-dialog {
          --dialog-content-position: static;
          --dialog-content-padding: 0;
          --dialog-z-index: 1000;
        }

        @media all and (min-width: 451px) and (min-height: 501px) {
          .wrapper {
            min-width: 400px;
          }
        }

        .content {
          display: block;
          padding: 20px 24px;
        }

        /* overrule the ha-style-dialog max-height on small screens */
        @media all and (max-width: 450px), all and (max-height: 500px) {
          ha-header-bar {
            --mdc-theme-primary: var(--app-header-background-color);
            --mdc-theme-on-primary: var(--app-header-text-color, white);
          }
        }

        mwc-button.warning {
          --mdc-theme-primary: var(--error-color);
        }

        :host([rtl]) app-toolbar {
          direction: rtl;
          text-align: right;
        }
      `];}}]};},s);

export { DialogEntityEditor };
