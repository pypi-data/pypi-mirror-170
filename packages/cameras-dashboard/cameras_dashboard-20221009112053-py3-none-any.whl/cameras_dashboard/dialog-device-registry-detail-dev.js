const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, f as fireEvent, $, o as haStyle, ax as haStyleDialog, r, n } from './main-dev.js';
import './ha-area-picker-dev.js';
import './ha-header-bar-dev.js';
import { b as computeDeviceName } from './device_registry-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './subscribe-mixin-dev.js';
import './ha-combo-box-dev.js';
import './compare-dev.js';

_decorate([n("dialog-device-registry-detail")],function(_initialize,_LitElement){class DialogDeviceRegistryDetail extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:DialogDeviceRegistryDetail,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_nameByUser",value:void 0},{kind:"field",decorators:[t()],key:"_error",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[e()],key:"_areaId",value:void 0},{kind:"field",decorators:[t()],key:"_disabledBy",value:void 0},{kind:"field",decorators:[t()],key:"_submitting",value:void 0},{kind:"method",key:"showDialog",value:async function showDialog(params){this._params=params;this._error=undefined;this._nameByUser=this._params.device.name_by_user||"";this._areaId=this._params.device.area_id;this._disabledBy=this._params.device.disabled_by;await this.updateComplete;}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._error="";this._params=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"method",key:"render",value:function render(){if(!this._params){return $``;}const device=this._params.device;return $`
      <ha-dialog
        open
        @closed=${this.closeDialog}
        .heading=${computeDeviceName(device,this.hass)}
      >
        <div>
          ${this._error?$`<ha-alert alert-type="error">${this._error}</ha-alert> `:""}
          <div class="form">
            <ha-textfield
              .value=${this._nameByUser}
              @input=${this._nameChanged}
              .label=${this.hass.localize("ui.panel.config.devices.name")}
              .placeholder=${device.name||""}
              .disabled=${this._submitting}
              dialogInitialFocus
            ></ha-textfield>
            <ha-area-picker
              .hass=${this.hass}
              .value=${this._areaId}
              @value-changed=${this._areaPicked}
            ></ha-area-picker>
            <div class="row">
              <ha-switch
                .checked=${!this._disabledBy}
                @change=${this._disabledByChanged}
              >
              </ha-switch>
              <div>
                <div>
                  ${this.hass.localize("ui.panel.config.devices.enabled_label","type",this.hass.localize(`ui.panel.config.devices.type.${device.entry_type||"device"}`))}
                </div>
                <div class="secondary">
                  ${this._disabledBy&&this._disabledBy!=="user"?this.hass.localize("ui.panel.config.devices.enabled_cause","type",this.hass.localize(`ui.panel.config.devices.type.${device.entry_type||"device"}`),"cause",this.hass.localize(`config_entry.disabled_by.${this._disabledBy}`)):""}
                  ${this.hass.localize("ui.panel.config.devices.enabled_description")}
                </div>
              </div>
            </div>
          </div>
        </div>
        <mwc-button
          slot="secondaryAction"
          @click=${this.closeDialog}
          .disabled=${this._submitting}
        >
          ${this.hass.localize("ui.common.cancel")}
        </mwc-button>
        <mwc-button
          slot="primaryAction"
          @click=${this._updateEntry}
          .disabled=${this._submitting}
        >
          ${this.hass.localize("ui.panel.config.devices.update")}
        </mwc-button>
      </ha-dialog>
    `;}},{kind:"method",key:"_nameChanged",value:function _nameChanged(ev){this._error=undefined;this._nameByUser=ev.target.value;}},{kind:"method",key:"_areaPicked",value:function _areaPicked(event){this._areaId=event.detail.value;}},{kind:"method",key:"_disabledByChanged",value:function _disabledByChanged(ev){this._disabledBy=ev.target.checked?null:"user";}},{kind:"method",key:"_updateEntry",value:async function _updateEntry(){this._submitting=true;try{await this._params.updateEntry({name_by_user:this._nameByUser.trim()||null,area_id:this._areaId||null,disabled_by:this._disabledBy||null});this.closeDialog();}catch(err){this._error=err.message||this.hass.localize("ui.panel.config.devices.unknown_error");}finally{this._submitting=false;}}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyle,haStyleDialog,r`
        .form {
          padding-bottom: 24px;
        }
        mwc-button.warning {
          margin-right: auto;
        }
        ha-textfield {
          display: block;
          margin-bottom: 16px;
        }
        ha-switch {
          margin-right: 16px;
        }
        .row {
          margin-top: 8px;
          color: var(--primary-text-color);
          display: flex;
          align-items: center;
        }
      `];}}]};},s);
