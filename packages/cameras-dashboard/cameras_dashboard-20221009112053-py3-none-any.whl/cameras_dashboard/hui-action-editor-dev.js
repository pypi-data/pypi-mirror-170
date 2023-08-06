const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, ef as mdiHelpCircle, r, n, b as memoizeOne, f as fireEvent } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import './auth-dev.js';
import './ha-selector-dev.js';

_decorate([n("ha-help-tooltip")],function(_initialize,_LitElement){class HaHelpTooltip extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaHelpTooltip,d:[{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e()],key:"position",value(){return "top";}},{kind:"method",key:"render",value:function render(){return $`
      <ha-svg-icon .path=${mdiHelpCircle}></ha-svg-icon>
      <paper-tooltip
        offset="4"
        .position=${this.position}
        .fitToVisibleBounds=${true}
        >${this.label}</paper-tooltip
      >
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-svg-icon {
        --mdc-icon-size: var(--ha-help-tooltip-size, 14px);
        color: var(--ha-help-tooltip-color, var(--disabled-text-color));
      }
    `;}}]};},s);

_decorate([n("hui-action-editor")],function(_initialize,_LitElement){class HuiActionEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiActionEditor,d:[{kind:"field",decorators:[e()],key:"config",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e()],key:"actions",value:void 0},{kind:"field",decorators:[e()],key:"tooltipText",value:void 0},{kind:"field",decorators:[e()],key:"hass",value:void 0},{kind:"get",key:"_navigation_path",value:function _navigation_path(){const config=this.config;return (config===null||config===void 0?void 0:config.navigation_path)||"";}},{kind:"get",key:"_url_path",value:function _url_path(){const config=this.config;return (config===null||config===void 0?void 0:config.url_path)||"";}},{kind:"get",key:"_service",value:function _service(){const config=this.config;return (config===null||config===void 0?void 0:config.service)||"";}},{kind:"field",key:"_serviceAction",value(){return memoizeOne(config=>({service:this._service,data:config.service_data,target:config.target}));}},{kind:"method",key:"render",value:function render(){var _this$config$action,_this$config,_this$config2,_this$config3,_this$config4,_this$hass$userData;if(!this.hass||!this.actions){return $``;}return $`
      <div class="dropdown">
        <ha-select
          .label=${this.label}
          .configValue=${"action"}
          @selected=${this._actionPicked}
          .value=${(_this$config$action=(_this$config=this.config)===null||_this$config===void 0?void 0:_this$config.action)!==null&&_this$config$action!==void 0?_this$config$action:"default"}
          @closed=${stopPropagation}
          fixedMenuPosition
          naturalMenuWidt
        >
          <mwc-list-item value="default">
            ${this.hass.localize("ui.panel.lovelace.editor.action-editor.actions.default_action")}
          </mwc-list-item>
          ${this.actions.map(action=>$`
              <mwc-list-item .value=${action}>
                ${this.hass.localize(`ui.panel.lovelace.editor.action-editor.actions.${action}`)}
              </mwc-list-item>
            `)}
        </ha-select>
        ${this.tooltipText?$`
              <ha-help-tooltip .label=${this.tooltipText}></ha-help-tooltip>
            `:""}
      </div>
      ${((_this$config2=this.config)===null||_this$config2===void 0?void 0:_this$config2.action)==="navigate"?$`
            <ha-textfield
              label=${this.hass.localize("ui.panel.lovelace.editor.action-editor.navigation_path")}
              .value=${this._navigation_path}
              .configValue=${"navigation_path"}
              @input=${this._valueChanged}
            ></ha-textfield>
          `:""}
      ${((_this$config3=this.config)===null||_this$config3===void 0?void 0:_this$config3.action)==="url"?$`
            <ha-textfield
              .label=${this.hass.localize("ui.panel.lovelace.editor.action-editor.url_path")}
              .value=${this._url_path}
              .configValue=${"url_path"}
              @input=${this._valueChanged}
            ></ha-textfield>
          `:""}
      ${((_this$config4=this.config)===null||_this$config4===void 0?void 0:_this$config4.action)==="call-service"?$`
            <ha-service-control
              .hass=${this.hass}
              .value=${this._serviceAction(this.config)}
              .showAdvanced=${(_this$hass$userData=this.hass.userData)===null||_this$hass$userData===void 0?void 0:_this$hass$userData.showAdvanced}
              narrow
              @value-changed=${this._serviceValueChanged}
            ></ha-service-control>
          `:""}
    `;}},{kind:"method",key:"_actionPicked",value:function _actionPicked(ev){var _this$config5;ev.stopPropagation();if(!this.hass){return;}const value=ev.target.value;if(((_this$config5=this.config)===null||_this$config5===void 0?void 0:_this$config5.action)===value){return;}if(value==="default"){fireEvent(this,"value-changed",{value:undefined});return;}let data;switch(value){case"url":{data={url_path:this._url_path};break;}case"call-service":{data={service:this._service};break;}case"navigate":{data={navigation_path:this._navigation_path};break;}}fireEvent(this,"value-changed",{value:{action:value,...data}});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){ev.stopPropagation();if(!this.hass){return;}const target=ev.target;const value=ev.target.value;if(this[`_${target.configValue}`]===value){return;}if(target.configValue){fireEvent(this,"value-changed",{value:{...this.config,[target.configValue]:value}});}}},{kind:"method",key:"_serviceValueChanged",value:function _serviceValueChanged(ev){ev.stopPropagation();fireEvent(this,"value-changed",{value:{...this.config,service:ev.detail.value.service||"",service_data:ev.detail.value.data||{},target:ev.detail.value.target||{}}});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .dropdown {
        position: relative;
      }
      ha-help-tooltip {
        position: absolute;
        right: 40px;
        top: 16px;
      }
      ha-select,
      ha-textfield {
        width: 100%;
      }
      ha-textfield {
        margin-top: 8px;
      }
      ha-service-control {
        --service-control-padding: 0;
      }
    `;}}]};},s);
