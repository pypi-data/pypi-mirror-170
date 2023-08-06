const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, ae as mdiAlertOutline, f as fireEvent, r, n } from './main-dev.js';
import './ha-header-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';

_decorate([n("dialog-box")],function(_initialize,_LitElement){class DialogBox extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:DialogBox,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[t()],key:"_value",value:void 0},{kind:"method",key:"showDialog",value:async function showDialog(params){this._params=params;if(params.prompt){this._value=params.defaultValue;}}},{kind:"method",key:"closeDialog",value:function closeDialog(){var _this$_params,_this$_params2;if((_this$_params=this._params)!==null&&_this$_params!==void 0&&_this$_params.confirmation||(_this$_params2=this._params)!==null&&_this$_params2!==void 0&&_this$_params2.prompt){return false;}if(this._params){this._dismiss();return true;}return true;}},{kind:"method",key:"render",value:function render(){if(!this._params){return $``;}const confirmPrompt=this._params.confirmation||this._params.prompt;return $`
      <ha-dialog
        open
        ?scrimClickAction=${confirmPrompt}
        ?escapeKeyAction=${confirmPrompt}
        @closed=${this._dialogClosed}
        defaultAction="ignore"
        .heading=${$`${this._params.warning?$`<ha-svg-icon
              .path=${mdiAlertOutline}
              style="color: var(--warning-color)"
            ></ha-svg-icon> `:""}${this._params.title?this._params.title:this._params.confirmation&&this.hass.localize("ui.dialogs.generic.default_confirmation_title")}`}
      >
        <div>
          ${this._params.text?$`
                <p class=${this._params.prompt?"no-bottom-padding":""}>
                  ${this._params.text}
                </p>
              `:""}
          ${this._params.prompt?$`
                <ha-textfield
                  dialogInitialFocus
                  .value=${this._value||""}
                  @keyup=${this._handleKeyUp}
                  @change=${this._valueChanged}
                  .label=${this._params.inputLabel?this._params.inputLabel:""}
                  .type=${this._params.inputType?this._params.inputType:"text"}
                ></ha-textfield>
              `:""}
        </div>
        ${confirmPrompt&&$`
          <mwc-button @click=${this._dismiss} slot="secondaryAction">
            ${this._params.dismissText?this._params.dismissText:this.hass.localize("ui.dialogs.generic.cancel")}
          </mwc-button>
        `}
        <mwc-button
          @click=${this._confirm}
          ?dialogInitialFocus=${!this._params.prompt}
          slot="primaryAction"
        >
          ${this._params.confirmText?this._params.confirmText:this.hass.localize("ui.dialogs.generic.ok")}
        </mwc-button>
      </ha-dialog>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){this._value=ev.target.value;}},{kind:"method",key:"_dismiss",value:function _dismiss(){var _this$_params3;if((_this$_params3=this._params)!==null&&_this$_params3!==void 0&&_this$_params3.cancel){this._params.cancel();}this._close();}},{kind:"method",key:"_handleKeyUp",value:function _handleKeyUp(ev){if(ev.keyCode===13){this._confirm();}}},{kind:"method",key:"_confirm",value:function _confirm(){if(this._params.confirm){this._params.confirm(this._value);}this._close();}},{kind:"method",key:"_dialogClosed",value:function _dialogClosed(ev){if(ev.detail.action==="ignore"){return;}this._dismiss();}},{kind:"method",key:"_close",value:function _close(){if(!this._params){return;}this._params=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"get",static:true,key:"styles",value:function styles(){return [// haStyleDialog,
r`
        :host([inert]) {
          pointer-events: initial !important;
          cursor: initial !important;
        }
        @media all and (max-width: 450px), all and (max-height: 500px) {
          ha-dialog {
            --ha-dialog-border-radius: 1.5rem;
          }
        }

        a {
          color: var(--accent-color);
        }
        p {
          margin: 0;
          padding-top: 6px;
          padding-bottom: 24px;
          color: var(--primary-text-color);
        }
        .no-bottom-padding {
          padding-bottom: 0;
        }
        .secondary {
          color: var(--secondary-text-color);
        }
        ha-dialog {
          /* Place above other dialogs */
          --dialog-z-index: 104;
        }
      `];}}]};},s);
